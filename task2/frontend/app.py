import reflex as rx
from .user_dashboard import user_dashboard
from .admin_dashboard import admin_dashboard

app = rx.App()
app.add_page(user_dashboard, route="/")
app.add_page(admin_dashboard, route="/admin")
