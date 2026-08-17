<template>
  <div class="login-page">
    <div class="login-container shadow-lg">
      
      <!-- Left side: Branding / Gradient -->
      <div class="login-brand d-none d-md-flex flex-column justify-content-center align-items-center text-white p-5">
        <h1 class="fw-bold mb-3 text-center">Placement Portal</h1>
        <p class="text-center lead mb-5">Empowering your career journey. Connect with top companies and unlock your potential.</p>
        <div class="brand-graphics d-flex">
          <i class="fas fa-graduation-cap fa-4x mx-3 animate-float"></i>
          <i class="fas fa-briefcase fa-4x mx-3 animate-float-delayed"></i>
        </div>
      </div>

      <!-- Right side: Form -->
      <div class="login-form-wrapper p-4 p-md-5">
        <div class="text-center mb-4 d-md-none">
          <h2 class="fw-bold text-primary">Placement Portal</h2>
        </div>
        <h3 class="fw-bold mb-1 text-dark">Welcome Back!</h3>
        <p class="text-muted mb-4">Please login to your account.</p>

        <form @submit.prevent="login">
          
          <div class="form-floating mb-3 custom-input">
            <input type="email" class="form-control" id="emailInput" v-model="form.email" placeholder="name@example.com" required />
            <label for="emailInput"><i class="fas fa-envelope me-2"></i>Email address</label>
          </div>

          <div class="form-floating mb-4 custom-input">
            <input type="password" class="form-control" id="passwordInput" v-model="form.password" placeholder="Password" required />
            <label for="passwordInput"><i class="fas fa-lock me-2"></i>Password</label>
          </div>

          <!-- Error Message -->
          <div v-if="error" class="alert alert-danger animate-fade-in" role="alert">
            <i class="fas fa-exclamation-circle me-2"></i>{{ error }}
          </div>

          <!-- Login Button -->
          <button type="submit" class="btn btn-login w-100 mb-4 position-relative overflow-hidden" :disabled="loading">
            <span v-if="loading" class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
            <span v-if="loading">Logging in...</span>
            <span v-else class="fw-bold fs-5">Login</span>
          </button>
        </form>

        <!-- Register Links -->
        <div class="register-links text-center">
          <p class="text-muted mb-2">
            New Student? <router-link to="/auth/student-register" class="fw-bold text-success text-decoration-none hover-underline">Register Here</router-link>
          </p>
          <p class="text-muted mb-0">
            Company? <router-link to="/auth/company-register" class="fw-bold text-primary text-decoration-none hover-underline">Register Company</router-link>
          </p>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import { login as loginUser } from "../../api/auth"
import auth from "../../store/auth"

export default {
  name: "Login",
  data() {
    return {
      form: { email: "", password: "" },
      error: "",
      loading: false
    }
  },
  methods: {
    async login() {
      this.loading = true
      this.error = ""
      try {
        const response = await loginUser(this.form)
        const user = response.data.user
        const token = response.data.token
        
        auth.login(user, token)
        
        if (user.role === "admin") {
          this.$router.push("/admin/dashboard")
        } else if (user.role === "student") {
          this.$router.push("/student/dashboard")
        } else if (user.role === "company") {
          this.$router.push("/company/dashboard")
        } else {
          this.error = "Invalid user role"
        }
      } catch (err) {
        this.error = err.response?.data?.message || "Invalid email or password"
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.login-page {
  /* Using blue and green hues for background */
  background: linear-gradient(135deg, #e0f2fe 0%, #dcfce7 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  /* Ensuring it overrides layout margins if needed */
  margin: -20px -20px 0 -20px; 
}

.login-container {
  display: flex;
  flex-direction: row;
  width: 100%;
  max-width: 1000px;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0,0,0,0.1);
  backdrop-filter: blur(10px);
  min-height: 550px;
}

.login-brand {
  flex: 1;
  /* Blue and green gradient as requested */
  background: linear-gradient(135deg, #0ea5e9 0%, #10b981 100%);
  position: relative;
  overflow: hidden;
}

.login-brand::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
  animation: pulse 10s infinite;
}

.login-form-wrapper {
  flex: 1;
  background-color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.btn-login {
  /* Blue to Green gradient for button */
  background: linear-gradient(90deg, #0ea5e9 0%, #10b981 100%);
  border: none;
  color: white;
  padding: 12px;
  border-radius: 10px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
}

.btn-login:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(14, 165, 233, 0.4);
  color: white;
}

.btn-login:active:not(:disabled) {
  transform: translateY(1px);
}

.custom-input .form-control {
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  padding: 12px 15px;
  transition: all 0.3s ease;
  height: calc(3.5rem + 2px); /* Bootstrap floating label height */
}

.custom-input .form-control:focus {
  border-color: #0ea5e9;
  box-shadow: 0 0 0 0.25rem rgba(14, 165, 233, 0.25);
}

.hover-underline:hover {
  text-decoration: underline !important;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

.animate-float-delayed {
  animation: float 6s ease-in-out infinite 3s;
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-15px); }
  100% { transform: translateY(0px); }
}

.animate-fade-in {
  animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

.form-floating > label {
  padding-left: 1.25rem;
}
</style>