from selenium import webdriver

# Initialize the WebDriver (assuming ChromeDriver is in your PATH)
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Print the title of the page
print(driver.title)

# Close the browser
# driver.quit()
