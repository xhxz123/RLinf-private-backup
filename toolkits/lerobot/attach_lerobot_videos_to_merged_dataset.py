#!/usr/bin/env python3
"""Attach/re-index videos for an already merged LeRobot dataset.

Use this when a previous merge already produced a valid merged ``data/`` and
``meta/`` directory, but did not copy ``videos/`` or write ``video_path``.

Assumption:
    The merged dataset episode order is:
      1. success episodes in original order
      2. failure episodes in original order

The script copies videos from two video roots into the merged dataset and names
them with the merged episode indices, so LeRobot can resolve:
    videos/chunk-{episode_chunk:03d}/{video_key}/episode_{episode_index:06d}.mp4
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any


VIDEO_PATH_TEMPLATE = (
    "videos/chunk-{episode_chunk:03d}/{video_key}/episode_{episode_index:06d}.mp4"
)
DEFAULT_CHUNKS_SIZE = 1000


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path: Path, value: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write("\n")


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _video_keys_from_info(info: dict[str, Any]) -> list[str]:
    return [
        key
        for key, feature in info.get("features", {}).items()
        if isinstance(feature, dict) and feature.get("dtype") == "video"
    ]


def _video_path(root: Path, episode_index: int, video_key: str) -> Path:
    episode_chunk = episode_index // DEFAULT_CHUNKS_SIZE
    return (
        root
        / f"chunk-{episode_chunk:03d}"
        / video_key
        / f"episode_{episode_index:06d}.mp4"
    )


def attach_videos(
    merged_dataset: Path,
    success_video_root: Path,
    fail_video_root: Path,
    success_count: int,
    *,
    dry_run: bool = False,
) -> None:
    info_path = merged_dataset / "meta" / "info.json"
    episodes_path = merged_dataset / "meta" / "episodes.jsonl"
    if not info_path.is_file():
        raise FileNotFoundError(f"missing {info_path}")
    if not episodes_path.is_file():
        raise FileNotFoundError(f"missing {episodes_path}")

    info = _read_json(info_path)
    episodes = _read_jsonl(episodes_path)
    total_episodes = len(episodes)
    if success_count < 0 or success_count > total_episodes:
        raise ValueError(
            f"success_count={success_count} must be in [0, {total_episodes}]"
        )

    video_keys = _video_keys_from_info(info)
    if not video_keys:
        raise ValueError("merged info.json has no video dtype features")

    print(f"[attach] merged dataset: {merged_dataset}")
    print(f"[attach] total episodes: {total_episodes}")
    print(f"[attach] success_count: {success_count}")
    print(f"[attach] fail_count: {total_episodes - success_count}")
    print(f"[attach] video keys: {video_keys}")

    missing: list[Path] = []
    copy_plan: list[tuple[Path, Path]] = []

    for ep in episodes:
        merged_ep_idx = int(ep["episode_index"])
        if merged_ep_idx < success_count:
            source_root = success_video_root
            source_ep_idx = merged_ep_idx
        else:
            source_root = fail_video_root
            source_ep_idx = merged_ep_idx - success_count

        for video_key in video_keys:
            src = _video_path(source_root, source_ep_idx, video_key)
            dst = _video_path(merged_dataset / "videos", merged_ep_idx, video_key)
            if not src.is_file():
                missing.append(src)
            else:
                copy_plan.append((src, dst))

    if missing:
        print("[attach] missing videos:", file=sys.stderr)
        for path in missing[:50]:
            print(f"  {path}", file=sys.stderr)
        if len(missing) > 50:
            print(f"  ... and {len(missing) - 50} more", file=sys.stderr)
        raise FileNotFoundError(f"{len(missing)} source video files are missing")

    print(f"[attach] videos to copy: {len(copy_plan)}")

    if dry_run:
        print("[attach] dry-run; no files written")
        return

    for idx, (src, dst) in enumerate(copy_plan, start=1):
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        if idx % 500 == 0 or idx == len(copy_plan):
            print(f"[attach] copied {idx}/{len(copy_plan)}")

    backup = info_path.with_suffix(".json.bak_no_video")
    if not backup.exists():
        shutil.copy2(info_path, backup)

    info["video_path"] = VIDEO_PATH_TEMPLATE
    info["total_videos"] = total_episodes * len(video_keys)
    info["chunks_size"] = int(info.get("chunks_size", DEFAULT_CHUNKS_SIZE))
    _write_json(info_path, info)

    print(f"[attach] updated {info_path}")
    print(f"[attach] backup: {backup}")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Attach videos to an already merged LeRobot dataset."
    )
    parser.add_argument("--merged-dataset", required=True)
    parser.add_argument("--success-video-root", required=True)
    parser.add_argument("--fail-video-root", required=True)
    parser.add_argument("--success-count", type=int, required=True)
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main() -> None:
    args = _build_parser().parse_args()
    attach_videos(
        merged_dataset=Path(args.merged_dataset),
        success_video_root=Path(args.success_video_root),
        fail_video_root=Path(args.fail_video_root),
        success_count=args.success_count,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
