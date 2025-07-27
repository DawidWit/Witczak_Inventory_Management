import React, { useState } from "react";
import styles from "./Login.module.css";
import { FaEnvelope, FaKey } from "react-icons/fa";
import { useNavigate } from "react-router-dom";

const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (event: React.FormEvent) => {
    event.preventDefault();
    const apiUrl = "http://localhost:8000/api/v1/auth/login";

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          password: password,
        }),
      });

      if (response.ok) {
        await response.json().then((data) => {
          localStorage.setItem('token', data.access_token)
        });
        setEmail('');
        setPassword('');
        navigate('/dashboard');
      } else {
        alert(`Login failed:`);
      }
    } catch (error) {
      console.error("Network error during registration:", error);
      alert("Could not connect to the server. Please try again later.");
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.left}>
        <h1 className={styles.title}>Inventory Management</h1>
        <p className={styles.subtitle}>One app to manage all your resources</p>
        <form className={styles.form}>
          <div className={styles['input-container']}>
            <div className={styles['input-wrapper']} >
              <FaEnvelope color="#2b7349" size="24px" />
              <input type="email" className={styles['input-field']} placeholder="e-mail" value={email} onChange={(e) => setEmail(e.target.value)} />
            </div>
            <div className={styles['input-wrapper']}>
              <FaKey color="#2b7349" size="24px" />
              <input type="password" className={styles['input-field']} placeholder="password" value={password}
                onChange={(e) => setPassword(e.target.value)} />
            </div>
          </div>
          <button className={styles.loginBtn} type="submit" onClick={handleLogin}>LOGIN</button>
        </form>
        <p className={styles.register}>
          Need an account? <a href="/signup">Create an account</a>
        </p>
      </div>
      <div className={styles.right} />
    </div>
  );
};

export default Login;
