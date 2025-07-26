import React from "react";
import styles from "./Login.module.css";
import { FaEnvelope, FaKey } from "react-icons/fa";

const Login: React.FC = () => {
  return (
    <div className={styles.container}>
      <div className={styles.left}>
        <div className={styles.box}>
          <h1 className={styles.title}>Inventory Management</h1>
          <p className={styles.subtitle}>One app to manage all your resources</p>
          <form className={styles.form}>
            <div className={styles.inputWrapper}>
              <FaEnvelope className={styles.icon} />
              <input type="email" placeholder="e-mail" />
            </div>
            <div className={styles.inputWrapper}>
              <FaKey className={styles.icon} />
              <input type="password" placeholder="password" />
            </div>
            <button className={styles.loginBtn} type="submit">LOGIN</button>
          </form>
          <p className={styles.register}>
            Need an account? <a href="/signup">Create an account</a>
          </p>
        </div>
      </div>
      <div className={styles.right} />
    </div>
  );
};

export default Login;
