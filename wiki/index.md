# 穿戴甲虛擬試戴 LLM Wiki — 目錄

> **核心問題**：「直接把指甲圖貼到手上（2D 貼圖）」和「用 diffusion 生成」差在哪？各自怎麼處理指甲曲面與光影？
>
> 第一次來：先讀 [比較頁](comparisons/overlay-vs-diffusion.md)，再依興趣點進概念頁。
> 規則見 [CLAUDE.md](../CLAUDE.md)，操作紀錄見 [log.md](log.md)，建 Wiki 前的討論見 [discussion.md](discussion.md)。

## 比較 / 綜合

| 頁面 | 摘要 |
|---|---|
| [2D 貼圖 vs Diffusion 生成](comparisons/overlay-vs-diffusion.md) | 兩條路線在款式還原、光影、曲面、速度上的比較，以及混合做法的假設 |

## 概念

| 頁面 | 摘要 |
|---|---|
| [指甲曲面與光影](concepts/curvature-and-lighting.md) | 核心問題本身：兩條路線怎麼處理弧度與反光 |
| [2D 貼圖試戴](concepts/2d-overlay-tryon.md) | AR 路線：找手 → 找指甲 → 貼圖 + 假反光 |
| [生成式試戴](concepts/diffusion-tryon.md) | 生成式路線：遮住指甲 → diffusion 依款式與形狀重畫 |
| [手部關鍵點偵測](concepts/hand-landmarks.md) | 先找手掌再找 21 個 2.5D 關鍵點 |
| [指甲分割](concepts/nail-segmentation.md) | 小物體分割、方向場、連通元件 |
| [Diffusion 與 Inpainting](concepts/diffusion-inpainting.md) | 潛在空間 diffusion、只重畫遮住的區域 |
| [條件控制](concepts/conditional-control.md) | ControlNet：用結構圖控制生成形狀 |
| [圖片提示](concepts/image-prompt.md) | IP-Adapter：用參考圖當提示，但細節不保證 |

## 資料（sources）

| 頁面 | 年份 | 在流程中的位置 | 核對狀態 |
|---|---|---|---|
| [Nail Polish Try-On](sources/2019-nail-polish-tryon.md) | 2019 | 找到指甲 + 貼上去 | 已核對 |
| [MediaPipe Hands](sources/2020-mediapipe-hands.md) | 2020 | 找到手 | 已核對 |
| [Latent Diffusion](sources/2021-latent-diffusion.md) | 2021 | 生成的基礎、inpainting | 部分核對 |
| [ControlNet](sources/2023-controlnet.md) | 2023 | 控制形狀 | 已核對 |
| [IP-Adapter](sources/2023-ip-adapter.md) | 2023 | 參考款式圖 | 已核對 |
| [IDM-VTON](sources/2024-idm-vton.md) | 2024 | 完整生成式試戴系統 | 已核對（DressCode 數字除外） |

## 其他

- [名詞表](glossary.md)
- [討論紀錄](discussion.md)
- [操作紀錄 log](log.md)
- [原始資料登記](../raw/sources.md)
