import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

class CNNCrawler:

    def __init__(self):
        self.start_url = 'https://www.cnn.com/2023/04/03/investing/dogecoin-elon-musk-twitter/index.html'
        self.max_pages = 10
        self.visited_pages = set()
        self.pages_to_visit = [self.start_url]
        self.current_url = None
        self.response = None
        self.html_content = None
        self.parsed_url = None
        self.soup = None
        self.links = set()
        self.a_tag = None
        self.href = None
        self.full_url = None
        self.new_links = set()
    
    def is_cnn_url(self):
        self.parsed_url = urlparse(self.current_url)
        return self.parsed_url.netloc.endswith("cnn.com")
    
    def fetch_page(self):
        try:
            self.response = requests.get(self.current_url)
            if self.response.status_code == 200:
                self.html_content = self.response.text
                return
        except requests.RequestException as e:
            print(f"Failed to fetch page {self.current_url}: {e}")
        self.html_content = None

    def extract_links(self):
        self.soup = BeautifulSoup(self.html_content, 'html.parser')
        self.links = set()
        for self.a_tag in self.soup.find_all('a', href=True):
            self.href = self.a_tag['href']
            self.full_url = urljoin(self.current_url, self.href)
            if self.is_cnn_url() and self.full_url not in self.visited_pages:
                self.links.add(self.full_url)
        self.new_links = self.links
    
    def crawl(self):
        while self.pages_to_visit and len(self.visited_pages) < self.max_pages:
            self.current_url = self.pages_to_visit.pop(0)
            if self.current_url in self.visited_pages:
                continue

            # Add the URL to visited pages
            self.visited_pages.add(self.current_url)

            # Check if max_pages limit is reached before printing
            if len(self.visited_pages) > self.max_pages:
                break

            print(f"Visiting: {self.current_url}")
            self.fetch_page()
            if self.html_content is None:
                continue

            self.extract_links()
            self.pages_to_visit.extend(self.new_links)

            time.sleep(1) 

if __name__ == '__main__':
    crawler = CNNCrawler()
    crawler.crawl()
    

