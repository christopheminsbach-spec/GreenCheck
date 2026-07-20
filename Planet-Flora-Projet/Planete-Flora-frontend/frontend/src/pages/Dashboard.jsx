export default function Dashboard() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">

      <div className="bg-white p-6 rounded-xl shadow">
        <h3 className="text-gray-500">Predictions</h3>
        <p className="text-2xl font-bold">128</p>
      </div>

      <div className="bg-white p-6 rounded-xl shadow">
        <h3 className="text-gray-500">Species détectées</h3>
        <p className="text-2xl font-bold">42</p>
      </div>

      <div className="bg-white p-6 rounded-xl shadow">
        <h3 className="text-gray-500">Précision moyenne</h3>
        <p className="text-2xl font-bold">91%</p>
      </div>

    </div>
  );
}