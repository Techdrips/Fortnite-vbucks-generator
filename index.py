from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

# Target URL (Replace with your actual target)
target_url = "https://www.fortnite.com/vbuckscard?lang=en-US"  # Replace with the actual URL
result_url = "file:///path/to/result.html"  # Change to a local file path or a live URL where you display results

# Initialize the WebDriver
driver = webdriver.Chrome()  # Ensure the ChromeDriver executable is in PATH or specify path

# Function to try inserting text into an input field
def try_insert_text(driver, attempts=5):
    for attempt in range(attempts):
        try:
            # Open the target website
            driver.get(target_url)
            time.sleep(2)  # Wait for the page to load
            
            # Find the input field (you can also use a specific ID/class if known)
            input_field = driver.find_element("tag name", "input")
            
            # Insert the code (you can change "YOUR_CODE_HERE" to any code you need)
            code = "YOUR_CODE_HERE"
            input_field.send_keys(code)
            input_field.submit()  # Or click a submit button if necessary
            
            # If successful, return True
            return True
        except (NoSuchElementException, ElementNotInteractableException):
            print(f"Attempt {attempt + 1} failed, retrying...")
            time.sleep(1)  # Wait before retrying
    
    # If all attempts fail, return False
    return False

# Function to display the result in the result page
def display_result(success):
    with open("result.html", "w") as file:
        if success:
            file.write("<h1>Code successfully submitted!</h1>")
        else:
            file.write("<h1>Failed to submit code after multiple attempts.</h1>")

# Main workflow
try:
    success = try_insert_text(driver)
    display_result(success)
finally:
    driver.quit()  # Ensure the browser is closed
