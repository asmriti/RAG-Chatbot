import requests
from bs4 import BeautifulSoup


def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = [p.get_text() for p in soup.find_all("p")]
    text = "\n".join(paragraphs)

    return {"url": url, "content": text}


if __name__ == "__main__":
    data = scrape_page("https://bigomega.dev/blogs/learning-techniques")
    print(data["content"][:500])
