# Online Exam Portal - ExamMaster
> A full-stack web application based on the MERN stack (MongoDB, Express.js, React, Node.js), designed to provide role-based exam management and participation features.

## Overview

Online Exam Portal – **ExamMaster** is a full-stack web application built using the **MERN stack (MongoDB, Express.js, React, Node.js)**. The platform simplifies the process of conducting online examinations with **role-based access control** for Admins/Teachers and Students.

Admins can create and manage both objective and subjective exams, organize them by subject and type, and assign exams to students securely. Students can attempt assigned exams, submit responses, view instant results for objective questions, and track their complete exam history.

The system ensures exam integrity by validating student access, automatically evaluating objective responses, and comparing subjective answers with predefined model answers. The application follows a modular architecture, making it scalable, maintainable, and suitable for real-world academic use.


## Features

| Admin | Student |
|-------|---------|
| Create subjective & objective exams | Attempt subjective and objective exams |
| Organize exams by subject & type | View scores instantly |
| Assign exams to students | Track exam history anytime |


> The answers submitted by students are matched with the model answers provided by the Admin/Teacher at the time of exam creation.

## Fields
### Login
- email
- password

### Signup
- name
- email  
  - `@exam-portal.com` → Admin / Teacher  
  - Other domains → Student
- password
- phone number

## Roles
There are two user roles:
1. **Student**
2. **Admin / Teacher**

## Folder Structure

### Client
```text
client/
├── vite-project/
│   ├── .github/
│   │   └── workflows/
│   │       └── client.yaml
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── redux/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── index.html
│   ├── vite.config.js
│   ├── vercel.json
│   ├── package.json
│   └── package-lock.json
```
### Server
```text
server/
├── .github/
│   └── workflows/
│       └── server.yaml
├── api/
│   └── index.js
├── Controllers/
├── DB/
├── Middleware/
├── Models/
├── Routes/
├── package.json
└── package-lock.json
```

## Getting Started
### Prerequisites
- Node.js
- MongoDB Atlas
- npm or yarn

### Setup
#### 1. Clone the repository
```bash
// For Client
git clone https://github.com/Siddharth2k14/online-exam-portal-client.git

// For Server
git clone https://github.com/Siddharth2k14/online-exam-portal-server.git
```

#### 2. Install Dependencies
```bash
// For Client
npm install

// For Server
npm install
```

#### 3. Backend Setup
```bash
cd server
npm install
# Create a .env file with your MongoDB URI
echo 'MONGO_URI="your-mongodb-uri-here"' > .env
npm start
```

#### 4. Frontend Setup
```bash
cd ../client/vite-project
npm install
npm run dev
```

#### 5. Open in Browser
Visit [http://localhost:5173](http://localhost:5173) to use the portal.

## API Endpoints
### Auth Endpoints
- `POST /api/auth/login` - Login the user
- `POST /api/auth/signup` - Signup the user
- `POST /api/auth/change-password` - Change the password of the user
- `POST /api/auth/forgot-password` - Forgot the password of the user
- `GET /api/auth/all` - Returns all the users based on role

### Question Endpoints
- `POST /api/questions/objective` - Create an objective question
- `POST /api/questions/subjective` - Create a subjective question
- `GET /api/questions/all` - Returns all the questions
- `DELETE /api/questions/objective/:exam_title` - Delete an objective question
- `DELETE /api/questions/subjective/:exam_title` - Delete a subjective question

### Submission Endpoints
- `POST /api/submissions/submit` - Submit the exam
- `POST /api/submissions/result/:submissionId` - Returns the result of the exam
- `GET /api/submissions/all` - Returns all the exams submitted

### Assign Exam Endpoints
- `GET /api/exams/assigned` - Returns the assigned exam
- `POST /api/exams/assign` - Assign an exam to a student

## Tech Stack
- **Frontend:** React, Material UI, Vite
- **Backend:** Node.js, Express, Mongoose
- **Database:** MongoDB
- **Deployment:** Vercel (For Frontend), Render (For Backend)
- **Monitoring:** Uptime Robot, Sentry
- **CI/CD:** Github Actions