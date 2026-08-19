# AgiBot G01 训练前数据质量报告

- 生成时间: `2026-08-15T06:19:33.047001+00:00`
- 视频检查: `metadata`
- 自动排除: 23 个 episode
- 人工复核: 127 个 episode

## 数据集汇总

| 数据集 | episode | 帧数 | 通过 | 复核 | 排除 | >50ms ts 间隔 |
|---|---:|---:|---:|---:|---:|---:|
| record_dataset_new3 | 150 | 154538 | 0 | 127 | 23 | 153 |

## 自动排除

| 数据集 | Episode | joint delta | action jump | state jump | 原因 |
|---|---:|---:|---:|---:|---|
| record_dataset_new3 | 2 | 0.208500 | 0.190446 | 0.256253 | max_state_jump=0.256253 |
| record_dataset_new3 | 12 | 0.253888 | 0.210882 | 0.269777 | max_state_jump=0.269777 |
| record_dataset_new3 | 27 | 0.265238 | 0.265478 | 0.230951 | max_action_jump=0.265478 |
| record_dataset_new3 | 28 | 0.269506 | 0.213221 | 0.269603 | max_state_jump=0.269603 |
| record_dataset_new3 | 29 | 0.245475 | 0.203840 | 0.256323 | max_state_jump=0.256323 |
| record_dataset_new3 | 30 | 0.307738 | 0.306072 | 0.183051 | max_action_jump=0.306072 |
| record_dataset_new3 | 33 | 0.228150 | 0.199976 | 0.271348 | max_state_jump=0.271348 |
| record_dataset_new3 | 35 | 0.226667 | 0.208475 | 0.254788 | max_state_jump=0.254788 |
| record_dataset_new3 | 37 | 0.219941 | 0.192797 | 0.259499 | max_state_jump=0.259499 |
| record_dataset_new3 | 40 | 0.239824 | 0.232269 | 0.254281 | max_state_jump=0.254281 |
| record_dataset_new3 | 48 | 0.255616 | 0.194269 | 0.262134 | max_state_jump=0.262134 |
| record_dataset_new3 | 58 | 0.250590 | 0.248924 | 0.266845 | max_state_jump=0.266845 |
| record_dataset_new3 | 63 | 0.232913 | 0.228804 | 0.268207 | max_state_jump=0.268207 |
| record_dataset_new3 | 66 | 0.234519 | 0.189825 | 0.256340 | max_state_jump=0.256340 |
| record_dataset_new3 | 72 | 0.226666 | 0.195732 | 0.259988 | max_state_jump=0.259988 |
| record_dataset_new3 | 75 | 0.215516 | 0.188200 | 0.256096 | max_state_jump=0.256096 |
| record_dataset_new3 | 78 | 0.256872 | 0.208823 | 0.266653 | max_state_jump=0.266653 |
| record_dataset_new3 | 84 | 0.257221 | 0.209818 | 0.266741 | max_state_jump=0.266741 |
| record_dataset_new3 | 86 | 0.248066 | 0.213349 | 0.266514 | max_state_jump=0.266514 |
| record_dataset_new3 | 102 | 0.276486 | 0.232750 | 0.281852 | max_state_jump=0.281852 |
| record_dataset_new3 | 117 | 0.229616 | 0.218215 | 0.277438 | max_state_jump=0.277438 |
| record_dataset_new3 | 129 | 0.227117 | 0.204004 | 0.254212 | max_state_jump=0.254212 |
| record_dataset_new3 | 135 | 0.234065 | 0.228420 | 0.259447 | max_state_jump=0.259447 |

## 人工复核

