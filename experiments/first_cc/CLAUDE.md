# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm run dev       # 開発サーバー起動 (http://localhost:5173)
npm run build     # TypeScript型チェック + Viteビルド
npm run preview   # ビルド結果をプレビュー
npm run test      # Vitestでテスト実行
npx tsc --noEmit  # 型チェックのみ
```

## Architecture

React + TypeScript + Vite + Tailwind CSS のシングルページTODOアプリ。

**状態管理:** `src/hooks/useTodos.ts` に全ロジックを集約。`localStorage` に永続化。フィルタ状態もこのフックが管理する。

**データフロー:** `App.tsx` が `useTodos` を呼び出し、各コンポーネントにpropsとして渡す。状態のリフトアップは `App` 止まり。

**コンポーネント構成:**
- `TodoInput` — 入力欄 + 一括完了ボタン(「❯」)
- `TodoItem` — 個別TODO。ダブルクリックで編集モード、Enter/blurで保存、Escでキャンセル
- `TodoList` — リストレンダリング + 空フィルタ時のフォールバック表示
- `TodoFilter` — フィルタ切替(すべて/未完了/完了済み) + 「完了を削除」ボタン

**型定義:** `src/types/todo.ts` の `Todo` インターフェースと `FilterType` Union型が全体で共有される。
