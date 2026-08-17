<!-- frontend/src/views/company/Profile.vue -->

<template>

<div class="container-fluid">


    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            Company Profile

        </h3>


        <button

            class="btn btn-primary"

            @click="updateProfile"

        >

            Save Changes

        </button>


    </div>





    <div class="card shadow-sm">


        <div class="card-body">


            <form @submit.prevent="updateProfile">



                <!-- Company Name -->


                <div class="mb-3">


                    <label class="form-label">

                        Company Name

                    </label>


                    <input

                        type="text"

                        class="form-control"

                        v-model="company.company_name"

                        required

                    />


                </div>







                <!-- Website -->


                <div class="mb-3">


                    <label class="form-label">

                        Website

                    </label>


                    <input

                        type="url"

                        class="form-control"

                        v-model="company.website"

                    />


                </div>







                <!-- Industry -->


                <div class="mb-3">


                    <label class="form-label">

                        Industry

                    </label>


                    <select

                        class="form-select"

                        v-model="company.industry"

                    >


                        <option>

                            IT

                        </option>


                        <option>

                            Finance

                        </option>


                        <option>

                            Manufacturing

                        </option>


                        <option>

                            Healthcare

                        </option>


                        <option>

                            Education

                        </option>


                    </select>


                </div>







                <!-- Company Description -->


                <div class="mb-3">


                    <label class="form-label">

                        Company Description

                    </label>


                    <textarea

                        class="form-control"

                        rows="4"

                        v-model="company.description"

                    ></textarea>


                </div>







                <hr>






                <h5 class="mb-3">

                    HR Details

                </h5>






                <!-- HR Name -->


                <div class="mb-3">


                    <label class="form-label">

                        HR Name

                    </label>


                    <input

                        type="text"

                        class="form-control"

                        v-model="company.hr_name"

                    />


                </div>







                <!-- HR Email -->


                <div class="mb-3">


                    <label class="form-label">

                        HR Email

                    </label>


                    <input

                        type="email"

                        class="form-control"

                        v-model="company.hr_email"

                        readonly

                    />


                </div>







                <!-- Phone -->


                <div class="mb-3">


                    <label class="form-label">

                        Contact Number

                    </label>


                    <input

                        type="tel"

                        class="form-control"

                        v-model="company.hr_phone"

                    />


                </div>







                <!-- Address -->


                <div class="mb-3">


                    <label class="form-label">

                        Company Address

                    </label>


                    <textarea

                        class="form-control"

                        rows="3"

                        v-model="company.address"

                    ></textarea>


                </div>







                <!-- Success/Error -->


                <div

                    v-if="message"

                    class="alert alert-success"

                >

                    {{ message }}

                </div>



                <div

                    v-if="error"

                    class="alert alert-danger"

                >

                    {{ error }}

                </div>







                <button

                    class="btn btn-primary"

                    type="submit"

                >

                    Update Profile

                </button>




            </form>


        </div>


    </div>



</div>


</template>





<script>


import {

    getCompanyProfile,

    updateCompanyProfile

}

from "../../api/company"





export default {


name:"CompanyProfile",



data(){


    return{


        company:{


            company_name:"",


            website:"",


            industry:"",


            description:"",


            hr_name:"",


            hr_email:"",


            hr_phone:"",


            address:""


        },


        message:"",


        error:""


    }


},





methods:{



async fetchProfile(){


    try{


        const response = await getCompanyProfile()


        this.company = response.data



    }


    catch(error){


        console.log(error)


    }


},





async updateProfile(){


    try{


        await updateCompanyProfile(

            this.company

        )


        this.message =

        "Profile updated successfully"



        this.error=""


    }


    catch(error){


        this.error =

        "Profile update failed"



        this.message=""


    }


}



},




mounted(){


    this.fetchProfile()


}



}


</script>