// frontend/src/store/auth.js


import { reactive } from "vue"



// =====================================================
// Authentication Store
// =====================================================


const auth = reactive({


    // Current User

    user: JSON.parse(

        localStorage.getItem("user")

    ) || null,



    // JWT Token

    token: localStorage.getItem(

        "token"

    ) || null,



    // User Role

    role: localStorage.getItem(

        "role"

    ) || null,



    // =================================================
    // Login Function
    // =================================================

    login(userData, token){


        this.user = userData


        this.token = token


        this.role = userData.role



        localStorage.setItem(

            "user",

            JSON.stringify(userData)

        )


        localStorage.setItem(

            "token",

            token

        )


        localStorage.setItem(

            "role",

            userData.role

        )


    },





    // =================================================
    // Logout Function
    // =================================================

    logout(){


        this.user = null


        this.token = null


        this.role = null



        localStorage.removeItem(

            "user"

        )


        localStorage.removeItem(

            "token"

        )


        localStorage.removeItem(

            "role"

        )


    },





    // =================================================
    // Check Login
    // =================================================

    isAuthenticated(){


        return this.token !== null


    },





    // =================================================
    // Check Role
    // =================================================

    hasRole(requiredRole){


        return this.role === requiredRole


    }


})



export default auth