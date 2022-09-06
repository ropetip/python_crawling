from site import execusercustomize
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5) # 웹페이지가 로딩 될때까지 5초는 기다림
driver.maximize_window()
driver.get("http://alm.emro.co.kr/login.jsp?os_destination=%2Fsecure%2FDashboard.jspa")

import time 
import pyautogui
import pyperclip

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#login-form-username")
id.click()
pyperclip.copy("service")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#login-form-password")
pw.click()
pyperclip.copy("clsrmsgks@9#8")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

login_btn = driver.find_element(By.CSS_SELECTOR, "#login-form-submit")
login_btn.click()

time.sleep(0.5)

driver.get("http://alm.emro.co.kr/issues/?filter=11207")