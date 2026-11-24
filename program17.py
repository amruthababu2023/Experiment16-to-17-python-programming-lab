
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome browser
driver = webdriver.Chrome()

try:
    # Open DemoQA webpage
    driver.get("https://demoqa.com/text-box")

    # Maximize browser
    driver.maximize_window()

    # Wait until elements are available
    wait = WebDriverWait(driver, 15)

    # Enter full name
    wait.until(EC.visibility_of_element_located(
        (By.ID, "userName")
    )).send_keys("Amrutha Babu")

    # Enter email
    driver.find_element(By.ID, "userEmail").send_keys(
        "amrutha@gmail.com"
    )

    # Enter current address
    driver.find_element(By.ID, "currentAddress").send_keys(
        "Irinjalakuda, Kerala"
    )

    # Enter permanent address
    driver.find_element(By.ID, "permanentAddress").send_keys(
        "Thrissur, Kerala"
    )

    # Scroll down to the Submit button
    submit_button = driver.find_element(By.ID, "submit")

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        submit_button
    )

    # Click Submit
    wait.until(
        EC.element_to_be_clickable((By.ID, "submit"))
    ).click()

    # Verify submitted details
    output = wait.until(
        EC.visibility_of_element_located((By.ID, "output"))
    )

    print("Form submitted successfully!")
    print(output.text)

finally:
    # Close browser
    driver.quit()
