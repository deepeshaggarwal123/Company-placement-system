<template>

<div class="card shadow-sm h-100">

    <div class="card-body">


        <!-- Header -->

        <div class="d-flex justify-content-between align-items-center">

            <h5 class="card-title">

                {{ drive.job_title }}

            </h5>


            <span
                class="badge"
                :class="statusClass"
            >

                {{ drive.status }}

            </span>


        </div>


        <hr>


        <!-- Company -->

        <p>

            <i class="bi bi-building"></i>

            <strong> Company:</strong>

            {{ drive.company_name }}

        </p>



        <!-- Description -->

        <p>

            <strong>Description:</strong>

            {{ drive.job_description }}

        </p>



        <!-- Eligibility -->

        <div>

            <h6>
                Eligibility
            </h6>


            <ul>

                <li>

                    Branch:

                    {{ drive.branch }}

                </li>


                <li>

                    Minimum CGPA:

                    {{ drive.min_cgpa }}

                </li>


                <li>

                    Passing Year:

                    {{ drive.year }}

                </li>


            </ul>


        </div>



        <!-- Deadline -->

        <p>

            <i class="bi bi-calendar"></i>


            <strong>
                Deadline:
            </strong>


            {{ formatDate(drive.application_deadline) }}


        </p>



        <!-- Actions -->

        <div class="mt-3">


            <!-- Student Apply Button -->

            <button

                v-if="showApply"

                class="btn btn-primary btn-sm"

                @click="apply"

            >

                Apply Now

            </button>



            <!-- Admin Actions -->


            <button

                v-if="showApproval"

                class="btn btn-success btn-sm me-2"

                @click="approve"

            >

                Approve

            </button>



            <button

                v-if="showApproval"

                class="btn btn-danger btn-sm"

                @click="reject"

            >

                Reject

            </button>



        </div>



    </div>

</div>

</template>



<script>


export default {


name:"DriveCard",



props:{


    drive:{

        type:Object,

        required:true

    },


    showApply:{

        type:Boolean,

        default:false

    },


    showApproval:{

        type:Boolean,

        default:false

    }


},



computed:{


    statusClass(){


        switch(this.drive.status){


            case "Approved":

                return "bg-success"



            case "Rejected":

                return "bg-danger"



            case "Closed":

                return "bg-secondary"



            default:

                return "bg-warning text-dark"


        }


    }


},



methods:{


    apply(){


        this.$emit(

            "apply",

            this.drive.id

        )


    },



    approve(){


        this.$emit(

            "approve",

            this.drive.id

        )


    },



    reject(){


        this.$emit(

            "reject",

            this.drive.id

        )


    },



    formatDate(date){


        if(!date)

            return ""



        return new Date(date)

        .toLocaleDateString()


    }


}


}


</script>