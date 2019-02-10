import requests
from bs4 import BeautifulSoup

pdf_links = []
href_links = []

URL = "https://www.spit.ac.in/category/exam/results/"
www = [
    "http://www.spit.ac.in/category/exam/results/",
    "https://www.spit.ac.in/category/exam/results/",
]

def get_pdfs(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, "html5lib")
    a_tags = soup.find_all('a')
    for link in a_tags:
        href = str(link.get('href'))
        if "results" in href:
            if href not in www:
                href_links.append(href)
        elif "pdf" in href:
            pdf_links.append(href)

def get_links(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html,"html5lib")
    a_tags = soup.find_all('a')
    for link in a_tags:
        href = str(link.get('href'))
        if "result" in href and href!="https://www.spit.ac.in/category/exam/results/":
            href_links.append(href)

    for x in set(href_links):
        # print("M LINK : ",x)
        get_pdfs(x)

def print_pdf(URL):
    get_links(URL)
    for x in set(pdf_links):
        print(x)


print_pdf(URL)

