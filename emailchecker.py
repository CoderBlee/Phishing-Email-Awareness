import re
from urllib.parse import urlparse

# Define a list of known malicious domains (example)
MALICIOUS_DOMAINS = [
    'malicious.com', 'phishingsite.org', 'fakebank.net'
]

def is_malicious_link(url):
    """
    Function to check if a URL is from a known malicious domain.
    """
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain in MALICIOUS_DOMAINS

def extract_links(text):
    """
    Function to extract URLs from text.
    """
    return re.findall(r'http[s]?://\S+', text)

# Example usage
if __name__ == "__main__":
    email_body = "Click here to claim your prize: http://malicious.com/prize"

    links = extract_links(email_body)
    for link in links:
        if is_malicious_link(link):
            print(f"Potential malicious link detected: {link}")
        else:
            print(f"Safe link: {link}")
