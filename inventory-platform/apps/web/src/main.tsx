import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom'; // <<< Import useLocation
import { AnimatePresence, motion } from 'framer-motion';

import './index.css';
import Login from './login/Login.tsx';
import Register from './register/Register.tsx';
import Dashboard from './dashboard/Dashboard.tsx';

function App() {
  const location = useLocation();

  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={location.pathname}
        initial={{ opacity: 0, x: 100 }}
        animate={{ opacity: 1, x: 0 }}
        exit={{ opacity: 0, x: -100 }}
        transition={{ duration: 0.3 }}
        style={{ height: '100%' }}
      >
        <Routes location={location}>
          <Route path="/" element={<Login />} />
          <Route path="/signup" element={<Register />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </motion.div>
    </AnimatePresence>
  );
}

createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
);