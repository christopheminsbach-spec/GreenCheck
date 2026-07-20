import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 backdrop-blur-md bg-white/70 border-b">
      <div className="max-w-6xl mx-auto flex justify-between p-4">

        <div className="font-bold text-lg">
          🌿 Planet Flora
        </div>

        <div className="flex gap-6 text-sm">
          <Link className="hover:text-green-600" to="/">Home</Link>
          <Link className="hover:text-green-600" to="/species">Species</Link>
          <Link className="hover:text-green-600" to="/predict">Predict</Link>
        </div>

      </div>
    </nav>
  );
}