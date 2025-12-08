const BASE_URL = "http://127.0.0.1:8000"; // your FastAPI backend

export async function createTask(task) {
  const response = await fetch(`${BASE_URL}/tasks/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(task),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || "Something went wrong");
  }

  return response.json();
}