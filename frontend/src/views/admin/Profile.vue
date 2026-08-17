<template>
  <div class="admin-profile-container p-4">
    <div class="card shadow-sm border-0">
      <div class="card-header bg-primary text-white">
        <h4 class="mb-0">Admin Profile</h4>
      </div>
      <div class="card-body text-center py-5">
        <div class="avatar-circle bg-primary text-white mx-auto mb-3 d-flex align-items-center justify-content-center">
          <i class="fas fa-user-shield fa-3x"></i>
        </div>
        <h3 class="mb-1">Administrator</h3>
        <p class="text-muted mb-4">admin@placement.com</p>
        <hr />
        <div class="row text-start mt-4">
          <div class="col-md-6 mb-3">
            <label class="form-label fw-bold text-muted">Role</label>
            <p>System Administrator</p>
          </div>
          <div class="col-md-6 mb-3">
            <label class="form-label fw-bold text-muted">Account Status</label>
            <p><span class="badge bg-success">Active</span></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminProfile"
};
</script>

<style scoped>
.avatar-circle {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
</style>
