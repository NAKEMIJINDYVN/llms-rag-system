from .context import BrowserCtx
from typing import *
from playwright_stealth import Stealth
from playwright.async_api import async_playwright, Page, Playwright, BrowserContext


class SearchEngineParams(TypedDict):
    headless: bool
    timeout: int
    browser_name: Literal["chromium", "firefox", "webkit"]
    use_proxy: bool
    verify_ssl: bool

CONST_SEARCH_ENGINE_PARAMS : SearchEngineParams = {
    "browser_name": "chromium",
    "headless": False,
    "timeout": 30000,
    "use_proxy": False,
    "verify_ssl": False
}

class SearchEngine:
    def __init__(self, kwargs: SearchEngineParams):
        self.params: SearchEngineParams = {
            **CONST_SEARCH_ENGINE_PARAMS,
            **kwargs
        }
        self.ctx: Optional[BrowserContext] = None
        self.playwright: Optional[Playwright] = None
        self.current_page: Optional[Page] = None

    async def init_ctx(self):
        try:
            # async with Stealth().use_async(async_playwright()) as p:
                self.playwright = await async_playwright().start()
                browser_name = self.params.get("browser_name", "chromium")
                self.ctx = await BrowserCtx.create_ctx(
                    browser_name=browser_name,
                    playwright=self.playwright
                )
                self.current_page = await self.ctx.new_page()
        except Exception as error:
            print(error)
            # await self.close_ctx()
    
    async def close_ctx(self):
        if self.ctx:
            await self.ctx.close()
        if self.playwright:
            await self.playwright.stop()

    async def scrape(self, url: str):
        await self.current_page.goto(url)
        return await self.current_page.content()