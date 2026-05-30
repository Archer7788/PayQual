import { useState, useEffect } from "react";

import axios from "axios";

import UploadSection from "./components/UploadSection";
import OverviewCards from "./components/OverviewCards";
import QualityChart from "./components/QualityChart";
import Recommendations from "./components/Recommendations";
import ReportsTable from "./components/ReportsTable";
import ValidationResults from "./components/ValidationResults";

function App() {

  const [file, setFile] = useState(null);

  const [report, setReport] = useState(null);

  const [history, setHistory] = useState([]);

  const chartData = report
    ? [
        {
          name: "Completeness",
          score:
            report.quality_report
            .completeness_score,
        },
        {
          name: "Uniqueness",
          score:
            report.quality_report
            .uniqueness_score,
        },
        {
          name: "Consistency",
          score:
            report.quality_report
            .consistency_score,
        },
        {
          name: "Overall",
          score:
            report.quality_report
            .overall_quality_score,
        },
      ]
    : [];

  useEffect(() => {

    fetchReports();

  }, []);

  const fetchReports = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/reports"
      );

      setHistory(response.data);

    } catch (error) {

      console.error(
        "Failed to fetch reports",
        error
      );
    }
  };

  const handleFileChange = (event) => {

    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {

    if (!file) {

      alert("Please select a file");

      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/analyze",
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data",
          },
        }
      );

      setReport(response.data);

      fetchReports();

    } catch (error) {

      console.error(error);

      alert("Upload failed");
    }
  };

  return (

    <div className="
      min-h-screen
      bg-gray-100
      p-10
    ">

      <div className="max-w-5xl mx-auto">

        <h1 className="
          text-4xl
          font-bold
          mb-8
          text-center
          text-blue-700
        ">
          PayQual Dashboard
        </h1>

        <UploadSection
          handleFileChange={
            handleFileChange
          }
          handleUpload={handleUpload}
        />

        {report && (

          <div className="space-y-6">

            <OverviewCards
              report={report}
            />

            <QualityChart
              chartData={chartData}
            />
            <ValidationResults
              report={report}
/>
            <Recommendations
              report={report}
            />

          </div>

        )}

        <div className="mt-8">

          <ReportsTable
            history={history}
          />

        </div>

      </div>

    </div>
  );
}

export default App;