<template>
  <footer class="custom-footer mt-auto">
    <div class="container py-5">
      <div class="row gy-4">
        
        <!-- Brand -->
        <div class="col-md-4 mb-3">
          <h4 class="fw-bold mb-3 d-flex align-items-center">
            <i class="fas fa-graduation-cap me-2 text-primary"></i> Placement Portal
          </h4>
          <p class="text-muted">
            A smart platform connecting students, companies, and the institute placement cell. Empowering careers through seamless recruitment.
          </p>
        </div>

        <!-- Quick Links -->
        <div class="col-md-4 mb-3">
          <h5 class="fw-bold mb-3">Quick Links</h5>
          <ul class="list-unstyled footer-links">
            <li class="mb-2">
              <router-link to="/" class="text-decoration-none">
                <i class="fas fa-angle-right me-1"></i> Home
              </router-link>
            </li>
            <li class="mb-2">
              <router-link to="/student/dashboard" class="text-decoration-none">
                <i class="fas fa-angle-right me-1"></i> Student Dashboard
              </router-link>
            </li>
            <li class="mb-2">
              <router-link to="/company/dashboard" class="text-decoration-none">
                <i class="fas fa-angle-right me-1"></i> Company Dashboard
              </router-link>
            </li>
          </ul>
        </div>

        <!-- Contact -->
        <div class="col-md-4 mb-3">
          <h5 class="fw-bold mb-3">Contact Us</h5>
          <ul class="list-unstyled contact-info text-muted">
            <li class="mb-2 d-flex align-items-center">
              <div class="icon-circle me-3"><i class="fas fa-envelope"></i></div>
              placement@institute.com
            </li>
            <li class="mb-2 d-flex align-items-center">
              <div class="icon-circle me-3"><i class="fas fa-phone-alt"></i></div>
              +91 9876543210
            </li>
            <li class="mb-2 d-flex align-items-center">
              <div class="icon-circle me-3"><i class="fas fa-map-marker-alt"></i></div>
              Institute Campus, City
            </li>
          </ul>
        </div>
      </div>
      
      <hr class="border-secondary opacity-25 my-4">
      
      <!-- Copyright -->
      <div class="row align-items-center">
        <div class="col-md-6 text-center text-md-start">
          <p class="mb-0 text-muted small">
            &copy; {{ year }} Placement Portal. All Rights Reserved.
          </p>
        </div>
        <div class="col-md-6 text-center text-md-end mt-3 mt-md-0">
          <div class="social-links">
            <a href="#" class="me-3"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="me-3"><i class="fab fa-twitter"></i></a>
            <a href="#" class="me-3"><i class="fab fa-linkedin-in"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      year: new Date().getFullYear()
    }
  }
}
</script>

<style scoped>
.custom-footer {
  background: #0f172a; /* Slate 900 for modern dark */
  color: #f8fafc;
  border-top: 4px solid #0ea5e9;
}

.text-primary {
  color: #0ea5e9 !important; /* Blue accent */
}

.text-muted {
  color: #94a3b8 !important; /* Slate 400 */
}

.footer-links a {
  color: #cbd5e1;
  transition: all 0.3s ease;
}

.footer-links a:hover {
  color: #10b981; /* Green hover */
  padding-left: 5px;
}

.icon-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(14, 165, 233, 0.1);
  color: #0ea5e9;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.icon-circle:hover {
  background: #0ea5e9;
  color: white;
}

.social-links a {
  color: #94a3b8;
  transition: color 0.3s ease;
  font-size: 1.2rem;
}

.social-links a:hover {
  color: #10b981; /* Green accent */
}
</style>