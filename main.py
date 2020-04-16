from selenium import webdriver
from time import sleep
import pdb
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
        sorted_not_following_back = [user for user in self.not_following_back if self.num_followers(user) >= amount]
        return sorted_not_following_back

    def num_followers(self, username):
        self.driver.get("https://instagram.com/" + username)
        sleep(2)
        abos = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        abo_number = abos.title #get_attribute("title")
        print(abo_number)
        abo_number = abo_number.replace(".", "")
        #abo_number = abo_number.replace("k", "000")
        #abo_number = abo_number.replace("m", "000000")
        #return int(abo_number)
        



my_bot = InstaBot('philip_singer', "12Flohkistei")
#my_bot.get_unfollowers()
#print(my_bot.sorting(2000))
my_bot.num_followers("offenegesellschaft")
