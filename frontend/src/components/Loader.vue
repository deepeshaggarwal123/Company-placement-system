<template>

<div class="d-flex justify-content-center align-items-center p-4">


    <div
        class="spinner-border text-primary"
        role="status"
    >

        <span class="visually-hidden">
            Loading...
        </span>

    </div>


    <span class="ms-3">

        {{ message }}

    </span>


</div>


</template>



<script>

export default {


name:"Loader",



props:{


    message:{

        type:String,

        default:"Loading..."

    }


}


}

</script>