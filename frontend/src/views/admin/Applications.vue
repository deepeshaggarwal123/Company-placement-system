<!-- frontend/src/views/admin/Applications.vue -->

<template>

<div class="container-fluid">


    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            Applications Management

        </h3>


        <button
            class="btn btn-primary"
            @click="fetchApplications"
        >

            Refresh

        </button>


    </div>




    <!-- Filter -->

    <div class="card shadow-sm mb-4">


        <div class="card-body">


            <div class="row">


                <div class="col-md-4">


                    <input

                        type="text"

                        class="form-control"

                        placeholder="Search student/company..."

                        v-model="search"

                    />


                </div>



                <div class="col-md-3">


                    <select

                        class="form-select"

                        v-model="statusFilter"

                    >

                        <option value="">

                            All Status

                        </option>


                        <option value="Pending">

                            Pending

                        </option>


                        <option value="Approved">

                            Approved

                        </option>


                        <option value="Rejected">

                            Rejected

                        </option>


                    </select>


                </div>


            </div>


        </div>


    </div>





    <!-- Applications Table -->


    <div class="card shadow-sm">


        <div class="card-body">


            <div class="table-responsive">


                <table class="table table-hover">


                    <thead class="table-dark">


                        <tr>

                            <th>
                                #
                            </th>

                            <th>
                                Student
                            </th>

                            <th>
                                Company
                            </th>

                            <th>
                                Drive
                            </th>

                            <th>
                                Applied Date
                            </th>

                            <th>
                                Status
                            </th>

                            <th>
                                Action
                            </th>

                        </tr>


                    </thead>



                    <tbody>


                        <tr

                            v-for="(application,index) in filteredApplications"

                            :key="application.id"

                        >


                            <td>

                                {{ index + 1 }}

                            </td>



                            <td>

                                {{ application.student_name }}

                            </td>



                            <td>

                                {{ application.company_name }}

                            </td>



                            <td>

                                {{ application.drive_title }}

                            </td>



                            <td>

                                {{ formatDate(application.created_at) }}

                            </td>



                            <td>


                                <span

                                    class="badge"

                                    :class="statusClass(application.status)"

                                >

                                    {{ application.status }}

                                </span>


                            </td>




                            <td>


                                <button

                                    class="btn btn-success btn-sm me-2"

                                    @click="updateStatus(application.id,'Approved')"

                                >

                                    Approve

                                </button>



                                <button

                                    class="btn btn-danger btn-sm"

                                    @click="updateStatus(application.id,'Rejected')"

                                >

                                    Reject

                                </button>


                            </td>



                        </tr>



                        <tr v-if="filteredApplications.length===0">


                            <td
                                colspan="7"
                                class="text-center"
                            >

                                No Applications Found

                            </td>


                        </tr>



                    </tbody>


                </table>


            </div>


        </div>


    </div>



</div>


</template>





<script>


import {

    getAllApplications as getApplications,

    approveDrive as updateApplicationStatus

}

from "../../api/admin"




export default {


name:"Applications",



data(){


    return {


        applications:[],


        search:"",


        statusFilter:""


    }


},



computed:{


filteredApplications(){


    return this.applications.filter(app=>{


        const text = (

            app.student_name +

            app.company_name +

            app.drive_title

        )

        .toLowerCase()



        const matchText = text.includes(

            this.search.toLowerCase()

        )



        const matchStatus =

        this.statusFilter === "" ||

        app.status === this.statusFilter



        return matchText && matchStatus



    })


}



},




methods:{



async fetchApplications(){


    try{


        const response = await getApplications()


        this.applications = response.data



    }

    catch(error){


        console.log(error)


    }


},





async updateStatus(id,status){



    try{


        await updateApplicationStatus(

            id,

            status

        )



        this.fetchApplications()



    }

    catch(error){


        console.log(error)


    }



},





statusClass(status){



    if(status==="Approved")

        return "bg-success"



    if(status==="Rejected")

        return "bg-danger"



    return "bg-warning text-dark"



},




formatDate(date){


    if(!date)

        return ""



    return new Date(date)

    .toLocaleDateString()



}



},



mounted(){


    this.fetchApplications()


}



}


</script>