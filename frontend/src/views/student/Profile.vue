<!-- frontend/src/views/student/History.vue -->

<template>

<div class="container-fluid">


    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            Placement History

        </h3>


        <button

            class="btn btn-primary"

            @click="fetchHistory"

        >

            Refresh

        </button>


    </div>







    <!-- Summary Cards -->


    <div class="row g-4 mb-4">



        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6>

                        Total Applications

                    </h6>


                    <h2 class="text-primary">

                        {{ summary.total }}

                    </h2>


                </div>


            </div>


        </div>







        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6>

                        Shortlisted

                    </h6>


                    <h2 class="text-warning">

                        {{ summary.shortlisted }}

                    </h2>


                </div>


            </div>


        </div>







        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6>

                        Selected

                    </h6>


                    <h2 class="text-success">

                        {{ summary.selected }}

                    </h2>


                </div>


            </div>


        </div>







        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6>

                        Rejected

                    </h6>


                    <h2 class="text-danger">

                        {{ summary.rejected }}

                    </h2>


                </div>


            </div>


        </div>



    </div>








    <!-- History Table -->


    <div class="card shadow-sm">


        <div class="card-header">


            <h5>

                Application History

            </h5>


        </div>





        <div class="card-body">


            <div class="table-responsive">


                <table class="table table-hover">


                    <thead class="table-dark">


                        <tr>

                            <th>
                                #
                            </th>


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
                                Applied Date
                            </th>


                            <th>
                                Status
                            </th>


                        </tr>


                    </thead>





                    <tbody>


                        <tr

                        v-for="(item,index) in history"

                        :key="item.id"

                        >


                            <td>

                                {{ index + 1 }}

                            </td>




                            <td>

                                {{ item.company_name }}

                            </td>





                            <td>

                                {{ item.job_title }}

                            </td>





                            <td>

                                {{ item.package }} LPA

                            </td>





                            <td>

                                {{ formatDate(item.applied_date) }}

                            </td>





                            <td>


                                <span

                                class="badge"

                                :class="statusClass(item.status)"

                                >

                                    {{ item.status }}

                                </span>


                            </td>



                        </tr>







                        <tr v-if="history.length===0">


                            <td

                            colspan="6"

                            class="text-center"

                            >

                                No Placement History Found

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

    getPlacementHistory

}

from "../../api/student"





export default {


name:"StudentHistory",




data(){


    return{


        history:[],


        summary:{


            total:0,


            shortlisted:0,


            selected:0,


            rejected:0


        }


    }


},





methods:{



async fetchHistory(){


    try{


        const response = await getPlacementHistory()



        this.history = response.data.history


        this.summary = response.data.summary



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



    if(status==="Interview")

        return "bg-info"



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


    this.fetchHistory()


}



}


</script>