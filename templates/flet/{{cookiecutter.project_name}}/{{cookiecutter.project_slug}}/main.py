from pathlib import Path

import flet as ft
import flet_easy as fs
from src.database import get_database
from src.settings import get_app_settings


def main():
    get_app_settings()
    get_database()
    app = fs.FletEasy(route_init="/home", path_views=Path(__file__).parent / "src" / "views")

    @app.config
    def page_config(page: ft.Page):
        """Removing animation on route change."""
        theme = ft.Theme()
        platforms = ["android", "ios", "macos", "linux", "windows"]
        for platform in platforms:
            setattr(theme.page_transitions, platform, ft.PageTransitionTheme.NONE)
        page.theme = theme

    # We run the application
    app.run()


main()
