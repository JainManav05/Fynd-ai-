import reflex as rx
from user_dashboard import user_dashboard, UserState
from admin_dashboard import admin_dashboard, AdminState

app = rx.App()

# Add pages with proper routes
app.add_page(user_dashboard, route="/", title="Submit Review")
app.add_page(admin_dashboard, route="/admin", title="Admin Dashboard")
