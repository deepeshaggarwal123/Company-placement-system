// frontend/src/api/company.js

import api from "./axios"


// =====================================================
// Company Dashboard
// =====================================================

export function getCompanyDashboard(){

    return api.get(
        "/company/dashboard"
    )

}



// =====================================================
// Company Profile
// =====================================================

export function getCompanyProfile(){

    return api.get(
        "/company/profile"
    )

}



export function updateCompanyProfile(data){

    return api.put(
        "/company/profile",
        data
    )

}



// =====================================================
// Placement Drive Management
// =====================================================

export function createPlacementDrive(data){

    return api.post(
        "/company/drives/create",
        data
    )

}



export function getMyDrives(){

    return api.get(
        "/company/drives"
    )

}



export function getDriveDetails(driveId){

    return api.get(
        `/company/drives/${driveId}`
    )

}



export function closeDrive(driveId){

    return api.put(
        `/company/drives/${driveId}/close`
    )

}



// =====================================================
// Student Applications
// =====================================================

export function getApplicants(driveId){

    return api.get(
        `/company/drives/${driveId}/applicants`
    )

}



// =====================================================
// Update Application Status
// =====================================================

export function updateApplicationStatus(
    applicationId,
    status
){

    return api.put(

        `/company/application/${applicationId}/status`,

        {
            status: status
        }

    )

}



// =====================================================
// Shortlist Student
// =====================================================

export function shortlistStudent(applicationId){

    return api.put(

        `/company/application/${applicationId}/shortlist`

    )

}



// =====================================================
// Reject Student
// =====================================================

export function rejectStudent(applicationId){

    return api.put(

        `/company/application/${applicationId}/reject`

    )

}



// =====================================================
// Schedule Interview
// =====================================================

export function scheduleInterview(
    applicationId,
    interviewData
){

    return api.put(

        `/company/application/${applicationId}/interview`,

        interviewData

    )

}



// =====================================================
// Final Selection
// =====================================================

export function selectStudent(applicationId){

    return api.put(

        `/company/application/${applicationId}/select`

    )

}

export const createDrive = createPlacementDrive;

export function deleteDrive(driveId){
    return api.delete(`/company/drives/${driveId}`);
}

export function updateDriveStatus(driveId, status){
    return api.put(`/company/drives/${driveId}/status`, { status });
}