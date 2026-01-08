import reflex as rx
import httpx
import asyncio

API_URL = "http://localhost:8000"

class UserState(rx.State):
    rating: int = 5
    review_text: str = ""
    ai_response: str = ""
    is_loading: bool = False
    
    async def submit_review(self):
        self.is_loading = True
        self.ai_response = ""
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{API_URL}/submit_review",
                    json={"rating": self.rating, "review_text": self.review_text},
                    timeout=30.0
                )
                if response.status_code == 200:
                    data = response.json()
                    self.ai_response = data.get("ai_response", "Thank you!")
                    self.review_text = "" # Clear input
                else:
                    self.ai_response = "Error submitting review."
            except Exception as e:
                self.ai_response = f"Connection error: {e}"
            finally:
                self.is_loading = False

def user_dashboard():
    return rx.center(
        rx.vstack(
            rx.heading("Submit Your Review", size="8"),
            rx.text("Share your experience with us!"),
            
            rx.link(
                rx.button("Go to Admin Dashboard", variant="outline", size="2"),
                href="/admin"
            ),
            
            rx.select(
                [1, 2, 3, 4, 5],
                value=UserState.rating,
                on_change=UserState.set_rating,
                label="Rating",
            ),
            
            rx.text_area(
                placeholder="Write your review here...",
                value=UserState.review_text,
                on_change=UserState.set_review_text,
                min_height="150px",
                width="100%",
            ),
            
            rx.button(
                "Submit Review",
                on_click=UserState.submit_review,
                loading=UserState.is_loading,
                width="100%",
                color_scheme="blue",
            ),
            
            rx.cond(
                UserState.ai_response,
                rx.box(
                    rx.text("Response from us:", weight="bold"),
                    rx.text(UserState.ai_response),
                    padding="4",
                    border="1px solid #eaeaea",
                    border_radius="md",
                    width="100%",
                    bg="fafafa"
                )
            ),
            
            width="50%",
            spacing="6",
            padding="10",
        ),
        height="100vh",
        bg="gray.50"
    )
