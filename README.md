# Crawler Monitor Pro

## Overview

'Crawler Monitor Pro' is a collection of Python scripts designed to demonstrate various web crawling and monitoring techniques. This repository includes crawlers for different websites and a monitoring script, showcasing how to extract and process information from web pages.

## Scripts

### 1. `brookings_crawler.py`

A web crawler that extracts links from the Brookings website. It visits a starting URL and follows links within the Brookings domain, up to a specified number of pages.

- **Features:**
  - Crawl the Brookings website.
  - Extract and follow links within the same domain.
  - Limit the number of pages visited.

### 2. `wikipedia_crawler.py`

A web crawler that extracts links from Wikipedia pages. It starts from a specific Wikipedia page and follows internal links, constrained by a page limit.

- **Features:**
  - Crawl Wikipedia starting from a specific page.
  - Extract and follow links within Wikipedia.
  - Limit the number of pages visited.

### 3. `cnn_crawler.py`

A web crawler for CNN's website, designed to extract and follow links from a specified starting URL.

- **Features:**
  - Crawl CNN's website.
  - Extract and follow links within the CNN domain.
  - Limit the number of pages visited.

### 4. `cnn_headline_monitor.py`

A headline monitoring script that periodically checks CNN's homepage for new headlines. It prints new headlines detected since the last check.

- **Features:**
  - Monitor CNN's homepage for new headlines.
  - Print newly detected headlines.
  - Adjustable time interval between checks.

## Conclusion

The 'Crawler Monitor Pro' is a versatile suite of tools for effective web data extraction and monitoring. By implementing advanced crawlers and a dynamic headline monitoring script, this project automates the retrieval and analysis of web content from diverse sources. It streamlines the process of gathering and processing information, reducing manual effort and enhancing data accessibility. 

## License
This project is licensed under the MIT License. See the LICENSE file for details.
