import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

class CNNHeadlineMonitor:
    def __init__(self):
        self.start_url = 'https://www.cnn.com/'
        self.interval = 100  # Time interval between checks (in seconds)
        self.previous_headlines = set()
        self.response = None
        self.html = None
        self.soup = None
        self.headlines = set()
        self.headline_text = ""
        self.html_content = None
        self.current_headlines = set()
        self.new_headlines = set()

    def fetch_page(self):
        try:
            self.response = requests.get(self.start_url)
            if self.response.status_code == 200:
                self.html = self.response.text
            else:
                self.html = None
        except requests.RequestException as e:
            print(f"Failed to fetch page {self.start_url}: {e}")
            self.html = None

    def extract_headlines(self):
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.headlines = set()
        for headline in self.soup.find_all('h2', class_=['container__title-text', 'container_lead-plus-headlines__title-text']):
            self.headline_text = headline.get_text(strip=True)
            self.headlines.add(self.headline_text)

    def monitor_headlines(self):
        while True:
            self.fetch_page()
            if self.html:
                self.extract_headlines()
                self.current_headlines = self.headlines
                self.new_headlines = self.current_headlines - self.previous_headlines
                if self.new_headlines:
                    print("New Headlines Detected:")
                    for headline in self.new_headlines:
                        print(headline)
                    self.previous_headlines = self.current_headlines
                else:
                    print("No new headlines detected.")
            else:
                print("Failed to fetch page content.")
            
            time.sleep(self.interval)

if __name__ == '__main__':
    monitor = CNNHeadlineMonitor()
    monitor.monitor_headlines()
