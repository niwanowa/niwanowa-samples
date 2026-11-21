import { FilterType } from '../types/todo'

interface Props {
  filter: FilterType
  setFilter: (f: FilterType) => void
  activeCount: number
  completedCount: number
  onClearCompleted: () => void
}

const FILTERS: { label: string; value: FilterType }[] = [
  { label: 'すべて', value: 'all' },
  { label: '未完了', value: 'active' },
  { label: '完了済み', value: 'completed' },
]

export function TodoFilter({
  filter,
  setFilter,
  activeCount,
  completedCount,
  onClearCompleted,
}: Props) {
  return (
    <div className="flex items-center justify-between px-4 py-3 text-sm text-gray-500 border-t border-gray-100">
      <span className="min-w-[80px]">
        {activeCount} 件残り
      </span>

      <div className="flex gap-1">
        {FILTERS.map(({ label, value }) => (
          <button
            key={value}
            onClick={() => setFilter(value)}
            className={`px-2.5 py-1 rounded border transition-colors ${
              filter === value
                ? 'border-violet-300 text-violet-600'
                : 'border-transparent hover:border-gray-200 text-gray-500 hover:text-gray-700'
            }`}
          >
            {label}
          </button>
        ))}
      </div>

      {completedCount > 0 ? (
        <button
          onClick={onClearCompleted}
          className="min-w-[80px] text-right text-gray-400 hover:text-red-400 transition-colors"
        >
          完了を削除
        </button>
      ) : (
        <span className="min-w-[80px]" />
      )}
    </div>
  )
}
