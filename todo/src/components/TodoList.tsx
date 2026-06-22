import React from 'react';
import { TodoListItem } from './TodoListItem';

interface TodoListProps {
    todos: Array<Todo>;
    toggleComplete: ToggleComplete;
    editTodo: EditTodo;
}

export const TodoList: React.FC<TodoListProps> = ({ todos, toggleComplete, editTodo }) => {
    return (
        <ul>
            {todos.map(todo => (<TodoListItem
                key={todo.text}
                todo={todo}
                editTodo={editTodo}
                toggleComplete={toggleComplete} />
            ))}
        </ul>
    )
}