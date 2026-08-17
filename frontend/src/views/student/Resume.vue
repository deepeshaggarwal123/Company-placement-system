<!-- frontend/src/views/student/Resume.vue -->

<template>

<div class="container-fluid">


    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">


        <h3>

            Resume Management

        </h3>


    </div>







    <div class="card shadow-sm">


        <div class="card-body">


            <form @submit.prevent="uploadResume">





                <!-- Current Resume -->


                <div class="mb-4">


                    <h5>

                        Current Resume

                    </h5>



                    <div v-if="resumeUrl">


                        <a

                            :href="resumeUrl"

                            target="_blank"

                            class="btn btn-outline-primary"

                        >

                            View Resume

                        </a>


                    </div>



                    <p

                    v-else

                    class="text-muted"

                    >

                        No Resume Uploaded

                    </p>


                </div>







                <!-- Upload -->


                <div class="mb-3">


                    <label class="form-label">

                        Upload New Resume (PDF)

                    </label>



                    <input

                        type="file"

                        class="form-control"

                        accept=".pdf"

                        @change="selectFile"

                    />


                </div>







                <!-- Error -->


                <div

                    v-if="error"

                    class="alert alert-danger"

                >

                    {{ error }}

                </div>






                <!-- Success -->


                <div

                    v-if="message"

                    class="alert alert-success"

                >

                    {{ message }}

                </div>








                <button

                    class="btn btn-primary"

                    type="submit"

                    :disabled="loading"

                >


                    <span v-if="loading">

                        Uploading...

                    </span>


                    <span v-else>

                        Upload Resume

                    </span>



                </button>




                <button

                    v-if="resumeUrl"

                    type="button"

                    class="btn btn-danger ms-2"

                    @click="deleteResume"

                >

                    Delete Resume

                </button>



            </form>


        </div>


    </div>



</div>


</template>





<script>


import {

    getResume,

    uploadResume,

    deleteResume

}

from "../../api/student"





export default {


name:"StudentResume",




data(){


    return{


        file:null,


        resumeUrl:"",


        message:"",


        error:"",


        loading:false


    }


},





methods:{





async fetchResume(){
    try{
        const response = await getResume()
        // Backend returns a binary PDF blob → create a local URL for viewing
        const blob = new Blob([response.data], { type: 'application/pdf' })
        if(this.resumeUrl) URL.revokeObjectURL(this.resumeUrl) // clean old URL
        this.resumeUrl = URL.createObjectURL(blob)
    }
    catch(error){
        // 404 = no resume yet, just silently ignore
        if(error.response?.status !== 404){
            console.log('Could not fetch resume:', error)
        }
        this.resumeUrl = ''
    }
},





selectFile(event){


    const selected = event.target.files[0]



    if(!selected)

        return





    if(selected.type !== "application/pdf"){


        this.error =

        "Only PDF files are allowed"


        this.file = null


        return


    }



    this.error = ""


    this.file = selected



},







async uploadResume(){
    if(!this.file){
        this.error = "Please select a resume file"
        return
    }

    try{
        this.loading = true
        this.error = ''
        this.message = ''

        // Pass raw File — the API function builds the FormData
        const response = await uploadResume(this.file)

        this.message = "Resume uploaded successfully!"
        this.error = ''

        // Refresh resume URL
        await this.fetchResume()

    }
    catch(error){
        this.error = error.response?.data?.message || "Resume upload failed. Please try again."
    }
    finally{
        this.loading = false
    }
},







async deleteResume(){


    try{


        await deleteResume()



        this.resumeUrl = ""



        this.message =

        "Resume deleted successfully"



    }


    catch(error){


        this.error =

        "Unable to delete resume"



    }


}



},





mounted(){


    this.fetchResume()


}



}


</script>