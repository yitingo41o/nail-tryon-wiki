# 條件控制（Conditional Control）

> 除了文字以外，再給 diffusion 模型一張「結構圖」，控制它畫出來的形狀和位置。

## 重點

- ControlNet 把原模型鎖住，另外訓練一份副本學新條件，兩者用初始化為 0 的「零卷積」連接，所以一開始不會破壞原模型。〔來源：[ControlNet](../sources/2023-controlnet.md) §3.1〕
- 可用的條件包括邊緣、深度圖、法向量圖、分割圖、人體姿勢、草稿。〔來源：[ControlNet](../sources/2023-controlnet.md) §4〕
- 多個條件可以疊加（輸出直接相加）。〔來源：[ControlNet](../sources/2023-controlnet.md) §3.4〕
- 小資料（1k 張）也能訓練，不會崩壞。〔來源：[ControlNet](../sources/2023-controlnet.md) §4.5〕
- 結構不一定被完全遵守：分割條件的重建 IoU 0.35，真實資料是 0.58。〔來源：[ControlNet](../sources/2023-controlnet.md) Table 2〕

## 和核心問題的關係

- **曲面**：法向量圖描述「表面每一點朝哪個方向」，就是曲面資訊。用指甲的法向量圖或深度圖當條件，是生成式路線處理曲面的方法。〔綜合推論〕
- 要做到這件事，得先能估出指甲的法向量 / 深度，Wiki 目前的資料都沒有做這件事 → 列為下一步要找的資料。〔綜合推論〕

## 來源

- [ControlNet（2023）](../sources/2023-controlnet.md)
