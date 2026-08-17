<template>
  <div class="ats-checker p-4">
    <div class="row mb-4">
      <div class="col-12">
        <h2 class="fw-bold text-dark mb-2"><i class="bi bi-shield-check text-primary me-2"></i>ATS Resume Matcher</h2>
        <p class="text-muted">Analyze your resume against a target job description to get an ATS compatibility score.</p>
      </div>
    </div>

    <div class="row gy-4">
      <div class="col-lg-6">
        <div class="card border-0 shadow-sm rounded-4 h-100">
          <div class="card-header bg-white border-0 pt-4 pb-0">
            <h5 class="fw-bold"><i class="bi bi-file-text me-2 text-info"></i>Job Description</h5>
          </div>
          <div class="card-body">
            <div class="form-floating h-100">
              <textarea 
                class="form-control h-100 border-2 custom-focus" 
                id="jobDesc" 
                placeholder="Paste Job Description here..."
                v-model="jobDescription"
                style="min-height: 250px;"
              ></textarea>
              <label for="jobDesc">Paste target Job Description here...</label>
            </div>
          </div>
        </div>
      </div>

      <div class="col-lg-6">
        <div class="card border-0 shadow-sm rounded-4 h-100">
          <div class="card-header bg-white border-0 pt-4 pb-0">
            <h5 class="fw-bold"><i class="bi bi-person-lines-fill me-2 text-success"></i>Your Resume Text</h5>
          </div>
          <div class="card-body">
            <div class="form-floating h-100">
              <textarea 
                class="form-control h-100 border-2 custom-focus" 
                id="resumeText" 
                placeholder="Paste your Resume text here..."
                v-model="resumeText"
                style="min-height: 250px;"
              ></textarea>
              <label for="resumeText">Paste your resume text here...</label>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-12 text-center mt-4">
        <button 
          class="btn btn-primary px-5 py-3 rounded-pill fw-bold shadow-sm analyze-btn"
          @click="analyzeResume"
          :disabled="!jobDescription || !resumeText || loading"
        >
          <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
          {{ loading ? 'Analyzing...' : 'Run ATS Analysis' }}
          <i v-if="!loading" class="bi bi-lightning-fill ms-2 text-warning"></i>
        </button>
      </div>

      <!-- Results Section -->
      <div class="col-12 mt-5" v-if="score !== null">
        <div class="card border-0 shadow rounded-4 overflow-hidden">
          <div class="card-body p-5">
            <h3 class="fw-bold text-center mb-5">Analysis Results</h3>
            
            <div class="row align-items-center">
              <div class="col-md-5 text-center mb-4 mb-md-0">
                <div class="score-circle mx-auto" :class="scoreColorClass">
                  <div class="score-inner">
                    <h1 class="display-3 fw-bold mb-0">{{ score }}<span class="fs-4">%</span></h1>
                    <span class="text-muted">Match Score</span>
                  </div>
                </div>
              </div>
              
              <div class="col-md-7">
                <h4 class="fw-bold mb-3">Feedback & Recommendations</h4>
                <div class="alert" :class="feedbackAlertClass">
                  <i class="bi me-2" :class="feedbackIconClass"></i>
                  {{ feedbackMessage }}
                </div>
                
                <h5 class="fw-bold mt-4 mb-3">Keyword Matching (Simulated)</h5>
                <div class="d-flex flex-wrap gap-2">
                  <span class="badge bg-success-subtle text-success px-3 py-2 rounded-pill border border-success"><i class="bi bi-check-circle me-1"></i>Found 8/10 core skills</span>
                  <span class="badge bg-warning-subtle text-warning px-3 py-2 rounded-pill border border-warning"><i class="bi bi-exclamation-circle me-1"></i>Missing action verbs</span>
                  <span class="badge bg-info-subtle text-info px-3 py-2 rounded-pill border border-info"><i class="bi bi-info-circle me-1"></i>Formatting looks clean</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ATSChecker",
  data() {
    return {
      jobDescription: "",
      resumeText: "",
      loading: false,
      score: null,
    }
  },
  computed: {
    scoreColorClass() {
      if (this.score >= 80) return "border-success text-success"
      if (this.score >= 50) return "border-warning text-warning"
      return "border-danger text-danger"
    },
    feedbackAlertClass() {
      if (this.score >= 80) return "alert-success"
      if (this.score >= 50) return "alert-warning"
      return "alert-danger"
    },
    feedbackIconClass() {
      if (this.score >= 80) return "bi-check-circle-fill"
      if (this.score >= 50) return "bi-exclamation-triangle-fill"
      return "bi-x-octagon-fill"
    },
    feedbackMessage() {
      if (this.score >= 80) return "Excellent! Your resume is highly tailored to this job description. It is very likely to pass the ATS filter."
      if (this.score >= 50) return "Good start, but there is room for improvement. Try integrating more specific keywords from the job description."
      return "Low match detected. You need to heavily revise your resume to include the required skills and phrases from the job description."
    }
  },
  methods: {
    analyzeResume() {
      this.loading = true
      this.score = null
      
      // Simulate API delay and dummy analysis
      setTimeout(() => {
        // Simple dummy logic based on length comparison and random factor
        const jdWords = this.jobDescription.split(' ').length
        const resWords = this.resumeText.split(' ').length
        
        let baseScore = 60
        if (Math.abs(jdWords - resWords) < 50) baseScore += 20
        else if (resWords > jdWords) baseScore += 10
        else baseScore -= 10
        
        // Add random variance between -15 and +15
        const variance = Math.floor(Math.random() * 30) - 15
        
        let finalScore = baseScore + variance
        if (finalScore > 98) finalScore = 98
        if (finalScore < 25) finalScore = 25
        
        this.score = finalScore
        this.loading = false
      }, 1500)
    }
  }
}
</script>

<style scoped>
.custom-focus:focus {
  border-color: #0ea5e9;
  box-shadow: 0 0 0 0.25rem rgba(14, 165, 233, 0.25);
}

.analyze-btn {
  background: linear-gradient(90deg, #0ea5e9 0%, #10b981 100%);
  border: none;
  transition: all 0.3s ease;
}

.analyze-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(16, 185, 129, 0.3) !important;
}

.score-circle {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  border: 15px solid;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  background: #f8fafc;
  box-shadow: inset 0 0 20px rgba(0,0,0,0.05), 0 10px 30px rgba(0,0,0,0.1);
  transition: all 0.5s ease-out;
}

.score-inner {
  text-align: center;
}

.badge {
  font-size: 0.9rem;
  font-weight: 600;
}
</style>
