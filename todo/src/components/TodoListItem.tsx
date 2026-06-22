import React, { useState, type ChangeEvent } from 'react';

interface TodoListItemProps {
    todo: Todo;
    toggleComplete: ToggleComplete;
    editTodo: EditTodo;
}

export const TodoListItem: React.FC<TodoListItemProps> = ({ todo, toggleComplete, editTodo }) => {
    const [isEditing, setEditing] = useState<boolean>(false);
    const [editText, setText] = useState<string>(todo.text);
    const handleEdit = () => {
        setEditing(true);
    }
    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        setText(e.target.value);
    }
    const handleSave = () => {
        editTodo(todo, editText);
        setEditing(false);
    }

    return (
        <li>
        <label className={todo.complete ? "todo-row completed" : "todo-row"}>
            <input
                type="checkbox"
                onChange={() => toggleComplete(todo)}
                checked={todo.complete}
            />
            {todo.text}
        </label>
        </li>
    )
}