import { useState } from "react";
import { createTask } from "../api";

export default function TaskForm() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [dueDatetime, setDueDatetime] = useState("");
  const [status, setStatus] = useState("pending");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");

    try {
      const task = { title, description, due_datetime: dueDatetime, status };
      const createdTask = await createTask(task);
      setMessage(`Task "${createdTask.title}" created successfully!`);
      setTitle(""); setDescription(""); setDueDatetime(""); setStatus("pending");
    } catch (err) {
      setMessage(err.message);
    }
  };

  return (
    <div>
      <h2>Create Task</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <input
          type="datetime-local"
          value={dueDatetime}
          onChange={(e) => setDueDatetime(e.target.value)}
          required
        />
        <button type="submit">Create Task</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
