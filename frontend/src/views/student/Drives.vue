<!-- frontend/src/views/student/Drives.vue -->

<template>

<div class="container-fluid">


    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            Available Placement Drives

        </h3>


        <button

            class="btn btn-primary"

            @click="fetchDrives"

        >

            Refresh

        </button>


    </div>







    <!-- Search Filter -->


    <div class="card shadow-sm mb-4">


        <div class="card-body">


            <div class="row g-3">


                <div class="col-md-5">


                    <input

                        type="text"

                        class="form-control"

                        placeholder="Search company or role..."

                        v-model="search"

                    />


                </div>





                <div class="col-md-3">


                    <select

                        class="form-select"

                        v-model="branchFilter"

                    >

                        <option value="">

                            All Branches

                        </option>


                        <option>

                            CSE

                        </option>


                        <option>

                            AI

                        </option>


                        <option>

                            ECE

                        </option>


                        <option>

                            ME

                        </option>


                    </select>


                </div>


            </div>


        </div>


    </div>








    <!-- Drive Cards -->


    <div class="row">


        <div

            class="col-md-4 mb-4"

            v-for="drive in filteredDrives"

            :key="drive.id"

        >


            <div class="card shadow-sm h-100">


                <div class="card-body">


                    <h5>

                        {{ drive.company_name }}

                    </h5>



                    <p>

                        <b>Role:</b>

                        {{ drive.job_title }}

                    </p>




                    <p>

                        <b>Package:</b>

                        {{ drive.package }} LPA

                    </p>





                    <p>

                        <b>Location:</b>

                        {{ drive.location }}

                    </p>





                    <p>

                        <b>Deadline:</b>

                        {{ formatDate(drive.deadline) }}

                    </p>





                    <p>

                        <b>Eligibility CGPA:</b>

                        {{ drive.min_cgpa }}

                    </p>







                    <span

                    class="badge bg-success"

                    v-if="isEligible(drive)"

                    >

                        Eligible

                    </span>



                    <span

                    class="badge bg-danger"

                    v-else

                    >

                        Not Eligible

                    </span>





                </div>







                <div class="card-footer">


                    <button

                    class="btn btn-primary w-100"

                    :disabled="

                    !isEligible(drive) ||

                    drive.applied

                    "

                    @click="apply(drive.id)"

                    >


                        <span v-if="drive.applied">

                            Applied

                        </span>


                        <span v-else>

                            Apply Now

                        </span>



                    </button>



                </div>


            </div>


        </div>


    </div>







    <!-- Empty -->

    <div

        v-if="filteredDrives.length===0"

        class="text-center mt-4"

    >

        <h5>

            No Drives Available

        </h5>


    </div>



</div>


</template>





<script>


import {

    getAvailableDrives,

    applyForDrive as applyDrive

}

from "../../api/student"





export default {


name:"StudentDrives",




data(){


    return{


        drives:[],


        search:"",


        branchFilter:"",



        student:{


            cgpa:0,


            branch:""


        }


    }


},




computed:{



filteredDrives(){


    return this.drives.filter(drive=>{


        const text = (

            drive.company_name +

            drive.job_title

        )

        .toLowerCase()



        const matchSearch =

        text.includes(

            this.search.toLowerCase()

        )



        const matchBranch =

        this.branchFilter === "" ||

        drive.branch === this.branchFilter



        return (

            matchSearch &&

            matchBranch

        )


    })


}



},





methods:{



async fetchDrives(){


    try{


        const response = await getAvailableDrives()



        this.drives = response.data.drives


        this.student = response.data.student



    }


    catch(error){


        console.log(error)


    }


},





isEligible(drive){


    return this.student.cgpa >= drive.min_cgpa &&

    (

        drive.branch === "" ||

        drive.branch.includes(

            this.student.branch

        )

    )


},





async apply(id){


    try{


        await applyDrive(id)


        this.fetchDrives()



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



}



},




mounted(){


    this.fetchDrives()


}



}


</script>