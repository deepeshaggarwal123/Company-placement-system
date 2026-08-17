// frontend/src/api/auth.js

import api from "./axios"


// =====================================================
// Login
// =====================================================

export function login(data){

    return api.post(
        "/auth/login",
        data
    )

}



// =====================================================
// Student Registration
// =====================================================

export function studentRegister(data){

    return api.post(
        "/auth/student/register",
        data
    )

}



// =====================================================
// Company Registration
// =====================================================

export function companyRegister(data){

    return api.post(
        "/auth/company/register",
        data
    )

}



// =====================================================
// Logout
// =====================================================

export function logout(){

    return api.post(
        "/auth/logout"
    )

}



// =====================================================
// Get Current User
// =====================================================

export function getCurrentUser(){

    return api.get(
        "/auth/me"
    )

}



// =====================================================
// Change Password
// =====================================================

export function changePassword(data){

    return api.put(
        "/auth/change-password",
        data
    )

}



// =====================================================
// Forgot Password
// =====================================================

export function forgotPassword(email){

    return api.post(
        "/auth/forgot-password",
        {
            email: email
        }
    )

}



// =====================================================
// Reset Password
// =====================================================

export function resetPassword(token, password){

    return api.post(

        `/auth/reset-password/${token}`,

        {
            password: password
        }

    )

}