// frontend/src/api/axios.js

import axios from "axios"


// =====================================================
// Axios Instance
// =====================================================

const api = axios.create({

    // Use Vite proxy to avoid CORS issues (proxy: /api -> http://localhost:5000)
    baseURL: "/api",

    // Do NOT send credentials cross-origin; proxy handles this
    withCredentials: false,

    headers: {
        "Content-Type": "application/json"
    }

})



// =====================================================
// Request Interceptor
// =====================================================

api.interceptors.request.use(

    (config) => {


        // JWT Token (if using token authentication)

        const token = localStorage.getItem(
            "token"
        )


        if(token){

            config.headers.Authorization =
            `Bearer ${token}`

        }


        return config

    },


    (error)=>{

        return Promise.reject(error)

    }

)



// =====================================================
// Response Interceptor
// =====================================================

api.interceptors.response.use(

    (response)=>{


        return response


    },


    (error)=>{


        if(error.response){


            const status =
            error.response.status



            // Unauthorized — only redirect if NOT already on an auth page
            if (status === 401) {
                const publicPaths = ["/auth/login", "/auth/student/register", "/auth/company/register"]
                const isPublic = publicPaths.some(p => window.location.pathname.startsWith(p))

                if (!isPublic) {
                    localStorage.removeItem("token")
                    localStorage.removeItem("user")
                    localStorage.removeItem("role")
                    window.location.href = "/auth/login"
                }
            }


            // Forbidden

            if(status === 403){

                console.log(
                    "Access denied"
                )

            }


        }


        return Promise.reject(error)

    }

)



export default api