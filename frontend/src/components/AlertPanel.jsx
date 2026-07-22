export default function AlertPanel({ status }) {
  return (
    <div className="bg-slate-900 rounded-xl h-[420px] p-5">
      <h2 className="text-xl font-bold mb-5">
        🚨 Live Alerts
      </h2>

      <div className="space-y-4">

        {status.phones > 0 && (
          <div className="bg-red-500/20 border border-red-500 p-3 rounded-lg">
            📱 {status.phones} Mobile Phone Detected
          </div>
        )}

        {status.talking && (
          <div className="bg-yellow-500/20 border border-yellow-500 p-3 rounded-lg">
            🗣 Talking Detected
          </div>
        )}

        {status.gesture && (
          <div className="bg-orange-500/20 border border-orange-500 p-3 rounded-lg">
            ✋ Suspicious Hand Gesture
          </div>
        )}

        {status.phones === 0 &&
          !status.talking &&
          !status.gesture && (
            <div className="bg-green-500/20 border border-green-500 p-3 rounded-lg">
              ✅ No Violations Detected
            </div>
          )}

      </div>
    </div>
  );
}