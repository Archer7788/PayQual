function ValidationResults({
  report
}) {

  const validation =
    report.validation_results;

  return (

    <div className="
      bg-white
      shadow-lg
      rounded-2xl
      p-6
    ">

      <h2 className="
        text-2xl
        font-semibold
        mb-6
      ">
        Validation Results
      </h2>

      <div className="
        grid
        grid-cols-2
        gap-4
      ">

        <div className="
          bg-red-100
          p-4
          rounded-xl
        ">
          <h3 className="font-bold">
            Invalid Emails
          </h3>

          <p className="text-2xl">
            {
              validation.invalid_emails
            }
          </p>
        </div>

        <div className="
          bg-yellow-100
          p-4
          rounded-xl
        ">
          <h3 className="font-bold">
            Invalid Phones
          </h3>

          <p className="text-2xl">
            {
              validation.invalid_phones
            }
          </p>
        </div>

        <div className="
          bg-blue-100
          p-4
          rounded-xl
        ">
          <h3 className="font-bold">
            Duplicate Rows
          </h3>

          <p className="text-2xl">
            {
              validation.duplicate_rows
            }
          </p>
        </div>

        <div className="
          bg-purple-100
          p-4
          rounded-xl
        ">
          <h3 className="font-bold">
            Outliers
          </h3>

          <p className="text-2xl">
            {
              validation.outlier_count
            }
          </p>
        </div>

      </div>

    </div>
  );
}

export default ValidationResults;