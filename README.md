# LinkedIn Scraper

This project is a LinkedIn scraper script that logs in to LinkedIn, scrapes posts from a specified profile, and saves the data to a PDF. The script uses Selenium for web scraping and FPDF for PDF generation.

## Features

- Logs in to LinkedIn using provided credentials.
- Scrapes posts from a specified LinkedIn profile.
- Saves the scraped posts data to a PDF file.

## Requirements

- Python 3.x
- Selenium
- FPDF
- Brave Browser (optional, replaceable with Chrome)
- ChromeDriver or BraveDriver

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/bhanu-pratap-rana/linkedin-scraper.git
    cd linkedin-scraper
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium fpdf
    ```

3. Download and install Brave Browser or Chrome Browser if you haven't already.

4. Download the ChromeDriver or BraveDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your project directory.

## Usage

1. Open the `main.py` file and replace the placeholder LinkedIn credentials with your own:
    ```python
    linkedin_username = "your_username"
    linkedin_password = "your_password"
    ```

2. Replace the placeholder LinkedIn profile URL with the profile you want to scrape:
    ```python
    profile_url = "https://www.linkedin.com/in/desired-profile/"
    ```

3. Adjust the path to your browser's executable and the driver:
    ```python
    chrome_options.binary_location = r"C:\Path\To\Brave-Browser\Application\brave.exe"
    service = ChromeService(executable_path=r'C:\Path\To\chromedriver.exe')
    ```

4. Run the script:
    ```sh
    python main.py
    ```

5. The scraped data will be saved in a file named `linkedin_posts.pdf` in the project directory.

## Notes

- The script includes a delay to ensure that LinkedIn pages load properly. You may need to adjust the sleep times based on your internet connection speed.
- Make sure to comply with LinkedIn's terms of service when using this script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## Contact

For any questions or issues, please open an issue on GitHub.

---

Happy scraping!
