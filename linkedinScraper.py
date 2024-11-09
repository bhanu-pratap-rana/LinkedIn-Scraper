from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fpdf import FPDF
import time

# Function to log in to LinkedIn
def linkedin_login(driver, username, password):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    
    # Input username and password
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    
    # Click login button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)  # Adjust based on your connection speed

# Function to scrape LinkedIn profile posts
def scrape_linkedin_posts(driver, profile_url):
    driver.get(profile_url)
    time.sleep(5)

    # Scroll down to load more posts
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    posts_data = []

    try:
        # Wait until posts are loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class*="pv0 ph5"] ul li'))
        )
        
        posts = driver.find_elements(By.CSS_SELECTOR, 'div[class*="pv0 ph5"] ul li')

        for post in posts:
            post_text = post.text
            post_link = post.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            posts_data.append({
                'Post Text': post_text,
                'Post Link': post_link
            })
    except Exception as e:
        print(f"Failed to scrape posts: {e}")
    
    return posts_data

# Function to sanitize text for PDF
def sanitize_text(text):
    return text.encode('latin1', 'replace').decode('latin1')

# Function to save scraped data to a PDF
def save_to_pdf(profile_url, posts_data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    # Add profile URL at the top
    pdf.cell(200, 10, txt="LinkedIn Profile: " + profile_url, ln=True, link=profile_url)

    # Add post data
    for idx, post in enumerate(posts_data, start=1):
        pdf.cell(200, 10, txt=f"Post {idx}:", ln=True)
        pdf.multi_cell(0, 10, sanitize_text(post['Post Text']))
        pdf.cell(200, 10, txt=f"Post Link: {post['Post Link']}", ln=True, link=post['Post Link'])
        pdf.ln()

    pdf.output("linkedin_posts.pdf")

# Main function
def main():
    # LinkedIn credentials (replace with yours)
    linkedin_username = ""  # Use environment variables or a secure vault in production
    linkedin_password = ""  # Use environment variables or a secure vault in production

    # LinkedIn profile URL you want to scrape
    profile_url = "https://www.linkedin.com/in/piyushptiwari/"

    # Set Chrome options
    chrome_options = Options()
    chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    # Set up Chrome driver
    service = ChromeService(executable_path=r'C:\Users\HP\Desktop\Scraping\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Log in to LinkedIn
        linkedin_login(driver, linkedin_username, linkedin_password)

        # Scrape posts from the profile
        posts_data = scrape_linkedin_posts(driver, profile_url)

        # Save posts data to PDF
        save_to_pdf(profile_url, posts_data)

        print("Data successfully saved to linkedin_posts.pdf")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
