# AgiBot G01 训练前数据质量报告

- 生成时间: `2026-08-15T06:14:46.884384+00:00`
- 视频检查: `metadata`
- 自动排除: 0 个 episode
- 人工复核: 3 个 episode

## 数据集汇总

| 数据集 | episode | 帧数 | 通过 | 复核 | 排除 | >50ms ts 间隔 |
|---|---:|---:|---:|---:|---:|---:|
| task_5867 | 203 | 90096 | 200 | 3 | 0 | 114 |

## 自动排除

没有自动排除的 episode。

## 人工复核

| 数据集 | Episode | 原因 |
|---|---:|---|
| task_5867 | 52 | source_timestamp_gap=63.357ms@114 |
| task_5867 | 69 | source_timestamp_gap=68.992ms@324 |
| task_5867 | 164 | source_timestamp_gap=61.118ms@233 |

## 自动排除阈值

```json
{
  "exclude_max_joint_delta": 0.35,
  "exclude_max_action_jump": 0.25,
  "exclude_max_state_jump": 0.25,
  "review_max_joint_delta": 0.25,
  "review_max_action_jump": 0.12,
  "review_max_state_jump": 0.12,
  "warning_ts_gap_ms": 50.0,
  "review_ts_gap_ms": 60.0,
  "moving_duplicate_threshold": 0.01
}
```

`exclude_a2d.txt` 必须同时传给归一化统计和训练命令。原始数据未被修改。
