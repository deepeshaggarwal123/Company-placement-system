<template>
  <nav class="navbar navbar-expand-lg custom-navbar sticky-top">
    <div class="container-fluid px-4">
      <!-- Mobile Toggle -->
      <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarMenu">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarMenu">
        <!-- Left Menu (Mobile only links, as sidebar handles desktop) -->
        <ul class="navbar-nav me-auto d-lg-none">
          <!-- Student -->
          <li class="nav-item" v-if="role === 'student'">
            <router-link class="nav-link" to="/student/dashboard">Dashboard</router-link>
          </li>
          <li class="nav-item" v-if="role === 'student'">
            <router-link class="nav-link" to="/student/drives">Placement Drives</router-link>
          </li>
          <!-- Company -->
          <li class="nav-item" v-if="role === 'company'">
            <router-link class="nav-link" to="/company/dashboard">Dashboard</router-link>
          </li>
          <li class="nav-item" v-if="role === 'company'">
            <router-link class="nav-link" to="/company/drives">My Drives</router-link>
          </li>
          <!-- Admin -->
          <li class="nav-item" v-if="role === 'admin'">
            <router-link class="nav-link" to="/admin/dashboard">Admin Panel</router-link>
          </li>
        </ul>

        <!-- Right Menu -->
        <ul class="navbar-nav ms-auto align-items-center">
          <li class="nav-item me-3 d-none d-md-block">
            <span class="badge bg-light text-primary border border-primary px-3 py-2 rounded-pill shadow-sm">
              <i class="fas fa-bell me-1"></i> Notifications
            </span>
          </li>
          <li class="nav-item dropdown" v-if="user">
            <a class="nav-link dropdown-toggle user-dropdown d-flex align-items-center" href="#" role="button" data-bs-toggle="dropdown">
              <div class="user-avatar bg-gradient-primary text-white rounded-circle me-2 d-flex justify-content-center align-items-center">
                {{ user.email ? user.email.charAt(0).toUpperCase() : 'U' }}
              </div>
              <span class="fw-bold text-dark">{{ user.name || user.email }}</span>
            </a>
            <ul class="dropdown-menu dropdown-menu-end shadow-sm border-0 mt-2 rounded-3">
              <li>
                <router-link class="dropdown-item py-2" :to="profileLink">
                  <i class="fas fa-user-circle me-2 text-primary"></i> Profile
                </router-link>
              </li>
              <li><hr class="dropdown-divider"></li>
              <li>
                <button class="dropdown-item py-2 text-danger fw-bold" @click="logout">
                  <i class="fas fa-sign-out-alt me-2"></i> Logout
                </button>
              </li>
            </ul>
          </li>
          <li v-else class="nav-item">
            <router-link class="btn btn-login shadow-sm" to="/login">Login</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import auth from "../store/auth"
import { logout as logoutAPI } from "../api/auth"

export default {
  name: "Navbar",
  computed: {
    user() {
      return auth.user
    },
    role() {
      return auth.role
    },
    profileLink() {
      if(this.role === "student") return "/student/profile"
      if(this.role === "company") return "/company/profile"
      return "/admin/profile"
    }
  },
  methods: {
    async logout() {
      try {
        await logoutAPI()
      } catch(error) {
        console.log(error)
      }
      localStorage.removeItem("token")
      localStorage.removeItem("user")
      auth.user = null
      auth.role = null
      this.$router.push("/")
    }
  }
}
</script>

<style scoped>
.custom-navbar {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(0,0,0,0.05);
  box-shadow: 0 4px 20px rgba(0,0,0,0.02);
  padding: 0.8rem 0;
}

.user-avatar {
  width: 35px;
  height: 35px;
  font-weight: bold;
}

.bg-gradient-primary {
  background: linear-gradient(135deg, #0ea5e9 0%, #10b981 100%);
}

.user-dropdown {
  padding: 0.5rem 1rem !important;
  border-radius: 50px;
  background: rgba(14, 165, 233, 0.05);
  transition: all 0.3s ease;
}

.user-dropdown:hover {
  background: rgba(14, 165, 233, 0.1);
}

.dropdown-item {
  transition: all 0.2s;
}

.dropdown-item:hover {
  background-color: #f8fafc;
  transform: translateX(3px);
}

.btn-login {
  background: linear-gradient(90deg, #0ea5e9 0%, #10b981 100%);
  border: none;
  color: white;
  padding: 8px 20px;
  border-radius: 10px;
  transition: all 0.3s ease;
}

.btn-login:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(14, 165, 233, 0.3);
  color: white;
}
</style>