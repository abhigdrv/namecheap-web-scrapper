from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip
import pyautogui
import json
movement_interval = 10
options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://www.namecheap.com/domains/registration/results/?domain=&type=beast")
start_value = "aaaa"
end_value = "zzzz"
all_values = []
for i in range(ord(start_value[0]), ord(end_value[0])+1):
    for j in range(ord(start_value[1]), ord(end_value[1])+1):
        for k in range(ord(start_value[2]), ord(end_value[2])+1):
            for l in range(ord(start_value[3]), ord(end_value[3])+1):
                all_values.append(chr(i) + chr(j) + chr(k) + chr(l) + ".com")
group_size = 4000
grouped_values = [' '.join(all_values[i:i+group_size]) for i in range(0, len(all_values), group_size)]
time.sleep(10)
with open('status.json', 'r') as file:
    statusData = json.load(file)
startFrom = int(statusData['completed'])
for index, group in enumerate(grouped_values):
    if index > startFrom and index < startFrom+20:
        print(index, 'Process started')
        driver.refresh()
        time.sleep(5)
        pyperclip.copy(group)
        print(index, 'Data copied')
        search_input = driver.find_element(By.ID, 'beast-keywords-input')
        time.sleep(1)
        search_input.clear()
        print(index, 'Input cleared')
        time.sleep(2)
        search_input.send_keys(Keys.CONTROL, 'v')
        time.sleep(5)
        print(index, 'Data pasted')
        submit_button = driver.find_element(By.XPATH, "//section[@class='beast']/div[@class='settings open']/form/button")
        submit_button.click()
        print(index, 'Data submitted')
        time.sleep(8)
        export_button = driver.find_element(By.XPATH, "//div[@class='results-actions']/div/button[@class='export']")
        export_button.click()
        print(index, 'Export started')
        for sleepSch in range(1, 101):
            print('Processing ', index, 'completed', int(sleepSch*100/101), '%')
            pyautogui.moveRel(1, 0)
            time.sleep(2)
        print(index, 'Process completed')
        with open('status.json', 'r') as file:
            data = json.load(file)
            data['completed'] = index
        with open('status.json', 'w') as file:
            json.dump(data, file)

# driver.quit()