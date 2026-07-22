import { LayoutDashboard, FileText, Settings } from "lucide-react";

export default function Sidebar() {
  return (
    <div className="w-64 bg-slate-900 h-screen p-6">

      <h1 className="text-2xl font-bold text-blue-400 mb-10">
        AI Invigilator
      </h1>

      <div className="space-y-6">

        <div className="flex items-center gap-3 cursor-pointer hover:text-blue-400">
          <LayoutDashboard />
          Dashboard
        </div>

        <div className="flex items-center gap-3 cursor-pointer hover:text-blue-400">
          <FileText />
          Reports
        </div>

        <div className="flex items-center gap-3 cursor-pointer hover:text-blue-400">
          <Settings />
          Settings
        </div>

      </div>

    </div>
  );
}