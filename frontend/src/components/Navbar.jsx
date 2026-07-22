import { Bell, Clock3 } from "lucide-react";

export default function Navbar() {

  const today = new Date().toLocaleString();

  return (
    <div className="h-16 bg-slate-900 border-b border-slate-700 flex items-center justify-between px-6">

      <div>
        <h1 className="text-2xl font-bold">
          AI Exam Invigilation System
        </h1>
      </div>

      <div className="flex items-center gap-8">

        <div className="flex items-center gap-2 text-gray-300">
          <Clock3 size={18}/>
          {today}
        </div>

        <div className="flex items-center gap-2">

          <Bell className="text-yellow-400"/>

          <span className="bg-green-600 px-3 py-1 rounded-full text-sm">
            System Online
          </span>

        </div>

      </div>

    </div>
  );
}