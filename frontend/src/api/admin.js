// frontend/src/api/admin.js

import api from "./axios"


// =====================================================
// Admin Dashboard
// =====================================================

export function getAdminDashboard(){

    return api.get(
        "/admin/dashboard"
    )

}



// =====================================================
// Students Management
// =====================================================

export function getAllStudents(){

    return api.get(
        "/admin/students"
    )

}


export function searchStudents(keyword){

    return api.get(
        `/admin/students/search?query=${keyword}`
    )

}


export function deactivateStudent(studentId){

    return api.put(
        `/admin/student/${studentId}/deactivate`
    )

}


export function blacklistStudent(studentId){

    return api.put(
        `/admin/student/${studentId}/blacklist`
    )

}



// =====================================================
// Companies Management
// =====================================================

export function getAllCompanies(){

    return api.get(
        "/admin/companies"
    )

}


export function searchCompanies(keyword){

    return api.get(
        `/admin/companies/search?query=${keyword}`
    )

}



export function approveCompany(companyId){

    return api.put(
        `/admin/company/${companyId}/approve`
    )

}



export function rejectCompany(companyId){

    return api.put(
        `/admin/company/${companyId}/reject`
    )

}



export function blacklistCompany(companyId){

    return api.put(
        `/admin/company/${companyId}/blacklist`
    )

}



// =====================================================
// Placement Drive Management
// =====================================================

export function getAllDrives(){

    return api.get(
        "/admin/drives"
    )

}



export function approveDrive(driveId){

    return api.put(
        `/admin/drive/${driveId}/approve`
    )

}



export function rejectDrive(driveId){

    return api.put(
        `/admin/drive/${driveId}/reject`
    )

}



// =====================================================
// Applications
// =====================================================

export function getAllApplications(){

    return api.get(
        "/admin/applications"
    )

}



// =====================================================
// Reports
// =====================================================

export function getPlacementReport(){

    return api.get(
        "/admin/reports/monthly"
    )

}



// =====================================================
// Export Report
// =====================================================

export function exportReport(){

    return api.get(
        "/admin/reports/export",
        {
            responseType:"blob"
        }
    )

}