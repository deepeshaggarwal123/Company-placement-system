<!-- frontend/src/App.vue -->
<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App"
}
</script>

<style>
/* Global Premium Design System Styles with Blue & Green theme */
:root {
  --primary-blue: #0ea5e9;
  --primary-blue-hover: #0284c7;
  --primary-green: #10b981;
  --primary-green-hover: #059669;
  --dark-slate: #0f172a;
  --light-slate: #f8fafc;
  --border-color: #e2e8f0;
  
  --glass-bg: rgba(255, 255, 255, 0.85);
  --glass-border: rgba(255, 255, 255, 0.4);
  --glass-shadow: 0 8px 32px 0 rgba(14, 165, 233, 0.08);
}

body {
  margin: 0;
  font-family: 'Inter', sans-serif;
  background-color: var(--light-slate);
  color: var(--dark-slate);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Glassmorphism styling helpers */
.glass-card {
  background: var(--glass-bg);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  box-shadow: var(--glass-shadow);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.glass-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px 0 rgba(16, 185, 129, 0.12);
}

/* Modern inputs */
.custom-form-control {
  border: 2px solid var(--border-color);
  border-radius: 10px;
  padding: 12px 16px;
  transition: all 0.3s ease;
}

.custom-form-control:focus {
  border-color: var(--primary-blue);
  box-shadow: 0 0 0 4px rgba(14, 165, 233, 0.15);
  outline: none;
}

/* Custom buttons */
.btn-blue {
  background: linear-gradient(135deg, var(--primary-blue) 0%, #38bdf8 100%);
  border: none;
  color: white;
  font-weight: 600;
  border-radius: 10px;
  padding: 10px 20px;
  transition: all 0.3s ease;
}

.btn-blue:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(14, 165, 233, 0.3);
  color: white;
}

.btn-green {
  background: linear-gradient(135deg, var(--primary-green) 0%, #34d399 100%);
  border: none;
  color: white;
  font-weight: 600;
  border-radius: 10px;
  padding: 10px 20px;
  transition: all 0.3s ease;
}

.btn-green:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.3);
  color: white;
}

.table-premium {
  border-collapse: separate;
  border-spacing: 0 8px;
}

.table-premium tr {
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.02);
  transition: transform 0.2s ease;
}

.table-premium tr:hover {
  transform: scale(1.005);
}

.table-premium td, .table-premium th {
  border: none;
  padding: 16px;
  vertical-align: middle;
}

.table-premium th {
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  font-size: 0.75rem;
  letter-spacing: 0.05em;
  padding-bottom: 4px;
}
</style>