# 2D 貼圖試戴（AR Overlay Try-On）

> 先找到手和指甲，再把款式「貼」上去，加上假的光影讓它看起來像真的。也就是「AR 路線」。

## 重點

- 流程：找到手（[手部關鍵點](hand-landmarks.md)）→ 找到每片指甲與方向（[指甲分割](nail-segmentation.md)）→ 把顏色或圖案畫在指甲遮罩上。〔來源：[MediaPipe Hands](../sources/2020-mediapipe-hands.md) §2；[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) §3.4〕
- 光影是**近似**的：用漸層模擬鏡面反光，並依每片指甲的方向擺放。〔來源：[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) §3.4〕
- 把遮罩往指尖拉長，蓋住真實指甲尖端顏色較淺的部分。〔來源：[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) §3.4〕
- 速度快，可以在手機或瀏覽器上即時跑（ModiFace：iPad Pro 每幀 29.8 ms；網頁版用 TensorFlow.js）。〔來源：[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) Abstract、§3.5〕

## 和核心問題的關係

- **曲面**：沒有真正的 3D 指甲形狀，只有平面遮罩 + 方向。〔來源：[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) §3.4〕
- **光影**：用漸層「畫」出來的假反光，論文沒有評估在不同光線下是否自然。〔來源：[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) §3.4〕
- **款式還原**：圖案是直接貼上去的，不會被模型改掉，這是它相對生成式路線的優勢。〔綜合推論〕
- **立體裝飾**（例如凸起的櫻桃、珍珠、水鑽）只能當平面圖貼，側面和陰影做不出來。〔綜合推論〕

## 來源

- [Nail Polish Try-On（2019）](../sources/2019-nail-polish-tryon.md)
- [MediaPipe Hands（2020）](../sources/2020-mediapipe-hands.md)
