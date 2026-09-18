# blendsmith

**從參考出發，製作讓下一位使用者容易接手編輯的 Blender 資產。**

[English](README.md) · [Skill 繁中閱讀副本](skill/blendsmith/SKILL.zh-TW.md) · [貢獻規範](CONTRIBUTING.md) · [版本紀錄](CHANGELOG.md)

**版本 2026.09.011 · 公開測試版 · GPL-3.0-only · 以 Blender 4.4 流程為基礎**

blendsmith 是由反覆製作模型、收集美術回饋形成的 AI 工作指引，涵蓋需求確認、模型、UV、材質、烘焙、Rig 與交付。它不是 Blender 外掛或一鍵建模工具，也不代表產業品質認證。使用的助手仍須能讀取參考並操作 Blender；安裝 skill 不會自動安裝 Blender 或取得檔案權限。

## 已有規範

- 先分析參考、未知尺寸與遮蔽結構，完整複述需求，再依確認內容製作。
- 優先確認輪廓比例；約定面數計法，避免任意三角扇，規劃孔洞周圍佈線。
- 確認 UV 圖集數量、方形解析度與 UDIM；交付四通道 PBR 貼圖。
- Shader Editor 清楚分區，所有圖片有對應 Coordinate／Mapping 鏈。
- 烘焙前確定平滑與法線；驗證烘焙代理模型，保留程序材質來源與烘焙版。
- 控制器採 Armature／Pose Mode，先核對動作、階層、軸向與限制，再測試實際操作。
- 助手自行生成並保存實際 `.blend`，重開驗證並提供可存取檔案；保留來源、分類貼圖及 Selection／Extras，不能只交腳本讓使用者生成。
- 英文 worklog 與有證據的回饋紀錄；未測試、未接受、未完成要清楚標示。

英文文件為正本，繁體中文版供閱讀；助手應配合使用者的語言溝通。以上是本 skill 的專案約定，使用者明確要求優先，個別差異要記入製作簡報。不存在適用所有模型的面數或平滑角度。

## 如何開始

1. 使用[需求模板](skill/blendsmith/assets/user-request.template.zh-TW.md)，不確定的項目可以寫「請先建議」。
2. 在 Codex 本機使用時，把完整 `skill/blendsmith` 資料夾複製為專案內 `.agents/skills/blendsmith`，或個人的 `~/.agents/skills/blendsmith`；保留授權檔，避免重複安裝。
3. 輸入 `$blendsmith`，提供工作資料夾、參考、用途與交付需求。未出現時可重啟使用的應用程式，或明確請助手讀取 skill 路徑。
4. 核對參考分析與完整製作摘要，再確認開始。已經回答的需求不必重複確認。

例如：「使用 $blendsmith 分析我的產品參考。我需要可翻蓋、按鍵能按壓的 Blender 模型，請先建議面數與貼圖預算，整理未知結構，確認 Rig 操作後再製作。保留來源並在專案寫英文 worklog。」

其他能讀檔的助手也可閱讀這份指引，但自動載入及操作工具取決於使用環境。[官方 skill 文件](https://learn.chatgpt.com/docs/build-skills)。這是一份 skill 原始套件，尚非已發布的 plugin。

## 驗證與限制

歷史案例改善過材質節點、原生控制器、面板佈線、法線與圖集烘焙流程。[回饋登錄](skill/blendsmith/references/feedback-register.md) 保留有範圍限制的結果。私人模型與原始證據未附在此套件，不能視為可獨立重跑的公開基準。

不規則曲面、近距離還原、複雜鉸鏈與視角效果仍需要美術檢查。部分案例尚有未完成階段；文件檢查通過不代表模型品質通過。[已知限制](docs/known-limitations.md)

## 如何共同改善

Fork → 建立修改分支 → 修改並附證據 → 開 Pull Request → 維護者審查。

依[貢獻規範](CONTRIBUTING.md)保留 R01–R11 編號，每次提交附上[英文修改紀錄](changes/TEMPLATE.md)，寫明基準版本、修改前後、適用範圍與實測結果。離線 ZIP 也採同一格式；版本號由維護者統一調整。

使用 Python 3.10 以上執行 `python scripts/validate.py`，檢查套件與文件一致性；這不會測試 Blender 幾何或美術品質。`worklog/`、備份與模型輸出預設留在本機。

## 版本命名

採用 `YYYY.MM.NNN`：年份、兩位月份、當月三位發布序號。文件版本為 `2026.09.011`，GitHub Tag 使用 `v2026.09.011`。首次日期版本由維護者指定起始序號，不代表已有九次公開發布。詳見[發布說明](docs/publishing.md)。

## 授權

[GNU GPL 第 3 版，僅此版本](LICENSE)（GPL-3.0-only）。來源與散布範圍見 [NOTICE.md](NOTICE.md)。
