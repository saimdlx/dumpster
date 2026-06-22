import React, { useState, type ChangeEvent, type SubmitEvent} from 'react';

interface TodoFormProps {
    addTodo: AddTodo;
}

export const TodoForm: React.FC<TodoFormProps> = ({addTodo}) => {

    const [newTodo, setTodo] = useState<string>("");
    const handleChange =  (e: ChangeEvent<HTMLInputElement>) => {
        setTodo(e.target.value);
    }
    const handleSubmit = (e: SubmitEvent<HTMLButtonElement>) => {
        e.preventDefault();
        addTodo(newTodo);
        setTodo("");
    }

    return (
        <form className='todo-form'>
            <input type="text" value={newTodo} onChange={handleChange} className='todo-input' />
            <button type="submit" onClick={handleSubmit} className='todo-button'>add todo</button>
        </form>
    )
}