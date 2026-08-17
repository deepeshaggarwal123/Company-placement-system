<!-- frontend/src/views/auth/StudentRegister.vue -->

<template>

<div>


    <h3 class="text-center mb-4">

        Student Registration

    </h3>



    <form @submit.prevent="register">



        <!-- Name -->

        <div class="mb-3">

            <label class="form-label">

                Full Name

            </label>


            <input

                type="text"

                class="form-control"

                v-model="form.name"

                required

            />

        </div>





        <!-- Email -->

        <div class="mb-3">

            <label class="form-label">

                Email

            </label>


            <input

                type="email"

                class="form-control"

                v-model="form.email"

                required

            />

        </div>






        <!-- Phone -->

        <div class="mb-3">

            <label class="form-label">

                Phone Number

            </label>


            <input

                type="tel"

                class="form-control"

                v-model="form.phone"

                required

            />

        </div>






        <!-- College Roll Number -->

        <div class="mb-3">

            <label class="form-label">

                Roll Number

            </label>


            <input

                type="text"

                class="form-control"

                v-model="form.roll_no"

                required

            />

        </div>






        <!-- Branch -->

        <div class="mb-3">

            <label class="form-label">

                Branch

            </label>


            <select

                class="form-select"

                v-model="form.branch"

                required

            >

                <option value="">

                    Select Branch

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


                <option>

                    Civil

                </option>


            </select>


        </div>






        <!-- CGPA -->

        <div class="mb-3">

            <label class="form-label">

                CGPA

            </label>


            <input

                type="number"

                step="0.01"

                class="form-control"

                v-model="form.cgpa"

                required

            />

        </div>







        <!-- Passing Year -->

        <div class="mb-3">

            <label class="form-label">

                Passing Year

            </label>


            <input

                type="number"

                class="form-control"

                v-model="form.year"

                required

            />

        </div>







        <!-- Skills -->

        <div class="mb-3">

            <label class="form-label">

                Skills

            </label>


            <input

                type="text"

                class="form-control"

                v-model="form.skills"

                placeholder="Python, Java, React"

            />

        </div>







        <!-- Password -->

        <div class="mb-3">

            <label class="form-label">

                Password

            </label>


            <input

                type="password"

                class="form-control"

                v-model="form.password"

                required

            />

        </div>








        <!-- Confirm Password -->

        <div class="mb-3">

            <label class="form-label">

                Confirm Password

            </label>


            <input

                type="password"

                class="form-control"

                v-model="confirmPassword"

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

            class="btn btn-primary w-100"

            type="submit"

        >

            Register Student

        </button>



    </form>






    <div class="text-center mt-3">


        <router-link to="/auth/login">

            Already have account? Login

        </router-link>


    </div>



</div>


</template>





<script>


import {

    studentRegister

}

from "../../api/auth"





export default {


name:"StudentRegister",



data(){


    return{


        form:{


            name:"",


            email:"",


            phone:"",


            roll_no:"",


            branch:"",


            cgpa:"",


            year:"",


            skills:"",


            password:""


        },



        confirmPassword:"",


        error:""


    }


},




methods:{



async register(){



    if(

        this.form.password !==

        this.confirmPassword

    ){


        this.error =

        "Password does not match"



        return


    }






    try{



        await studentRegister(

            this.form

        )



        this.$router.push(

            "/auth/login"

        )



    }



    catch(err){



        this.error =

        err.response?.data?.message ||

        "Registration failed"



    }



}



}



}

</script>