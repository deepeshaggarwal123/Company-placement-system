<!-- frontend/src/views/company/MyDrives.vue -->

<template>

<div class="container-fluid">


    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            My Placement Drives

        </h3>



        <router-link

            to="/company/create-drive"

            class="btn btn-primary"

        >

            + Create Drive

        </router-link>


    </div>







    <!-- Search & Filter -->


    <div class="card shadow-sm mb-4">


        <div class="card-body">


            <div class="row g-3">


                <div class="col-md-5">


                    <input

                        type="text"

                        class="form-control"

                        placeholder="Search Job Role..."

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


                        <option value="Approved">

                            Approved

                        </option>


                        <option value="Pending">

                            Pending

                        </option>


                        <option value="Closed">

                            Closed

                        </option>


                        <option value="Rejected">

                            Rejected

                        </option>


                    </select>


                </div>


            </div>


        </div>


    </div>







    <!-- Drives Table -->


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
                                Job Role
                            </th>

                            <th>
                                Package
                            </th>

                            <th>
                                Vacancies
                            </th>

                            <th>
                                Deadline
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

                        v-for="(drive,index) in filteredDrives"

                        :key="drive.id"

                        >


                            <td>

                                {{ index + 1 }}

                            </td>



                            <td>

                                {{ drive.job_title }}

                            </td>



                            <td>

                                {{ drive.package }} LPA

                            </td>



                            <td>

                                {{ drive.vacancies }}

                            </td>



                            <td>

                                {{ formatDate(drive.deadline) }}

                            </td>




                            <td>


                                <span

                                class="badge"

                                :class="statusClass(drive.status)"

                                >

                                    {{ drive.status }}

                                </span>


                            </td>





                            <td>


                                <button

                                class="btn btn-warning btn-sm me-2"

                                @click="editDrive(drive.id)"

                                >

                                    Edit

                                </button>





                                <button

                                class="btn btn-danger btn-sm me-2"

                                @click="removeDrive(drive.id)"

                                >

                                    Delete

                                </button>





                                <button

                                v-if="drive.status==='Approved'"

                                class="btn btn-secondary btn-sm"

                                @click="closeDrive(drive.id)"

                                >

                                    Close

                                </button>


                            </td>



                        </tr>







                        <tr v-if="filteredDrives.length===0">


                            <td

                            colspan="7"

                            class="text-center"

                            >

                                No Drives Found

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

    getMyDrives,

    deleteDrive,

    updateDriveStatus

}

from "../../api/company"





export default {


name:"MyDrives",




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

            drive.status

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


        const response = await getMyDrives()


        this.drives = response.data



    }


    catch(error){


        console.log(error)


    }


},





editDrive(id){


    this.$router.push(

        `/company/edit-drive/${id}`

    )


},





async removeDrive(id){


    try{


        await deleteDrive(id)


        this.fetchDrives()



    }


    catch(error){


        console.log(error)


    }


},





async closeDrive(id){


    try{


        await updateDriveStatus(

            id,

            "Closed"

        )


        this.fetchDrives()



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



    if(status==="Closed")

        return "bg-secondary"



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


    this.fetchDrives()


}



}


</script>