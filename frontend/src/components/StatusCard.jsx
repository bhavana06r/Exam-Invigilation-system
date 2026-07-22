import {
  Users,
  Smartphone,
  MessageCircle,
  ShieldAlert
} from "lucide-react";

const icons = {
  Students: <Users size={28}/>,
  Phones: <Smartphone size={28}/>,
  Talking: <MessageCircle size={28}/>,
  Violations: <ShieldAlert size={28}/>
};

export default function StatusCard({ title, value }) {

  return (

    <div className="bg-slate-900 rounded-xl p-5 shadow-lg hover:scale-105 transition">

      <div className="flex justify-between">

        <div>

          <p className="text-gray-400">

            {title}

          </p>

          <h1 className="text-4xl font-bold mt-3">

            {value}

          </h1>

        </div>

        <div className="text-blue-400">

          {icons[title]}

        </div>

      </div>

    </div>

  );

}