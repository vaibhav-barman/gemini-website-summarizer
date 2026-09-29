from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def fetch_website_contents(url):
    """
    Return the title and contents of the given website at the given url,
    truncate to 2,000 characters as a sensible limit
    """
    parsed_url = urlparse(url)

    if parsed_url.scheme not in ("http", "https") or not parsed_url.hostname:
        raise ValueError("Please provide a valid HTTP or HTTPS URL.")
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    if soup.body:
        for irrelevant in soup.body(["script", "style", "image", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    return (title + "\n\n" + text)[:2_000]

def fetch_website_links(url):
    """
    Return the links on the webiste at the given url
    """
    parsed_url = urlparse(url)

    if parsed_url.scheme not in ("http", "https") or not parsed_url.hostname:
        raise ValueError("Please provide a valid HTTP or HTTPS URL.")
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]