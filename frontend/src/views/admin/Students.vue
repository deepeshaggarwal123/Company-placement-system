<!-- frontend/src/views/admin/Students.vue -->

<template>

<div class="container-fluid">


    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            Students Management

        </h3>



        <button

            class="btn btn-primary"

            @click="fetchStudents"

        >

            Refresh

        </button>


    </div>





    <!-- Search and Filter -->


    <div class="card shadow-sm mb-4">


        <div class="card-body">


            <div class="row g-3">


                <div class="col-md-5">


                    <input

                        type="text"

                        class="form-control"

                        placeholder="Search Student..."

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


                        <option value="CSE">

                            CSE

                        </option>


                        <option value="AI">

                            AI

                        </option>


                        <option value="ECE">

                            ECE

                        </option>


                        <option value="ME">

                            ME

                        </option>


                    </select>


                </div>





                <div class="col-md-3">


                    <select

                        class="form-select"

                        v-model="statusFilter"

                    >

                        <option value="">

                            All Status

                        </option>


                        <option value="Active">

                            Active

                        </option>


                        <option value="Blacklisted">

                            Blacklisted

                        </option>


                    </select>


                </div>


            </div>


        </div>


    </div>






    <!-- Student Cards -->


    <div class="row">


        <div

            class="col-md-4 mb-4"

            v-for="student in filteredStudents"

            :key="student.id"

        >


            <StudentCard

                :student="student"

                :showActions="true"

                @blacklist="blacklistStudent"

            />


        </div>


    </div>






    <!-- Empty Result -->


    <div

        v-if="filteredStudents.length===0"

        class="text-center mt-4"

    >

        <h5>

            No Students Found

        </h5>


    </div>



</div>


</template>





<script>


import StudentCard

from "../../components/StudentCard.vue"



import {

    getAllStudents as getStudents,

    blacklistStudent as blacklistStudentAPI

}

from "../../api/admin"




export default {


name:"Students",



components:{


    StudentCard


},




data(){


    return{


        students:[],


        search:"",


        branchFilter:"",


        statusFilter:""


    }


},





computed:{



filteredStudents(){


    return this.students.filter(student=>{


        const searchText = (

            student.name +

            student.email +

            student.branch

        )

        .toLowerCase()



        const matchSearch =

        searchText.includes(

            this.search.toLowerCase()

        )



        const matchBranch =

        this.branchFilter === "" ||

        student.branch === this.branchFilter



        const matchStatus =

        this.statusFilter === "" ||

        student.status === this.statusFilter



        return (

            matchSearch &&

            matchBranch &&

            matchStatus

        )


    })


}



},





methods:{



async fetchStudents(){


    try{


        const response = await getStudents()


        this.students = response.data



    }


    catch(error){


        console.log(error)


    }


},





async blacklistStudent(id){


    try{


        await blacklistStudentAPI(id)


        this.fetchStudents()



    }


    catch(error){


        console.log(error)


    }



}



},




mounted(){


    this.fetchStudents()


}



}


</script>