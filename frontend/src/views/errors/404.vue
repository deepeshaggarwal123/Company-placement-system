<!-- frontend/src/views/errors/404.vue -->

<template>

<div class="container text-center mt-5">


    <div class="card shadow p-5">


        <h1 class="display-1 text-danger">

            404

        </h1>



        <h3 class="mb-3">

            Page Not Found

        </h3>




        <p class="text-muted">

            Sorry, the page you are looking for does not exist.

        </p>






        <div class="mt-4">


            <button

                class="btn btn-primary me-2"

                @click="goDashboard"

            >

                Go Dashboard

            </button>





            <button

                class="btn btn-outline-secondary me-2"

                @click="goBack"

            >

                Go Back

            </button>





            <button

                class="btn btn-outline-dark"

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


name:"Error404",





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






goBack(){


    this.$router.go(-1)


},






goHome(){


    this.$router.push(

        "/"

    )


}



}



}


</script>