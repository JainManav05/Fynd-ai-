# Fynd AI Intern Assessment 2.0 - Project Report

**Submitted by:** Manav Jain  
**GitHub Repository:** https://github.com/JainManav05/Fynd-ai-.git  
**Date:** January 8, 2026

---

## Executive Summary

This report presents a complete AI-powered review management system developed as part of the Fynd AI Intern Assessment 2.0. The project demonstrates proficiency in full-stack development, machine learning integration, and modern web technologies.

**Key Achievements:**
- ✅ Implemented rating prediction using multiple LLM prompting strategies
- ✅ Built production-ready FastAPI backend with MySQL integration
- ✅ Developed interactive web dashboards using Reflex framework
- ✅ Integrated Google Gemini AI for automated review analysis
- ✅ Deployed code to GitHub with professional documentation

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Task 1: Rating Prediction via Prompting](#task-1)
3. [Task 2: AI Review System](#task-2)
4. [Technical Architecture](#technical-architecture)
5. [Implementation Details](#implementation-details)
6. [Testing & Validation](#testing-validation)
7. [Deployment Strategy](#deployment-strategy)
8. [Challenges & Solutions](#challenges-solutions)
9. [Future Enhancements](#future-enhancements)
10. [Conclusion](#conclusion)

---

## 1. Project Overview {#project-overview}

### 1.1 Objective
Develop a comprehensive AI-powered review management system that:
- Predicts ratings from review text using LLM prompting
- Processes customer reviews with AI-generated responses
- Provides admin analytics with actionable insights

### 1.2 Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Backend | FastAPI | RESTful API server |
| Frontend | Reflex | Python-based web framework |
| Database | MySQL | Persistent data storage |
| AI/ML | Google Gemini | LLM for text generation |
| ORM | SQLAlchemy | Database abstraction |
| Validation | Pydantic | Data validation |
| Notebook | Jupyter | Task 1 analysis |

### 1.3 Project Structure

```
project_root/
├── task1/                      # Rating Prediction
│   ├── rating_prediction.ipynb
│   ├── prompts.py
│   └── evaluator.py
├── task2/
│   ├── backend/                # FastAPI Backend
│   │   ├── main.py
│   │   ├── db.py
│   │   ├── schemas.py
│   │   ├── llm.py
│   │   └── prompts.py
│   └── frontend/               # Reflex Frontend
│       ├── app.py
│       ├── user_dashboard.py
│       └── admin_dashboard.py
├── requirements.txt
└── README.md
```

---

## 2. Task 1: Rating Prediction via Prompting {#task-1}

### 2.1 Objective
Predict star ratings (1-5) from review text using different LLM prompting strategies.

### 2.2 Prompting Strategies Implemented

#### Strategy 1: Zero-Shot Prompting
**Approach:** Direct instruction without examples or context.

**Prompt Template:**
```
You are an expert sentiment analyzer. 
Predict the star rating (1-5) for the following review.
Return the result in JSON format.

Review: "{review}"
```

**Advantages:**
- Simple and fast
- No training data required
- Works well for clear sentiment

**Limitations:**
- May struggle with nuanced reviews
- Less consistent on edge cases

#### Strategy 2: Rubric-Based Prompting
**Approach:** Provide explicit rating criteria.

**Rubric:**
- 1 Star: Extremely negative, severe issues
- 2 Stars: Mostly negative, significant complaints
- 3 Stars: Mixed, average experience
- 4 Stars: Mostly positive, minor complaints
- 5 Stars: Excellent, highly satisfied

**Advantages:**
- More consistent results
- Better handling of edge cases
- Aligns with business criteria

#### Strategy 3: Self-Reasoning (Chain of Thought)
**Approach:** Guide LLM through step-by-step analysis.

**Steps:**
1. Identify tone (positive/negative/neutral)
2. List specific praises and complaints
3. Weigh praises against complaints
4. Assign rating based on overall sentiment

**Advantages:**
- Most accurate predictions
- Provides reasoning/explanation
- Better for complex reviews

### 2.3 Evaluation Metrics

| Metric | Description | Purpose |
|--------|-------------|---------|
| Accuracy | % of correct predictions | Overall performance |
| JSON Validity | % of valid JSON responses | Reliability |
| Response Time | Average time per prediction | Efficiency |

### 2.4 Implementation

**File:** `task1/rating_prediction.ipynb`

Key components:
- Data loading and preprocessing
- LLM API integration (Google Gemini)
- Prompt execution for all three strategies
- Results comparison and visualization
- Evaluation metrics calculation

### 2.5 Results & Analysis

The notebook demonstrates:
- Successful integration with Google Gemini API
- JSON parsing and validation
- Comparative analysis of prompting strategies
- Trade-offs between accuracy and complexity

---

## 3. Task 2: AI Review System {#task-2}

### 3.1 System Overview

A full-stack web application that:
1. Accepts customer reviews via user dashboard
2. Processes reviews with AI to generate responses
3. Displays analytics on admin dashboard

### 3.2 User Dashboard Features

**Functionality:**
- Rating selection (1-5 stars)
- Review text input
- Submit button with loading state
- AI-generated response display

**User Flow:**
1. User selects rating
2. User writes review
3. User clicks "Submit Review"
4. System processes with AI
5. Personalized response displayed

### 3.3 Admin Dashboard Features

**Functionality:**
- View all submitted reviews
- AI-generated summaries
- Recommended actions
- Timestamp tracking
- Refresh capability

**Data Displayed:**
- Rating (1-5 stars)
- Review text
- AI Summary (concise overview)
- AI Action (business recommendation)
- Submission timestamp

### 3.4 AI Processing Pipeline

For each review submission:

1. **User Response Generation**
   - Personalized thank you message
   - Empathetic acknowledgment
   - Appropriate tone based on rating

2. **Admin Summary**
   - One-sentence overview
   - Key issues or praises highlighted
   - Actionable insights

3. **Recommended Action**
   - Business-specific recommendation
   - Examples: "Refund customer", "Reward staff", "Investigate issue"

---

## 4. Technical Architecture {#technical-architecture}

### 4.1 Backend Architecture (FastAPI)

**Components:**

1. **API Layer** (`main.py`)
   - RESTful endpoints
   - CORS middleware
   - Request validation
   - Error handling

2. **Database Layer** (`db.py`)
   - SQLAlchemy ORM
   - MySQL connection
   - Session management
   - Table initialization

3. **Schema Layer** (`schemas.py`)
   - Pydantic models
   - Request/response validation
   - Type safety

4. **LLM Service** (`llm.py`)
   - Google Gemini integration
   - Async processing
   - Error handling
   - Response parsing

5. **Prompts** (`prompts.py`)
   - Centralized prompt templates
   - Consistent formatting
   - Easy maintenance

### 4.2 Database Schema

**Table: reviews**

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key, auto-increment |
| rating | INTEGER | Star rating (1-5) |
| review_text | TEXT | Customer review content |
| ai_response | TEXT | AI-generated user response |
| ai_summary | TEXT | AI-generated admin summary |
| ai_action | TEXT | Recommended business action |
| created_at | DATETIME | Timestamp of submission |

**Indexes:**
- Primary key on `id`
- Index on `created_at` for sorting

### 4.3 Frontend Architecture (Reflex)

**Components:**

1. **App Entry** (`app.py`)
   - Route configuration
   - Page registration
   - App initialization

2. **User Dashboard** (`user_dashboard.py`)
   - State management
   - Form handling
   - API integration
   - UI components

3. **Admin Dashboard** (`admin_dashboard.py`)
   - Data fetching
   - Table rendering
   - Refresh functionality
   - State management

### 4.4 API Endpoints

#### POST `/submit_review`
**Purpose:** Submit new review with AI processing

**Request:**
```json
{
  "rating": 5,
  "review_text": "Amazing service!"
}
```

**Response:**
```json
{
  "id": 1,
  "rating": 5,
  "review_text": "Amazing service!",
  "ai_response": "Thank you for your wonderful feedback!",
  "ai_summary": "Customer highly satisfied with service",
  "ai_action": "Reward staff member",
  "created_at": "2026-01-08T00:00:00"
}
```

#### GET `/get_reviews`
**Purpose:** Retrieve all reviews

**Response:** Array of review objects

#### GET `/health`
**Purpose:** Health check endpoint

**Response:**
```json
{
  "status": "ok"
}
```

---

## 5. Implementation Details {#implementation-details}

### 5.1 LLM Integration

**Provider:** Google Gemini AI  
**Model:** gemini-pro

**Implementation Highlights:**
- Async processing for better performance
- Error handling for API failures
- Retry logic for transient errors
- Response validation

**Prompt Engineering:**
- Clear, specific instructions
- Structured output format (JSON where applicable)
- Context-appropriate tone
- Business-aligned recommendations

### 5.2 Database Configuration

**Development:** SQLite (for quick setup)  
**Production:** MySQL (for scalability)

**Features:**
- Connection pooling
- Automatic table creation
- Session management
- Transaction support

**Configuration:**
```python
DATABASE_URL = mysql+pymysql://user:pass@host:port/db
```

### 5.3 Security Considerations

1. **Environment Variables**
   - API keys stored in `.env`
   - `.env` excluded from Git
   - `.env.example` provided as template

2. **CORS Configuration**
   - Configured for frontend access
   - Should be restricted in production

3. **Input Validation**
   - Pydantic schemas validate all inputs
   - Empty review text rejected
   - Rating range validated (1-5)

4. **Error Handling**
   - Graceful degradation on LLM failures
   - User-friendly error messages
   - Logging for debugging

---

## 6. Testing & Validation {#testing-validation}

### 6.1 Manual Testing

**Test Cases:**

1. **Submit Valid Review**
   - ✅ Review saved to database
   - ✅ AI response generated
   - ✅ Response displayed to user

2. **Submit Empty Review**
   - ✅ Error message displayed
   - ✅ Submission prevented

3. **Admin Dashboard Load**
   - ✅ All reviews displayed
   - ✅ Sorted by newest first
   - ✅ All AI fields populated

4. **Database Persistence**
   - ✅ Data persists across server restarts
   - ✅ Timestamps accurate

### 6.2 Database Verification

**SQL Queries Used:**
```sql
USE fynd_reviews;
SELECT * FROM reviews;
SELECT COUNT(*) FROM reviews;
```

**Verification:**
- ✅ Table created automatically
- ✅ All columns present
- ✅ Data types correct
- ✅ Constraints enforced

### 6.3 API Testing

**Tools:** FastAPI Swagger UI (`/docs`)

**Tests Performed:**
- ✅ POST /submit_review with valid data
- ✅ POST /submit_review with invalid data
- ✅ GET /get_reviews
- ✅ GET /health

---

## 7. Deployment Strategy {#deployment-strategy}

### 7.1 Backend Deployment (Render)

**Steps:**
1. Push code to GitHub
2. Create Web Service on Render
3. Connect GitHub repository
4. Configure build settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn task2.backend.main:app --host 0.0.0.0 --port $PORT`
5. Set environment variables:
   - `GEMINI_API_KEY`
   - `DATABASE_URL` (PostgreSQL on Render)

### 7.2 Frontend Deployment (Vercel)

**Steps:**
1. Connect GitHub repository
2. Configure build settings:
   - Framework: Other
   - Build Command: `reflex export --frontend-only`
   - Output Directory: `.web/_static`
3. Set environment variable:
   - `BACKEND_URL` (Render backend URL)

### 7.3 Database Deployment

**Options:**
1. **Render PostgreSQL** (recommended for Render backend)
2. **PlanetScale** (MySQL)
3. **AWS RDS** (production-grade)

**Migration:**
- Tables created automatically via SQLAlchemy
- No manual schema setup required

---

## 8. Challenges & Solutions {#challenges-solutions}

### Challenge 1: Import Errors in Backend
**Problem:** Relative imports failing when running uvicorn

**Solution:**
- Created `__init__.py` in backend folder
- Used module syntax: `python -m uvicorn task2.backend.main:app`
- Removed unused imports

### Challenge 2: LLM Response Consistency
**Problem:** Inconsistent JSON formatting from Gemini

**Solution:**
- Clear prompt instructions for JSON format
- Robust parsing with error handling
- Fallback responses on parse failures

### Challenge 3: Database Connection
**Problem:** MySQL authentication and connection issues

**Solution:**
- Created comprehensive setup guide
- Provided connection test script
- Documented common errors and fixes

### Challenge 4: Virtual Environment Management
**Problem:** User confusion about venv activation

**Solution:**
- Created step-by-step guides
- Provided copy-paste commands
- Documented for both Windows and Unix

---

## 9. Future Enhancements {#future-enhancements}

### 9.1 Technical Improvements

1. **Caching**
   - Redis for LLM response caching
   - Reduce API costs
   - Faster response times

2. **Authentication**
   - User login system
   - Admin role-based access
   - JWT tokens

3. **Analytics Dashboard**
   - Sentiment trends over time
   - Rating distribution charts
   - Common complaint themes

4. **Batch Processing**
   - Process multiple reviews at once
   - CSV import/export
   - Scheduled analysis

### 9.2 Feature Additions

1. **Email Notifications**
   - Alert admins on negative reviews
   - Send responses to customers
   - Weekly summary reports

2. **Multi-language Support**
   - Detect review language
   - Generate responses in same language
   - Translation capabilities

3. **Advanced AI Features**
   - Sentiment analysis scores
   - Topic extraction
   - Competitor comparison

4. **Mobile App**
   - React Native frontend
   - Push notifications
   - Offline support

---

## 10. Conclusion {#conclusion}

### 10.1 Project Summary

This project successfully demonstrates:
- ✅ Full-stack development capabilities
- ✅ AI/ML integration expertise
- ✅ Database design and management
- ✅ Modern web framework usage
- ✅ Professional code organization
- ✅ Comprehensive documentation

### 10.2 Learning Outcomes

**Technical Skills:**
- FastAPI backend development
- Reflex framework for Python web apps
- Google Gemini AI integration
- MySQL database management
- RESTful API design
- Async programming in Python

**Soft Skills:**
- Problem-solving and debugging
- Documentation writing
- Project organization
- Version control with Git

### 10.3 Assessment Compliance

**Task 1: Rating Prediction** ✅
- Implemented 3 prompting strategies
- Jupyter notebook with evaluation
- Comparison and analysis

**Task 2: Review System** ✅
- FastAPI backend with MySQL
- Reflex frontend (user + admin dashboards)
- AI-powered responses and analytics
- Data persistence

**Deployment** ✅
- Code on GitHub
- Professional README
- Deployment instructions

### 10.4 Repository Information

**GitHub:** https://github.com/JainManav05/Fynd-ai-.git

**Key Files:**
- `README.md` - Complete setup guide
- `requirements.txt` - All dependencies
- `.env.example` - Configuration template
- `task1/rating_prediction.ipynb` - Task 1 notebook
- `task2/backend/main.py` - API server
- `task2/frontend/app.py` - Web application

---

## Appendix

### A. Installation Commands

```bash
# Clone repository
git clone https://github.com/JainManav05/Fynd-ai-.git
cd Fynd-ai-

# Setup virtual environment
python -m venv venv
.\venv\Scripts\Activate  # Windows
source venv/bin/activate  # Unix

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your credentials

# Start backend
python -m uvicorn task2.backend.main:app --reload

# Start frontend (new terminal)
cd task2/frontend
reflex run
```

### B. Environment Variables

```
GEMINI_API_KEY=your_gemini_api_key
DATABASE_URL=mysql+pymysql://user:pass@localhost:3306/fynd_reviews
```

### C. MySQL Setup

```sql
CREATE DATABASE fynd_reviews 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
```

---

**End of Report**

**Submitted by:** Manav Jain  
**Contact:** GitHub @JainManav05  
**Date:** January 8, 2026
