<!-- frontend/src/views/admin/Reports.vue -->

<template>

<div class="container-fluid">


    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            Placement Reports

        </h3>



        <button

            class="btn btn-success"

            @click="exportReport"

        >

            <i class="bi bi-download"></i>

            Export CSV

        </button>


    </div>





    <!-- Statistics -->

    <div class="row g-4">



        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6>

                        Total Students

                    </h6>


                    <h2 class="text-primary">

                        {{ report.total_students }}

                    </h2>


                </div>


            </div>


        </div>





        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6>

                        Placed Students

                    </h6>


                    <h2 class="text-success">

                        {{ report.placed_students }}

                    </h2>


                </div>


            </div>


        </div>





        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6>

                        Companies

                    </h6>


                    <h2 class="text-warning">

                        {{ report.total_companies }}

                    </h2>


                </div>


            </div>


        </div>





        <div class="col-md-3">


            <div class="card shadow-sm text-center">


                <div class="card-body">


                    <h6>

                        Placement %

                    </h6>


                    <h2 class="text-danger">

                        {{ placementPercentage }}%

                    </h2>


                </div>


            </div>


        </div>



    </div>






    <!-- Company Report -->


    <div class="card shadow-sm mt-5">


        <div class="card-header">


            <h5>

                Company Wise Report

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
                                Students Hired
                            </th>

                            <th>
                                Package
                            </th>

                        </tr>


                    </thead>



                    <tbody>


                        <tr

                        v-for="company in report.company_report"

                        :key="company.id"

                        >


                            <td>

                                {{ company.name }}

                            </td>


                            <td>

                                {{ company.hired }}

                            </td>


                            <td>

                                {{ company.package }}

                            </td>


                        </tr>


                    </tbody>


                </table>


            </div>


        </div>


    </div>







    <!-- Application Report -->


    <div class="card shadow-sm mt-4">


        <div class="card-header">


            <h5>

                Application Status Report

            </h5>


        </div>




        <div class="card-body">


            <div class="row text-center">


                <div class="col-md-4">


                    <h6>

                        Pending

                    </h6>


                    <h3 class="text-warning">

                        {{ report.pending }}

                    </h3>


                </div>



                <div class="col-md-4">


                    <h6>

                        Approved

                    </h6>


                    <h3 class="text-success">

                        {{ report.approved }}

                    </h3>


                </div>



                <div class="col-md-4">


                    <h6>

                        Rejected

                    </h6>


                    <h3 class="text-danger">

                        {{ report.rejected }}

                    </h3>


                </div>


            </div>


        </div>


    </div>



</div>


</template>





<script>


import {

    getPlacementReport as getReports,

    exportReport as exportReports

}

from "../../api/admin"




export default {


name:"Reports",



data(){


    return{


        report:{


            total_students:0,


            placed_students:0,


            total_companies:0,


            pending:0,


            approved:0,


            rejected:0,


            company_report:[]


        }


    }


},




computed:{



placementPercentage(){


    if(this.report.total_students===0)

        return 0



    return Math.round(

        (

        this.report.placed_students /

        this.report.total_students

        )

        *100

    )


}



},




methods:{



async fetchReports(){


    try{


        const response = await getReports()


        this.report = response.data



    }


    catch(error){


        console.log(error)


    }


},





async exportReport(){


    try{


        await exportReports()



    }


    catch(error){


        console.log(error)


    }


}



},




mounted(){


    this.fetchReports()


}



}


</script>