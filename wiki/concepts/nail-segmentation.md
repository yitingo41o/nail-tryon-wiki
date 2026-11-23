# 指甲分割（Fingernail Segmentation）

> 讓電腦判斷照片裡「哪些像素是指甲」，而且分得出是哪一根手指的指甲。

## 重點

- 指甲在照片中很小，難點是同時要夠精細、又要夠輕，才能在手機上即時跑。〔來源：[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) Abstract、§1〕
- ModiFace 的模型同時輸出三樣東西：是不是指甲、是哪根手指、每個像素的「根部 → 指尖」方向。〔來源：[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) §3.2〕
- 指甲只佔畫面一小部分（類別不平衡），用只算最難 10% 像素的 Loss Max-Pooling 改善，mIoU 從 91.3 提升到 93.3。〔來源：[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) §3.3、§3.5〕
- 預測完再用**連通元件**把結果切成一片一片的指甲，計算每片的角度。〔來源：[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) §3.4〕
- 最好的設定：iPad Pro 上 94.5 mIoU、每幀 29.8 ms。〔來源：[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) Abstract〕

## 和核心問題的關係

- 兩條路線都需要知道指甲在哪裡：2D 貼圖要知道「貼在哪」，生成式路線要知道「遮住哪裡重畫」（inpainting 的遮罩）。〔綜合推論〕
- 方向場讓貼圖可以順著指甲方向旋轉，是 2D 路線處理「方向」的關鍵。

## 來源

- [Nail Polish Try-On（2019）](../sources/2019-nail-polish-tryon.md)
