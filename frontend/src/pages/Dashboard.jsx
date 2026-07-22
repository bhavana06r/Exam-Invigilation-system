import { useEffect, useState } from "react";
import API from "../services/api";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import StatusCard from "../components/StatusCard";
import LiveFeed from "../components/LiveFeed";
import AlertPanel from "../components/AlertPanel";
import EventTable from "../components/EventTable";
import SystemHealth from "../components/SystemHealth";
import AnalyticsChart from "../components/AnalyticsChart";
import ReportButton from "../components/ReportButton";

export default function Dashboard() {
  const [status, setStatus] = useState({
    students: 0,
    phones: 0,
    talking: false,
    gesture: false,
  });

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const res = await API.get("/status");
        setStatus(res.data);
      } catch (err) {
        console.error(err);
      }
    };

    // Load data immediately
    fetchStatus();

    // Auto refresh every 2 seconds
    const interval = setInterval(fetchStatus, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-white flex">
      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <div className="flex-1">
        <Navbar />

        <div className="p-6">

          {/* Status Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

            <StatusCard
              title="Students"
              value={status.students}
            />

            <StatusCard
              title="Phones"
              value={status.phones}
            />

            <StatusCard
              title="Talking"
              value={status.talking ? "YES" : "NO"}
            />

            <StatusCard
              title="Gesture"
              value={status.gesture ? "YES" : "NO"}
            />

          </div>

          {/* Main Dashboard */}
          <div className="grid grid-cols-1 xl:grid-cols-3 gap-6 mt-6">

            {/* Left Side */}
            <div className="xl:col-span-2 space-y-6">

              <LiveFeed />

              <AnalyticsChart status={status} />

              <EventTable />
              <div className="mt-6">
  <ReportButton status={status} />
</div>

            </div>

            {/* Right Side */}
            <div className="space-y-6">

              <AlertPanel status={status} />

              <SystemHealth status={status} />

            </div>

          </div>

        </div>
      </div>""
    </div>
  );
}