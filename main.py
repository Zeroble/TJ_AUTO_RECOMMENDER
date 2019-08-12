import time
from selenium import webdriver
from bs4 import BeautifulSoup
import threading

#############################################################
###SETTING FORMS#############################################
TYPE = "가요" # 가요, POP, JPOP, 중국
SONG_NAME = "show me your love"
SONG_ARTIST = "성시경"
TIMES = 10#추천 횟수
#############################################################
class myThread (threading.Thread): #threading.Thread 상속받음
    def __init__(self, threadID): #초기화 작업
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self): #.start()를 했을때 실행될 내용
        go()
        print("Exiting " + str(self.threadID))

def getFun():
    global URL
    global options
    driver = webdriver.Chrome(r'.\chromedriver.exe',options=options)
    driver.implicitly_wait(5)
    #driver.set_window_position(-10000,0)
    driver.get(URL)
    driver.switch_to.frame(2)
    html = driver.page_source
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    doc = str(soup.select_one("#BoardType1 > table > tbody > tr:nth-child(2) > td:nth-child(7) > a"))
    print(doc)
    fun = doc.replace('<a href="javascript:',"").replace('"><img src="../images/tjsong/btn_recommand.gif"/></a>',"")
    # driver.find_element_by_css_selector("#BoardType1 > table > tbody > tr:nth-child(2) > td:nth-child(7) > a > img").click()
    driver.quit()
    return fun
def go():
    global fun
    global URL
    global options
    driver = webdriver.Chrome(r'.\chromedriver.exe', options=options)
    driver.implicitly_wait(5)
    driver.get(URL)
    driver.switch_to.frame(2)
    driver.execute_script(fun)
    driver.quit()


#https://www.tjmedia.co.kr/tjsong/song_songRequestEnd.asp?dt_code=20&song=Lil+Tecca&title=Ransom
VAR_FOR_TYPE = {"가요":"10", "POP":"20", "JPOP":"30", "중국":"40"}

SONG_NAME = SONG_NAME.replace(" ", "+")
SONG_ARTIST = SONG_ARTIST.replace(" ", "+")
URL = "https://www.tjmedia.co.kr/tjsong/song_songRequestEnd.asp?dt_code="+VAR_FOR_TYPE[TYPE]+"&song="+SONG_ARTIST+"&title="+SONG_NAME


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

# html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
print(URL)
print("getting funtion...")
fun = getFun()
print(fun)
for i in range(0, TIMES):
    myThread(i).start()
    print("추천 {0}회 완료".format(i+1))