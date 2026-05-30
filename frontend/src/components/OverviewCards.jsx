function OverviewCards({ report }) {

  return (

    <div className="
      bg-white
      shadow-lg
      rounded-2xl
      p-6
    ">

      <h2 className="text-2xl font-semibold mb-4">
        Dataset Overview
      </h2>

      <div className="grid grid-cols-3 gap-4">

        <div className="
          bg-blue-100
          p-4
          rounded-xl
        ">
          <h3 className="font-bold">
            Filename
          </h3>

          <p>{report.filename}</p>
        </div>

        <div className="
          bg-green-100
          p-4
          rounded-xl
        ">
          <h3 className="font-bold">
            Rows
          </h3>

          <p>{report.rows}</p>
        </div>

        <div className="
          bg-purple-100
          p-4
          rounded-xl
        ">
          <h3 className="font-bold">
            Columns
          </h3>

          <p>{report.columns}</p>
        </div>

      </div>

    </div>
  );
}

export default OverviewCards;