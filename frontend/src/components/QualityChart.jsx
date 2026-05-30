import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

function QualityChart({ chartData }) {

  return (

    <div className="
      bg-white
      shadow-lg
      rounded-2xl
      p-6
    ">

      <h2 className="text-2xl font-semibold mb-6">
        Quality Analytics
      </h2>

      <div style={{ width: "100%", height: 400 }}>

        <ResponsiveContainer>

          <BarChart data={chartData}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="name" />

            <YAxis />

            <Tooltip />

            <Bar
              dataKey="score"
              fill="#2563eb"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}

export default QualityChart;