import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import { useState } from "react";

export default function AppLayout({ children }) {
    
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="flex min-h-screen bg-gray-50">

      {/* Sidebar */}
      <Sidebar />

      {/* Main content */}
      <div className="flex-1 flex flex-col">

        <Navbar />

        <main className="p-6">
          {children}
        </main>

      </div>

    </div>
    
  );
  
}