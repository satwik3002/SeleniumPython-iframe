from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the local Iframe HTML file
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH
driver.get("file:///E:/Testing/HTML/Iframe.html.html")
driver.maximize_window()

# Step 2: Switch to the first iframe and login to Holland & Barrett
driver.switch_to.frame("HollandandBarrett")  # Ensure frame name is correct
driver.get("https://auth.hollandandbarrett.com/u/login")
time.sleep(2)

# Enter username
driver.find_element(By.ID, "username").send_keys("satwikkatamaraju@gmail.com")

# Enter password (correcting to use send_keys)
driver.find_element(By.ID, "password").send_keys("Y2#ssv@Xp/xP8Wt")

# Click the login button
driver.find_element(By.XPATH, "/html/body/main/section/div/div/div/form/div[2]/button").click()
time.sleep(5)

# Step 3: Return to the main HTML and navigate to Selenium website
driver.switch_to.default_content()
driver.get("file:///E:/Testing/HTML/Iframe.html.html")
time.sleep(2)

# Click the link in the main HTML
driver.find_element(By.XPATH, "/html/body/a").click()
driver.get("https://www.selenium.dev/")
time.sleep(2)

# Step 4: Click on the Downloads button
driver.find_element(By.XPATH, "//span[contains(text(),'Downloads')]").click()
time.sleep(3)

# Step 5: Switch to the second iframe and search for a product in OpenCart
driver.get("file:///E:/Testing/HTML/Iframe.html.html")
driver.switch_to.frame("My Store")  # Ensure frame name is correct
driver.get("https://demo-opencart.com/")
time.sleep(3)

# Enter a product name in the search box
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("product")
time.sleep(2)

# Click the search icon
search_icon = driver.find_element(By.XPATH, "//i[contains(@class, 'fa-magnifying-glass')]")
search_icon.click()
time.sleep(5)

# Step 6: Return to the main content and click on the body element
driver.switch_to.default_content()
driver.find_element(By.XPATH, "/html/body").click()
time.sleep(2)

# Close the browser
driver.quit()
