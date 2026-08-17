// frontend/src/router/index.js

import {
    createRouter,
    createWebHistory
} from "vue-router"
import auth from "../store/auth"



// =====================================================
// Routes
// =====================================================

const routes = [



    // =========================
    // Authentication Routes
    // =========================

    {
        path:"/auth",

        component:()=>import(
            "../layouts/AuthLayout.vue"
        ),

        children:[

            {
                path:"login",

                name:"Login",

                component:()=>import(
                    "../views/auth/Login.vue"
                )
            },


            {
                path:"student-register",

                name:"StudentRegister",

                component:()=>import(
                    "../views/auth/StudentRegister.vue"
                )
            },

            {
                path:"company-register",

                name:"CompanyRegister",

                component:()=>import(
                    "../views/auth/companyRegister.vue"
                )
            }

        ]

    },





    // =========================
    // Admin Routes
    // =========================

    {
        path:"/admin",

        component:()=>import(
            "../layouts/AdminLayout.vue"
        ),


        children:[


            {
                path:"dashboard",

                name:"AdminDashboard",

                component:()=>import(
                    "../views/admin/Dashboard.vue"
                )

            },


            {
                path:"students",

                name:"AdminStudents",

                component:()=>import(
                    "../views/admin/Students.vue"
                )

            },


            {
                path:"companies",

                name:"AdminCompanies",

                component:()=>import(
                    "../views/admin/companies.vue"
                )

            },


            {
                path:"drives",

                name:"AdminDrives",

                component:()=>import(
                    "../views/admin/Drives.vue"
                )

            },


            {
                path:"applications",

                name:"AdminApplications",

                component:()=>import(
                    "../views/admin/Applications.vue"
                )

            },


            {
                path:"reports",

                name:"AdminReports",

                component:()=>import(
                    "../views/admin/Reports.vue"
                )

            },

            {
                path:"profile",

                name:"AdminProfile",

                component:()=>import(
                    "../views/admin/Profile.vue"
                )
            }

        ]

    },







    // =========================
    // Student Routes
    // =========================

    {
        path:"/student",

        component:()=>import(
            "../layouts/studentLayout.vue"
        ),


        children:[


            {
                path:"dashboard",

                name:"StudentDashboard",

                component:()=>import(
                    "../views/student/Dashboard.vue"
                )

            },


            {
                path:"drives",

                name:"StudentDrives",

                component:()=>import(
                    "../views/student/Drives.vue"
                )

            },


            {
                path:"applications",

                name:"StudentApplications",

                component:()=>import(
                    "../views/student/Applications.vue"
                )

            },


            {
                path:"history",

                name:"StudentHistory",

                component:()=>import(
                    "../views/student/History.vue"
                )

            },


            {
                path:"profile",

                name:"StudentProfile",

                component:()=>import(
                    "../views/student/Profile.vue"
                )

            },


            {
                path:"resume",

                name:"StudentResume",

                component:()=>import(
                    "../views/student/Resume.vue"
                )

            },
            {
                path:"ats-checker",

                name:"StudentATSChecker",

                component:()=>import(
                    "../views/student/ATSChecker.vue"
                )

            }


        ]

    },







    // =========================
    // Company Routes
    // =========================

    {
        path:"/company",

        component:()=>import(
            "../layouts/CompanyLayout.vue"
        ),


        children:[


            {
                path:"dashboard",

                name:"CompanyDashboard",

                component:()=>import(
                    "../views/company/Dashboard.vue"
                )

            },


            {
                path:"profile",

                name:"CompanyProfile",

                component:()=>import(
                    "../views/company/Profile.vue"
                )

            },


            {
                path:"create-drive",

                name:"CreateDrive",

                component:()=>import(
                    "../views/company/CreateDrive.vue"
                )

            },


            {
                path:"drives",

                name:"CompanyDrives",

                component:()=>import(
                    "../views/company/MyDrives.vue"
                )

            },


            {
                path:"applicants",

                name:"CompanyApplicants",

                component:()=>import(
                    "../views/company/Applicants.vue"
                )

            }


        ]

    },







    // =========================
    // Default Route
    // =========================

    {
        path:"/",

        redirect:"/auth/login"

    },






    // =========================
    // 404 Page
    // =========================

    {
        path:"/:pathMatch(.*)*",

        name:"NotFound",

        component:()=>import(
            "../views/errors/404.vue"
        )

    }



]




const router = createRouter({


    history:createWebHistory(),


    routes,


    scrollBehavior(){

        return {

            top:0

        }

    }


})


router.beforeEach((to, from, next) => {
  const publicPages = ['/auth/login', '/auth/student-register', '/auth/company-register']
  const authRequired = !publicPages.includes(to.path)
  
  if (authRequired && !auth.isAuthenticated()) {
    return next('/auth/login')
  }
  
  if (to.path.startsWith('/admin') && !auth.hasRole('admin')) {
    return next('/auth/login')
  }
  
  if (to.path.startsWith('/student') && !auth.hasRole('student')) {
    return next('/auth/login')
  }
  
  if (to.path.startsWith('/company') && !auth.hasRole('company')) {
    return next('/auth/login')
  }
  
  next()
})


export default router