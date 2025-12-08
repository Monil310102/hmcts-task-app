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
      const task = { title, description, due_datetime: dueDatetime,  status: "pending"  };
      const createdTask = await createTask(task);

      const msg = `Success: Task "${createdTask.title}" created!\nDetails:
- Description: ${createdTask.description || "-"}
- Due: ${createdTask.due_datetime}
- Status: ${createdTask.status}`;

      setMessage(msg);

      // Reset form
      setTitle("");
      setDescription("");
      setDueDatetime("");
      setStatus("pending");
    } catch (err) {
      setMessage(`Error: ${err.message}`);
    }
  };

  return (
    <div>
      <h2>Create Task</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <h3>Title</h3>
          <input
            type="text"
            placeholder="Enter title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>

        <div>
          <h3>Description</h3>
          <input
            type="text"
            placeholder="Enter description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>

        <div>
          <h3>Due Date & Time</h3>
          <input
            type="datetime-local"
            value={dueDatetime}
            onChange={(e) => setDueDatetime(e.target.value)}
            required
          />
        </div>

        <button type="submit">Create Task</button>
      </form>

      {message && (
        <div>
          <h3>Message</h3>
          <pre>{message}</pre>
        </div>
      )}
    </div>
  );
}
