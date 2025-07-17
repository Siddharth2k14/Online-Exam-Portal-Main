<<<<<<< HEAD
# Online Exam Portal

An online exam management system built with the MERN stack (MongoDB, Express, React, Node.js) and Vite for a fast, modern development experience.

## Features

- **Admin Panel**
  - Create new exams and add questions (objective type supported)
  - View all exams as cards with exam title and number of questions
  - Delete exams (removes all associated questions)
  - View all questions for a specific exam

- **Authentication**
  - Simple signup and login for admin and students (MongoDB-based)

- **Exam Management**
  - Exams and questions are stored in MongoDB
  - Exams are grouped and displayed by title
  - Each exam card shows:
    - Exam title
    - Number of questions
    - View and Delete buttons

## Folder Structure

```
online-exam-portal/
├── client/
│   └── vite-project/
│       └── src/
│           └── components/
│               ├── Exam Creation/
│               ├── Manage Exams/
│               └── Objective Exam Creation/
├── server/
│   ├── DB/
│   ├── Models/
│   ├── Routes/
│   ├── .env
│   └── index.js
```

## Getting Started

### Prerequisites

- Node.js (v18+ recommended)
- MongoDB Atlas account (or local MongoDB)

### Setup

#### 1. Clone the repository

```bash
git clone https://github.com/yourusername/online-exam-portal.git
cd online-exam-portal
```

#### 2. Backend Setup

```bash
cd server
npm install
# Create a .env file with your MongoDB URI
echo 'MONGO_URI="your-mongodb-uri-here"' > .env
npm start
```

#### 3. Frontend Setup

```bash
cd ../client/vite-project
npm install
npm run dev
```

#### 4. Open in Browser

Visit [http://localhost:5173](http://localhost:5173) to use the portal.

## API Endpoints

- `POST /api/auth/signup` — Register a new user
- `POST /api/auth/:role/login` — Login as admin or student
- `POST /api/questions` — Add a question to an exam
- `GET /api/questions/all` — Get all exams grouped by title
- `GET /api/questions/:examTitle` — Get all questions for an exam
- `DELETE /api/questions/:examTitle` — Delete an exam and its questions

## Technologies Used

- **Frontend:** React, Vite, Material UI
- **Backend:** Node.js, Express, Mongoose
- **Database:** MongoDB Atlas

## License

This project is licensed under the MIT License.

---

**Contributions and feedback
=======
>>>>>>> d784a9d (Adding the component for Account Settings for the admin dashboard)
