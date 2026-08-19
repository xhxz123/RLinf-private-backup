# AgiBot G01 训练前数据质量报告

- 生成时间: `2026-08-15T06:13:05.569522+00:00`
- 视频检查: `metadata`
- 自动排除: 1 个 episode
- 人工复核: 9 个 episode

## 数据集汇总

| 数据集 | episode | 帧数 | 通过 | 复核 | 排除 | >50ms ts 间隔 |
|---|---:|---:|---:|---:|---:|---:|
| task_5867 | 479 | 215745 | 469 | 9 | 1 | 234 |

## 自动排除

| 数据集 | Episode | joint delta | action jump | state jump | 原因 |
|---|---:|---:|---:|---:|---|
| task_5867 | 355 | 0.549684 | 0.505178 | 0.382138 | max_joint_delta=0.549684; max_action_jump=0.505178; max_state_jump=0.382138 |

## 人工复核

| 数据集 | Episode | 原因 |
|---|---:|---|
| task_5867 | 137 | source_timestamp_gap=60.142ms@198 |
| task_5867 | 194 | source_timestamp_gap=69.545ms@265 |
| task_5867 | 219 | max_action_jump=0.160002; max_state_jump=0.155794 |
| task_5867 | 257 | source_timestamp_gap=60.407ms@224 |
| task_5867 | 260 | source_timestamp_gap=60.435ms@163 |
| task_5867 | 272 | source_timestamp_gap=69.874ms@394 |
| task_5867 | 287 | source_timestamp_gap=66.383ms@104; max_action_jump=0.122326 |
| task_5867 | 298 | source_timestamp_gap=63.290ms@193 |
| task_5867 | 447 | source_timestamp_gap=63.942ms@363 |

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
