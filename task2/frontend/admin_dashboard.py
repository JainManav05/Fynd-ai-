import reflex as rx
import httpx
from typing import List, Dict, Any

API_URL = "http://localhost:8000"

class AdminState(rx.State):
    reviews: List[Dict[str, Any]] = []
    
    async def load_reviews(self):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{API_URL}/get_reviews")
                if response.status_code == 200:
                    self.reviews = response.json()
            except Exception as e:
                print(f"Error fetching reviews: {e}")

def review_row(review):
    return rx.tr(
        rx.td(review["rating"]),
        rx.td(review["review_text"], max_width="300px", overflow="hidden", text_overflow="ellipsis", white_space="nowrap"),
        rx.td(review["ai_summary"]),
        rx.td(review["ai_action"]),
        rx.td(review["created_at"]),
    )

def admin_dashboard():
    return rx.vstack(
        rx.heading("Admin Dashboard", size="8"),
        
        rx.hstack(
            rx.button("Refresh", on_click=AdminState.load_reviews),
            rx.link(
                rx.button("Go to User Dashboard", variant="outline"),
                href="/"
            ),
            spacing="4"
        ),
        
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Rating"),
                    rx.table.column_header_cell("Review"),
                    rx.table.column_header_cell("AI Summary"),
                    rx.table.column_header_cell("Action"),
                    rx.table.column_header_cell("Time"),
                )
            ),
            rx.table.body(
                rx.foreach(AdminState.reviews, review_row)
            ),
            width="100%",
        ),
        
        spacing="6",
        padding="10",
        width="100%",
        on_mount=AdminState.load_reviews,
    )
