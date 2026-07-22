import { jsPDF } from "jspdf";

export default function ReportButton({ status }) {
  const generateReport = () => {
    const doc = new jsPDF();

    doc.setFontSize(20);
    doc.text("AI Exam Invigilation Report", 20, 20);

    doc.setFontSize(12);

    doc.text(`Date : ${new Date().toLocaleString()}`, 20, 40);

    doc.text(`Students : ${status.students}`, 20, 55);

    doc.text(`Phones Detected : ${status.phones}`, 20, 70);

    doc.text(`Talking : ${status.talking ? "YES" : "NO"}`, 20, 85);

    doc.text(`Gesture : ${status.gesture ? "YES" : "NO"}`, 20, 100);

    const risk =
      status.phones > 0 || status.talking || status.gesture
        ? "HIGH"
        : "LOW";

    doc.text(`Overall Risk : ${risk}`, 20, 115);

    doc.text("System Status : ACTIVE", 20, 130);

    doc.save("AI_Exam_Report.pdf");
  };

  return (
    <button
      onClick={generateReport}
      className="w-full bg-blue-600 hover:bg-blue-700 transition rounded-lg py-3 font-semibold"
    >
      📄 Generate Report
    </button>
  );
}