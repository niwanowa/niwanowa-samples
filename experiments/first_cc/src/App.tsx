import { useTodos } from './hooks/useTodos'
import { TodoInput } from './components/TodoInput'
import { TodoList } from './components/TodoList'
import { TodoFilter } from './components/TodoFilter'

export default function App() {
  const {
    todos,
    allTodos,
    filter,
    setFilter,
    addTodo,
    toggleTodo,
    deleteTodo,
    editTodo,
    toggleAll,
    clearCompleted,
    activeCount,
    completedCount,
  } = useTodos()

  const allCompleted = allTodos.length > 0 && allTodos.every(t => t.completed)

  return (
    <div className="min-h-screen bg-gradient-to-br from-violet-50 via-purple-50 to-indigo-100 flex flex-col items-center pt-16 px-4 pb-16">
      <div className="w-full max-w-lg">
        <h1 className="text-6xl font-thin text-center text-violet-300 mb-8 tracking-widest">
          todos
        </h1>

        <div className="bg-white rounded-xl shadow-2xl overflow-hidden">
          <TodoInput
            onAdd={addTodo}
            onToggleAll={toggleAll}
            allCompleted={allCompleted}
            hasTodos={allTodos.length > 0}
          />

          {allTodos.length > 0 && (
            <>
              <TodoList
                todos={todos}
                onToggle={toggleTodo}
                onDelete={deleteTodo}
                onEdit={editTodo}
              />
              <TodoFilter
                filter={filter}
                setFilter={setFilter}
                activeCount={activeCount}
                completedCount={completedCount}
                onClearCompleted={clearCompleted}
              />
            </>
          )}
        </div>

        {allTodos.length === 0 && (
          <p className="text-center text-gray-400 text-sm mt-6">
            タスクを入力してEnterで追加できます
          </p>
        )}
        {allTodos.length > 0 && (
          <p className="text-center text-gray-400 text-xs mt-4">
            テキストをダブルクリックで編集 · Escでキャンセル
          </p>
        )}
      </div>
    </div>
  )
}
