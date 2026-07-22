import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

export default function AnalyticsChart({ status }) {
  const data = [
    {
      name: "Phones",
      value: status.phones,
    },
    {
      name: "Talking",
      value: status.talking ? 1 : 0,
    },
    {
      name: "Gesture",
      value: status.gesture ? 1 : 0,
    },
  ];

  return (
    <div className="bg-slate-900 rounded-xl p-5 border border-slate-700 shadow-xl">
      <h2 className="text-xl font-bold mb-5">
        📊 Today's Analytics
      </h2>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
          <XAxis dataKey="name" stroke="#cbd5e1" />
          <YAxis stroke="#cbd5e1" />
          <Tooltip />
          <Bar dataKey="value" fill="#3b82f6" radius={[8,8,0,0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}