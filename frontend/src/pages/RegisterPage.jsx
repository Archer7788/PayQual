import { useState } from "react";
import axios from "axios";

export default function RegisterPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();

    try {
      await axios.post(
        "https://payqual-backend.onrender.com/register",
        {
          username,
          password,
        }
      );

     alert("Registration successful");

window.location.reload();
    } catch (error) {

  if (
    password.length < 6
  ) {

    alert(
      "Password must be at least 6 characters long"
    );

  } else if (
    username.length < 3
  ) {

    alert(
      "Username must be at least 3 characters long"
    );

  } else {

    alert(
      "Registration failed. Username may already exist."
    );

  }
}
  };

  return (
    <div className="min-h-screen flex justify-center items-center bg-gray-100">
      <form
        onSubmit={handleRegister}
        className="bg-white p-8 rounded shadow-md w-96"
      >
        <h2 className="text-2xl font-bold mb-6">
          Register
        </h2>

        <input
          className="border p-2 w-full mb-4"
          placeholder="Username"
          value={username}
          onChange={(e) =>
            setUsername(e.target.value)
          }
        />

        <input
          className="border p-2 w-full mb-4"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <button
          className="bg-green-600 text-white p-2 rounded w-full"
          type="submit"
        >
          Register
        </button>
      </form>
    </div>
  );
}