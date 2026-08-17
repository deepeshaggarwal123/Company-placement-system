<template>

<div class="input-group mb-3">


    <input

        type="text"

        class="form-control"

        :placeholder="placeholder"

        v-model="searchText"

        @keyup.enter="search"

    />



    <button

        class="btn btn-primary"

        @click="search"

    >

        <i class="bi bi-search"></i>

        Search

    </button>


</div>


</template>



<script>

export default {


name:"SearchBar",



props:{


    placeholder:{

        type:String,

        default:"Search..."

    }


},



data(){

    return{

        searchText:""

    }

},



methods:{


    search(){


        this.$emit(

            "search",

            this.searchText

        )


    }


}


}

</script>