<template>

<div class="card shadow-sm h-100">

    <div class="card-body">

        <!-- Company Header -->

        <div class="d-flex justify-content-between align-items-center">

            <h5 class="card-title mb-0">

                {{ company.company_name }}

            </h5>


            <span
                class="badge"
                :class="statusClass"
            >

                {{ company.approval_status }}

            </span>


        </div>


        <hr>


        <!-- Company Details -->

        <p class="card-text">

            <i class="bi bi-person"></i>

            <strong> HR:</strong>

            {{ company.hr_name }}

        </p>



        <p class="card-text">

            <i class="bi bi-envelope"></i>

            <strong>Email:</strong>

            {{ company.hr_email }}

        </p>



        <p class="card-text">

            <i class="bi bi-telephone"></i>

            <strong>Phone:</strong>

            {{ company.hr_phone }}

        </p>



        <p class="card-text">

            <i class="bi bi-globe"></i>

            <strong>Website:</strong>

            <a
                :href="company.website"
                target="_blank"
            >

                Visit

            </a>

        </p>



        <!-- Actions -->

        <div
            class="mt-3"
            v-if="showActions"
        >

            <button
                class="btn btn-success btn-sm me-2"
                @click="approveCompany"
            >

                Approve

            </button>



            <button
                class="btn btn-danger btn-sm"
                @click="rejectCompany"
            >

                Reject

            </button>


        </div>


    </div>


</div>

</template>


<script>

export default {


name:"CompanyCard",


props:{


    company:{

        type:Object,

        required:true

    },


    showActions:{

        type:Boolean,

        default:false

    }


},



computed:{


    statusClass(){


        if(this.company.approval_status === "Approved"){

            return "bg-success"

        }


        if(this.company.approval_status === "Rejected"){

            return "bg-danger"

        }


        return "bg-warning text-dark"


    }


},



methods:{


    approveCompany(){


        this.$emit(

            "approve",

            this.company.id

        )


    },



    rejectCompany(){


        this.$emit(

            "reject",

            this.company.id

        )


    }


}


}

</script>