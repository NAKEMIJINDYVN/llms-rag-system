from .config import *
from playwright.async_api import (
    Playwright,
    BrowserType,
    BrowserContext
)
from typing import *


class OptionsContextField(TypedDict):
    user_data_dir: Path
    load_extension: Path

class OptionsContext(TypedDict):
    chromium: OptionsContextField
    firefox: OptionsContextField
    webkit: OptionsContextField


class BrowserCtx:
    options: OptionsContext = {
        "chromium": {
            "user_data_dir": PATH_CHROMIUM,
            "load_extension": PATH_ETENSION
        }
    }


    @staticmethod
    async def create_ctx(
        browser_name: Optional[Literal["chromium", "firefox", "webkit"]] = "chromium",
        playwright: Optional[Playwright] = None
    ) -> BrowserContext:
        user_data_dir = BrowserCtx.options["chromium"]["user_data_dir"]
        load_extension = BrowserCtx.options["chromium"]["load_extension"]

        ctx = await getattr(playwright, browser_name).launch_persistent_context(
            user_data_dir,
            headless=False,
            channel=browser_name,
            args=[

            ]
        )

        return ctx