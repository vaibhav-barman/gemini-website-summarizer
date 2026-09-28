# Gemini-Powered Website Summarizer

A simple Python project that fetches a website's text and uses Google's
Gemini API to generate a short, humorous summary.

## Features

-   Fetches a webpage using `requests`.
-   Parses HTML with BeautifulSoup.
-   Extracts the page title and readable body text.
-   Truncates the extracted content to 2,000 characters.
-   Uses the Gemini API to generate a short summary in Markdown.
-   Loads the Gemini API key from a local `.env` file.

## Tech Stack

-   Python
-   Google Gen AI SDK (`google-genai`)
-   Gemini API
-   Requests
-   BeautifulSoup (`beautifulsoup4`)
-   `python-dotenv`

## Project Structure

``` text
gemini-website-summarizer/
├── .env                 # Local API key; do not commit
├── .gitignore
├── main.py              # Runs the summarization workflow
├── scraper.py           # Fetches and extracts website content
└── requirements.txt     # Python dependencies
```

The `.venv/` virtual environment directory is created locally and should
not be committed to Git.

## Setup

### 1. Clone the repository

``` bash
git clone https://github.com/vaibhav-barman/gemini-website-summarizer.git
cd gemini-website-summarizer
```

### 2. Create and activate a virtual environment

On macOS or Linux:

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

``` bash
python -m pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Get an API key from [Google AI
Studio](https://aistudio.google.com/apikey).

Create a file named `.env` in the project root and add:

``` dotenv
GEMINI_API_KEY=your_actual_api_key_here
```

Replace the placeholder with your own API key. Keep `.env` private and
do not commit it to GitHub.

### 5. Run the application

``` bash
python main.py
```

When prompted, enter a website URL. The program fetches the page content
and asks Gemini to summarize it.

## How It Works

1.  `main.py` loads the API key from `.env`.
2.  The program asks the user for a URL.
3.  `scraper.py` downloads the page and extracts its title and body
    text.
4.  The extracted content is combined with a summarization prompt.
5.  The Gemini API generates a short, humorous Markdown summary.
6.  The summary is printed in the terminal.

## Current Limitations

-   The scraper truncates extracted page content to the first 2,000
    characters.
-   Some websites may block automated requests or require JavaScript to
    render their content.
-   Error handling and automated tests are not yet implemented.
-   The application currently runs in the terminal; it does not yet have
    a web interface or public deployment.
-   The configured Gemini model must be available to your API key. Check
    the [Gemini API model
    documentation](https://ai.google.dev/gemini-api/docs/models) if the
    API reports that the model is unavailable.

## Security

-   Store the API key in `.env`, not in Python source code.
-   Ensure `.env` and `.venv/` are listed in `.gitignore`.
-   Never publish your API key in a commit, screenshot, or issue.

## Project Status

**Current milestone:** Core website summarization with the Gemini API is
implemented.

Planned improvements include stronger URL validation, request timeouts
and HTTP error handling, automated tests, a user interface, and
deployment.

## Acknowledgements

Built while practising concepts from Ed Donner's LLM Engineering course.
This project uses the Google Gemini API rather than the OpenAI API in
the corresponding exercise.
