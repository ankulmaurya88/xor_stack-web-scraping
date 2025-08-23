


'''

    input=    [value ="Section 8 Company"]




li
    span-[class='p-hidden-accessible']

div_id ='pn_id_34'
    class='w-full p-dropdown p-component p-inputwrapper p-dropdown-clearable p-inputwrapper-filled'

        span='combobox'

            aria-label='Jharkhand'
'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Use webdriver-manager to auto-install correct ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://ngodarpan.gov.in/#/search-ngo")

wait = WebDriverWait(driver, 15)



# 1. Select State = "Jharkhand"




state_dropdown = wait.until( EC.element_to_be_clickable(  (By.XPATH, '//*[@id="commonScrollTo"]/div/form/div/div[1]/p-floatlabel/span/p-dropdown') ))
state_dropdown.click()
jharkhand_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pn_id_17_list"]/p-dropdownitem[14]' )))
jharkhand_option.click()



# 2. Select NGO Type = "Section 8 Company"
ngo_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pn_id_22"]/div[2]')))
ngo_type_dropdown.click()
section_8_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pn_id_22_list"]/div[2]/ul/p-multiselectitem[1]')))
section_8_option.click()
state_dropdown.send_keys(Keys.ESCAPE)

# 3. Click Search button
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="commonScrollTo"]/div/form/div/div[7]/div/p-button')))
driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
time.sleep(1)
search_button.click()

# 4. Scrape Table Results
rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//table//tbody//tr")))

print("\nNGO Results for Section 8 Company in Jharkhand:\n")
for row in rows:
    print(row.text)

driver.quit()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://ngodarpan.gov.in/#/search-ngo")

wait = WebDriverWait(driver, 15)

# 1. Select State = "Jharkhand"
state_dropdown = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="commonScrollTo"]/div/form/div/div[1]/p-floatlabel/span/p-dropdown')
))
state_dropdown.click()
jharkhand_option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="pn_id_17_list"]/p-dropdownitem[5]')
))
jharkhand_option.click()

# 2. Select NGO Type = "Section 8 Company"
ngo_type_dropdown = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="pn_id_22"]/div[2]')
))
ngo_type_dropdown.click()
section_8_option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="pn_id_22_list"]/div[2]/ul/p-multiselectitem[1]')
))
section_8_option.click()

# Close any open dropdowns
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

# 3. Wait for manual CAPTCHA solving
print("⚠️ Please solve the CAPTCHA manually in the browser.")
input("After completing CAPTCHA, press Enter to continue...")

# 4. Click Search button safely
search_button = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="commonScrollTo"]/div/form/div/div[7]/div/p-button')
))

# Wait until button is enabled
wait.until(lambda driver: "p-disabled" not in search_button.get_attribute("class"))
driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
time.sleep(0.5)
search_button.click()
print("Search button clicked!")

# 5. Scrape Table Results across pages
all_rows = []


while True:
    # Wait for table rows
    rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//table//tbody//tr")))
    # rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="pn_id_25-table"]/thead')))
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        data = [col.text for col in cols]
        all_rows.append(data)

    # Check if "Next" button is enabled
    try:
        next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next Page']")
        if "p-disabled" in next_button.get_attribute("class"):
            break  # last page reached
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        time.sleep(1)
        next_button.click()
        time.sleep(2)  # wait for table to load
    except:
        break  # no next button, exit

# 6. Save to CSV
with open("npo_Bihar_section8.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Sr. No", "Name of NPO", "Registration No,District (State)", "Address", "Sectors" ]) # adjust headers if needed
    writer.writerows(all_rows)

print(f"✅ Scraped {len(all_rows)} NGOs successfully!")
driver.quit()





# # 5. Scrape Table Results across pages
# all_data = []

# while True:
#     # Wait for table rows
#     rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="pn_id_25-table"]/thead')))
    
#     for row in rows:
#         cols = row.find_elements(By.TAG_NAME, "td")
#         data = [col.text for col in cols]
#         all_data.append(data)

#     # Check if "Next" button is enabled
#     try:
#         next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next Page']")
#         if "p-disabled" in next_button.get_attribute("class"):
#             break  # last page reached
#         driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
#         time.sleep(1)
#         next_button.click()
#         time.sleep(2)  # wait for table to load
#     except:
#         break  # no next button, exit



# # 6. Save to Excel
# df = pd.DataFrame(all_data, columns=["Sr. No", "Name of NPO", "Registration No,District (State)", "Address", "Sectors"])
# df.to_excel("ngo_jharkhand_section8.xlsx", index=False)

# print(f"✅ Scraped {len(all_data)} NGOs successfully and saved to Excel!")
# driver.quit()




# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # Setup WebDriver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
# driver.get("https://ngodarpan.gov.in/#/search-ngo")
# wait = WebDriverWait(driver, 15)

# # Select State = Jharkhand
# state_dropdown = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="commonScrollTo"]/div/form/div/div[1]/p-floatlabel/span/p-dropdown')
# ))
# state_dropdown.click()
# jharkhand_option = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="pn_id_17_list"]/p-dropdownitem[14]')
# ))
# jharkhand_option.click()

# # Select NGO Type = Section 8 Company
# ngo_type_dropdown = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="pn_id_22"]/div[2]')
# ))
# ngo_type_dropdown.click()
# section_8_option = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="pn_id_22_list"]/div[2]/ul/p-multiselectitem[1]')
# ))
# section_8_option.click()

# driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

# # Wait for manual CAPTCHA
# print("⚠️ Please solve the CAPTCHA manually in the browser.")
# input("After completing CAPTCHA, press Enter to continue...")

# # Click Search button
# search_button = wait.until(EC.presence_of_element_located(
#     (By.XPATH, '//*[@id="commonScrollTo"]/div/form/div/div[7]/div/p-button')
# ))
# wait.until(lambda driver: "p-disabled" not in search_button.get_attribute("class"))
# driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
# time.sleep(0.5)
# search_button.click()
# print("Search button clicked!")

# # Scrape table across pages
# all_data = []

# while True:
#     rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//table[@id='pn_id_25-table']//tbody//tr")))
    
#     for row in rows:
#         cols = row.find_elements(By.TAG_NAME, "td")
#         if len(cols) >= 5:
#             sr_no = cols[0].text
#             name = cols[1].text
#             reg_district = cols[2].text
#             # Split Registration No and District if comma exists
#             if "," in reg_district:
#                 reg_no, district_state = map(str.strip, reg_district.split(",", 1))
#             else:
#                 reg_no, district_state = reg_district, ""
#             address = cols[3].text
#             sectors = cols[4].text
#             all_data.append([sr_no, name, reg_no, district_state, address, sectors])
    
#     # Next page
#     try:
#         next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next Page']")
#         if "p-disabled" in next_button.get_attribute("class"):
#             break
#         driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
#         time.sleep(1)
#         next_button.click()
#         time.sleep(2)
#     except:
#         break

# # Save to Excel
# df = pd.DataFrame(all_data, columns=["Sr. No", "Name of NPO", "Registration No", "District (State)", "Address", "Sectors"])
# df.to_excel("ngo_jharkhand_section8.xlsx", index=False)

# print(f"✅ Scraped {len(all_data)} NGOs successfully and saved to Excel!")
# driver.quit()
