<!-- frontend/src/views/student/Dashboard.vue -->

<template>

<div class="container-fluid">


    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            Student Dashboard

        </h3>



        <button

            class="btn btn-primary"

            @click="fetchDashboard"

        >

            Refresh

        </button>


    </div>







    <!-- Student Stats -->


    <div class="row g-4">



        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6 class="text-muted">

                        Available Drives

                    </h6>


                    <h2 class="text-primary">

                        {{ stats.available_drives }}

                    </h2>


                </div>


            </div>


        </div>







        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6 class="text-muted">

                        Applied Drives

                    </h6>


                    <h2 class="text-success">

                        {{ stats.applied_drives }}

                    </h2>


                </div>


            </div>


        </div>







        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6 class="text-muted">

                        Shortlisted

                    </h6>


                    <h2 class="text-warning">

                        {{ stats.shortlisted }}

                    </h2>


                </div>


            </div>


        </div>







        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6 class="text-muted">

                        Selected

                    </h6>


                    <h2 class="text-danger">

                        {{ stats.selected }}

                    </h2>


                </div>


            </div>


        </div>



    </div>








    <!-- Profile Card -->


    <div class="card shadow-sm mt-5">


        <div class="card-header">


            <h5>

                My Profile

            </h5>


        </div>




        <div class="card-body">


            <div class="row">


                <div class="col-md-4">


                    <p>

                        <b>Name:</b>

                        {{ student.name }}

                    </p>


                </div>



                <div class="col-md-4">


                    <p>

                        <b>Branch:</b>

                        {{ student.branch }}

                    </p>


                </div>



                <div class="col-md-4">


                    <p>

                        <b>CGPA:</b>

                        {{ student.cgpa }}

                    </p>


                </div>



            </div>


        </div>


    </div>







    <!-- Recent Drives -->


    <div class="card shadow-sm mt-4">


        <div class="card-header">


            <h5>

                Latest Placement Drives

            </h5>


        </div>





        <div class="card-body">


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
                            Package
                        </th>

                        <th>
                            Action
                        </th>

                    </tr>


                </thead>




                <tbody>


                    <tr

                    v-for="drive in drives"

                    :key="drive.id"

                    >


                        <td>

                            {{ drive.company_name }}

                        </td>



                        <td>

                            {{ drive.job_title }}

                        </td>



                        <td>

                            {{ drive.package }} LPA

                        </td>





                        <td>


                            <button

                            class="btn btn-success btn-sm"

                            @click="applyDrive(drive.id)"

                            >

                                Apply

                            </button>


                        </td>



                    </tr>


                </tbody>


            </table>


        </div>


    </div>








    <!-- Applications -->


    <div class="card shadow-sm mt-4">


        <div class="card-header">


            <h5>

                Recent Applications

            </h5>


        </div>




        <div class="card-body">


            <table class="table">


                <thead>


                    <tr>

                        <th>
                            Company
                        </th>

                        <th>
                            Role
                        </th>

                        <th>
                            Status
                        </th>

                    </tr>


                </thead>




                <tbody>


                    <tr

                    v-for="application in applications"

                    :key="application.id"

                    >


                        <td>

                            {{ application.company_name }}

                        </td>



                        <td>

                            {{ application.job_title }}

                        </td>



                        <td>


                            <span

                            class="badge"

                            :class="statusClass(application.status)"

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

    getStudentDashboard,

    applyForDrive as applyDrive

}

from "../../api/student"




export default {


name:"StudentDashboard",




data(){


    return{


        stats:{


            available_drives:0,


            applied_drives:0,


            shortlisted:0,


            selected:0


        },



        student:{},


        drives:[],


        applications:[]


    }


},





methods:{



async fetchDashboard(){


    try{


        const response = await getStudentDashboard()



        this.stats = response.data.stats


        this.student = response.data.student


        this.drives = response.data.drives


        this.applications = response.data.applications



    }


    catch(error){


        console.log(error)


    }


},





async applyDrive(id){


    try{


        await applyDrive(id)


        this.fetchDashboard()



    }


    catch(error){


        console.log(error)


    }


},





statusClass(status){


    if(status==="Selected")

        return "bg-success"



    if(status==="Rejected")

        return "bg-danger"



    if(status==="Shortlisted")

        return "bg-primary"



    return "bg-warning text-dark"


}



},




mounted(){


    this.fetchDashboard()


}



}


</script>