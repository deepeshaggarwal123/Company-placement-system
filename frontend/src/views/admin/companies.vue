<!-- frontend/src/views/admin/Companies.vue -->

<template>

<div class="container-fluid">


    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            Companies Management

        </h3>


        <button

            class="btn btn-primary"

            @click="fetchCompanies"

        >

            Refresh

        </button>


    </div>





    <!-- Search -->

    <div class="card shadow-sm mb-4">


        <div class="card-body">


            <input

                type="text"

                class="form-control"

                placeholder="Search Company..."

                v-model="search"

            />


        </div>


    </div>





    <!-- Company Cards -->

    <div class="row">


        <div

            class="col-md-4 mb-4"

            v-for="company in filteredCompanies"

            :key="company.id"

        >


            <CompanyCard

                :company="company"

                :showActions="true"

                @approve="approveCompany"

                @reject="rejectCompany"

            />


        </div>


    </div>





    <!-- Empty -->

    <div

        v-if="filteredCompanies.length===0"

        class="text-center"

    >

        <h5>

            No Companies Found

        </h5>


    </div>



</div>


</template>





<script>


import CompanyCard 

from "../../components/CompanyCard.vue"



import {

    getAllCompanies as getCompanies,

    approveCompany as approveCompanyAPI,

    rejectCompany as rejectCompanyAPI

}

from "../../api/admin"




export default {


name:"Companies",



components:{


    CompanyCard


},



data(){


    return{


        companies:[],


        search:""


    }


},



computed:{



filteredCompanies(){


    return this.companies.filter(company=>{


        const name =

        company.company_name

        .toLowerCase()



        return name.includes(

            this.search.toLowerCase()

        )


    })


}



},




methods:{



async fetchCompanies(){


    try{


        const response = await getCompanies()


        this.companies = response.data



    }


    catch(error){


        console.log(error)


    }



},





async approveCompany(id){


    try{


        await approveCompanyAPI(id)


        this.fetchCompanies()


    }


    catch(error){


        console.log(error)

    }



},





async rejectCompany(id){


    try{


        await rejectCompanyAPI(id)


        this.fetchCompanies()


    }


    catch(error){


        console.log(error)

    }



}



},



mounted(){


    this.fetchCompanies()


}



}


</script>