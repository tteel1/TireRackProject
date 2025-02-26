from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Set up the WebDriver
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)
driver.get("https://www.tirerack.com/tires/TireSearchResults.jsp?tireIndex=0&autoMake=Toyota&autoYear=2025&autoModel=Camry%20AWD&autoModClar=SE&width=235/&ratio=45&diameter=18&sortCode=53850&skipOver=true&minSpeedRating=H&minLoadRating=S&performance=ALL")  # Replace with the actual TireRack URL

# Wait for the page to load completely (adjust the wait time as needed)
time.sleep(3)

# Extract the pricing value
def extract_data():

    tire_prices = driver.find_elements(By.CLASS_NAME, "pricing")
    brand_name = driver.find_elements(By.CLASS_NAME, "brandName")
    model_name = driver.find_elements(By.CLASS_NAME, "modelName")

    # Collect the data
    tire_price_list = [element.text for element in tire_prices]
    brand_name_list = [element.text for element in brand_name]
    model_name_list = [element.text for element in model_name]

    total_price_list = []
    index = 1
    while True:
        try:
            total_price_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, f"priceTotal{index}"))
            )
            total_price_list.append(total_price_element.text)
            index += 1
        except:
            break

    for i in range(len(tire_price_list)):
        brand = brand_name_list[i] if i < len(brand_name_list) else "N/A"
        model = model_name_list[i] if i < len(model_name_list) else "N/A"
        tire_price = tire_price_list[i] if i < len(tire_price_list) else "N/A"
        total_price = total_price_list[i] if i < len(total_price_list) else "N/A"

        print(f"Brand: {brand}, Model: {model}, Tire Price: {tire_price}, Total Price for Four Tires: {total_price}")

# Extract data from the first page
extract_data()

# Handle pagination
while True:
    try:
        # Wait for the "Next" button to be clickable
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nextArrowLink")))
        next_button.click()

        # Wait for the next page to load completely
        time.sleep(3)

        # Extract data from the next page
        extract_data()
    except:
        # Break the loop if there is no "Next" button
        break

# Close the browser
driver.quit()
