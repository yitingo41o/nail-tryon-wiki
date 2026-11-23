# 手部關鍵點偵測（Hand Landmark Detection）

> 在照片或影片裡找出手的位置，以及每根手指關節的座標。

## 重點

- 常見做法分兩步：先找手掌，再在手掌附近的小範圍內找 21 個關鍵點；先找手掌是因為手掌形狀固定、比較好框。〔來源：[MediaPipe Hands](../sources/2020-mediapipe-hands.md) §2、§2.1〕
- 每個關鍵點有 x、y 和相對深度（2.5D），可以知道手指朝哪裡、哪根手指比較靠近鏡頭。〔來源：[MediaPipe Hands](../sources/2020-mediapipe-hands.md) §2.2〕
- 影片中不必每幀都重新偵測，用上一幀的結果追蹤，所以手機上也能即時跑（Full 版在 iPhone 11 上約 5.3 ms）。〔來源：[MediaPipe Hands](../sources/2020-mediapipe-hands.md) §2、Table 3〕

## 和核心問題的關係

- **2D 貼圖路線**需要它來決定貼圖的位置和旋轉角度。
- **生成式路線**也可以用它產生手部姿勢圖，當作 [條件控制](conditional-control.md) 的輸入。〔綜合推論〕
- 它只給「點」，不給指甲的輪廓，也沒有指甲表面的曲面資訊，所以還需要 [指甲分割](nail-segmentation.md)。

## 來源

- [MediaPipe Hands（2020）](../sources/2020-mediapipe-hands.md)
