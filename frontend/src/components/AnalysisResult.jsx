function FlagChip({ label, type }) {
  const colors = {
    green: "#16a34a",
    yellow: "#ca8a04",
    red: "#dc2626",
  };

  return (
    <span
      style={{
        background: colors[type],
        color: "white",
        padding: "4px 10px",
        borderRadius: "999px",
        fontSize: "12px",
        marginRight: "8px",
      }}
    >
      {label}
    </span>
  );
}

function AnalysisResult({ analysis }) {
  if (!analysis) return null;

  const { green_flags, yellow_flags, red_flags, explanations } = analysis;

  return (
    <div style={{ marginTop: "2rem" }}>
      <h2>Analysis</h2>

      <div>
        <strong>Green:</strong>{" "}
        {green_flags.length
          ? green_flags.map((f) => (
              <FlagChip key={f} label={f} type="green" />
            ))
          : "None"}
      </div>

      <div style={{ marginTop: "0.5rem" }}>
        <strong>Yellow:</strong>{" "}
        {yellow_flags.length
          ? yellow_flags.map((f) => (
              <FlagChip key={f} label={f} type="yellow" />
            ))
          : "None"}
      </div>

      <div style={{ marginTop: "0.5rem" }}>
        <strong>Red:</strong>{" "}
        {red_flags.length
          ? red_flags.map((f) => (
              <FlagChip key={f} label={f} type="red" />
            ))
          : "None"}
      </div>

      {explanations && Object.keys(explanations).length > 0 && (
        <div style={{ marginTop: "1rem" }}>
          <h4>Why?</h4>
          {Object.entries(explanations).map(([label, words]) => (
            <p key={label}>
              <strong>{label}:</strong> {words.join(", ")}
            </p>
          ))}
        </div>
      )}
    </div>
  );
}

export default AnalysisResult;
