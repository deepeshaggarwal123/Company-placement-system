<!-- frontend/src/components/StudentCard.vue -->

<template>

<div class="card shadow-sm h-100">


    <div class="card-body">


        <!-- Student Header -->

        <div class="d-flex justify-content-between align-items-center">


            <h5 class="card-title mb-0">

                {{ student.name }}

            </h5>


            <span
                class="badge"
                :class="statusClass"
            >

                {{ student.status }}

            </span>


        </div>



        <hr>



        <!-- Student Details -->


        <p>

            <i class="bi bi-envelope"></i>

            <strong>Email:</strong>

            {{ student.email }}

        </p>



        <p>

            <i class="bi bi-mortarboard"></i>

            <strong>Branch:</strong>

            {{ student.branch }}

        </p>



        <p>

            <i class="bi bi-bar-chart"></i>

            <strong>CGPA:</strong>

            {{ student.cgpa }}

        </p>



        <p>

            <i class="bi bi-calendar"></i>

            <strong>Passing Year:</strong>

            {{ student.year }}

        </p>




        <!-- Skills -->


        <div v-if="student.skills">


            <strong>

                Skills:

            </strong>


            <div class="mt-2">


                <span

                    v-for="skill in skillList"

                    :key="skill"

                    class="badge bg-primary me-1"

                >

                    {{ skill }}

                </span>


            </div>


        </div>




        <!-- Resume -->


        <div
            class="mt-3"
            v-if="student.resume"
        >

            <a

                :href="student.resume"

                target="_blank"

                class="btn btn-outline-primary btn-sm"

            >

                <i class="bi bi-file-earmark-pdf"></i>

                View Resume

            </a>


        </div>




        <!-- Actions -->


        <div

            class="mt-3"

            v-if="showActions"

        >


            <button

                class="btn btn-danger btn-sm"

                @click="blacklist"

            >

                Blacklist

            </button>


        </div>


    </div>


</div>


</template>



<script>


export default {


name:"StudentCard",



props:{


    student:{

        type:Object,

        required:true

    },


    showActions:{

        type:Boolean,

        default:false

    }


},



computed:{


    skillList(){


        if(!this.student.skills){

            return []

        }


        return this.student.skills.split(",")


    },



    statusClass(){


        if(this.student.status==="Active"){

            return "bg-success"

        }


        if(this.student.status==="Blacklisted"){

            return "bg-danger"

        }


        return "bg-warning text-dark"


    }


},



methods:{


    blacklist(){


        this.$emit(

            "blacklist",

            this.student.id

        )


    }


}



}

</script>