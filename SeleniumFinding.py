from selenium import webdriver
browser = webdriver.Chrome()
browser.get(" Link")

try:
    elem = browser.find_element_by_class_name('bookcover')
    print("Found <%s> element with that class name!"%(elem.tag_name))
except:
    print("Element not found")