| 数据集 | Episode | 原因 |
|---|---:|---|
| record_dataset_new3 | 0 | source_timestamp_gap=108.864ms@1; max_action_jump=0.209001; max_state_jump=0.190118 |
| record_dataset_new3 | 1 | source_timestamp_gap=102.193ms@1; max_action_jump=0.204339; max_state_jump=0.234633 |
| record_dataset_new3 | 3 | source_timestamp_gap=94.785ms@1; max_action_jump=0.199748; max_state_jump=0.248558 |
| record_dataset_new3 | 4 | source_timestamp_gap=102.106ms@1; max_action_jump=0.184188; max_state_jump=0.238210 |
| record_dataset_new3 | 5 | source_timestamp_gap=101.638ms@1; max_action_jump=0.189733; max_state_jump=0.247127 |
| record_dataset_new3 | 6 | source_timestamp_gap=87.832ms@1; max_joint_delta=0.252580; max_action_jump=0.200945; max_state_jump=0.244230 |
| record_dataset_new3 | 7 | source_timestamp_gap=97.392ms@1; max_action_jump=0.217822; max_state_jump=0.220062 |
| record_dataset_new3 | 8 | source_timestamp_gap=97.693ms@1; max_action_jump=0.231223; max_state_jump=0.208842 |
| record_dataset_new3 | 9 | source_timestamp_gap=103.319ms@1; max_action_jump=0.216118; max_state_jump=0.176332 |
| record_dataset_new3 | 10 | source_timestamp_gap=100.511ms@1; max_action_jump=0.202951; max_state_jump=0.230288 |
| record_dataset_new3 | 11 | source_timestamp_gap=97.851ms@1; max_action_jump=0.184462; max_state_jump=0.238245 |
| record_dataset_new3 | 13 | source_timestamp_gap=96.164ms@1; max_action_jump=0.197010; max_state_jump=0.200186 |
| record_dataset_new3 | 14 | source_timestamp_gap=100.436ms@1; max_action_jump=0.212069; max_state_jump=0.238629 |
| record_dataset_new3 | 15 | source_timestamp_gap=103.186ms@1; max_action_jump=0.199710; max_state_jump=0.231125 |
| record_dataset_new3 | 16 | source_timestamp_gap=104.482ms@1; max_action_jump=0.206520; max_state_jump=0.219521 |
| record_dataset_new3 | 17 | source_timestamp_gap=107.834ms@1; max_action_jump=0.156711; max_state_jump=0.216118 |
| record_dataset_new3 | 18 | source_timestamp_gap=106.480ms@1; max_action_jump=0.176593; max_state_jump=0.212558 |
| record_dataset_new3 | 19 | source_timestamp_gap=105.723ms@1; max_action_jump=0.177583; max_state_jump=0.245574 |
| record_dataset_new3 | 20 | source_timestamp_gap=105.425ms@1; max_action_jump=0.232360; max_state_jump=0.201059 |
| record_dataset_new3 | 21 | source_timestamp_gap=97.154ms@1; max_action_jump=0.174027; max_state_jump=0.174622 |
| record_dataset_new3 | 22 | source_timestamp_gap=97.854ms@1; max_action_jump=0.214493; max_state_jump=0.196243 |
| record_dataset_new3 | 23 | source_timestamp_gap=84.143ms@1; max_action_jump=0.151436; max_state_jump=0.210744 |
| record_dataset_new3 | 24 | source_timestamp_gap=102.246ms@1; max_action_jump=0.215245; max_state_jump=0.214094 |
| record_dataset_new3 | 25 | source_timestamp_gap=73.311ms@2; max_action_jump=0.172268; max_state_jump=0.206468 |
| record_dataset_new3 | 26 | source_timestamp_gap=98.642ms@1; max_action_jump=0.169613; max_state_jump=0.224163 |
| record_dataset_new3 | 31 | source_timestamp_gap=99.339ms@1 |
| record_dataset_new3 | 32 | source_timestamp_gap=96.621ms@1; max_action_jump=0.156170; max_state_jump=0.201670 |
| record_dataset_new3 | 34 | source_timestamp_gap=95.260ms@1; max_action_jump=0.239459; max_state_jump=0.200064 |
| record_dataset_new3 | 36 | source_timestamp_gap=81.475ms@1; max_action_jump=0.147486; max_state_jump=0.216397 |
| record_dataset_new3 | 38 | source_timestamp_gap=78.515ms@1; max_action_jump=0.172144; max_state_jump=0.249029 |
| record_dataset_new3 | 39 | source_timestamp_gap=106.653ms@1; max_action_jump=0.222461; max_state_jump=0.233202 |
| record_dataset_new3 | 41 | source_timestamp_gap=105.726ms@1; max_action_jump=0.182767; max_state_jump=0.224547 |
| record_dataset_new3 | 42 | source_timestamp_gap=96.711ms@1; max_action_jump=0.211249; max_state_jump=0.192090 |
| record_dataset_new3 | 43 | source_timestamp_gap=100.671ms@1; max_action_jump=0.235998; max_state_jump=0.207009 |
| record_dataset_new3 | 44 | source_timestamp_gap=73.406ms@2; max_action_jump=0.169631; max_state_jump=0.214740 |
| record_dataset_new3 | 45 | source_timestamp_gap=106.215ms@1; max_action_jump=0.159231; max_state_jump=0.249360 |
| record_dataset_new3 | 46 | source_timestamp_gap=68.982ms@2; max_action_jump=0.165069; max_state_jump=0.201233 |
| record_dataset_new3 | 47 | source_timestamp_gap=98.891ms@1; max_action_jump=0.183482; max_state_jump=0.210377 |
| record_dataset_new3 | 49 | source_timestamp_gap=100.464ms@1; max_action_jump=0.166646; max_state_jump=0.241997 |
| record_dataset_new3 | 50 | source_timestamp_gap=80.262ms@1; max_action_jump=0.176035; max_state_jump=0.210552 |
| record_dataset_new3 | 51 | source_timestamp_gap=102.995ms@1; max_action_jump=0.160662; max_state_jump=0.221737 |
| record_dataset_new3 | 52 | source_timestamp_gap=101.756ms@1; max_action_jump=0.166211; max_state_jump=0.230706 |
| record_dataset_new3 | 53 | source_timestamp_gap=104.297ms@1; max_action_jump=0.204303; max_state_jump=0.223308 |
| record_dataset_new3 | 54 | source_timestamp_gap=104.998ms@1; max_action_jump=0.172423; max_state_jump=0.213710 |
| record_dataset_new3 | 55 | source_timestamp_gap=103.532ms@1; max_action_jump=0.211097; max_state_jump=0.249919 |
| record_dataset_new3 | 56 | source_timestamp_gap=98.253ms@1; max_action_jump=0.171992; max_state_jump=0.244108 |
| record_dataset_new3 | 57 | source_timestamp_gap=106.146ms@1; max_action_jump=0.147730; max_state_jump=0.220917 |
| record_dataset_new3 | 59 | source_timestamp_gap=103.924ms@1; max_action_jump=0.157503; max_state_jump=0.246638 |
| record_dataset_new3 | 60 | source_timestamp_gap=103.968ms@1; max_action_jump=0.200936; max_state_jump=0.201757 |
| record_dataset_new3 | 61 | source_timestamp_gap=103.603ms@1; max_action_jump=0.145532; max_state_jump=0.215316 |
| record_dataset_new3 | 62 | source_timestamp_gap=97.543ms@1; max_action_jump=0.176384; max_state_jump=0.199593 |
| record_dataset_new3 | 64 | source_timestamp_gap=98.310ms@1; max_action_jump=0.221736; max_state_jump=0.235086 |
| record_dataset_new3 | 65 | source_timestamp_gap=95.346ms@1; max_action_jump=0.170891; max_state_jump=0.236831 |
| record_dataset_new3 | 67 | source_timestamp_gap=103.258ms@1; max_action_jump=0.161970; max_state_jump=0.206817 |
| record_dataset_new3 | 68 | source_timestamp_gap=94.876ms@1; max_action_jump=0.156150; max_state_jump=0.216293 |
| record_dataset_new3 | 69 | source_timestamp_gap=99.764ms@1; max_action_jump=0.135612; max_state_jump=0.162076 |
| record_dataset_new3 | 70 | source_timestamp_gap=103.670ms@1; max_action_jump=0.176546; max_state_jump=0.222575 |
| record_dataset_new3 | 71 | source_timestamp_gap=99.730ms@1; max_action_jump=0.195153; max_state_jump=0.200291 |
| record_dataset_new3 | 73 | source_timestamp_gap=99.832ms@1; max_action_jump=0.190937; max_state_jump=0.238140 |
| record_dataset_new3 | 74 | source_timestamp_gap=102.988ms@1; max_action_jump=0.222225; max_state_jump=0.202996 |
| record_dataset_new3 | 76 | source_timestamp_gap=72.438ms@1; max_action_jump=0.189175; max_state_jump=0.195806 |
| record_dataset_new3 | 77 | source_timestamp_gap=105.751ms@1; max_joint_delta=0.263048; max_action_jump=0.227913; max_state_jump=0.168026 |
| record_dataset_new3 | 79 | source_timestamp_gap=104.932ms@1; max_action_jump=0.199690; max_state_jump=0.207289 |
| record_dataset_new3 | 80 | source_timestamp_gap=91.675ms@1; max_action_jump=0.183448; max_state_jump=0.220306 |
| record_dataset_new3 | 81 | source_timestamp_gap=105.221ms@1; max_action_jump=0.143927; max_state_jump=0.177257 |
| record_dataset_new3 | 82 | source_timestamp_gap=97.269ms@1; max_action_jump=0.186500; max_state_jump=0.215508 |
| record_dataset_new3 | 83 | source_timestamp_gap=108.802ms@1; max_action_jump=0.176942; max_state_jump=0.248139 |
| record_dataset_new3 | 85 | source_timestamp_gap=100.160ms@1; max_action_jump=0.191416; max_state_jump=0.165653 |
| record_dataset_new3 | 87 | source_timestamp_gap=98.075ms@1; max_action_jump=0.212767; max_state_jump=0.168881 |
| record_dataset_new3 | 88 | source_timestamp_gap=101.316ms@1 |
| record_dataset_new3 | 89 | source_timestamp_gap=96.268ms@1; max_action_jump=0.147417; max_state_jump=0.179264 |
| record_dataset_new3 | 90 | source_timestamp_gap=86.044ms@1; max_action_jump=0.148220; max_state_jump=0.172022 |
| record_dataset_new3 | 91 | source_timestamp_gap=104.658ms@1; max_action_jump=0.174071; max_state_jump=0.153159 |
| record_dataset_new3 | 92 | source_timestamp_gap=98.997ms@1; max_action_jump=0.182247; max_state_jump=0.192648 |
| record_dataset_new3 | 93 | source_timestamp_gap=102.304ms@1; max_action_jump=0.166403; max_state_jump=0.186994 |
| record_dataset_new3 | 94 | source_timestamp_gap=61.854ms@1; max_action_jump=0.180886; max_state_jump=0.192334 |
| record_dataset_new3 | 95 | source_timestamp_gap=100.289ms@1 |
| record_dataset_new3 | 96 | source_timestamp_gap=95.929ms@1; max_action_jump=0.153533; max_state_jump=0.225611 |
| record_dataset_new3 | 97 | source_timestamp_gap=100.106ms@1; max_action_jump=0.159430; max_state_jump=0.180852 |
| record_dataset_new3 | 98 | source_timestamp_gap=100.919ms@1 |
| record_dataset_new3 | 99 | source_timestamp_gap=102.516ms@1; max_action_jump=0.198453; max_state_jump=0.184010 |
| record_dataset_new3 | 100 | source_timestamp_gap=98.989ms@1 |
| record_dataset_new3 | 101 | source_timestamp_gap=76.513ms@2; max_action_jump=0.161191; max_state_jump=0.242381 |
| record_dataset_new3 | 103 | source_timestamp_gap=81.112ms@1; max_action_jump=0.166235; max_state_jump=0.164850 |
| record_dataset_new3 | 104 | source_timestamp_gap=96.549ms@1; max_action_jump=0.125831; max_state_jump=0.171062 |
| record_dataset_new3 | 105 | source_timestamp_gap=102.870ms@1; max_action_jump=0.223900; max_state_jump=0.178671 |
| record_dataset_new3 | 106 | source_timestamp_gap=98.705ms@1; max_action_jump=0.208491; max_state_jump=0.207289 |
| record_dataset_new3 | 107 | source_timestamp_gap=103.933ms@1; max_action_jump=0.177054; max_state_jump=0.213291 |
| record_dataset_new3 | 108 | source_timestamp_gap=73.598ms@1; max_action_jump=0.168270; max_state_jump=0.179892 |
| record_dataset_new3 | 109 | source_timestamp_gap=100.753ms@1; max_state_jump=0.135586 |
| record_dataset_new3 | 110 | source_timestamp_gap=74.527ms@2 |
| record_dataset_new3 | 111 | source_timestamp_gap=104.789ms@1; max_action_jump=0.192926; max_state_jump=0.171795 |
| record_dataset_new3 | 112 | source_timestamp_gap=97.841ms@1; max_action_jump=0.158479; max_state_jump=0.135360 |
| record_dataset_new3 | 113 | source_timestamp_gap=102.936ms@1; max_action_jump=0.178893; max_state_jump=0.218020 |
| record_dataset_new3 | 114 | source_timestamp_gap=97.547ms@1; max_action_jump=0.145933; max_state_jump=0.154310 |
| record_dataset_new3 | 115 | source_timestamp_gap=94.426ms@1; max_action_jump=0.189157; max_state_jump=0.221196 |
| record_dataset_new3 | 116 | source_timestamp_gap=104.914ms@1; max_action_jump=0.201025; max_state_jump=0.241316 |
| record_dataset_new3 | 118 | source_timestamp_gap=108.901ms@1; max_action_jump=0.171145; max_state_jump=0.213954 |
| record_dataset_new3 | 119 | source_timestamp_gap=100.862ms@1; max_action_jump=0.180345; max_state_jump=0.218840 |
| record_dataset_new3 | 120 | source_timestamp_gap=78.908ms@2; max_joint_delta=0.261008; max_action_jump=0.223586; max_state_jump=0.180660 |
| record_dataset_new3 | 121 | source_timestamp_gap=96.512ms@1 |
| record_dataset_new3 | 122 | source_timestamp_gap=108.980ms@1; max_action_jump=0.168392; max_state_jump=0.196975 |
| record_dataset_new3 | 123 | source_timestamp_gap=105.508ms@1; max_action_jump=0.178861; max_state_jump=0.183766 |
| record_dataset_new3 | 124 | source_timestamp_gap=77.577ms@2 |
| record_dataset_new3 | 125 | source_timestamp_gap=98.977ms@1; max_action_jump=0.144280; max_state_jump=0.183417 |
| record_dataset_new3 | 126 | source_timestamp_gap=98.008ms@1; max_action_jump=0.179427; max_state_jump=0.146667 |
| record_dataset_new3 | 127 | source_timestamp_gap=97.778ms@1; max_action_jump=0.158105; max_state_jump=0.176926 |
| record_dataset_new3 | 128 | source_timestamp_gap=98.103ms@1 |
| record_dataset_new3 | 130 | source_timestamp_gap=93.002ms@1; max_action_jump=0.212737; max_state_jump=0.196958 |
| record_dataset_new3 | 131 | source_timestamp_gap=106.319ms@1; max_state_jump=0.134435 |
| record_dataset_new3 | 132 | source_timestamp_gap=109.270ms@1; max_action_jump=0.171376; max_state_jump=0.232225 |
| record_dataset_new3 | 133 | source_timestamp_gap=107.353ms@1; max_action_jump=0.208121; max_state_jump=0.222243 |
| record_dataset_new3 | 134 | source_timestamp_gap=90.604ms@1; max_action_jump=0.141810; max_state_jump=0.139513 |
| record_dataset_new3 | 136 | source_timestamp_gap=106.151ms@1; max_action_jump=0.167228; max_state_jump=0.184795 |
| record_dataset_new3 | 137 | source_timestamp_gap=105.625ms@1; max_action_jump=0.129459; max_state_jump=0.157661 |
| record_dataset_new3 | 138 | source_timestamp_gap=95.463ms@1; max_action_jump=0.204269; max_state_jump=0.202996 |
| record_dataset_new3 | 139 | source_timestamp_gap=61.396ms@1; max_action_jump=0.168721; max_state_jump=0.155986 |
| record_dataset_new3 | 140 | source_timestamp_gap=100.207ms@1; max_joint_delta=0.255651; max_action_jump=0.183347; max_state_jump=0.244509 |
| record_dataset_new3 | 141 | source_timestamp_gap=95.970ms@1; max_action_jump=0.201190; max_state_jump=0.166752 |
| record_dataset_new3 | 142 | source_timestamp_gap=93.660ms@1; max_action_jump=0.144869; max_state_jump=0.159092 |
| record_dataset_new3 | 143 | source_timestamp_gap=110.146ms@1; max_action_jump=0.226676; max_state_jump=0.170888 |
| record_dataset_new3 | 144 | source_timestamp_gap=105.260ms@1; max_action_jump=0.207139; max_state_jump=0.135342 |
| record_dataset_new3 | 145 | source_timestamp_gap=100.510ms@1; max_action_jump=0.218462; max_state_jump=0.209191 |
| record_dataset_new3 | 146 | source_timestamp_gap=102.513ms@1; max_action_jump=0.179560; max_state_jump=0.158586 |
| record_dataset_new3 | 147 | source_timestamp_gap=96.610ms@1; max_action_jump=0.159614; max_state_jump=0.192299 |
| record_dataset_new3 | 148 | source_timestamp_gap=105.931ms@1; max_action_jump=0.206295; max_state_jump=0.239938 |
| record_dataset_new3 | 149 | source_timestamp_gap=102.210ms@1; max_action_jump=0.189558; max_state_jump=0.180852 |

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
