import "./index.css";
import { TodoForm } from './components/TodoForm';
import { TodoList } from "./components/TodoList";
import { useState } from "react";


export function App() {

  const [todos, setTodos] = useState<Array<Todo>>([]);
  const toggleComplete: ToggleComplete = selectedTodo => {
    const updatedTodos = todos.map(todo => {
      if (todo == selectedTodo){
        return {...todo, complete: !todo.complete};
      }
      return todo;
    });
    setTodos(updatedTodos);
  };
  const addTodo: AddTodo = newTodo => {
    if (newTodo !== "") {
      setTodos([...todos, { text: newTodo, complete: false }]);
    }
  };
  const editTodo: EditTodo = (selectedTodo, editText) => {
    const updatedTodos = todos.map(todo => {
      if (todo == selectedTodo){
        return {...todo, text: editText}
      }
      return todo;
    });
    setTodos(updatedTodos);
  }


  return (
    <div className="todo-app">
      <h1>a todo app</h1>
      <TodoForm addTodo={addTodo}/>
      <TodoList todos={todos} toggleComplete={toggleComplete}/>
    </div>
  );
};

export default App;
