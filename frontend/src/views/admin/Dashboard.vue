<!-- frontend/src/views/admin/Dashboard.vue -->

<template>

<div class="container-fluid">


    <!-- Page Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            Admin Dashboard

        </h3>


        <button

            class="btn btn-primary"

            @click="fetchDashboard"

        >

            Refresh

        </button>


    </div>





    <!-- Statistics Cards -->

    <div class="row g-4">



        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6 class="text-muted">

                        Total Students

                    </h6>


                    <h2 class="text-primary">

                        {{ stats.students }}

                    </h2>


                </div>


            </div>


        </div>





        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6 class="text-muted">

                        Companies

                    </h6>


                    <h2 class="text-success">

                        {{ stats.companies }}

                    </h2>


                </div>


            </div>


        </div>





        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6 class="text-muted">

                        Active Drives

                    </h6>


                    <h2 class="text-warning">

                        {{ stats.drives }}

                    </h2>


                </div>


            </div>


        </div>





        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6 class="text-muted">

                        Applications

                    </h6>


                    <h2 class="text-danger">

                        {{ stats.applications }}

                    </h2>


                </div>


            </div>


        </div>


    </div>






    <!-- Recent Drives -->


    <div class="card shadow-sm mt-5">


        <div class="card-header">

            <h5 class="mb-0">

                Recent Placement Drives

            </h5>


        </div>



        <div class="card-body">


            <div class="table-responsive">


                <table class="table table-hover">


                    <thead>


                        <tr>

                            <th>
                                Company
                            </th>

                            <th>
                                Role
                            </th>

                            <th>
                                Deadline
                            </th>

                            <th>
                                Status
                            </th>

                        </tr>


                    </thead>



                    <tbody>


                        <tr

                        v-for="drive in recentDrives"

                        :key="drive.id"

                        >


                            <td>

                                {{ drive.company_name }}

                            </td>


                            <td>

                                {{ drive.job_title }}

                            </td>


                            <td>

                                {{ formatDate(drive.deadline) }}

                            </td>


                            <td>


                                <span

                                class="badge bg-success"

                                >

                                    {{ drive.status }}

                                </span>


                            </td>


                        </tr>


                    </tbody>


                </table>


            </div>


        </div>


    </div>






    <!-- Recent Applications -->


    <div class="card shadow-sm mt-4">


        <div class="card-header">


            <h5 class="mb-0">

                Recent Applications

            </h5>


        </div>



        <div class="card-body">


            <table class="table">


                <thead>


                    <tr>

                        <th>
                            Student
                        </th>

                        <th>
                            Company
                        </th>

                        <th>
                            Status
                        </th>

                    </tr>


                </thead>



                <tbody>


                    <tr

                    v-for="application in recentApplications"

                    :key="application.id"

                    >


                        <td>

                            {{ application.student_name }}

                        </td>


                        <td>

                            {{ application.company_name }}

                        </td>


                        <td>


                            <span

                            class="badge"

                            :class="applicationStatus(application.status)"

                            >

                                {{ application.status }}

                            </span>


                        </td>


                    </tr>


                </tbody>


            </table>


        </div>


    </div>


</div>


</template>





<script>


import {

    getAdminDashboard as getDashboardData

}

from "../../api/admin"




export default {


name:"AdminDashboard",




data(){


return{


    stats:{


        students:0,


        companies:0,


        drives:0,


        applications:0


    },



    recentDrives:[],


    recentApplications:[]


}



},





methods:{



async fetchDashboard(){


    try{


        const response = await getDashboardData()



        this.stats = response.data.stats


        this.recentDrives = response.data.drives


        this.recentApplications = response.data.applications



    }


    catch(error){


        console.log(error)


    }


},




formatDate(date){


    if(!date)

        return ""



    return new Date(date)

    .toLocaleDateString()



},




applicationStatus(status){



    if(status==="Approved")

        return "bg-success"



    if(status==="Rejected")

        return "bg-danger"



    return "bg-warning text-dark"


}



},




mounted(){


    this.fetchDashboard()


}



}


</script>