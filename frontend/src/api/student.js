// frontend/src/api/student.js

import api from "./axios"

// =====================================================
// Student Dashboard
// =====================================================

export function getStudentDashboard() {
    return api.get("/student/dashboard")
}

// =====================================================
// Student Profile
// =====================================================

export function getStudentProfile() {
    return api.get("/student/profile")
}

export function updateStudentProfile(data) {
    return api.put("/student/profile", data)
}

// =====================================================
// Placement Drives
// =====================================================

export function getAvailableDrives() {
    return api.get("/student/drives")
}

export function searchDrives(keyword) {
    return api.get(`/student/drives/search?query=${keyword}`)
}

export function getDriveDetails(driveId) {
    return api.get(`/student/drives/${driveId}`)
}

// =====================================================
// Apply For Placement Drive
// =====================================================

export function applyForDrive(driveId) {
    return api.post(`/student/apply/${driveId}`)
}

// =====================================================
// Application History
// =====================================================

export function getMyApplications() {
    return api.get("/student/applications")
}

export function getApplicationStatus(applicationId) {
    return api.get(`/student/application/${applicationId}`)
}

// =====================================================
// Resume Upload
// =====================================================

export function uploadResume(file) {
    const formData = new FormData()
    formData.append("resume", file)

    return api.post("/student/upload-resume", formData)
}

// =====================================================
// Placement History
// =====================================================

export function getPlacementHistory() {
    return api.get("/student/placement-history")
}

// =====================================================
// Export Application History CSV
// =====================================================

export function exportApplications() {
    return api.get("/student/export-applications", {
        responseType: "blob"
    })
}

export function getResume() {
    return api.get("/student/resume", { responseType: "blob" })
}

export function deleteResume() {
    return api.delete("/student/resume")
}
