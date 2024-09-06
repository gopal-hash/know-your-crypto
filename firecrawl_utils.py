from firecrawl import FirecrawlApp
import google.generativeai as genai
import os

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")
# Initialize Firecrawl SDK with API key
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")


def scrape_website(url):
    """Scrape the given URL and return markdown and HTML content."""
    scrape_result = app.scrape_url(url, params={'formats': ['markdown', 'html']})
    response = model.generate_content("Here is the Markdown content of the top result for the crypto token .Please analyze the page by extracting key information such as market performance, utility, and any partnerships or roadmap details mentioned. Additionally, leverage your own knowledge to provide a comprehensive overview of the token, including its history, use cases, technical details, and future potential. Ensure the report covers: token overview (purpose, creation date, and any significant events in its history), technical details (blockchain, consensus mechanism, and any unique technology), market performance (key performance metrics like market cap, trading volume, recent price trends, and growth potential), partnerships and roadmap (strategic partnerships or upcoming milestones that might impact the token's value), and expert insight (based on your knowledge, give an evaluation of the token's long-term viability and risks). Ensure the report is detailed, combining both data from the webpage and your knowledge. "+scrape_result['markdown'])
    return response.text

