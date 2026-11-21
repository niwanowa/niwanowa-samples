import { useState, useRef, useEffect, KeyboardEvent } from 'react'
import { Todo } from '../types/todo'

interface Props {
  todo: Todo
  onToggle: (id: string) => void
  onDelete: (id: string) => void
  onEdit: (id: string, text: string) => void
}

export function TodoItem({ todo, onToggle, onDelete, onEdit }: Props) {
  const [editing, setEditing] = useState(false)
  const [editText, setEditText] = useState(todo.text)
  const inputRef = useRef<HTMLInputElement>(null)

  useEffect(() => {
    if (editing) {
      inputRef.current?.focus()
      inputRef.current?.select()
    }
  }, [editing])

  const startEdit = () => {
    setEditing(true)
    setEditText(todo.text)
  }

  const commitEdit = () => {
    onEdit(todo.id, editText)
    setEditing(false)
  }

  const cancelEdit = () => {
    setEditing(false)
    setEditText(todo.text)
  }

  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') commitEdit()
    if (e.key === 'Escape') cancelEdit()
  }

  return (
    <div className="group flex items-center gap-3 px-4 py-3 border-b border-gray-100 last:border-0 hover:bg-gray-50 transition-colors">
      <button
        onClick={() => onToggle(todo.id)}
        className={`flex-shrink-0 w-7 h-7 rounded-full border-2 flex items-center justify-center transition-all ${
          todo.completed
            ? 'bg-violet-500 border-violet-500'
            : 'border-gray-300 hover:border-violet-300'
        }`}
        aria-label={todo.completed ? '未完了に戻す' : '完了にする'}
      >
        {todo.completed && (
          <svg className="w-3.5 h-3.5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={3}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
          </svg>
        )}
      </button>

      {editing ? (
        <input
          ref={inputRef}
          type="text"
          value={editText}
          onChange={e => setEditText(e.target.value)}
          onBlur={commitEdit}
          onKeyDown={handleKeyDown}
          className="flex-1 outline-none border-b-2 border-violet-400 py-0.5 text-gray-800 bg-transparent text-base"
        />
      ) : (
        <span
          onDoubleClick={startEdit}
          className={`flex-1 text-base cursor-default select-none transition-colors ${
            todo.completed ? 'line-through text-gray-400' : 'text-gray-800'
          }`}
        >
          {todo.text}
        </span>
      )}

      <button
        onClick={() => onDelete(todo.id)}
        className="flex-shrink-0 w-6 h-6 flex items-center justify-center text-gray-300 hover:text-red-400 transition-all opacity-0 group-hover:opacity-100 text-xl leading-none"
        aria-label="削除"
      >
        ×
      </button>
    </div>
  )
}
