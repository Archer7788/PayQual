import axios from "axios";
function ReportsTable({ history }) {
const handleExport = async (id) => {

  try {

    const response = await axios.get(
      `http://127.0.0.1:8000/export/${id}`,
      {
        responseType: "blob",
      }
    );

    const url = window.URL.createObjectURL(
      new Blob([response.data])
    );

    const link = document.createElement("a");

    link.href = url;

    link.setAttribute(
      "download",
      `report_${id}.pdf`
    );

    document.body.appendChild(link);

    link.click();

    link.remove();

  } catch (error) {

    console.error(
      "Export failed",
      error
    );
  }
};
  return (

    <div className="
      bg-white
      shadow-lg
      rounded-2xl
      p-6
    ">

      <h2 className="text-2xl font-semibold mb-6">
        Historical Reports
      </h2>

      <div className="overflow-x-auto">

        <table className="
          min-w-full
          border
          border-gray-200
        ">

          <thead className="bg-gray-100">

            <tr>

              <th className="p-3 border">
                ID
              </th>

              <th className="p-3 border">
                Filename
              </th>

              <th className="p-3 border">
                Completeness
              </th>

              <th className="p-3 border">
                Uniqueness
              </th>

              <th className="p-3 border">
                Consistency
              </th>

              <th className="p-3 border">
                Overall
              </th>
              <th className="p-3 border">
                 Export
              </th>

            </tr>

          </thead>

          <tbody>

            {
              history.map((item) => (

                <tr
                  key={item.id}
                  className="text-center"
                >

                  <td className="p-3 border">
                    {item.id}
                  </td>

                  <td className="p-3 border">
                    {item.filename}
                  </td>

                  <td className="p-3 border">
                    {item.completeness_score}
                  </td>

                  <td className="p-3 border">
                    {item.uniqueness_score}
                  </td>

                  <td className="p-3 border">
                    {item.consistency_score}
                  </td>

                  <td className="
                    p-3
                    border
                    font-bold
                  ">
                    {item.overall_quality_score}
                  </td>
                   <td className="p-3 border">

  <button
    onClick={() =>
      handleExport(item.id)
    }
    className="
      bg-blue-600
      text-white
      px-4
      py-2
      rounded-lg
      hover:bg-blue-700
    "
  >
    Export
  </button>

</td>
                </tr>

              ))
            }

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default ReportsTable;