

const BASE_URL = "http://localhost:8000";


export async function classifyBio(bio) {
  const response = await fetch(`${BASE_URL}/classify`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ bio }),
  });

  if (!response.ok) {
    throw new Error("Failed to classify bio");
  }

  return response.json();
}


export async function rewriteBio(bio, tone = "confident") {
  const response = await fetch(`${BASE_URL}/rewrite`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ bio, tone }),
  });

  if (!response.ok) {
    throw new Error("Failed to rewrite bio");
  }

  return response.json();
}
