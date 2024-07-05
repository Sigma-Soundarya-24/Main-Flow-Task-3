import requests
from bs4 import BeautifulSoup

url = "https://realpython.com/python-web-scraping-practical-introduction/"

response = requests.get(url)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    page_text = soup.get_text()

    links = [a["href"] for a in soup.find_all('a',href=True)]
        
    images = [img['src'] for img in soup.find_all('img',src=True)]

    print("Page Text:")
    print(page_text)

    print("\nLinks:")
    for link in links:
        print(link)

    print("\nImages:")
    for image in images:
        print(image)

else:
    print(f"Failed to retrieve the web page.Status code: {response.status_code}")
        
