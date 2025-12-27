import { useState } from "react";
import BioInput from "./components/BioInput";
import AnalysisResult from "./components/AnalysisResult";
import RewriteResult from "./components/RewriteResult";
import Loader from "./components/Loader";
import './App.css'
import { classifyBio, rewriteBio } from "./api/bioApi";

function App() {
  const [analysis, setAnalysis] = useState(null);
  const [rewrittenBio, setRewrittenBio] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleAnalyze(bio, tone) {
    setLoading(true);
    setAnalysis(null);
    setRewrittenBio("");

    try {
      const analysisResult = await classifyBio(bio);
      setAnalysis(analysisResult);

      const rewriteResult = await rewriteBio(bio, tone);
      setRewrittenBio(rewriteResult.improved_bio);
    } catch (err) {
      alert("Something went wrong. Check backend.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container" style={{ maxWidth: "700px", margin: "auto", padding: "2rem" }}>
      <h1>AI Green / Red Flag Detector</h1>

      <BioInput onAnalyze={handleAnalyze} loading={loading} />

      {loading && <Loader />}

      <AnalysisResult analysis={analysis} />

      <RewriteResult rewrittenBio={rewrittenBio} />
    </div>
  );
}

export default App;
