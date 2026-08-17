<!-- frontend/src/components/Sidebar.vue -->
<template>
  <div class="sidebar d-flex flex-column p-3 text-white">
    <!-- Brand Title & Graphic -->
    <div class="brand-section text-center mb-4 mt-2">
      <div class="brand-icon mb-2">
        <i class="fas fa-graduation-cap fa-2x animate-pulse"></i>
      </div>
      <h4 class="fw-bold mb-0">Placement Portal</h4>
      <hr class="border-white opacity-25 mt-3 mb-0" />
    </div>

    <!-- Admin Menu -->
    <ul class="nav flex-column flex-grow-1" v-if="role === 'admin'">
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/admin/dashboard" exact-active-class="active">
          <i class="bi bi-speedometer2 me-2"></i> Dashboard
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/admin/students" exact-active-class="active">
          <i class="bi bi-people me-2"></i> Students
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/admin/companies" exact-active-class="active">
          <i class="bi bi-building me-2"></i> Companies
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/admin/drives" exact-active-class="active">
          <i class="bi bi-briefcase me-2"></i> Placement Drives
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/admin/applications" exact-active-class="active">
          <i class="bi bi-file-earmark-text me-2"></i> Applications
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/admin/reports" exact-active-class="active">
          <i class="bi bi-bar-chart me-2"></i> Reports
        </router-link>
      </li>
    </ul>

    <!-- Student Menu -->
    <ul class="nav flex-column flex-grow-1" v-if="role === 'student'">
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/student/dashboard" exact-active-class="active">
          <i class="bi bi-house me-2"></i> Dashboard
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/student/drives" exact-active-class="active">
          <i class="bi bi-search me-2"></i> Find Drives
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/student/applications" exact-active-class="active">
          <i class="bi bi-file-earmark-text me-2"></i> Applications
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/student/profile" exact-active-class="active">
          <i class="bi bi-person me-2"></i> Profile
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/student/resume" exact-active-class="active">
          <i class="bi bi-file-person me-2"></i> Resume
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/student/ats-checker" exact-active-class="active">
          <i class="bi bi-shield-check me-2"></i> ATS Checker
        </router-link>
      </li>
    </ul>

    <!-- Company Menu -->
    <ul class="nav flex-column flex-grow-1" v-if="role === 'company'">
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/company/dashboard" exact-active-class="active">
          <i class="bi bi-speedometer me-2"></i> Dashboard
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/company/create-drive" exact-active-class="active">
          <i class="bi bi-plus-circle me-2"></i> Create Drive
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/company/drives" exact-active-class="active">
          <i class="bi bi-briefcase me-2"></i> My Drives
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/company/applicants" exact-active-class="active">
          <i class="bi bi-person-lines-fill me-2"></i> Applicants
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-white" to="/company/profile" exact-active-class="active">
          <i class="bi bi-building me-2"></i> Company Profile
        </router-link>
      </li>
    </ul>

  </div>
</template>

<script>
import auth from "../store/auth"

export default {
  name: "Sidebar",
  computed: {
    role() {
      return auth.role
    }
  }
}
</script>

<style scoped>
.sidebar {
  width: 260px;
  min-height: 100vh;
  background: linear-gradient(180deg, #0ea5e9 0%, #10b981 100%);
  box-shadow: 4px 0 15px rgba(0, 0, 0, 0.05);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.brand-icon i {
  color: #ffffff;
  filter: drop-shadow(0px 2px 4px rgba(0,0,0,0.2));
}

.nav-link {
  padding: 12px 20px;
  border-radius: 10px;
  margin-bottom: 8px;
  transition: all 0.3s ease;
  font-weight: 500;
  opacity: 0.9;
}

.nav-link:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateX(5px);
  opacity: 1;
}

.nav-link.active {
  background: rgba(255, 255, 255, 0.25);
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  font-weight: 600;
  opacity: 1;
}

.nav-link i {
  font-size: 1.1rem;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}

.animate-pulse {
  animation: pulse 3s infinite;
}
</style>