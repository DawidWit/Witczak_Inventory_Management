import React, { useState } from "react";
import styles from "./Register.module.css";
import { FaEnvelope, FaKey } from "react-icons/fa";
import { Link, useNavigate } from "react-router-dom";

const Register: React.FC = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleRegister = async (event: React.FormEvent) => {
        event.preventDefault();

        const apiUrl = "http://localhost:8000/api/v1/auth/register"; 

        try {
            console.log(email, password);
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
                const data = await response.json();
                console.log("Registration successful:", data);
                setEmail('');
                setPassword('');
                alert("Registration successful! You can now log in.");
                navigate('/');
            } else {
                const errorData = await response.json();
                console.error("Registration failed:", errorData);
                alert(`Registration failed: ${errorData.detail || 'Unknown error'}`);
            }
        } catch (error) {
            console.error("Network error during registration:", error);
            alert("Could not connect to the server. Please try again later.");
        }
    };

    return (
        <div className={styles.container}>
            <div className={styles.left} />
            <div className={styles.right}>
                <h1 className={styles.title}>Inventory Management</h1>
                <p className={styles.subtitle}>One app to manage all your resources</p>
                <form className={styles.form} onSubmit={handleRegister}>
                    <div className={styles['input-container']}>
                        <div className={styles['input-wrapper']} >
                            <FaEnvelope color="#2b7349" size="24px" />
                            <input
                                type="email"
                                className={styles['input-field']}
                                placeholder="e-mail"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                required
                            />
                        </div>
                        <div className={styles['input-wrapper']}>
                            <FaKey color="#2b7349" size="24px" />
                            <input
                                type="password"
                                className={styles['input-field']}
                                placeholder="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                        </div>
                    </div>
                    <button className={styles.loginBtn} type="submit">REGISTER</button>
                </form>
                <p className={styles.register}>
                    Already have an account? <Link to="/">Back to login</Link>
                </p>
            </div>
        </div>
    );
};

export default Register;