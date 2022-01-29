from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os

link = "https://instagram.com"

followersList = []
unfollowersList = []
followedList = []

browser = webdriver.Chrome(executable_path='C:/driver/chromedriver.exe')
def login(username,password):
    browser.get(link)
    time.sleep(5)
    usernameArea = browser.find_element_by_name('username')
    usernameArea.send_keys(username)
    passwordArea = browser.find_element_by_name('password')
    passwordArea.send_keys(password)
    passwordArea.send_keys(Keys.ENTER)
    time.sleep(5)

    goFollowers(username)


def scrollDown():
    javaScriptCommand = """
        page = document.querySelector(".isgrP");
        page.scrollTo(0,page.scrollHeight);
        const pageEnd = page.scrollHeight;
        return pageEnd;
    """

    pageEnd = browser.execute_script(javaScriptCommand)
    while True:
        end = pageEnd
        time.sleep(1)
        pageEnd = browser.execute_script(javaScriptCommand)
        if end == pageEnd:
            break

def goFollowers(username):
    browser.get(link+"/"+username)
    time.sleep(2)
    browser.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(2) > a").click()
    time.sleep(5)

    scrollDown()

    followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
    
    for follower in followers:
        followersList.append(follower.text)
    time.sleep(5)

    goFollowed(username)

def goFollowed(username):

    browser.get(link+"/"+username)
    time.sleep(5)
    browser.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a").click()
    time.sleep(5)

    scrollDown()

    followeds = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
    
    for followed in followeds:
        followedList.append(followed.text)

    os.system("cls")

    
def unf():
    for f in followersList:
        if f in followedList:
            followedList.remove(f)
    unfollowersList = followedList
    os.system("cls")
    browser.close()
    return unfollowersList
