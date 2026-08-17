// frontend/src/api/drive.js

import api from "./axios"


// =====================================================
// Get All Approved Placement Drives
// =====================================================

export function getApprovedDrives(){

    return api.get(
        "/drives/approved"
    )

}



// =====================================================
// Search Placement Drives
// =====================================================

export function searchDrives(keyword){

    return api.get(
        `/drives/search?query=${keyword}`
    )

}



// =====================================================
// Filter Eligible Drives
// =====================================================

export function getEligibleDrives(){

    return api.get(
        "/drives/eligible"
    )

}



// =====================================================
// Get Single Drive Details
// =====================================================

export function getDriveById(driveId){

    return api.get(
        `/drives/${driveId}`
    )

}



// =====================================================
// Create Placement Drive (Company)
// =====================================================

export function createDrive(data){

    return api.post(
        "/drives/create",
        data
    )

}



// =====================================================
// Update Drive Details (Company)
// =====================================================

export function updateDrive(
    driveId,
    data
){

    return api.put(

        `/drives/${driveId}`,

        data

    )

}



// =====================================================
// Delete Drive (Company)
// =====================================================

export function deleteDrive(driveId){

    return api.delete(

        `/drives/${driveId}`

    )

}



// =====================================================
// Approve Drive (Admin)
// =====================================================

export function approveDrive(driveId){

    return api.put(

        `/drives/${driveId}/approve`

    )

}



// =====================================================
// Reject Drive (Admin)
// =====================================================

export function rejectDrive(driveId){

    return api.put(

        `/drives/${driveId}/reject`

    )

}



// =====================================================
// Close Drive
// =====================================================

export function closeDrive(driveId){

    return api.put(

        `/drives/${driveId}/close`

    )

}



// =====================================================
// Apply For Placement Drive (Student)
// =====================================================

export function applyForDrive(driveId){

    return api.post(

        `/drives/${driveId}/apply`

    )

}



// =====================================================
// Check Application Status
// =====================================================

export function getApplicationStatus(driveId){

    return api.get(

        `/drives/${driveId}/application-status`

    )

}



// =====================================================
// Get Drive Applications
// =====================================================

export function getDriveApplications(driveId){

    return api.get(

        `/drives/${driveId}/applications`

    )

}