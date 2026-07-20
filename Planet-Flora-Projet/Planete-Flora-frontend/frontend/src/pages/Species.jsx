import PlantCard from "../components/PlantCard";

export default function Species() {
  const plants = [
    { name: "Monstera", family: "Araceae" },
    { name: "Ficus", family: "Moraceae" },
    { name: "Palmier", family: "Arecaceae" }
  ];

  return (
    <div className="max-w-6xl mx-auto p-8">
      <h1 className="text-3xl font-bold mb-6">Catalogue</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {plants.map((p, i) => (
          <PlantCard key={i} plant={p} />
        ))}
      </div>
    </div>
  );
}