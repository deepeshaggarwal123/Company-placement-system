<!-- frontend/src/views/company/Dashboard.vue -->

<template>

<div class="container-fluid">


    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            Company Dashboard

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

                        Total Drives

                    </h6>


                    <h2 class="text-primary">

                        {{ stats.total_drives }}

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


                    <h2 class="text-success">

                        {{ stats.active_drives }}

                    </h2>


                </div>


            </div>


        </div>





        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6 class="text-muted">

                        Applicants

                    </h6>


                    <h2 class="text-warning">

                        {{ stats.applicants }}

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







    <!-- Recent Drives -->


    <div class="card shadow-sm mt-5">


        <div class="card-header">


            <h5>

                Recent Placement Drives

            </h5>


        </div>




        <div class="card-body">


            <div class="table-responsive">


                <table class="table table-hover">


                    <thead>


                        <tr>

                            <th>
                                Job Role
                            </th>

                            <th>
                                Package
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

                                {{ drive.job_title }}

                            </td>


                            <td>

                                {{ drive.package }} LPA

                            </td>


                            <td>

                                {{ formatDate(drive.deadline) }}

                            </td>


                            <td>


                                <span

                                class="badge"

                                :class="driveStatus(drive.status)"

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







    <!-- Recent Applicants -->


    <div class="card shadow-sm mt-4">


        <div class="card-header">


            <h5>

                Recent Applicants

            </h5>


        </div>



        <div class="card-body">


            <table class="table table-hover">


                <thead>


                    <tr>

                        <th>
                            Student
                        </th>

                        <th>
                            Branch
                        </th>

                        <th>
                            CGPA
                        </th>

                        <th>
                            Status
                        </th>

                    </tr>


                </thead>



                <tbody>


                    <tr

                    v-for="student in applicants"

                    :key="student.id"

                    >


                        <td>

                            {{ student.name }}

                        </td>



                        <td>

                            {{ student.branch }}

                        </td>



                        <td>

                            {{ student.cgpa }}

                        </td>



                        <td>


                            <span

                            class="badge"

                            :class="applicationStatus(student.status)"

                            >

                                {{ student.status }}

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

    getCompanyDashboard

}

from "../../api/company"




export default {


name:"CompanyDashboard",




data(){


    return{


        stats:{


            total_drives:0,


            active_drives:0,


            applicants:0,


            selected:0


        },



        recentDrives:[],


        applicants:[]


    }


},




methods:{



async fetchDashboard(){


    try{


        const response = await getCompanyDashboard()



        this.stats = response.data.stats


        this.recentDrives = response.data.drives


        this.applicants = response.data.applicants



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





driveStatus(status){


    if(status==="Approved")

        return "bg-success"



    if(status==="Rejected")

        return "bg-danger"



    return "bg-warning text-dark"


},





applicationStatus(status){


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

