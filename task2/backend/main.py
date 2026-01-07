from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List
from .db import engine, get_db, init_db, Review
from .schemas import ReviewCreate, ReviewResponse
from .llm import llm_service
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Fynd AI Review System")

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB
@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/submit_review", response_model=ReviewResponse)
async def submit_review(review: ReviewCreate, db: Session = Depends(get_db)):
    """
    Submits a review, triggers LLM processing, and saves to DB.
    """
    if not review.review_text.strip():
        raise HTTPException(status_code=400, detail="Review text cannot be empty")

    # Call LLM logic
    # Note: For very long reviews, we might want to truncate or handle differently.
    # Here we process them directly.
    
    ai_results = await llm_service.process_review(review.review_text, review.rating)
    
    db_review = Review(
        rating=review.rating,
        review_text=review.review_text,
        ai_response=ai_results["ai_response"],
        ai_summary=ai_results["ai_summary"],
        ai_action=ai_results["ai_action"]
    )
    
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    
    return db_review

@app.get("/get_reviews", response_model=List[ReviewResponse])
def get_reviews(db: Session = Depends(get_db)):
    """
    Retrieves all reviews, ordered by latest first.
    """
    return db.query(Review).order_by(Review.created_at.desc()).all()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
