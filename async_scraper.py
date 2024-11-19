import aiohttp
import asyncio
from bs4 import BeautifulSoup
import time

async def fetch_and_process_page(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        return [book.text for book in soup.select('h3 > a')]

async def main():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        with open('book_titles.txt', 'w', encoding='utf-8') as f:
            # Create and execute tasks for all pages
            tasks = [
                fetch_and_process_page(session, url = f"https://openlibrary.org/search?q=birds&mode=everything&page={page}")
                for page in range(1, 51)
            ]
            results = await asyncio.gather(*tasks)
            
            # Write all titles at once
            for titles in results:
                for title in titles:
                    f.write(title + '\n')
    print(f"{(time.time() - start_time):.2f} seconds")

asyncio.run(main())