import { useState, KeyboardEvent } from 'react'

interface Props {
  onAdd: (text: string) => void
  onToggleAll: () => void
  allCompleted: boolean
  hasTodos: boolean
}

export function TodoInput({ onAdd, onToggleAll, allCompleted, hasTodos }: Props) {
  const [value, setValue] = useState('')

  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      onAdd(value)
      setValue('')
    }
  }

  return (
    <div className="flex items-center border-b border-gray-100">
      {hasTodos && (
        <button
          onClick={onToggleAll}
          className={`px-4 py-4 text-xl transition-colors ${
            allCompleted ? 'text-violet-500' : 'text-gray-300 hover:text-gray-400'
          }`}
          title="すべて完了にする"
        >
          ❯
        </button>
      )}
      <input
        type="text"
        value={value}
        onChange={e => setValue(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="タスクを入力してEnterキーを押してください..."
        className={`flex-1 py-4 text-gray-700 placeholder-gray-300 outline-none text-lg bg-transparent ${
          hasTodos ? 'pr-4' : 'px-4'
        }`}
        autoFocus
      />
    </div>
  )
}
