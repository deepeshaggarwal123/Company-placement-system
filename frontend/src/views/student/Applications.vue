<template>
  <div class="container-fluid py-3">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h2 class="fw-bold mb-1">My Applications</h2>
        <p class="text-muted mb-0">Track the status of your placement applications.</p>
      </div>
    </div>

    <div class="card shadow-sm">
      <div class="card-body">
        <div v-if="loading" class="text-center py-4">Loading...</div>
        <div v-else-if="applications.length === 0" class="text-center py-4 text-muted">
          No applications found yet.
        </div>
        <div v-else class="table-responsive">
          <table class="table table-hover align-middle mb-0">
            <thead>
              <tr>
                <th>Drive</th>
                <th>Company</th>
                <th>Status</th>
                <th>Applied On</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="application in applications" :key="application.id">
                <td>{{ application.drive_title || application.drive?.title || "N/A" }}</td>
                <td>{{ application.company_name || application.company?.name || "N/A" }}</td>
                <td>
                  <span class="badge rounded-pill" :class="statusClass(application.status)">
                    {{ application.status || "Applied" }}
                  </span>
                </td>
                <td>{{ formatDate(application.created_at) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getMyApplications } from "../../api/student"

export default {
  name: "StudentApplications",
  data() {
    return {
      applications: [],
      loading: true
    }
  },
  async mounted() {
    try {
      const response = await getMyApplications()
      this.applications = response.data.applications || response.data || []
    } catch (error) {
      console.error(error)
    } finally {
      this.loading = false
    }
  },
  methods: {
    statusClass(status) {
      const map = {
        applied: "bg-primary",
        shortlisted: "bg-info",
        selected: "bg-success",
        rejected: "bg-danger"
      }
      return map[status?.toLowerCase()] || "bg-secondary"
    },
    formatDate(value) {
      if (!value) return "N/A"
      return new Date(value).toLocaleDateString()
    }
  }
}
</script>
