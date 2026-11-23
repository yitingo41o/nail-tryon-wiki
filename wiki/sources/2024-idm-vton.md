# IDM-VTON：Improving Diffusion Models for Authentic Virtual Try-on in the Wild

| 欄位 | 內容 |
|---|---|
| 作者 | Yisol Choi, Sangkyung Kwak, Kyungmin Lee, et al.（KAIST、OMNIOUS.AI） |
| 年份 / 發表 | arXiv 2024-03（2403.05139），ECCV 2024（依官方 GitHub README） |
| 連結 | https://arxiv.org/abs/2403.05139 ・ https://github.com/yisol/IDM-VTON |
| 讀過的章節 | Abstract、§1、§3.2、§4.1、§4.2、§5；GitHub README |
| 核對狀態 | 已核對（DressCode 數字除外） |

## 一句話

一個完整的 diffusion 虛擬試穿系統：給一張人的照片和一件衣服的照片，生成這個人穿上那件衣服的樣子，而且盡量保留衣服的圖案細節。

## 在試戴流程中的位置

**完整生成式試戴系統的案例**。它做的是衣服，不是指甲，但它示範了怎麼把 [Latent Diffusion](2021-latent-diffusion.md) 的 inpainting、[IP-Adapter](2023-ip-adapter.md) 和「保留細節」的設計組在一起。

## 重點

1. **任務定義**：給一張人物照和一張服裝照，生成人物穿上該服裝的圖。難處是讓衣服貼合各種姿勢，同時不扭曲圖案和材質。〔§1〕
2. **既有問題**：之前的 diffusion 試穿方法看起來自然，但無法保留衣服本身的特徵（圖案、文字）。〔Abstract〕
3. **TryonNet**：以 SDXL 的 inpainting UNet 為主體，輸入包含遮罩、被遮住的人物圖、DensePose 姿勢圖。〔§3.2〕
4. **高階語意**：用 IP-Adapter（CLIP 圖片編碼器）把衣服特徵送進 cross-attention。〔Abstract、§3.2〕
5. **低階細節（GarmentNet）**：另一個平行的 UNet 專門編碼衣服，把特徵接進 TryonNet 的 self-attention，用來保留細節。〔Abstract、§3.2〕
6. **詳細文字描述**：用「短袖圓領 T 恤」這類具體描述，取代「上衣」這種籠統標籤。〔§3.2〕
7. **單組客製化**：只用一組「人物 + 衣服」照片微調解碼器的 attention 層，就能提升真實照片的效果（學習率 1e-6、100 步）。〔§3.2、§4.1〕
8. **成績**：在 VITON-HD 上 FID 6.29（GP-VTON 6.43）、CLIP-I 0.883（GP-VTON 0.874）較好；但 SSIM 0.870 低於 GP-VTON 的 0.898。〔Table 1、§4.2〕

## 關於曲面與光影

本篇沒有討論指甲。和核心問題相關的是它的**設計思路**：

- 光影和皺褶交給 diffusion 依照人物照片的上下文生成。
- 為了解決「生成會改掉圖案」的問題，特地加了 GarmentNet 抓低階細節。這正好對應 [IP-Adapter](2023-ip-adapter.md) 的限制：只靠 IP-Adapter 細節不夠。

## 限制

- 遮罩區域內的人物細節（例如刺青、痣）很難保留。〔§5〕
- 需要的輸入多：遮罩、DensePose 姿勢圖。

## 待確認

- DressCode 的成績在附錄表格（Table 5、6），本 Wiki 沒有讀到數字，所以沒有收錄。
- 會議名稱 ECCV 2024 來自官方 GitHub README，arXiv 頁面沒有寫。

## 相關頁面

- 概念：[生成式試戴](../concepts/diffusion-tryon.md)、[圖片提示](../concepts/image-prompt.md)
- 比較：[2D 貼圖 vs Diffusion 生成](../comparisons/overlay-vs-diffusion.md)
