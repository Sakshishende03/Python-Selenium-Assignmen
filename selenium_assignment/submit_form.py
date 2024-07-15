from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the form
    driver.get('https://forms.gle/WT68aV5UnPajeoSc8')

    # Implicit wait
    driver.implicitly_wait(10)

    print("Waiting for the name field...")
    name_field = WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @aria-label='Full Name']"))
    )
    name_field.send_keys('Sakshi Shende')

    print("Waiting for the email field...")
    email_field = WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='email' and @aria-label='Email']"))
    )
    email_field.send_keys('sakshishende06@gmail.com')

    print("Waiting for the submit button...")
    submit_button = WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and contains(text(), 'Submit')]"))
    )
    submit_button.click()

    print("Waiting for the confirmation message...")
    confirmation_message = WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Your response has been recorded')]"))
    )

    # Save screenshot after confirmation message appears
    screenshot_path = r'C:\Users\ASUS\PycharmProjects\SeleniumDjangoAutomation\selenium_assignment\confirmation_page.png'
    driver.save_screenshot(screenshot_path)
    print("Screenshot saved as confirmation_page.png")

except Exception as e:
    print(f"Error: {e}")
    error_screenshot_path = r'C:\Users\ASUS\PycharmProjects\SeleniumDjangoAutomation\selenium_assignment\error_screenshot.png'
    driver.save_screenshot(error_screenshot_path)
    print(f"Error screenshot saved as {error_screenshot_path}")

finally:
    driver.quit()
