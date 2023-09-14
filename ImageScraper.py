from selenium import webdriver
import bs4
import os
import requests
import time
from time import sleep
from selenium.common.exceptions import NoSuchElementException

chromeDriverPath = r'C:\Users\kkeer\OneDrive\Documents\Drivers\chromedriver.exe'
driver = webdriver.Chrome(chromeDriverPath)

searchURL = "https://www.google.com/search?q=goku+base+form&source=Inms&tbm=isch"
driver.get(searchURL)

driver.maximize_window()
driver.execute_script("window.scrollTo(0,0);")

# a = input("Hold up: ")
sleep(20)

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div', {'class':"isv-r PNCib MSM1fd BUooTd"})

len_containers = len(containers)

print(len_containers)

folder_name = 'GokuDataset/Form0'

# if not os.path.isdir(folder_name):
#     os.makedirs(folder_name)

def download(url, folder_name, num):
    response = requests.get(url)
    if response.status_code==200:
        with open(os.path.join(folder_name, str(num)+".jpg"), 'wb') as file:
            file.write(response.content)

def check_exists_by_xpath(xpath):
    try:
        driver.find_element("xpath", xpath)
    except NoSuchElementException:
        return False
    return True

temp = False
for i in range(1, len_containers+1):
    if i % 25 == 0:
        continue
    if i < 400:
        continue

    xPath = '//*[@id="islrg"]/div[1]/div[%s]'%(i)

    previewImageXPath = '//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img'%(i)
    previewImageElement = driver.find_element("xpath", previewImageXPath)
    previewImageURL = previewImageElement.get_attribute("src")

    driver.find_element("xpath", xPath).click()

    timeStarted = time.time()

    # imageElement = driver.find_element("xpath", """//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img""")

    # imageURL = imageElement.get_attribute("src")


    while True:
        print(i)

        if check_exists_by_xpath('//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img') == False:
            temp = True
            break

        imageElement = driver.find_element("xpath", '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img')

        imageURL = imageElement.get_attribute("src")

        print("Waiting for the full res image")
        if imageURL != previewImageURL:
            break

        else:
            currentTime = time.time();

            if (currentTime - timeStarted) > 5:
                break

    if temp == False:
        try:
            download(imageURL, folder_name, i)
            print("Downloaded image %s out of %s total. URL: %s"%(i, len_containers+1, imageURL))
        except:
            print("Couldn't download an image %s, continuing downloading the next one" %(i))
    temp = False

