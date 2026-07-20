export default function PlantCard({ plant }) {
  return (
    <div className="bg-white rounded-2xl shadow hover:shadow-lg transition p-5 border">
      <h2 className="font-bold text-lg">{plant.name}</h2>
      <p className="text-gray-500">{plant.family}</p>
    </div>
  );
}