export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center text-center px-6">

      <h1 className="text-5xl font-bold mb-4">
        🌿 Planet Flora
      </h1>

      <p className="text-gray-600 text-lg max-w-xl">
        Identifiez instantanément n’importe quelle plante grâce à l’intelligence artificielle.
      </p>

      <div className="mt-8 flex gap-4">
        <a href="/predict" className="px-6 py-3 bg-black text-white rounded-xl">
          Commencer
        </a>

        <a href="/species" className="px-6 py-3 border rounded-xl">
          Explorer
        </a>
      </div>

    </div>
  );
}