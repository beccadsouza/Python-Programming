import requests
from bs4 import BeautifulSoup

pdf_links = []
href_links = []
www = [
    "http://www.spit.ac.in/category/exam/results/",
    "https://www.spit.ac.in/category/exam/results/",
]
URL = "https://www.spit.ac.in/2018/04/10/provisional-grievance-result-for-all-branch-ug-pg/"

def get_links(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html,"html5lib")
    a_tags = soup.find_all('a')
    for link in a_tags:
        href = str(link.get('href'))
        if "results" in href:
            if href not in www:
                href_links.append(href)
        elif "pdf" in href:
                pdf_links.append(href)

    for x in set(href_links):
        print("M LINK : ",x)
    for x in set(pdf_links):
        print("P LINK : ", x)

get_links(URL)




