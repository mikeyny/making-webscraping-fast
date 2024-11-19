import requests
from bs4 import BeautifulSoup
import time

# Create/open a file to write the titles
with open('book_titles.txt', 'w', encoding='utf-8') as f:
    start_time = time.time()
    # Loop through first 50 pages
    for page in range(1, 51):
        url = f"https://openlibrary.org/search?q=birds&mode=everything&page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract book titles from current page
        for book in soup.select('h3 > a'):
            title = book.text
            f.write(title + '\n')
    print(f"{(time.time() - start_time):.2f} seconds")