# 作答資料

- 學號：3B417025
- 姓名：曾湣皓

## 第 2 題：Git 的三個版本

請填寫完成第二步後，`version.txt` 在三個位置中的內容。

- 已提交版本：v1
- 暫存區版本：v2
- 工作區版本：v3

### 使用的 Git 指令

請填寫你用來確認三種差異的 Git 指令。

1. 工作區 vs 暫存區：
git diff -- version.txt
   ```bash
   C:\vs code\git-quiz1>git diff -- version.txt
diff --git a/version.txt b/version.txt
index 8c1384d..b3b9677 100644
--- a/version.txt
+++ b/version.txt
@@ -1 +1,2 @@
-v2
+v3
+
   ```

2. 暫存區 vs 上一次 commit：
git diff --cached -- version.txt
   ```bash
   C:\vs code\git-quiz1>git diff --cached -- version.txt
diff --git a/version.txt b/version.txt
index 626799f..8c1384d 100644
--- a/version.txt
+++ b/version.txt
@@ -1 +1 @@
-v1
+v2
   ```

3. 工作區 vs 上一次 commit：
git diff HEAD -- version.txt
   ```bash
   C:\vs code\git-quiz1>git diff HEAD -- version.txt
diff --git a/version.txt b/version.txt
index 626799f..b3b9677 100644
--- a/version.txt
+++ b/version.txt
@@ -1 +1,2 @@
-v1
+v3
+
   ```

## 完成前自我檢查

- [ok ] 我保留了題目專案原本的 Git commit 歷史。
- [ok ] `.vscode` 已從目前版本開始停止追蹤，但本機檔案仍保留。
- [ok ] `version.txt` 的 Git 歷史依序為 `v1 → v2 → v3`。
- [ok ] 程式修正與文件修改分成不同的 commit。
- [ok ] `python app.py` 執行後平均為 `72.6`。
- [ok ] 我已確認 `git status` 沒有尚未處理的變更。
- [ok ] 我已把完成結果推送到自己的 GitHub Repository。
