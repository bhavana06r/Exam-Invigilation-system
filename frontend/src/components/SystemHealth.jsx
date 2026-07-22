import {
  Server,
  Cpu,
  Wifi,
  ShieldCheck,
  Camera,
  Mic,
} from "lucide-react";

export default function SystemHealth({ status }) {
  const services = [
    {
      name: "Backend API",
      icon: <Server size={18} />,
      state: "Online",
      color: "bg-green-500",
    },
    {
      name: "Frontend",
      icon: <Wifi size={18} />,
      state: "Connected",
      color: "bg-green-500",
    },
    {
      name: "Phone Detection",
      icon: <Camera size={18} />,
      state: status.phones > 0 ? "Running" : "Waiting",
      color: status.phones > 0 ? "bg-green-500" : "bg-yellow-500",
    },
    {
      name: "Talking Detection",
      icon: <Mic size={18} />,
      state: status.talking ? "Running" : "Waiting",
      color: status.talking ? "bg-green-500" : "bg-yellow-500",
    },
    {
      name: "Gesture Detection",
      icon: <Cpu size={18} />,
      state: status.gesture ? "Running" : "Waiting",
      color: status.gesture ? "bg-green-500" : "bg-yellow-500",
    },
    {
      name: "AI Monitor",
      icon: <ShieldCheck size={18} />,
      state: "Active",
      color: "bg-green-500",
    },
  ];

  return (
    <div className="bg-slate-900 rounded-xl p-5 shadow-xl border border-slate-700">
      <h2 className="text-xl font-bold mb-5">
        🖥 AI System Health
      </h2>

      <div className="space-y-4">
        {services.map((service) => (
          <div
            key={service.name}
            className="flex items-center justify-between bg-slate-800 rounded-lg p-3 hover:bg-slate-700 transition"
          >
            <div className="flex items-center gap-3">
              {service.icon}
              <span>{service.name}</span>
            </div>

            <div className="flex items-center gap-2">
              <span
                className={`w-3 h-3 rounded-full ${service.color} animate-pulse`}
              ></span>
              <span className="text-sm font-semibold">
                {service.state}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}