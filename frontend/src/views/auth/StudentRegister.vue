<!-- frontend/src/views/auth/StudentRegister.vue -->
<template>
  <div class="register-page">
    <div class="register-container shadow-lg">

      <!-- Left: Branding -->
      <div class="register-brand d-none d-md-flex flex-column justify-content-center align-items-center text-white p-5">
        <i class="fas fa-user-graduate fa-5x mb-4 animate-float"></i>
        <h2 class="fw-bold text-center">Join as a Student</h2>
        <p class="text-center lead mt-3 opacity-75">Start your career journey. Apply to placement drives and get hired by top companies.</p>
      </div>

      <!-- Right: Form -->
      <div class="register-form-wrapper p-4 p-md-5">
        <h3 class="fw-bold mb-1 text-dark">Student Registration</h3>
        <p class="text-muted mb-4">Fill in your details to create an account.</p>

        <form @submit.prevent="register" novalidate ref="regForm">

          <!-- Row 1: Name + Email -->
          <div class="row g-3 mb-3">
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="text" class="form-control" id="studentName" v-model="form.name"
                  :class="fieldClass('name')" placeholder="Full Name" required minlength="2" @blur="touch('name')" />
                <label for="studentName"><i class="fas fa-user me-2"></i>Full Name</label>
                <div class="invalid-feedback">Name is required (min 2 chars).</div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="email" class="form-control" id="studentEmail" v-model="form.email"
                  :class="fieldClass('email')" placeholder="Email" required @blur="touch('email')" />
                <label for="studentEmail"><i class="fas fa-envelope me-2"></i>Email</label>
                <div class="invalid-feedback">Please enter a valid email.</div>
              </div>
            </div>
          </div>

          <!-- Row 2: Phone + Roll No -->
          <div class="row g-3 mb-3">
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="tel" class="form-control" id="studentPhone" v-model="form.phone"
                  :class="fieldClass('phone')" placeholder="Phone" required pattern="[0-9]{10}" @blur="touch('phone')" />
                <label for="studentPhone"><i class="fas fa-phone me-2"></i>Phone Number</label>
                <div class="invalid-feedback">Enter a valid 10-digit phone number.</div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="text" class="form-control" id="studentRoll" v-model="form.roll_no"
                  :class="fieldClass('roll_no')" placeholder="Roll No" required @blur="touch('roll_no')" />
                <label for="studentRoll"><i class="fas fa-id-card me-2"></i>Roll Number</label>
                <div class="invalid-feedback">Roll number is required.</div>
              </div>
            </div>
          </div>

          <!-- Row 3: Branch + CGPA -->
          <div class="row g-3 mb-3">
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <select class="form-select" id="studentBranch" v-model="form.branch"
                  :class="fieldClass('branch')" required @blur="touch('branch')">
                  <option value="">Select Branch</option>
                  <option>CSE</option>
                  <option>AI</option>
                  <option>ECE</option>
                  <option>ME</option>
                  <option>Civil</option>
                  <option>EE</option>
                </select>
                <label for="studentBranch"><i class="fas fa-code-branch me-2"></i>Branch</label>
                <div class="invalid-feedback">Please select a branch.</div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="number" step="0.01" min="0" max="10" class="form-control" id="studentCgpa"
                  v-model="form.cgpa" :class="fieldClass('cgpa')" placeholder="CGPA" required @blur="touch('cgpa')" />
                <label for="studentCgpa"><i class="fas fa-star me-2"></i>CGPA</label>
                <div class="invalid-feedback">Enter CGPA between 0 and 10.</div>
              </div>
            </div>
          </div>

          <!-- Row 4: Year + Skills -->
          <div class="row g-3 mb-3">
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="number" min="2020" max="2035" class="form-control" id="studentYear"
                  v-model="form.year" :class="fieldClass('year')" placeholder="Year" required @blur="touch('year')" />
                <label for="studentYear"><i class="fas fa-calendar me-2"></i>Passing Year</label>
                <div class="invalid-feedback">Enter a valid year (2020-2035).</div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="text" class="form-control" id="studentSkills" v-model="form.skills" placeholder="Skills" />
                <label for="studentSkills"><i class="fas fa-tools me-2"></i>Skills (e.g. Python, Java)</label>
              </div>
            </div>
          </div>

          <!-- Row 5: Password + Confirm -->
          <div class="row g-3 mb-3">
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="password" class="form-control" id="studentPass" v-model="form.password"
                  :class="fieldClass('password')" placeholder="Password" required minlength="6" @blur="touch('password')" />
                <label for="studentPass"><i class="fas fa-lock me-2"></i>Password</label>
                <div class="invalid-feedback">Min 6 characters required.</div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="password" class="form-control" id="studentConfirm" v-model="confirmPassword"
                  :class="confirmClass" placeholder="Confirm" required @blur="touch('confirmPassword')" />
                <label for="studentConfirm"><i class="fas fa-lock me-2"></i>Confirm Password</label>
                <div class="invalid-feedback">Passwords do not match.</div>
              </div>
            </div>
          </div>

          <!-- Error -->
          <div v-if="error" class="alert alert-danger py-2 animate-fade-in">
            <i class="fas fa-exclamation-circle me-2"></i>{{ error }}
          </div>

          <!-- Success -->
          <div v-if="success" class="alert alert-success py-2 animate-fade-in">
            <i class="fas fa-check-circle me-2"></i>{{ success }}
          </div>

          <!-- Submit -->
          <button type="submit" class="btn btn-register w-100 mb-3" :disabled="loading">
            <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
            {{ loading ? 'Registering...' : 'Create Account' }}
          </button>
        </form>

        <div class="text-center">
          <p class="text-muted mb-0">
            Already have an account? <router-link to="/auth/login" class="fw-bold text-primary text-decoration-none">Login here</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { studentRegister } from "../../api/auth"

