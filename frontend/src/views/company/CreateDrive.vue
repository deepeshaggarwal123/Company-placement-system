<!-- frontend/src/views/company/CreateDrive.vue -->

<template>

<div class="container-fluid">


    <h3 class="mb-4">

        Create Placement Drive

    </h3>




    <div class="card shadow-sm">


        <div class="card-body">


            <form @submit.prevent="createDrive">



                <!-- Job Title -->

                <div class="mb-3">

                    <label class="form-label">

                        Job Title

                    </label>


                    <input

                        type="text"

                        class="form-control"

                        v-model="form.job_title"

                        placeholder="Software Developer"

                        required

                    />

                </div>





                <!-- Description -->

                <div class="mb-3">


                    <label class="form-label">

                        Job Description

                    </label>


                    <textarea
                        class="form-control"
                        rows="4"
                        v-model="form.job_description"
                        placeholder="Enter job description"
                    ></textarea>


                </div>






                <!-- Location -->

                <div class="mb-3">


                    <label class="form-label">

                        Job Location

                    </label>


                    <input
                        type="text"
                        class="form-control"
                        v-model="form.job_location"
                        required
                    />


                </div>






                <!-- Package -->

                <div class="row">


                    <div class="col-md-6 mb-3">


                        <label class="form-label">

                            Salary Package (LPA)

                        </label>


                        <input

                            type="number"

                            step="0.1"

                            class="form-control"

                            v-model="form.package"

                            required

                        />


                    </div>





                    <div class="col-md-6 mb-3">


                        <label class="form-label">

                            Vacancies

                        </label>


                        <input

                            type="number"

                            class="form-control"

                            v-model="form.vacancies"

                            required

                        />


                    </div>


                </div>







                <!-- Eligibility -->


                <div class="row">


                    <div class="col-md-6 mb-3">


                        <label class="form-label">

                            Minimum CGPA

                        </label>


                        <input
                            type="number"
                            step="0.01"
                            class="form-control"
                            v-model="form.minimum_cgpa"
                        />


                    </div>





                    <div class="col-md-6 mb-3">


                        <label class="form-label">

                            Eligible Branch

                        </label>


                        <select
                            class="form-select"
                            v-model="form.eligible_branch"
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

                    <div class="col-md-4 mb-3">
                        <label class="form-label">
                            Eligible Year
                        </label>
                        <input
                            type="number"
                            class="form-control"
                            v-model="form.eligible_year"
                            placeholder="e.g. 2026"
                            required
                        />
                    </div>


                </div>








                <!-- Last Date -->


                <div class="mb-3">


                    <label class="form-label">

                        Application Deadline

                    </label>


                    <input
                        type="date"
                        class="form-control"
                        v-model="form.application_deadline"
                        required
                    />


                </div>








                <!-- Error -->

                <div

                    v-if="error"

                    class="alert alert-danger"

                >

                    {{ error }}

                </div>








                <!-- Submit -->


                <button

                    class="btn btn-primary"

                    type="submit"

                    :disabled="loading"

                >


                    <span v-if="loading">

                        Creating...

                    </span>


                    <span v-else>

                        Create Drive

                    </span>


                </button>



            </form>


        </div>


    </div>


</div>


</template>





<script>


import {

    createDrive

}

from "../../api/company"




export default {


name:"CreateDrive",



data(){


    return{


        form:{
            job_title:"",
            job_description:"",
            job_location:"",
            package:"",
            vacancies:"",
            minimum_cgpa:"",
            eligible_branch:"",
            eligible_year:"",
            application_deadline:""
        },



        error:"",


        loading:false


    }


},




methods:{



async createDrive(){


    try{


        this.loading=true


        this.error=""




        await createDrive(

            this.form

        )



        this.$router.push(

            "/company/drives"

        )



    }


    catch(err){


        this.error =

        err.response?.data?.message ||

        "Drive creation failed"



    }


    finally{


        this.loading=false


    }


}



}



}

</script>