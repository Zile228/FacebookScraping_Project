from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import time
'''-------'''
class FacebookGroup:
    def __init__(self, path):
        # Vô hiệu hóa thông báo
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        # Khởi tạo WebDriver
        self.driver = webdriver.Chrome(service = ChromeService(executable_path= path), options=chrome_options)
        self.driver.get("https://web.facebook.com")
        self.driver.maximize_window()
    
     # Đăng nhập Facebook
    def login(self, email: str, password: str):
        username_input = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        password_input = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

        username_input.clear()
        username_input.send_keys(email)

        password_input.clear()
        password_input.send_keys(password)

        button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']")))
        button.click()
    
    # Thu thập thông tin:
    def scrape(self, url: str):
        # Truy cập đường link nhóm:
        time.sleep(5)
        self.driver.get(url)
        time.sleep(10)

        post_collected = []
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        for _ in range (0,20):
            # Sử dụng BeautifulSoup để trích html tĩnh
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            # Tìm tất cả bài viết
            all_posts = soup.find_all("div", {"class":"x1n2onr6 x1ja2u2z"})
            for post in all_posts:
                try:
                    post_content = post.find("div", {"class":"html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd"}, {"dir":"auto"}).text
                    if post_content not in post_collected:
                        post_collected.append(post_content)
                except:
                    post = "Post not found"

            self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight-700));")
            time.sleep(5)  # Chờ trang tải xong
            
            # Cuộn trang
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("Scroll finished")
                break  # Nếu không có nội dung mới
            last_height = new_height

        return post_collected



        
        
