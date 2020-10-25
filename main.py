from selenium import webdriver
import parserplus

def codeEntry(driver, codes_list):
    is_Winner = False
    code_count = 0 
    for code in codes_list:
        code_count +=1
        inputCode = driver.find_element_by_id('CodeEntry.Code')
        inputCode.send_keys(code)
        submitButton = driver.find_element_by_name('submit')
        submitButton.click()
        is_Winner = is_Winner or parserplus.check_Winner(driver.title)
        if is_Winner:
            break
        if code_count != len(codes_list):
            driver.get('https://winxbox.com/en-us/EnterCode')
    return is_Winner

def startEntry(email, codes_list):
    is_Winner = False
    driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
    driver.get('https://winxbox.com/')
    inputEmail = driver.find_element_by_id('Email_Identifier')
    inputEmail.send_keys(email)
    inputEmail.submit()
    if parserplus.verify_Eligibility(driver.title) == False:
        driver.close()
    else:
        is_Winner = is_Winner or codeEntry(driver, codes_list)
        driver.close()
    return is_Winner



email_list = parserplus.parse_Text('./emails.txt')
codes_list = parserplus.parse_Text('./codes.txt')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
for email in email_list:
    is_Winner = startEntry(email, codes_list)
    if is_Winner:
        print("OH SHIT OH FUCK")
        break
    else:
        print("Nope!")
    
