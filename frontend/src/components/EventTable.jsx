export default function EventTable() {

  return (

    <div className="bg-slate-900 rounded-xl p-5">

      <h2 className="text-xl font-bold mb-5">

        Event History

      </h2>

      <table className="w-full">

        <thead className="text-left border-b border-slate-700">

          <tr>

            <th className="py-3">Time</th>

            <th>Event</th>

            <th>Status</th>

          </tr>

        </thead>

        <tbody>

          <tr className="border-b border-slate-800">

            <td className="py-4">10:22 AM</td>

            <td>📱 Phone Detected</td>

            <td className="text-red-400">High</td>

          </tr>

          <tr>

            <td className="py-4">10:25 AM</td>

            <td>🗣 Talking</td>

            <td className="text-yellow-400">Medium</td>

          </tr>

        </tbody>

      </table>

    </div>

  );

}