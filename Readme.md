# AniTools，給2D動畫人員使用的Blender輔助插件

> **AniTools是一個讓2D動畫人員能夠快速上手工作流程的輔助插件**



AniTools是一種可以簡化了Blender介面的輔助程式，通過簡單介面，能夠使剛開始操作的使用者能夠快速上手。其中包含了以下幾種功能:
* 紙張生成(安全框)
* 輸出設定
* 工作區域、人物模型的預設


## 環境
*此插件支援一鍵安裝所有依賴，因此請在第一次執行的時候使用管理員的身份執行Blender(僅限Windows)*

* Blender 2.9 以上
* Windows 10, Mac, Linux
* Pillow 8.4

>如果使用Mac系統，請使用手動安裝方式安裝(詳細方式請參考手動安裝)

## 安裝
### 簡易安裝
1. 以系統管理員的身分打開Blender
2. 打開 **Edit-> Preferences**
3. 在左側的欄位中點選**Add-ons**
4. 點選右上的**Install** ，選取插件的壓縮檔並安裝
5. 如果插件已經安裝完畢，在右上的搜尋欄中搜尋插件名稱並打開此插件左方的下三角形
6. 點選**install dependencies**

### 手動安裝
1. 以系統管理員身分打開Blender
2. 點選**Scripting**的工作區並在**command line**(預設於左邊的中間高度)輸入以下程式:
```python
import sys
sys.exec_prefix
```
3. 將結果複製下來
4. 以系統管理員的身份打開終端機(cmd)並輸入以下指令:
```
cd (剛剛複製的位址)/bin
python -m ensurepip
python -m pip install pillow
```

## 功能
### Paper Tools
> Paper Tools 能夠生成並渲染動畫用的紙張，並套用至攝影機背景以方便構圖，支援使用安全區及留白等畫框。

主要有以下參數可調整:
1. Paper Size:
 + 同 Clip Studio 中的基準尺寸。能夠調整紙張的基本尺寸。
2. Title Safe Area:
 + 同 Clip Studio 中的演出畫格。為 Paper Size 的向內延伸。
 + 可單獨關閉此區域是否顯示或渲染
3. Overflow Area:
 + 同 Clip Studio 中的作畫尺寸。
 + 可單獨關閉此區域是否顯示或渲染
4. Blank Space:
 + 同 Clip Studio 中的餘白
 + 可單獨關閉此區域是否顯示或渲染

+ 設定完成後必須按下Generate以更新畫紙

### Output Tools
> Output Tools 能夠依需求輸出動畫序列，並自定義序列命名方式、檔案類型和渲染方式。

#### Basic setting
Basic setting 能夠設定如何選擇關鍵禎並加以渲染的方式。
主要有以下參數可調整:
1. Render Type
 1. Default: 照Blender 預設的方式渲染 (選定起始禎和結束禎，並設定間隔)。
 2. Keyframe of Selected Objects: 將所選取物件中所建立的關鍵禎都進行渲染。
 3. Selected Keyframe: 將在Dope Sheet 中所選取的所有關鍵禎都進行渲染。
 4. All of Keyframe: 將所有關鍵禎進行渲染。
2. Frame Start: 起始禎，只有在Render Type 為Default 時有效。
3. Frame End: 結束禎，只有在Render Type 為Default 時有效。
3. Step: 間隔，只有在Render Type 為Default 時有效。

#### File Setting
File Setting 能夠設定輸出序列的位置、命名方式、檔案格式及色彩深度。
1. Output Path: 指定序列的輸出位置。
2. Name: 指定序列命名方式，用#可代表序列數字應該擺放的位置。`ex: 命名為abc###時，序列為abc001,abc002,abc003...以此類推`
3. Color Depth: 設定色彩深度(此功能有些Bug, 如需詳細調整請使用Blender所提供的方式)
4. Format: 設定檔案檔案格式。

#### Scanner Setting
Scanner Setting 能夠設定渲染設定，如:紙張渲染、二值化
1. Render Paper: 可以選擇是否渲染紙張
2. Binirization: 可以選擇是否進行二值化
 + 使用時請確保渲染出來時背景為全白。
 + 可依照顏色進行二值化的閥值控制。
### AniTools Preset
#### Workspace
套用AniTools中所附設的工作區域預設。
#### Human
連結(Link)人物模型並將之Library Override。

