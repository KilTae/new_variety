import requests
import ipyplot
from bs4 import BeautifulSoup as bs
search = "토마토"
url = f"https://www.nongsaro.go.kr/portal/ps/psa/psab/psabf/spciesRsrchLst.ps?findRdaItemCd=&findTechInfoSvcCd=&findPage=1&findOtptCode=&sKidofcomdtySeCode=&sTchnlgyPrcuseTyCode=&searchStyle=&menuId=PS65425&tabAt=&sCropsCode=&sCropsNm=&sMtrtSeCode=&sSkllSeCode=&sGrdlSeCode=&sUnbrngYear=&sTextType=sNmSjInfo&sSrchType=&chkVer=&group=kindOfCorp&sText=%ED%86%A0%EB%A7%88%ED%86%A0&sType=sNmSjInfo&detSchCode=N"
res = requests.get(url)
soup = bs(res.text, "html.parser")
image_src_list = [img.get("src") for img in soup.select(".con .thumImg > img")]

ipyplot.plot_images(image_src_list, img_width=200)


if n == 9:
        n = 1
        print(button_n)
        print(button_n%10)
        if button_n%10 == 0 and button_n > 1: 
            button_n += 1
            button = browser.find_element(By.CSS_SELECTOR, '#paging > a.next')
            button.click()
            print('>')
            time.sleep(5)

        else :
            button_n += 1
            button = browser.find_element(By.CSS_SELECTOR,'#paging > span:nth-child({}) > a'.format(button_n))
            button.click()
            print('다음 번호')
            time.sleep(5)

            cur_css_type = '#srchFm > div.kind-bx > ul > li:nth-child({}) > dl > dt'.format(n)
    cur_css_title = '#srchFm > div.kind-bx > ul > li:nth-child({}) > dl > dd.kind > span'.format(n)
    cur_css_function = '#srchFm > div.kind-bx > ul > li:nth-child({}) > dl > dd.txt-B'.format(n)
    cur_css_img = '#srchFm > div.kind-bx > ul > li:nth-child({}) > dl > dd.thumImg > img'.format(n)



        nong_titles.append(title.text)
        nong_functions.append(function.text)
        nong_img_urls.append(img)
        print(type.text)
        print(title.text)
        print(function.text)
        print(img)
        print('\n')

= browser.find_elements(By.CLASS_NAME, "thumImg").__getattribute__("src")


    btn = WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, '#product-list-paging > div > a:nth-child({})'.format(button_n))
                    )
                )
    browser.execute_script("arguments[0].click();", btn)
    time.sleep(3)

url = f"https://www.coupang.com/np/categories/194282?listSize=120&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&channel=user&fromComponent=N&selectedPlpKeepFilter=&sorter=bestAsc&filter=&component=194182&rating=0&page=" + f"{button_n}"
    time.sleep(5)

    btn = browser.find_element(By.CSS_SELECTOR, By.CSS_SELECTOR, '#product-list-paging > div > a:nth-child({})'.format(button_n))
    btn.click()