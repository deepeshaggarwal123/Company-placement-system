<!-- frontend/src/views/auth/CompanyRegister.vue -->
<template>
  <div class="register-page">
    <div class="register-container shadow-lg">

      <!-- Left: Branding -->
      <div class="register-brand d-none d-md-flex flex-column justify-content-center align-items-center text-white p-5">
        <i class="fas fa-building fa-5x mb-4 animate-float"></i>
        <h2 class="fw-bold text-center">Register Your Company</h2>
        <p class="text-center lead mt-3 opacity-75">Connect with talented students. Create placement drives and recruit the best candidates.</p>
      </div>

      <!-- Right: Form -->
      <div class="register-form-wrapper p-4 p-md-5">
        <h3 class="fw-bold mb-1 text-dark">Company Registration</h3>
        <p class="text-muted mb-4">Fill in your company details to get started.</p>

        <form @submit.prevent="register" novalidate>

          <!-- Company Name -->
          <div class="form-floating mb-3 custom-input">
            <input type="text" class="form-control" id="compName" v-model="form.company_name"
              :class="fieldClass('company_name')" placeholder="Company Name" required minlength="2" @blur="touch('company_name')" />
            <label for="compName"><i class="fas fa-building me-2"></i>Company Name</label>
            <div class="invalid-feedback">Company name is required (min 2 chars).</div>
          </div>

          <!-- Website -->
          <div class="form-floating mb-3 custom-input">
            <input type="url" class="form-control" id="compWebsite" v-model="form.website"
              placeholder="https://company.com" />
            <label for="compWebsite"><i class="fas fa-globe me-2"></i>Website (optional)</label>
          </div>

          <!-- Row: HR Name + HR Email -->
          <div class="row g-3 mb-3">
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="text" class="form-control" id="hrName" v-model="form.hr_name"
                  :class="fieldClass('hr_name')" placeholder="HR Name" required @blur="touch('hr_name')" />
                <label for="hrName"><i class="fas fa-user-tie me-2"></i>HR Name</label>
                <div class="invalid-feedback">HR name is required.</div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="email" class="form-control" id="hrEmail" v-model="form.hr_email"
                  :class="fieldClass('hr_email')" placeholder="HR Email" required @blur="touch('hr_email')" />
                <label for="hrEmail"><i class="fas fa-envelope me-2"></i>HR Email</label>
                <div class="invalid-feedback">Please enter a valid email.</div>
              </div>
            </div>
          </div>

          <!-- Row: Phone + Industry -->
          <div class="row g-3 mb-3">
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="tel" class="form-control" id="hrPhone" v-model="form.hr_phone"
                  :class="fieldClass('hr_phone')" placeholder="Phone" required pattern="[0-9]{10}" @blur="touch('hr_phone')" />
                <label for="hrPhone"><i class="fas fa-phone me-2"></i>HR Contact Number</label>
                <div class="invalid-feedback">Enter a valid 10-digit number.</div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <select class="form-select" id="compIndustry" v-model="form.industry" @blur="touch('industry')">
                  <option value="">Select Industry</option>
                  <option>IT</option>
                  <option>Finance</option>
                  <option>Manufacturing</option>
                  <option>Education</option>
                  <option>Healthcare</option>
                  <option>Consulting</option>
                </select>
                <label for="compIndustry"><i class="fas fa-industry me-2"></i>Industry</label>
              </div>
            </div>
          </div>

          <!-- Row: Password + Confirm -->
          <div class="row g-3 mb-3">
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="password" class="form-control" id="compPass" v-model="form.password"
                  :class="fieldClass('password')" placeholder="Password" required minlength="6" @blur="touch('password')" />
                <label for="compPass"><i class="fas fa-lock me-2"></i>Password</label>
                <div class="invalid-feedback">Min 6 characters required.</div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-floating custom-input">
                <input type="password" class="form-control" id="compConfirm" v-model="confirmPassword"
                  :class="confirmClass" placeholder="Confirm" required @blur="touch('confirmPassword')" />
                <label for="compConfirm"><i class="fas fa-lock me-2"></i>Confirm Password</label>
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
            {{ loading ? 'Registering...' : 'Register Company' }}
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
import { companyRegister } from "../../api/auth"

export default {
  name: "CompanyRegister",
  data() {
    return {
      form: {
        company_name: "", website: "", hr_name: "",
        hr_email: "", hr_phone: "", industry: "", password: ""
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
      if (field === 'hr_email') return val && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val) ? 'is-valid' : 'is-invalid'
      if (field === 'hr_phone') return val && /^[0-9]{10}$/.test(val) ? 'is-valid' : 'is-invalid'
      if (field === 'password') return val && val.length >= 6 ? 'is-valid' : 'is-invalid'
      if (field === 'company_name') return val && val.length >= 2 ? 'is-valid' : 'is-invalid'
      return val ? 'is-valid' : 'is-invalid'
    },
    async register() {
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
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.form.hr_email)) {
        this.error = "Please enter a valid HR email address"
        return
      }

      this.loading = true
      try {
        await companyRegister(this.form)
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
  background: linear-gradient(135deg, #10b981 0%, #0ea5e9 100%);
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
  background: linear-gradient(90deg, #10b981 0%, #0ea5e9 100%);
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