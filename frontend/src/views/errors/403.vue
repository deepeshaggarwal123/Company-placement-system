<!-- frontend/src/views/errors/403.vue -->

<template>

<div class="container text-center mt-5">


    <div class="card shadow p-5">


        <h1 class="display-1 text-danger">

            403

        </h1>



        <h3 class="mb-3">

            Access Forbidden

        </h3>




        <p class="text-muted">

            You do not have permission to access this page.

        </p>





        <div class="mt-4">


            <button

                class="btn btn-primary me-2"

                @click="goDashboard"

            >

                Go Dashboard

            </button>





            <button

                class="btn btn-outline-secondary"

                @click="goHome"

            >

                Home

            </button>


        </div>


    </div>



</div>


</template>





<script>


export default {


name:"Error403",




methods:{



goDashboard(){



    const role = localStorage.getItem(

        "role"

    )



    if(role==="admin"){


        this.$router.push(

            "/admin/dashboard"

        )


    }


    else if(role==="student"){


        this.$router.push(

            "/student/dashboard"

        )


    }


    else if(role==="company"){


        this.$router.push(

            "/company/dashboard"

        )


    }


    else{


        this.$router.push(

            "/auth/login"

        )


    }



},





goHome(){


    this.$router.push(

        "/"

    )


}



}



}


</script>