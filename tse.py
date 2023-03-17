from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def getStatusIds(user,nbStatus=3,headless=True):
	if user[0] == "@":
		user = user[1:]
	regex = f"/{user}\/status\/\d*/g"
	jsPart1 = f"var out = [];var str = document.getElementsByTagName('html')[0].innerHTML;var patt = {regex};"
	jsToRun = jsPart1+"while(match=patt.exec(str)){out.push(match[0]);}return out;"
	options = Options()
	if(headless == True):
		options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(options=options)
	driver.get(f"https://twitter.com/{user}") 
	time.sleep(3)
	#WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/div/article")))
	arrOut = logic(driver,nbStatus,jsToRun)
	driver.close()
	return arrOut

def logic(driver,nbStatus,jsToRun):
	arrOut = list()
	while len(arrOut) < nbStatus:
		arrTweets = driver.execute_script(jsToRun)
		for tweet in arrTweets:
			arrOut.append(int(tweet.split("/")[-1]))
		arrOut = list(dict.fromkeys(arrOut))
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
		time.sleep(1)
	arrOut.sort(reverse=True)
	length = len(arrOut)
	if length > nbStatus:
		arrOut = arrOut[:nbStatus]
	return arrOut

def getStatusMultipleUsers(listUsers,nbStatus=3,headless=True):
	options = Options()
	if(headless == True):
		options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(options=options)
	arrOutMulti = {}
	for user in listUsers:
		try:
			if user[0] == "@":
				user = user[1:]
			regex = f"/{user}\/status\/\d*/g"
			jsPart1 = f"var out = [];var str = document.getElementsByTagName('html')[0].innerHTML;var patt = {regex};"
			jsToRun = jsPart1+"while(match=patt.exec(str)){out.push(match[0]);}return out;"
			driver.get(f"https://twitter.com/{user}") 
			time.sleep(3)
			#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/div/article")))
			arrOut = logic(driver,nbStatus,jsToRun)
			arrOutMulti[user] = arrOut
		except:
			arrOutMulti[user] = "invalid"
	driver.close()
	return arrOutMulti

if __name__ == "__main__":
	print("This is a module, don't run it like this !")