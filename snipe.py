import os, time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Config
email = ""
password = ""
channel = ""
kakera = 0 # Kakera above the number placed are claimed
driver_path = r"\chromedriver_win32\chromedriver.exe"
chromium_path = r"\chromium\chrome.exe"

# Web driver
opts = Options()
opts.add_argument("--log-level=3")
opts.headless=True
opts.add_argument("--start-maximized")
opts.binary_location = chromium_path
driver = uc.Chrome(executable_path=driver_path, options=opts)

for i in range(100):
    time.sleep(0.02)
    print(f'Loading [+]... [Percent {i + 1} %] => Keeping your System in SYNC..', end="\r", flush=True)
try:
    os.system('cls')
except:
    os.system('clear')

print('''

        ╭━╮╭━╮╱╱╱╱╭╮╱╱╱╱╱╱╭━━━╮
        ┃┃╰╯┃┃╱╱╱╱┃┃╱╱╱╱╱╱┃╭━╮┃
        ┃╭╮╭╮┣╮╭┳━╯┣━━┳━━╮┃╰━━┳━╮╭┳━━┳━━┳━╮
        ┃┃┃┃┃┃┃┃┃╭╮┃╭╮┃┃━┫╰━━╮┃╭╮╋┫╭╮┃┃━┫╭╯
        ┃┃┃┃┃┃╰╯┃╰╯┃╭╮┃┃━┫┃╰━╯┃┃┃┃┃╰╯┃┃━┫┃
        ╰╯╰╯╰┻━━┻━━┻╯╰┻━━╯╰━━━┻╯╰┻┫╭━┻━━┻╯
        ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
        ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯

''')

driver.get("https://discord.com/login")
time.sleep(5)
driver.find_element_by_css_selector("input[name='email']").send_keys(email)
time.sleep(0.1)
driver.find_element_by_css_selector("input[name='password']").send_keys(password)
time.sleep(0.1)
driver.find_element_by_css_selector("button[type='submit']").submit()

while True:
    if driver.current_url == "https://discord.com/channels/@me":
        break

time.sleep(2)
driver.get(channel)

while True:
    try:
        msgbox = driver.find_element_by_css_selector("[class='markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP']")
    except:
        pass
    else:
        print("Established Discord Channel ready to SNIPE [+]")
        break

def reactsnipe(card, emb):
    try:
        reaction = card.find_element_by_css_selector("[class='reactionInner-15NvIl']")
    except:
        print(f'Except = {emb.find_element_by_css_selector("strong").text} | {kakera} - {int(emb.find_element_by_css_selector("strong").text) > kakera}', end="\r", flush=True)
        if int(emb.find_element_by_css_selector("strong").text) > kakera:
            print(f"CLAIMING: Greater than {kakera}", end="\r", flush=True)
            msgbox.send_keys("+:heartpulse:")
            msgbox.send_keys(Keys.ENTER)
            print(f'''Success SNIPED {emb.find_element_by_css_selector("[class='embedAuthorName-3mnTWj']").text}!''')
            cyn = input("Continue SNIPING [Y | N] > ").lower()
            if cyn != "y":
                driver.quit()
                exit()
    else:
        print(f'Else = {emb.find_element_by_css_selector("strong").text} | {kakera} - {int(emb.find_element_by_css_selector("strong").text) > kakera}', end="\r", flush=True)
        if reaction.get_attribute("aria-pressed") != "true":
            if int(emb.find_element_by_css_selector("strong").text) > kakera:
                print(f"CLAIMING: Greater than {kakera}", end="\r", flush=True)
                msgbox.send_keys("+:heartpulse:")
                msgbox.send_keys(Keys.ENTER)
                print(f'''Success SNIPED {emb.find_element_by_css_selector("[class='embedAuthorName-3mnTWj']").text}!''')
                cyn = input("Continue SNIPING [Y | N] > ").lower()
                if cyn != "y":
                    driver.quit()
                    exit()

while True:
    time.sleep(0.01)
    msgs = driver.find_elements_by_css_selector("[class='message-2qnXI6 cozyMessage-3V1Y8y groupStart-23k01U wrapper-2a6GCs cozy-3raOZG zalgo-jN1Ica']")
    try:
        msg = msgs[len(msgs) - 1].find_element_by_css_selector("[class='embedWrapper-lXpS3L embedFull-2tM8-- embed-IeVjo6 markup-2BOw-j']")
    except Exception as e:
        pass
    else:
        try:
            reactsnipe(msgs[len(msgs) - 1], msg)
        except:
            pass