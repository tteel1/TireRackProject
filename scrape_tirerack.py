
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Set up the WebDriver
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)
driver.get("https://www.tirerack.com/tires/TireSearchResults.jsp?tireIndex=0&autoMake=Toyota&autoYear=2025&autoModel=Camry%20AWD&autoModClar=SE&width=235/&ratio=45&diameter=18&sortCode=53850&skipOver=true&minSpeedRating=H&minLoadRating=S&performance=ALL")  # Replace with the actual TireRack URL

# Perform the necessary actions to reach the page containing the pricing value
# Example: Search for a specific product, navigate to product page, etc.

# Wait for the page to load completely (adjust the wait time as needed)
time.sleep(3)

# Extract the pricing value
tire_prices = driver.find_elements(By.CLASS_NAME, "pricing")
brand_name = driver.find_elements(By.CLASS_NAME, "brandName")
model_name = driver.find_elements(By.CLASS_NAME, "modelName")


tire_price_list = [element.text for element in tire_prices]
brand_name_list = [element.text for element in brand_name]
model_name_list = [element.text for element in model_name]

total_price_list = []
index = 1
while True:
    try:
        total_price_element = driver.find_element(By.ID, f"priceTotal{index}")
        total_price_list.append(total_price_element.text)
        index += 1
    except:
        break
print("Brand Names:")
for brand in brand_name_list:
    print(brand)    

print("Model Names:")
for model in model_name_list:
    print(model)

print("Tire Prices:")
for price in tire_price_list:
    print(price)

print("\nTotal Prices for Four Tires:")
for price in total_price_list:
    print(price)

# Close the browser
driver.quit()
