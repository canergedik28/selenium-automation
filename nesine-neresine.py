from selenium import webdriver 
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys

class NesineAutomation:
    chromeDriverPath = "chromedriver.exe"
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_experimental_option('useAutomationExtension', False)
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--log-level=1')
        self.chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36')
        self.chrome_options.add_experimental_option("detach", True)
        self.pageLink = 'https://www.nesine.com/'
        self.driver = webdriver.Chrome(options=self.chrome_options,executable_path=self.chromeDriverPath) 
        self.username = "username"
        self.password = "password"    
        self.script = """
                        function sleep(ms) {
                                return new Promise(resolve => setTimeout(resolve, ms));
                        }
                        async function clickFunction(){
                            var dataItems = [1,2,3];
                            var newData = [];
                            var itemCount  = 1;                    
                            while(dataItems.length != 0){
                                        for (var i=0; i<2; i++){
                                            randInt = Math.floor(Math.random() * dataItems.length);
                                            addItem = dataItems[randInt];
                                            newData.push(addItem);
                                            dataItems = dataItems.filter(item => item !== addItem);
                                            await sleep(1000);
                                        }
                                        for (var i=0; i<newData.length; i++){
                                            console.log(newData[i]);
                                            let item = document.querySelector('div[data-mid="'+newData[i]+'"][data-ocid="2"]');
                                            sleep(500);
                                            item.click();
                                            // sleep(200);
                                            //console.log(newData[i]);
                                        
                                        if(i == 1){
                                                let buttonClick = $('div[id="btnPlay"]');
                                                await sleep(500);
                                                buttonClick.click();
                                                itemCount = 1;
                                                await sleep(15000);
                                                window.location.reload();
                                                await sleep(5000);
                                                
                                            }
                                            await sleep(1000);
                                            itemCount++;
                                        }
                                    newData = [];
                            }
                        }
                        clickFunction();
    """
        
    def nesineNeresine(self):
         webDriver = WebDriverWait(self.driver,60)
         self.driver.get(self.pageLink)
         usernameInput =  webDriver.until(EC.presence_of_element_located((By.XPATH,'//input[contains(@name,"header-username-input")]')))
         usernameInput.send_keys(self.username)
         passwordInput =  webDriver.until(EC.presence_of_element_located((By.XPATH,'//input[contains(@name,"header-password-input")]')))
         passwordInput.send_keys(self.password)
         loginButton =  webDriver.until(EC.presence_of_element_located((By.XPATH,'//button[contains(@data-test-id,"header-login-btn")]')))
         loginButton.click()
         cookieButton =  webDriver.until(EC.presence_of_element_located((By.XPATH,'//button[contains(@class,"c-bn")]')))
         cookieButton.click()
         time.sleep(5)
         self.driver.execute_script(self.script)
if __name__  ==  '__main__':
     nesineBot = NesineAutomation()
     nesineBot.nesineNeresine() 
       
       




        

         



