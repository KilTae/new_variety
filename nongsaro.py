from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import warnings

slang_title = []
slang_description = []
browser = webdriver.Safari()
url = f'https://www.nongsaro.go.kr/portal/ps/psa/psab/psabf/spciesRsrchLst.ps?menuId=PS65425'
browser.get(url)


nong_types = []
nong_titles = []
nong_functions = []
nong_img_urls = []
nong_urls = []

n = 1
button_n = 1
while(1) :
    if button_n == 300: break 
    # 300

    print(n)

    types = browser.find_elements(By.CSS_SELECTOR, "#srchFm > div.kind-bx > ul > li > dl > dt > span")
    titles = browser.find_elements(By.CLASS_NAME, "kind")
    functions = browser.find_elements(By.CLASS_NAME, "txt-B")
    imgs = browser.find_elements(By.CSS_SELECTOR, "#srchFm > div.kind-bx > ul > li > dl > dd.thumImg > img")
    urls = browser.find_elements(By.CSS_SELECTOR,"#srchFm > div.kind-bx > ul > li > dl > dd.inner_btnArea.tc > a:nth-child(1)")
    for type, title, function, img, url in zip(types, titles, functions, imgs, urls):
        nong_types.append(type.text)
        nong_titles.append(title.text)
        nong_functions.append(function.text[3:])
        nong_img_urls.append(img.get_attribute("src"))
        if url.text != "요약정보" :
            nong_urls.append(" ")
        else:
            nong_urls.append(url.get_attribute("onclick").split("'")[3])
        
        print(type.text)
        print(title.text)
        print(function.text[3:])
        #print(url.get_attribute("onclick"))
       # print(url.get_attribute("onclick").split("'")[3])

        print('\n')

    button_n += 1
    url = 'https://www.nongsaro.go.kr/portal/ps/psa/psab/psabf/spciesRsrchLst.ps?findRdaItemCd=&findTechInfoSvcCd=&findOtptCode=&sKidofcomdtySeCode=&sTchnlgyPrcuseTyCode=&searchStyle=&menuId=PS65425&tabAt=&sCropsCode=&sCropsNm=&sMtrtSeCode=&sSkllSeCode=&sGrdlSeCode=&sUnbrngYear=&sTextType=sNmSjInfo&sSrchType=&chkVer=&group=kindOfCorp&sText=&sType=sNmSjInfo&detSchCode=N=&findPage={}'.format(button_n)
    browser.get(url)
    time.sleep(3)
        

data = {'type' : nong_types, 'title' : nong_titles, 'fuction' : nong_functions , 'img' : nong_img_urls, 'url' : nong_urls}
df = pd.DataFrame(data)
print(df)
df.to_csv('nongsaro1.csv', encoding = 'utf-8-sig')
time.sleep(5)
browser.close()