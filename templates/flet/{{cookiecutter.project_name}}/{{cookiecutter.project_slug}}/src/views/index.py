import flet as ft
import flet_easy as fs
from sqlalchemy import text
from src.database import get_database

index = fs.AddPagesy()


# We add a page
@index.page(route="/home", title="Home")
async def index_page(data: fs.Datasy):
    database = get_database()
    async with database.session_maker() as session:
        result = (await session.exec(text("SELECT 1 "))).scalar()

    return ft.View(
        controls=[
            ft.Text(f"Home page {result}", size=30),
            # ft.FilledButton("Go to Counter", on_click=data.go("/counter/test/0")),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
