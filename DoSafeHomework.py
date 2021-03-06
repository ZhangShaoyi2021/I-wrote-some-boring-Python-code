#2021年2月23日 瞎蒙答题器

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random 

url = "http://dati.lzwuyou.com/WeChat/"

driver = webdriver.Edge()   #打开Edge浏览器
driver.get(url)  #打开网址
time.sleep(0.2)

name = "张绍翊"
mobile = "12345678910" #听说老师不检查电话号码，但没有电话号码登不进网站
school = "壮小"
class_ = "六年级7班"

for i in range(2): driver.find_element_by_tag_name("body").send_keys(Keys.SPACE) #按2下空格,跳到页面底部
    
nameInput = driver.find_element_by_id("RealName")
mobileInput = driver.find_element_by_id("Mobile")
schoolInput = driver.find_element_by_id("SchoolName")    #分别找到标签
classInput = driver.find_element_by_id("ClassName")
time.sleep(0.2)

nameInput.send_keys(name)
mobileInput.send_keys(mobile)
schoolInput.send_keys(school)    #分别输入标签
classInput.send_keys(class_)
time.sleep(0.2)

driver.find_element_by_xpath("/html/body/section/section/div/div/div/button").click() #找到“确定”按钮，鼠标右键
time.sleep(1)

while True:   #极致速度
    try:
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div").click()#找到开始答题按钮，鼠标右键
        break
    except:
        pass
        
        
for i in range(20):  #共20题
    print("第%d题  正在盲猜" %(i+1))
    time.sleep(0.1)
    
    while True: #极致速度
        try:
            optionList = driver.find_elements_by_class_name("option_item")
            time.sleep(0.02)
            randomIndex = random.randint(0,len(optionList)-1)  #随机索引生成
            optionList[randomIndex].click() #根据随机索引取值，鼠标右键
            break
        except:
            time.sleep(0.1)

else:
    time.sleep(1.8) #大概1.8秒后把答题速度和分数显示
    driver.get_screenshot_as_file(r"C:\Users\stone\Desktop\代码\python\图片\FinishMyHomework.png")
    #答题完毕立刻截图,发给老师
    #我们快速答题后，网站懵逼，会一直叠加我们的答题时间(手动也一样)
    
    driver.quit()
