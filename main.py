# -*- coding: utf-8 -*-
# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time
from pyautogui import hotkey
import pyperclip

# Config
login_time = 30     # Time for login (in seconds)
new_msg_time = 8    # TTime for a new message (in seconds)
send_msg_time = 3   # Time for sending a message (in seconds)
country_code = 91   # Set your country code

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Encode Message Text
# with open('message.txt', 'r') as file:

msg = """\t\t\tफार्मेसी काउंसिल मेंबर चुनाव \n\n\n


फार्मेसी काउंसिल मेंबर चुनाव में आपके अपने प्रत्याशी  "अरविन्द कुमार मिश्रा"(फार्मेसी)को आप अपना बहुमूल्य वोट दे !  अरविन्द मिश्रा जी का नाम वैलेट पेपर पर 4 नंबर पर अंकित रहेगा उनके नाम के आगे क्रॉस (❎) का निशान बनाकर अपना, अपने सहभागियों और मित्रों का बहुमूल्य वोट  दिलवाए। आपके आशीर्वाद, सपोर्ट,और प्यार के लिए तत्पर उपस्थित रहेंगे🙏🏻🙏🏻 बैलेट पेपर आपके घर के रजिस्टर्ड एड्रेस पर आयेगा और आपको पोस्ट द्वारा ही वोटिंग भेजना है।\n\n                         
\t\t\t||धन्यवाद||\n
\t\t\tसंपर्क नंबर -9752409686(अरविन्द कुमार मिश्रा)।\n"""

# Open browser with default link
link = 'https://api.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# Loop Through Numbers List
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://api.whatsapp.com/send/?phone={country_code}{num}&text={msg}'
        # link = f'https://web.whatsapp.com/send/?phone={country_code}{num}'
        driver.get(link)
        time.sleep(new_msg_time)
        actions = ActionChains(driver)
        # print("action", actions)
        # value = pyperclip.paste()
        # Link = str(value)
        # hotkey('ctrl', 'v')
        # hotkey('enter')
        # time.sleep(2)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        with open("completeSendNo.txt", "a") as file:
            file.write(
                f" {num} \n")
        time.sleep(send_msg_time)

# Quit the driver
# driver.quit()
# pic.jpeg
# IMG_20190906_075807.jpg
