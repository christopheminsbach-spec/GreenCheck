import { useState } from "react";
import api from "../services/api";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function handleLogin() {
    const res = await api.post("/login", {
      email,
      password
    });

    localStorage.setItem("token", res.data.access_token);
    alert("Logged in !");
  }

  return (
    <div className="flex flex-col gap-3 p-10 max-w-md mx-auto">

      <input
        placeholder="Email"
        className="border p-2"
        onChange={e => setEmail(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        className="border p-2"
        onChange={e => setPassword(e.target.value)}
      />

      <button
        onClick={handleLogin}
        className="bg-black text-white p-2 rounded"
      >
        Login
      </button>

    </div>
  );
}