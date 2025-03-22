# 📦 IoT Dashboard Full Stack App

A full-stack web application for managing users, IoT devices, and time-series data.

- ⚙️ **Backend**: FastAPI, PostgreSQL, DynamoDB  
- 🖥️ **Frontend**: Next.js (React), Tailwind CSS, ShadCN UI

---

## 🚀 Features

- User registration and login with JWT
- Protected routes using OAuth2
- Device creation and listing
- IoT data ingestion via FastAPI and DynamoDB
- Fully styled frontend with modern component library

---

## 🧰 Prerequisites

### Backend
- Python 3.11+
- PostgreSQL running locally on port `5432`
- AWS account with DynamoDB table `IoT_Data` created

### Frontend
- Node.js (LTS version recommended)
- npm

---

## 🛠️ Backend Setup (FastAPI)

### 1. Clone the Repo & Create Virtual Environment
```bash
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1   # For Windows PowerShell
# or
source venv/bin/activate      # For macOS/Linux
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
Create a `.env` file in the `backend/` folder:

```env
DATABASE_URL=postgresql+asyncpg://iot_user:securepassword@localhost/iot_backend
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_REGION=us-west-2
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 4. Set Up PostgreSQL
- Create the `iot_backend` database
- Create a user `iot_user` with password `securepassword`
- Grant all privileges to that user

### 5. Run Alembic Migrations
```bash
python -m alembic upgrade head
```

### 6. Start the API
```bash
uvicorn app.main:app --reload
```

- API: http://127.0.0.1:8000  
- Swagger Docs: http://127.0.0.1:8000/docs

---

## 💻 Frontend Setup (Next.js + ShadCN UI)

### 1. Navigate to Frontend Directory
```bash
cd frontend
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Environment Variables
Create a `.env.local` file with:

```env
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
```

### 4. Start the Frontend
```bash
npm run dev
```

- Frontend: http://localhost:3000

---

## 📂 Project Structure

```
iot-dashboard/
├── backend/
│   ├── app/
│   ├── .env
│   ├── requirements.txt
│   ├── alembic/
│   └── alembic.ini
├── frontend/
│   ├── src/
│   ├── package.json
│   └── .env.local
└── README.md
```

---

## 🔐 Notes on Webhook Support

You can add a webhook receiver endpoint in FastAPI by creating a `/webhook` route.  
This will allow IoT sensors to POST data directly to your backend.

---

## ✅ To Reinstall on a New Machine

### Backend:
```bash
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Frontend:
```bash
cd frontend
npm install
```

---

## 📄 License

MIT License

---

_For help, contact: [Zack](mailto:zack@mule-labs.com)_
