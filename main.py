from selenium import webdriver
from time import sleep
import pdb
import sys
#from secrets import pw


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Firefox()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
        #     .click()
        # sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        # sleep(4)
        while True:
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Jetzt nicht')]")\
                .click()
            except:
                continue
            break
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        print("aboniert")
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        print("Abonnenten")
        followers = self._get_names()
        self.not_following_back = [user for user in following if user not in followers]
        return (self.not_following_back)

    def _get_names(self):
        sleep(2)
        # not necessairy anymore
        #sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        #self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names

    def sorting(self, amount):
        sorted_not_following_back = [user for user in self.not_following_back if self.num_followers(user) <= amount]
        return sorted_not_following_back

    def num_followers(self, username):
        self.driver.get("https://instagram.com/" + username)
        while True:
            try:
                # You have to click first before you can access the desired element with the title
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        
                abo_number = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").\
                    get_attribute("title")
            except:
                continue
            break
        abo_number = abo_number.replace(".", "")
        return int(abo_number)
    
    def true_follower(self):
        # definitively not finished
        friends = []
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/p/')]")\
            .click()
        # while True:
        #     try:
        #         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a")\
        #             .click()
        #     except:
        #         print("Error:", sys.exc_info()[0])
        #         continue
        #     break

        def spam(self):
            # definitively not finished
            self.driver.get("https://www.instagram.com/direct/inbox/")
            sleep(2)
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Anfrage')]")\
                .click()
                print("Es gibt Anfragen")
            except:
                print("Keine Anfrage")
            else:
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div/a")\
                    .click()
                
                


        
        
my_bot = InstaBot('philip_singer', "12Flohkistei")
#my_bot.get_unfollowers()
#print(my_bot.sorting(2000))
my_bot.true_follower()
