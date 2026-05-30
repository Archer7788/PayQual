function UploadSection({
  handleFileChange,
  handleUpload
}) {

  return (

    <div className="
      bg-white
      shadow-lg
      rounded-2xl
      p-6
      mb-8
    ">

      <h2 className="text-2xl font-semibold mb-4">
        Upload Dataset
      </h2>

      <div className="flex gap-4">

        <input
          type="file"
          onChange={handleFileChange}
          className="
            border
            p-2
            rounded-lg
            w-full
          "
        />

        <button
          onClick={handleUpload}
          className="
            bg-blue-600
            text-white
            px-6
            py-2
            rounded-lg
            hover:bg-blue-700
          "
        >
          Analyze
        </button>

      </div>

    </div>
  );
}

export default UploadSection;