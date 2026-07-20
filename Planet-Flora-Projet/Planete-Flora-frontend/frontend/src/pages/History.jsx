import { useEffect, useState } from "react";
import api from "../services/api";

export default function History() {
  const [data, setData] = useState([]);

  useEffect(() => {
    api.get("/history").then(res => setData(res.data));
  }, []);

  return (
    <div className="p-6">

      <h1 className="text-2xl font-bold mb-4">
        Historique
      </h1>

      {data.map((item, i) => (
        <div key={i} className="p-4 bg-white shadow rounded mb-2">

          <p className="font-bold">{item.species}</p>
          <p>Confidence: {item.confidence}</p>

        </div>
      ))}

    </div>
  );
}

