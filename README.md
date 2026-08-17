# Placement Portal

A modern, comprehensive full-stack web application designed to connect students, companies, and university administrators on a single seamless platform for managing the entire campus recruitment process.

---

## 🚀 Features

### 👨‍🎓 Student Module
- **Registration & Authentication**: Secure sign up and login.
- **Student Dashboard**: View application stats, available drives, and notifications.
- **Placement Drives**: Browse available drives matching eligibility criteria.
- **Job Applications**: Apply for placement drives and track application status.
- **Resume Management**: Upload, update, and manage resumes (PDFs).
- **Placement History**: Keep a record of past applications and selections.

### 🏢 Company Module
- **Registration & Authentication**: Company onboarding (requires admin approval).
- **Company Dashboard**: Monitor active drives, applicant counts, and recruitment metrics.
- **Drive Management**: Create, edit, and close placement drives.
- **Applicant Tracking**: View students who applied for drives.
- **Screening & Selection**: Shortlist, interview, select, or reject candidates.

### 👨‍💼 Admin Module
- **System Overview**: High-level dashboard with statistics across the platform.
- **User Management**: Manage student and company accounts (approve/reject/blacklist).
- **Drive Monitoring**: Oversee all placement drives.
- **Reporting**: Export applications and user data to CSV for analysis.

---

## 🛠️ Technology Stack

### Frontend (Client-side)
- **Framework**: Vue 3
- **Build Tool**: Vite
- **Routing & State**: Vue Router, Vuex
- **Styling**: Bootstrap 5, Custom CSS
- **HTTP Client**: Axios

### Backend (Server-side)
- **Framework**: Flask (Python)
- **Database**: SQLite (via SQLAlchemy)
- **Authentication**: Flask-Security-Too (Session/Token based auth)
- **Caching**: Flask-Caching (SimpleCache)
- **File Uploads**: Werkzeug for secure file processing

---

## 📁 Project Structure

```
placement-portal/
│
├── backend/                  # Flask REST API backend
│   ├── app.py                # App entry point
│   ├── config.py             # Configuration settings
│   ├── extensions.py         # Flask extensions (db, security, etc.)
│   ├── models/               # SQLAlchemy database models
│   ├── routes/               # API endpoints (auth, student, company, admin)
│   ├── services/             # Business logic and database queries
│   └── uploads/              # Uploaded resumes and files
│
├── frontend/                 # Vue 3 Frontend application
│   ├── public/               # Static assets
│   ├── src/
│   │   ├── api/              # Axios API communication services
│   │   ├── components/       # Reusable Vue components
│   │   ├── router/           # Vue Router configuration
│   │   ├── store/            # Vuex state management
│   │   └── views/            # Main pages (Admin, Student, Company)
│   ├── index.html
│   └── package.json
│
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Node.js (v16+)
- Python (3.8+)
- pip (Python package manager)

### 1. Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`

4. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the backend development server:**
   ```bash
   python app.py
   ```
   *The backend will start running on `http://127.0.0.1:5000`*

### 2. Frontend Setup

1. **Open a new terminal and navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install Node dependencies:**
   ```bash
   npm install
   ```

3. **Start the frontend development server:**
   ```bash
   npm run dev
   ```
   *The application will start running on `http://localhost:5173`. Open this URL in your browser.*

*(Note: The frontend uses a Vite proxy to forward `/api` requests to the backend server seamlessly without CORS issues).*

---

## 🔐 Authentication Flow

The application uses **Flask-Security-Too** for robust authentication.
- Passwords are securely hashed and salted.
- Sessions and CSRF protection are managed via HTTP Cookies.
- Different user types (Students, Companies, Admin) share a unified auth system but are assigned specific `Roles` to control access to API endpoints.

---

## 👥 User Roles & Permissions

| Role | Access Level | Description |
| :--- | :--- | :--- |
| **Admin** | Full System Access | Can approve/reject companies, manage all users, and monitor system health. |
| **Student** | Student Dashboard | Can upload resumes, apply for eligible placement drives, and track statuses. |
| **Company**| Company Dashboard | Can create placement drives, review applicants, and update applicant statuses. Must be approved by Admin first. |

---

## 📄 License

This project is licensed under the MIT License.