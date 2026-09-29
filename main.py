from scraper import fetch_website_contents
from summarizer import summarize_website

def main():
    url = input("Enter a URL: ").strip()

    if not url:
        print("Please enter a website URL.")
        return

    # Fetch website content
    website_content = fetch_website_contents(url)

    # Generate the summary
    summary = summarize_website(website_content)

    # Display the summary
    print(summary)

if __name__ == "__main__":
    main()