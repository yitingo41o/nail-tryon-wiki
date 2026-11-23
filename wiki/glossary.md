# 名詞表

> 依英文字母排序。每個名詞附上最主要的來源頁。

| 名詞 | 中文 | 一句話解釋 | 來源 |
|---|---|---|---|
| 2.5D landmark | 2.5D 關鍵點 | 有 x、y 座標，加上「相對」深度的關鍵點，不是真正的 3D 座標。 | [MediaPipe Hands](sources/2020-mediapipe-hands.md) |
| Autoencoder | 自編碼器 | 先把圖片壓縮成小的表示，再還原回圖片的模型。 | [Latent Diffusion](sources/2021-latent-diffusion.md) |
| Class imbalance | 類別不平衡 | 某一類（例如指甲）在資料中佔的比例很小，模型容易忽略它。 | [Nail Polish Try-On](sources/2019-nail-polish-tryon.md) |
| CLIP image encoder | CLIP 圖片編碼器 | 把圖片轉成向量的模型，常用來讓生成模型「看懂」參考圖。 | [IP-Adapter](sources/2023-ip-adapter.md) |
| Connected components | 連通元件 | 把相連的同類像素歸成一塊，用來把分割結果切成一片片指甲。 | [Nail Polish Try-On](sources/2019-nail-polish-tryon.md) |
| ControlNet | ControlNet | 讓 diffusion 模型照著邊緣、深度、姿勢等結構圖生成的外掛網路。 | [ControlNet](sources/2023-controlnet.md) |
| Cross-attention | 交叉注意力 | 讓圖片特徵去「查詢」文字或參考圖特徵的機制，是把條件放進 diffusion 的主要方法。 | [Latent Diffusion](sources/2021-latent-diffusion.md) |
| DensePose | DensePose | 把人體表面對應到標準人體模型的姿勢圖，IDM-VTON 用它當輸入。 | [IDM-VTON](sources/2024-idm-vton.md) |
| Diffusion model | 擴散模型 | 從雜訊開始、一步步去雜訊來生成圖片的模型。 | [Latent Diffusion](sources/2021-latent-diffusion.md) |
| Direction field | 方向場 | 每個指甲像素都記錄「根部 → 指尖」方向的向量圖。 | [Nail Polish Try-On](sources/2019-nail-polish-tryon.md) |
| FID | FID | 衡量生成圖片和真實圖片分布差距的指標，越低越好。 | [Latent Diffusion](sources/2021-latent-diffusion.md) |
| Image prompt | 圖片提示 | 用參考圖（而不是文字）告訴模型要畫什麼。 | [IP-Adapter](sources/2023-ip-adapter.md) |
| Inpainting | 影像修補 / 局部重繪 | 只重畫照片中被遮罩蓋住的區域，其他地方不變。 | [Latent Diffusion](sources/2021-latent-diffusion.md) |
| IP-Adapter | IP-Adapter | 約 22M 參數的外掛，讓 diffusion 模型能用圖片當提示。 | [IP-Adapter](sources/2023-ip-adapter.md) |
| Latent space | 潛在空間 | 自編碼器壓縮後的小空間，在這裡做 diffusion 比較省計算。 | [Latent Diffusion](sources/2021-latent-diffusion.md) |
| mIoU | 平均交並比 | 分割準確度指標：預測區域和正確區域重疊的比例，越高越好。 | [Nail Polish Try-On](sources/2019-nail-polish-tryon.md) |
| Normal map | 法向量圖 | 記錄表面每一點朝哪個方向的圖，可以描述曲面。 | [ControlNet](sources/2023-controlnet.md) |
| Palm detector | 手掌偵測器 | 先框出手掌（比整隻手好框），再交給關鍵點模型。 | [MediaPipe Hands](sources/2020-mediapipe-hands.md) |
| Segmentation | 分割 | 判斷每個像素屬於哪一類（例如指甲 / 背景）。 | [Nail Polish Try-On](sources/2019-nail-polish-tryon.md) |
| Specular reflection | 鏡面反光 | 光滑表面（例如凝膠指甲）上亮亮的高光。 | [Nail Polish Try-On](sources/2019-nail-polish-tryon.md) |
| Virtual try-on (VTON) | 虛擬試穿 / 試戴 | 生成「某人穿戴某件商品」的圖片或影像。 | [IDM-VTON](sources/2024-idm-vton.md) |
| Zero convolution | 零卷積 | 權重和偏差都從 0 開始的 1×1 卷積，訓練初期不會干擾原模型。 | [ControlNet](sources/2023-controlnet.md) |
