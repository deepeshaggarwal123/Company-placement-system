<!-- frontend/src/layouts/AdminLayout.vue -->

<template>

<div class="d-flex min-vh-100">


    <!-- Sidebar -->
    <Sidebar />

    <div class="flex-grow-1 main-wrapper">
        <!-- Navbar -->
        <Navbar />



        <!-- Main Content -->

        <main class="container-fluid p-4">


            <router-view />


        </main>



        <!-- Footer -->

        <Footer />


    </div>


</div>


</template>



<script>


import Sidebar from "../components/Sidebar.vue"

import Navbar from "../components/Navbar.vue"

import Footer from "../components/Footer.vue"



export default {


name:"AdminLayout",



components:{


    Sidebar,

    Navbar,

    Footer


}



}


</script>



<style scoped>
.main-wrapper {
  background: #f8fafc; /* Modern light background */
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1;
  background: #f8fafc;
}
</style>