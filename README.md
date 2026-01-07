# Fynd AI Intern Assessment 2.0

A complete AI-powered review management system built with FastAPI, Reflex, and Google Gemini AI.

## 🎯 Project Overview

This project consists of two main tasks:

### Task 1: Rating Prediction via Prompting
- Jupyter notebook demonstrating LLM-based rating prediction
- Three prompting strategies: Zero-shot, Rubric-based, and Self-reasoning
- Evaluation metrics and comparison analysis

### Task 2: AI Review System
- **Backend**: FastAPI with MySQL database
- **Frontend**: Reflex (Python-based web framework)
- **AI Integration**: Google Gemini for automated responses and analysis

## 🚀 Features

- ✅ Submit customer reviews with ratings (1-5 stars)
- ✅ AI-generated personalized responses to customers
- ✅ Admin dashboard with AI-powered summaries and recommended actions
- ✅ MySQL database for persistent storage
- ✅ RESTful API with interactive documentation
- ✅ Real-time review processing

## 📁 Project Structure

```
project_root/
├── task1/                      # Rating Prediction Task
│   ├── rating_prediction.ipynb
│   ├── prompts.py
│   └── evaluator.py
├── task2/                      # Review System
│   ├── backend/                # FastAPI Backend
│   │   ├── main.py
│   │   ├── db.py
│   │   ├── schemas.py
│   │   ├── llm.py
│   │   └── prompts.py
│   └── frontend/               # Reflex Frontend
│       ├── app.py
│       ├── user_dashboard.py
│       ├── admin_dashboard.py
│       └── rxconfig.py
├── requirements.txt
├── .env.example
└── README.md
```

## 🛠️ Tech Stack

- **Backend**: FastAPI, SQLAlchemy, Uvicorn
- **Frontend**: Reflex (Python)
- **Database**: MySQL
- **AI/ML**: Google Gemini AI, Pandas, Scikit-learn
- **Others**: Pydantic, Python-dotenv

## 📋 Prerequisites

- Python 3.8+
- MySQL Server (or MySQL Workbench)
- Google Gemini API Key ([Get it here](https://makersuite.google.com/app/apikey))

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JainManav05/Fynd-ai-.git
cd Fynd-ai-
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
.\venv\Scripts\Activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup MySQL Database

Open MySQL Workbench and run:

```sql
CREATE DATABASE fynd_reviews CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

For detailed MySQL setup, see [MYSQL_SETUP.md](MYSQL_SETUP.md)

### 5. Configure Environment Variables

Copy `.env.example` to `.env` and update:

```bash
cp .env.example .env
```

Edit `.env`:

```
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=mysql+pymysql://root:your_password@localhost:3306/fynd_reviews
```

### 6. Test Database Connection

```bash
python test_db_connection.py
```

## 🚀 Running the Application

### Start Backend (Terminal 1)

```bash
cd project_root
.\venv\Scripts\Activate
python -m uvicorn task2.backend.main:app --reload
```

Backend will run on: **http://localhost:8000**

### Start Frontend (Terminal 2)

```bash
cd project_root
.\venv\Scripts\Activate
cd task2/frontend
reflex init
reflex run
```

Frontend will run on: **http://localhost:3000**

## 🌐 Access Points

- **User Dashboard**: http://localhost:3000
- **Admin Dashboard**: http://localhost:3000/admin
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📊 Task 1: Running the Notebook

```bash
cd task1
jupyter notebook rating_prediction.ipynb
```

## 🔑 API Endpoints

### POST `/submit_review`
Submit a new review with AI processing

**Request Body:**
```json
{
  "rating": 5,
  "review_text": "Amazing service and great food!"
}
```

**Response:**
```json
{
  "id": 1,
  "rating": 5,
  "review_text": "Amazing service and great food!",
  "ai_response": "Thank you for your wonderful feedback!...",
  "ai_summary": "Customer highly satisfied with service and food",
  "ai_action": "Reward staff member",
  "created_at": "2026-01-07T23:00:00"
}
```

### GET `/get_reviews`
Retrieve all reviews with AI analysis

### GET `/health`
Health check endpoint

## 📸 Screenshots

### User Dashboard
Submit reviews and receive AI-generated responses

### Admin Dashboard
View all reviews with AI summaries and recommended actions

## 🧪 Testing

1. Submit a review via User Dashboard
2. Check Admin Dashboard for AI analysis
3. Verify data in MySQL:
   ```sql
   USE fynd_reviews;
   SELECT * FROM reviews;
   ```

## 📦 Deployment

### Backend (Render)
1. Push to GitHub
2. Create Web Service on Render
3. Set environment variables
4. Deploy from repository

### Frontend (Vercel)
1. Connect GitHub repository
2. Set build command: `reflex export --frontend-only`
3. Set output directory: `.web/_static`
4. Deploy

See [README.md](README.md) for detailed deployment instructions.

## 🤝 Contributing

This is an assessment project. For questions or issues, please contact the repository owner.

## 📄 License

This project is created for the Fynd AI Intern Assessment.

## 👤 Author

**Manav Jain**
- GitHub: [@JainManav05](https://github.com/JainManav05)

## 🙏 Acknowledgments

- Fynd Academy for the assessment opportunity
- Google Gemini AI for LLM capabilities
- FastAPI and Reflex communities

---

**Note**: Make sure to never commit your `.env` file with actual API keys to GitHub!
