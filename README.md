# Vibe Coding Test

AIを活用した開発環境（Vibe Coding）のテストプロジェクトです。

## 特徴

- Issue作成から自動ブランチ生成
- AIによるコード実装（Aider + Claude）
- 自動PR作成
- 自動テスト実行

## 使い方

1. Issueを作成する
   ```bash
   gh issue create -t "機能名" -b "詳細説明"
   ```

2. 自動生成されたブランチにスイッチ
   ```bash
   git fetch --all
   git switch issue/番号-機能名
   ```

3. Aiderでコード実装
   ```bash
   aider
   ```

4. 変更をプッシュすると自動的にPRが作成される
   ```bash
   git push -u origin HEAD
   ```

5. PRをレビューしてマージ

## 必要な環境

- Python 3.12
- Aider
- Git
- GitHub CLI
- Anthropic API Key

## ディレクトリ構成

- `.github/workflows/` - GitHub Actions設定
- `app.py` - FastAPIアプリケーション
- `test_app.py` - テストコード
- `.aider.conf` - Aider設定