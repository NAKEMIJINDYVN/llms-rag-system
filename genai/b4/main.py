from search_engine import SearchEngine
from search_engine.config import PATH_EXPORT
from search_engine.parse_html import ParseHTML

async def main():
    try:
        scraper = SearchEngine(
            kwargs={
                "headless": True,
                "timeout": 30000,
                "use_proxy": False,
                "verify_ssl": False,
                "browser_name": "chromium"
            }
        )

        await scraper.init_ctx()

        try:
            content1 = await scraper.scrape("https://viblo.asia/p/tim-hieu-ve-nextjs-phan-1-V3m5WQkwZO7")
            # print(content1)

            with open(f"./data.html", "w", encoding="utf-8") as f:
                f.write(content1)

            ParseHTML.kwargs = {
                "html_content":content1
            }

            text_content = (ParseHTML.get_all_text(out_type="string"))

            with open(f"./text.txt", "w", encoding="utf-8") as f:
                f.write(text_content)
        finally:
            await scraper.close_ctx()
    
    except Exception as e:
        print(e)

    # await scraper.close_ctx()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())




    