import requests
from bs4 import BeautifulSoup
import time
import json

def main():
    url = "https://www.tamildigitallibrary.in/book-list-view-publisher?act=%E0%AE%A4&id=jZY9lup2kZl6TuXGlZQdjZp6k0ly&tag=%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D%E0%AE%AA%E0%AF%8D+%E0%AE%AA%E0%AE%B2%E0%AF%8D%E0%AE%95%E0%AE%B2%E0%AF%88%E0%AE%95%E0%AF%8D+%E0%AE%95%E0%AE%B4%E0%AE%95%E0%AE%AE%E0%AF%8D"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")

    book_id = 0
    tamilvu_data = []

    container = soup.find("div", class_="tamilauthor-names col-md-12 list-title-view")
    books = container.find_all("li")
    for book in books:
        time.sleep(5)
        book_id += 1
        book_href = book.find("a").get("href")
        book_url = "https://www.tamildigitallibrary.in/"+book_href

        response_in = requests.get(book_url).text
        soup_in = BeautifulSoup(response_in, "lxml")

        book_details = soup_in.find("div", class_="books-content")
        book_title = book_details.find("h4").text.strip()

        book_data = {}
        book_data["id"] = book_id
        book_data["title"] = book_title

        other_details = book_details.find_all("tr")
        for other_detail in other_details:
            items = other_detail.find_all("td")
            key = items[0].text.strip()
            value = items[1].text.strip()
            if key == "ஆசிரியர்":
                book_authors = value
                book_data["authors"] = book_authors
            elif key == "பதிப்பாளர்":
                book_publishers = value
                book_data["publishers"] = book_publishers
            elif key == "வடிவ விளக்கம்":
                page_numbers = value
                book_data["page numbers"] = page_numbers
            elif key == "தொடர் தலைப்பு":
                series_title = value
                book_data["series title"] = series_title
            elif key == "குறிச் சொற்கள்":
                tags = value
                book_data["tags"] = tags
            elif key == "துறை / பொருள்":
                subject_theme = value
                book_data["subject or theme"] = subject_theme

        more_details = soup_in.find("div", class_="author-cover")
        uploaded_details = more_details.find_all("tr")
        document_location = uploaded_details[0].find("p").text
        book_data["document location"] = document_location
        uploaded_date = uploaded_details[1].find("p").text
        book_data["uploaded date"] = uploaded_date

        tamilvu_data.append(book_data)

        with open("tamilvu_data.json", "w", encoding="utf8") as file:
            json.dump(tamilvu_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()