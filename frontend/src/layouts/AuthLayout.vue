<!-- frontend/src/layouts/AuthLayout.vue -->
<template>
  <div class="auth-wrapper">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "AuthLayout"
}
</script>

<style scoped>
.auth-wrapper {
  min-height: 100vh;
  width: 100%;
}
</style>