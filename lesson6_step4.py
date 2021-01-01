#-*-coding:utf-8-*-


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
#from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.support.ui import Select
#import string
#import random
'''
link="http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_link_text("224592")
    button.click()
    #FILLS INPUT TAGS
    #time.sleep(3)
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")    
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")            
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()
    
finally:
	time.sleep(30)
	browser.quit()
    
'''

'''
#FILLS OUT A HUNDRED TEXT FIELDS
try:
    browser=webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")

    answer_length=5
    for element in elements:
        ltrz=string.ascii_letters
        answer=''.join(random.choice(ltrz) for j in range(answer_length))
        element.send_keys(answer)

    button=browser.find_element_by_css_selector("button.btn")
    button.click()    

finally:
    time.sleep(30)
    browser.quit()
'''
'''
#FINDS ELEMENT BY XPATH SELECTOR
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
'''    
#REGISTRATION FORM
'''
try:
    time.sleep(2)
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    input1 = browser.find_element_by_class_name("first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_class_name("second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("third")
    input3.send_keys("mail@nodomain.com")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)
    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text=welcome_text_elt
    assert "Congratulations!You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()
'''
#ROBOT CAPTCHA
'''
try:
    def calc(n_x):
        return str(math.log(abs(12*math.sin(int(x)))))    
    browser = webdriver.Chrome()    
    browser.get("http://suninjuly.github.io/math.html")
    x_val=browser.find_element_by_id("input_value")
    x=x_val.text
    rsl=calc(x)
    #print("Function returns: ",rsl)
    inp_field=browser.find_element_by_id("answer")
    inp_field.send_keys(rsl)
    chk_box=browser.find_element_by_class_name("form-check-label")
    chk_box.click()
    rob_text=browser.find_element_by_css_selector("[for='robotsRule']")
    rtext=rob_text.text
    print("Rules? ",rtext)
    rob_text.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    time.sleep(30)
    browser.quit()
'''
'''
#TREASURE
try:
    def calc(n_x):
        return str(math.log(abs(12*math.sin(int(n_x)))))    
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    tresr_id=browser.find_element_by_id("treasure")
    val=tresr_id.get_attribute("valuex")
    #x=val.text    
    r=calc(val)
    #print(r)
    inp1=browser.find_element_by_id("answer")
    inp1.send_keys(r)
    chk_robot=browser.find_element_by_id("robotCheckbox")
    chk_robot.click()
    chk_robot1=browser.find_element_by_id("robotsRule")
    chk_robot1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
'''
'''
#DROPDOWN LISTS
try:
    browser=webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    sel1=browser.find_element_by_tag_name("select")
    sel1.click()
    sel2=browser.find_element_by_css_selector("[value='1']")
    sel2.click()
finally:
    time.sleep(5)
    browser.quit()
'''
'''
#DROPDOWN LISTS.CALCULATE A SUM
try:
    browser=webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    n1_id=browser.find_element_by_id("num1")
    n1=n1_id.text
    n2_id=browser.find_element_by_id("num2")
    n2=n2_id.text        
    s=int(n1)+int(n2)
    s1=str(s)
    sel=Select(browser.find_element_by_tag_name('select'))
    sel.select_by_value(s1)    
    button = browser.find_element_by_css_selector("button.btn")    
    button.click()
finally:
    time.sleep(10)
    browser.quit
'''
'''
#METHOD OF EXECUTE_SCRIPT
try:
    browser=webdriver.Chrome()
    browser.execute_script("document.title='Vamp.';alert('Robots at work!');")
finally:
    time.sleep(10)
    browser.quit()
'''
'''
#EXECUTE_SCRIPT ERR.
try:
    def f(k):
        k=float(k)
        r=log(abs(12*sin(k)))
        return r
    browser=webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
    var_id=browser.find_element_by_id("input_value")
    n=var_id.text    
    r1=f(n)
    #print(n,r1)    
    
    inp=browser.find_element_by_id("answer")    
    browser.execute_script("return arguments[0].scrollIntoView(true);", inp)    
    inp.send_keys(str(r1))

    rob_chk=browser.find_element_by_id("robotCheckbox")
    rob_chk.click()

    rob_radb=browser.find_element_by_id("robotsRule")
    rob_radb.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()    
finally:
    time.sleep(15)    
    browser.quit()
'''    
'''
try:
    browser=webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    first_name=browser.find_element_by_name('firstname')
    first_name.send_keys('Rustam')
    last_name=browser.find_element_by_name('lastname')
    last_name.send_keys('Hood')
    email=browser.find_element_by_name('email')
    email.send_keys('nomail@domain.net')        
    chs=browser.find_element_by_css_selector("form > input#file")
    chs.send_keys("C:\\Users\\RUST\\file.txt")
    subm_btn=browser.find_element_by_css_selector("button.btn")
    subm_btn.click()
finally:
    time.sleep(30)    
    browser.quit()
'''
'''
try:
	browser=webdriver.Chrome()
	browser.get('http://suninjuly.github.io/alert_accept.html')
	btn=browser.find_element_by_css_selector("button.btn.btn-primary")
	btn.click()
	alert=browser.switch_to.alert
	alert.accept()
	value=browser.find_element_by_id("input_value")
	x=value.text
	reslt=log(abs(12*sin(float(x))))
	print("x: ",x)
	inp=browser.find_element_by_id("answer")
	inp.send_keys(str(reslt))
	btn1=browser.find_element_by_css_selector("button.btn.btn-primary")
	btn1.click()
finally:
	time.sleep(30)
	browser.quit()
'''
'''
#WORKING WITH A NEW BROWSER TAB
try:
	browser=webdriver.Chrome()
	browser.get('http://suninjuly.github.io/redirect_accept.html')
	window_before = browser.window_handles[0]#SAVING 1ST LINK
	btn1=browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
	btn1.click()
	window_after = browser.window_handles[1]
	browser.switch_to.window(window_after)
	value=browser.find_element_by_css_selector("span#input_value")
	x=value.text
	#print("x is: ",x)
	reslt=log(abs(12*sin(float(x))))
	inp=browser.find_element_by_css_selector("input#answer")
	inp.send_keys(str(reslt))
	btn2=browser.find_element_by_css_selector("button.btn.btn-primary")
	btn2.click()
finally:
	time.sleep(30)
	browser.quit()
'''
'''
try:
	browser=webdriver.Chrome()
	browser.get('http://suninjuly.github.io/cats.html')
	btn=browser.find_element_by_id("button")
	#btn.click()
finally:
	time.sleep(2)
	browser.quit()
'''
try:
	browser=webdriver.Chrome()
	browser.get('http://suninjuly.github.io/explicit_wait2.html')	
	button=WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
	btn_book=browser.find_element_by_css_selector('button#book')
	btn_book.click()
	var=browser.find_element_by_css_selector('span#input_value')
	n=var.text
	n=float(n)
	result=log(abs(12*sin(n)))
	print(result)
	inp=browser.find_element_by_css_selector("input#answer")    
	browser.execute_script("return arguments[0].scrollIntoView(true);", inp)    
	inp.send_keys(str(result))
	btn_submit=browser.find_element_by_css_selector("button#solve")
	btn_submit.click()
	alert1=browser.switch_to.alert
	alert_text=alert1.text
	print(alert_text)
finally:
	time.sleep(10)	
	browser.quit()