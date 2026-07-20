import { useState } from "react";
import api from "../services/api";

export default function Predict() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  function handleFileChange(e) {
    const selected = e.target.files[0];

    setFile(selected);
    setResult(null);
    setError(null);

    if (selected) {
      setPreview(URL.createObjectURL(selected));
    }
  }

  async function handleSubmit() {
    if (!file) return;

    try {
      setLoading(true);
      setError(null);

      const formData = new FormData();
      formData.append("file", file);

      const res = await api.post("/predict", formData);

      setResult(res.data);
    } catch (err) {
      setError("Erreur lors de la prédiction");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold mb-4">
        Identifier une plante
      </h1>

      <input type="file" onChange={handleFileChange} />

      {preview && (
        <img
          src={preview}
          alt="preview"
          className="w-64 mt-4 rounded"
        />
      )}

      <button
        onClick={handleSubmit}
        className="mt-4 bg-green-600 text-white px-4 py-2"
      >
        {loading ? "Analyse..." : "Prédire"}
      </button>

      {error && <p className="text-red-500 mt-3">{error}</p>}

      {result && (
        <div className="mt-4">
          <h2>{result.species}</h2>
          <p>{result.confidence}</p>
        </div>
      )}
    </div>
  );
}