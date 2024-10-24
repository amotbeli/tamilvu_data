import requests
from bs4 import BeautifulSoup
import time
import json

def main():
    url = "https://www.tamildigitallibrary.in/book-list-view-publisher?act=%E0%AE%A4&id=jZY9lup2kZl6TuXGlZQdjZp6k0ly&tag=%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D%E0%AE%AA%E0%AF%8D+%E0%AE%AA%E0%AE%B2%E0%AF%8D%E0%AE%95%E0%AE%B2%E0%AF%88%E0%AE%95%E0%AF%8D+%E0%AE%95%E0%AE%B4%E0%AE%95%E0%AE%AE%E0%AF%8D"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")

    book_id = 0

    container = soup.find("div", class_="tamilauthor-names col-md-12 list-title-view")
    books = container.find_all("li")
    for book in books:
        time.sleep(2)
        book_id += 1
        book_href = book.find("a").get("href")
        book_url = "https://www.tamildigitallibrary.in/"+book_href

        with open("acl_data.json", "a", encoding="utf8") as file:
            json.dump(f"{book_id}: {book_url}", file)

if __name__ == "__main__":
    main()