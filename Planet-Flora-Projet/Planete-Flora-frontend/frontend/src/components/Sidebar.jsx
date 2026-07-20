import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <div className="w-64 bg-white border-r min-h-screen p-4">

      <h1 className="text-xl font-bold mb-6">
        🌿 Planet Flora
      </h1>

      <nav className="flex flex-col gap-3 text-sm">

        <Link className="hover:text-green-600" to="/">
          🏠 Home
        </Link>

        <Link className="hover:text-green-600" to="/species">
          🌱 Species
        </Link>

        <Link className="hover:text-green-600" to="/predict">
          📸 Predict
        </Link>

        <Link className="hover:text-green-600" to="/dashboard">
          📊 Dashboard
        </Link>

        

      </nav>

    </div>
  );
}