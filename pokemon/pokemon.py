import io
import urllib.request

from selenium import webdriver
import time
driver = webdriver.Chrome("chromedriver.exe")
from PIL import Image

def first_site():
    driver.get("https://zufallspokemon.de/en/")
    element = driver.find_element_by_xpath('//*[@id="content"]/form/input')
    element.click()
    time.sleep(1)
    url = driver.find_element_by_xpath('//*[@id="pokemonbild"]').get_attribute("src")
    name = driver.find_element_by_xpath('//*[@id="english"]').text
    return url,name
def second_site():
     driver.get('https://randompokemon.com/')
     element = driver.find_elements_by_css_selector('input')
     lists = driver.find_element_by_xpath("//select[@name='n']/option[text()='1']")
     element = element[5]
     element.click()
     pokemon = driver.find_elements_by_xpath("//section[@id='results']")
     time.sleep(1)
     url = driver.find_element_by_xpath("//section[@id='results']/ol/li/div/img").get_attribute("src")
     name = driver.find_element_by_xpath("//section[@id='results']/ol/li/div/img").get_attribute("title")
     return url,name
def check_id(id):
    r=''
    for i in id:
       if i.isdigit() == True:
           r+=str(i)
    return int(r)

if __name__=="__main__":
    res = first_site()
    fd = urllib.request.urlopen(res[0])
    id = check_id(res[0][len(res)-10:])
    print(f"WOW! You are #{id} {res[1]}! Check it: {res[0]}")
    img = io.BytesIO(fd.read())
    img = Image.open(img)
    img.show()
    driver.close()





