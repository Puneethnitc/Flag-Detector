function RewriteResult({ rewrittenBio }) {
  if (!rewrittenBio) return null;

  return (
    <div
      style={{
        marginTop: "2rem",
        padding: "1rem",
        background: "#f8fafc",
        borderRadius: "12px",
        border: "1px solid #e5e7eb",
      }}
    >
      <h2>Improved Bio</h2>
      <p style={{ fontSize: "15px", lineHeight: 1.6 }}>{rewrittenBio}</p>
    </div>
  );
}

export default RewriteResult;
