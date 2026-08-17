<!-- frontend/src/views/admin/Drives.vue -->

<template>

<div class="container-fluid">


    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            Placement Drives Management

        </h3>


        <button

            class="btn btn-primary"

            @click="fetchDrives"

        >

            Refresh

        </button>


    </div>





    <!-- Search & Filter -->

    <div class="card shadow-sm mb-4">


        <div class="card-body">


            <div class="row g-3">


                <div class="col-md-5">


                    <input

                        type="text"

                        class="form-control"

                        placeholder="Search drive/company..."

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


                        <option value="Closed">

                            Closed

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


            <DriveCard

                :drive="drive"

                :showApproval="true"

                @approve="approveDrive"

                @reject="rejectDrive"

            />


        </div>


    </div>






    <!-- Empty Message -->

    <div

        v-if="filteredDrives.length===0"

        class="text-center mt-4"

    >

        <h5>

            No Drives Found

        </h5>


    </div>



</div>


</template>





<script>


import DriveCard

from "../../components/DriveCard.vue"



import {

    getAllDrives as getDrives,

    approveDrive as approveDriveAPI,

    rejectDrive as rejectDriveAPI

}

from "../../api/admin"




export default {


name:"Drives",



components:{


    DriveCard


},



data(){


    return{


        drives:[],


        search:"",


        statusFilter:""


    }


},




computed:{



filteredDrives(){


    return this.drives.filter(drive=>{


        const text = (

            drive.job_title +

            drive.company_name

        )

        .toLowerCase()



        const matchSearch = text.includes(

            this.search.toLowerCase()

        )



        const matchStatus =

        this.statusFilter === "" ||

        drive.status === this.statusFilter



        return matchSearch && matchStatus



    })


}



},




methods:{



async fetchDrives(){


    try{


        const response = await getDrives()


        this.drives = response.data



    }


    catch(error){


        console.log(error)


    }


},





async approveDrive(id){


    try{


        await approveDriveAPI(id)


        this.fetchDrives()


    }


    catch(error){


        console.log(error)


    }


},





async rejectDrive(id){


    try{


        await rejectDriveAPI(id)


        this.fetchDrives()


    }


    catch(error){


        console.log(error)


    }


},





async removeDrive(id){


    try{


        await deleteDrive(id)


        this.fetchDrives()



    }


    catch(error){


        console.log(error)


    }


}



},




mounted(){


    this.fetchDrives()


}



}


</script>