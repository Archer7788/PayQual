function Recommendations({ report }) {

  return (
      
    <div className="
      bg-white
      shadow-lg
      rounded-2xl
      p-6
    ">

      <h2 className="text-2xl font-semibold mb-4">
        AI Recommendations
      </h2>

      <ul className="space-y-3">

        {
          report.quality_report
          .recommendations
          .map((rec, index) => (

            <li
              key={index}
              className="
                bg-yellow-100
                p-4
                rounded-lg
              "
            >
              {rec}
            </li>

          ))
        }

      </ul>
        <div className="
  mt-6
  bg-blue-50
  p-4
  rounded-xl
">

  <h3 className="
    text-xl
    font-bold
    mb-2
  ">
    AI Executive Summary
  </h3>

  <p className="text-gray-700">
    {report.ai_summary}
  </p>

</div>
    </div>
    
  );
}

export default Recommendations;