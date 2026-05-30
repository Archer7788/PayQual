import { useState } from "react";
import axios from "axios";

export default function LoginPage({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        "https://payqual-backend.onrender.com/login",
        {
          username,
          password,
        }
      );

      sessionStorage.setItem(
  "token",
  response.data.access_token
);

      onLogin();
    } catch (err) {
      setError("Invalid username or password");
    }
  };

  return (
    <div className="min-h-screen flex justify-center items-center bg-gray-100">
      <form
        onSubmit={handleLogin}
        className="bg-white p-8 rounded shadow-md w-96"
      >
        <h2 className="text-2xl font-bold mb-6">
          PayQual Login
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

        {error && (
          <p className="text-red-500 mb-4">
            {error}
          </p>
        )}

        <button
          className="bg-blue-600 text-white p-2 rounded w-full"
          type="submit"
        >
          Login
        </button>
         <p className="text-center mb-4">
  Don't have an account?
</p>

<button
  type="button"
  className="
    text-blue-600
    mb-4
  "
  onClick={() =>
    window.dispatchEvent(
      new Event("show-register")
    )
  }
>
  Create Account
</button>
      </form>
    </div>
  );
}