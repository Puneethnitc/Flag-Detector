import { useState } from "react";

function BioInput({ onAnalyze, loading }) {
  const [bio, setBio] = useState("");
  const [tone, setTone] = useState("confident");

  function handleSubmit() {
    if (!bio.trim()) return;
    onAnalyze(bio, tone);
  }

  return (
    <div>
      <h2>Enter Bio</h2>

      <textarea
        rows="5"
        style={{ width: "100%" }}
        placeholder="Enter dating bio here..."
        value={bio}
        onChange={(e) => setBio(e.target.value)}
      />

      <div style={{ marginTop: "1rem" }}>
        <label>Tone: </label>
        <select value={tone} onChange={(e) => setTone(e.target.value)}>
          <option value="confident">Confident</option>
          <option value="wholesome">Wholesome</option>
          <option value="funny">Funny</option>
          <option value="calm">Calm</option>
        </select>
      </div>

      <button
        style={{ marginTop: "1rem" }}
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? "Analyzing..." : "Analyze Bio"}
      </button>
    </div>
  );
}

export default BioInput;
