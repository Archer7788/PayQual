export default function ProtectedRoute({
  children,
}) {

  const token =
    sessionStorage.getItem("token")

  if (!token) {

    return null;
  }

  return children;
}