import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import styles from "./resetPassword.module.css"; // Import your CSS module

const ResetPassword = () => {
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const { token } = useParams(); // Extract token from the URL
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (newPassword !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }
    if (newPassword.length < 8) {
      setError("Password must be at least 8 characters long.");
      return;
    }

    setIsLoading(true);
    try {
      // Sending the request using fetch API
      const response = await fetch(`http://localhost:5000/auth/reset-password/${token}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          new_password: newPassword,
        }),
      });

      const result = await response.json(); // Parse the response as JSON

      if (response.ok) {
        setSuccess(result.message);
        setError("");
        setTimeout(() => navigate("/login"), 2000); // Redirect to login after success
      } else {
        setError(result.error || "Something went wrong.");
        setSuccess("");
      }
    } catch (err) {
      console.error("Error:", err);
      setError("Something went wrong.");
      setSuccess("");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.authContainer}>
      <div className={styles.authCard}>
        {/* Left Section */}
        <div className={styles.left}>
          <h2 className={styles.title}>Reset Password</h2>
          {error && <p className={styles.error}>{error}</p>}
          {success && <p className={styles.success}>{success}</p>}
          <form onSubmit={handleSubmit}>
            <input
              type="password"
              placeholder="New Password"
              aria-label="New Password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
              className={styles.input}
              required
            />
            <input
              type="password"
              placeholder="Confirm Password"
              aria-label="Confirm Password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              className={styles.input}
              required
            />
            <button type="submit" className={styles.btn} disabled={isLoading}>
              {isLoading ? "Processing..." : "Reset Password"}
            </button>
          </form>
        </div>

        {/* Right Section */}
        <div className={styles.right}>
          <h3 className={styles.welcomeBack}>Welcome Back!</h3>
          <p className={styles.resetMessage}>Reset your password and access your account quickly.</p>
        </div>
      </div>
    </div>
  );
};

export default ResetPassword;
