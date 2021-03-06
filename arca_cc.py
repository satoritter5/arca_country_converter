import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import count

###[유저설정부분]###
####################
wd_locate = 'chromedriver.exe의 위치'

board = '보드의 영문코드(programmers)'
category = '보드의 카테고리(Python)'

login_id = '아카라이브의 아이디'
login_password = '아카라이브의 비밀번호'

ban_country = [지역코드(숫자만)]
start_page = 시작페이지(숫자만)
end_page = 끝페이지(숫자만)

#게시글은 기본 총 30개까지 출력되며 1페이지 기준 start_post는 8, end_post는 37 range 함수를 쓰기때문에 end_post에 1을 더한 38을 입력 해 주셔야 합니다.
#아무리 해도 프로그램이 뻑 난다면 xpath값을 직접 기입해주는것이 좋습니다.
start_post = 2
end_post = 32
####################


#webdriver options
options = webdriver.ChromeOptions()
#디버깅 시에 headless 부분을 지워주시고 작업 해 주세요.
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(wd_locate, options=options)

#URL
login_url = 'https://arca.live/u/login?goto=/b/' + board
arc_url = 'https://arca.live/b/' + board + '?' + 'category=' + category + '&target=all&keyword=&p='

#아카라이브 로그인
print('로그인을 시도합니다.')
driver.get(login_url)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="idInput"]').send_keys(login_id)
driver.find_element_by_xpath('//*[@id="idPassword"]').send_keys(login_password)
driver.find_element_by_xpath('/html/body/div/div[3]/article/div/div[2]/div/div/form/div[3]/button').click()

#아카라이브 채널 열기
print('채널에 접속합니다.')
driver.get(arc_url)
time.sleep(1)

#경고창 스킵
try:
    print('경고창이 스킵되었습니다.')
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
except:
    pass

#국가제한 변경구문
for page in range(start_page, end_page):
    url = arc_url + str(page)
    driver.get(url)
    time.sleep(1)
    for op in range(start_post, end_post):
        print('[ 현재 게시글은 '+str(page)+' 페이지의 '+str(op)+' 번째 게시글 입니다. ]\n')
        
        #새창으로 게시글 열기
        opget = driver.find_element_by_xpath('/html/body/div/div[3]/article/div/div[4]/div[3]/a['+str(op)+']')
        opget.send_keys(Keys.CONTROL + Keys.ENTER)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.1)
        #Article 클릭
        driver.find_element_by_xpath('//*[@id="controlArticle"]').click()
        time.sleep(0.1)
        
        #국가제한 클릭
        try:
            driver.find_element_by_xpath('/html/body/div/div[3]/article/div[2]/div[3]/div[1]/span[3]/span[2]/a[6]').click()
        except:
            driver.find_element_by_xpath('/html/body/div/div[3]/article/div[2]/div[2]/div[1]/span[3]/span[2]/a[6]').click()
        time.sleep(0.1)
        for check in ban_country:
            if driver.find_element_by_xpath('/html/body/div[1]/div[3]/article/div[1]/div/form/div[2]/div/div/div['+str(check)+']/input').get_attribute('checked'):
                print('이 게시글은 이미 지역설정이 완료되어있습니다.\n\n')
                driver.find_element_by_xpath('/html/body/div[1]/div[3]/article/div[1]/div/form/div[3]/button[1]').click()
            else:
                driver.find_element_by_xpath('/html/body/div[1]/div[3]/article/div[1]/div/form/div[2]/div/div/div['+str(check)+']/input').click()
                print('이 게시글의 지역설정을 완료했습니다.\n\n')
                driver.find_element_by_xpath('//*[@id="modal-country-restriction"]/div/form/div[3]/button[2]').click()
        time.sleep(0.1)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    print('\n\n※[ 다음 페이지로 넘어갑니다. ]※\n\n\n\n')
print('모든 작업이 끝났습니다.')