export default {
  name: "StudentRegister",
  data() {
    return {
      form: {
        name: "", email: "", phone: "", roll_no: "",
        branch: "", cgpa: "", year: "", skills: "", password: ""
      },
      confirmPassword: "",
      error: "",
      success: "",
      loading: false,
      touched: {}
    }
  },
  computed: {
    confirmClass() {
      if (!this.touched.confirmPassword) return ''
      return this.confirmPassword && this.confirmPassword === this.form.password ? 'is-valid' : 'is-invalid'
    }
  },
  methods: {
    touch(field) {
      this.touched[field] = true
    },
    fieldClass(field) {
      if (!this.touched[field]) return ''
      const val = this.form[field]
      if (field === 'email') return val && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val) ? 'is-valid' : 'is-invalid'
      if (field === 'phone') return val && /^[0-9]{10}$/.test(val) ? 'is-valid' : 'is-invalid'
      if (field === 'cgpa') return val && val >= 0 && val <= 10 ? 'is-valid' : 'is-invalid'
      if (field === 'year') return val && val >= 2020 && val <= 2035 ? 'is-valid' : 'is-invalid'
      if (field === 'password') return val && val.length >= 6 ? 'is-valid' : 'is-invalid'
      if (field === 'name') return val && val.length >= 2 ? 'is-valid' : 'is-invalid'
      return val ? 'is-valid' : 'is-invalid'
    },
    async register() {
      // Touch all fields
      Object.keys(this.form).forEach(k => this.touch(k))
      this.touch('confirmPassword')

      this.error = ""
      this.success = ""

      if (this.form.password !== this.confirmPassword) {
        this.error = "Passwords do not match"
        return
      }
      if (this.form.password.length < 6) {
        this.error = "Password must be at least 6 characters"
        return
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.form.email)) {
        this.error = "Please enter a valid email address"
        return
      }
      if (!/^[0-9]{10}$/.test(this.form.phone)) {
        this.error = "Please enter a valid 10-digit phone number"
        return
      }

      this.loading = true
      try {
        await studentRegister(this.form)
        this.success = "Registration successful! Redirecting to login..."
        setTimeout(() => this.$router.push("/auth/login"), 1500)
      } catch (err) {
        this.error = err.response?.data?.message || "Registration failed. Please try again."
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.register-page {
  background: linear-gradient(135deg, #e0f2fe 0%, #dcfce7 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.register-container {
  display: flex;
  width: 100%;
  max-width: 1100px;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}

.register-brand {
  flex: 0 0 35%;
  background: linear-gradient(135deg, #0ea5e9 0%, #10b981 100%);
  position: relative;
  overflow: hidden;
}

.register-brand::before {
  content: '';
  position: absolute;
  top: -50%; left: -50%;
  width: 200%; height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
  animation: pulse 10s infinite;
}

.register-form-wrapper {
  flex: 1;
  background: white;
  overflow-y: auto;
  max-height: 95vh;
}

.custom-input .form-control,
.custom-input .form-select {
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  transition: all 0.3s ease;
}

.custom-input .form-control:focus,
.custom-input .form-select:focus {
  border-color: #0ea5e9;
  box-shadow: 0 0 0 0.25rem rgba(14, 165, 233, 0.15);
}

.custom-input .form-control.is-valid,
.custom-input .form-select.is-valid {
  border-color: #10b981;
}

.custom-input .form-control.is-invalid,
.custom-input .form-select.is-invalid {
  border-color: #ef4444;
}

.btn-register {
  background: linear-gradient(90deg, #0ea5e9 0%, #10b981 100%);
  border: none;
  color: white;
  padding: 12px;
  border-radius: 10px;
  font-weight: 600;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
}

.btn-register:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(14, 165, 233, 0.4);
  color: white;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-15px); }
  100% { transform: translateY(0px); }
}

.animate-fade-in {
  animation: fadeIn 0.4s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>