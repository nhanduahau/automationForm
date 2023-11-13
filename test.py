import openpyxl
from selenium import webdriver

# Đọc dữ liệu từ tệp Excel
wb = openpyxl.load_workbook('DS.xlsx')
sheet = wb['Sheet 1']
data = sheet['A1'].value

# Truy cập vào trang web và điền dữ liệu
driver = webdriver.Edge()
driver.get('https://forms.gle/HQPF9KGQXeAyJ1Nd9')
element = driver.find_element_by_id('Xb9hP')
element.send_keys(data)
button = driver.find_element_by_id('l4V7wb Fxmcue')
button.click()