from transitions.extensions import GraphMachine

from utils import send_text_message,send_sticker_message,send_button_message
import random


user_ask='哈囉!媽咪\n想知道我最近在幹嘛嗎?\n趕快留言問我喔\n請輸入數字代號\n(1)三餐\n(2)在做什麼\n(3)什麼時候回來\n(4)花費'
eating_ask="想要問:(請輸入數字代號)\n(1)早餐吃什麼?\n(2)午餐吃什麼?\n(3)晚餐吃什麼?\n(4)最近吃什麼消夜嗎\n(5)返回"
life_ask="想要問:(請輸入數字代號)\n(1)現在在做什麼呢?\n(2)什麼時候回家呢?\n(3)最近有去哪裡玩嗎\n(4)返回"
cost_ask="想要問:(請輸入數字代號)\n(1)最近買了什麼嗎?\n(2)零用錢夠花嗎?\n(3)這個月打工賺多少錢?\n(4)返回"
school_ask="想要問:(請輸入數字代號)\n(1)作業寫的怎麼樣了\n(2)考試考得如何\n(3)學校生活如何\n(4)返回"
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_eating(self, event):
        text = event.message.text
        return text.lower() == "三餐" 
    def is_going_to_breakfast(self, event):
        text = event.message.text
        return text.lower() == "1" 
    def is_going_to_lunch(self, event):
        text = event.message.text
        return text.lower() == "2" 
    def is_going_to_dinner(self, event):
        text = event.message.text
        return text.lower() == "3" 
    def is_going_to_nightsnack(self, event):
        text = event.message.text
        return text.lower() == "4" 
    def is_going_to_exitEating(self, event):
        text = event.message.text
        return text.lower() == "5"
    #======================================================================
    def is_going_to_life(self, event):
        text = event.message.text
        return text.lower() == "生活" 
    def is_going_to_thing(self, event):
        text = event.message.text
        return text.lower() == "1" 
    def is_going_to_goHome(self, event):
        text = event.message.text
        return text.lower() == "2" 
    def is_going_to_entertainment(self, event):
        text = event.message.text
        return text.lower() == "3" 
    def is_going_to_exitLife(self, event):
        text = event.message.text
        return text.lower() == "4" 
    #======================================================================
    def is_going_to_cost(self, event):
        text = event.message.text
        return text.lower() == "花費" 
    def is_going_to_buying(self, event):
        text = event.message.text
        return text.lower() == "1" 
    def is_going_to_allowance(self, event):
        text = event.message.text
        return text.lower() == "2" 
    def is_going_to_parttime(self, event):
        text = event.message.text
        return text.lower() == "3" 
    def is_going_to_exitCost(self, event):
        text = event.message.text
        return text.lower() == "4" 
    #======================================================================
    def is_going_to_school(self, event):
        text = event.message.text
        return text.lower() == "課業" 
    def is_going_to_homework(self, event):
        text = event.message.text
        return text.lower() == "1" 
    def is_going_to_test(self, event):
        text = event.message.text
        return text.lower() == "2" 
    def is_going_to_school_life(self, event):
        text = event.message.text
        return text.lower() == "3" 
    def is_going_to_exitSchool(self, event):
        text = event.message.text
        return text.lower() == "4" 

    ######################################################################################
    def on_enter_user(self, event):
        print("I'm entering eating")
        reply_token = event.reply_token
        send_button_message(reply_token)
        #self.go_back() 

    def on_enter_eating(self, event):
        print("I'm entering eating")
        reply_token = event.reply_token
        send_text_message(reply_token,eating_ask)
        #self.go_back() 

    def on_enter_breakfast(self, event):
        eat=""
        r = random.randrange(1,5)
        if(r==1):eat='蛋餅加紅茶'
        if(r==2):eat='鮮奶加麥片'
        if(r==3):eat='咖啡配麵包'
        if(r==4):eat='睡太晚了沒有吃'
        if(r==5):eat='要趕著上課來不及吃'
        reply_token = event.reply_token
        #send_sticker_message(reply_token,1,2)
        send_text_message(reply_token, eat+"\n\n"+eating_ask)
        self.go_back_eating()
    def on_enter_lunch(self, event):
        eat=""
        r = random.randrange(1,5)
        if(r==1):eat='泡麵'
        if(r==2):eat='水煮餐'
        if(r==3):eat='人參雞粥'
        if(r==4):eat='牛肉湯'
        if(r==5):eat='自己煮飯'
        reply_token = event.reply_token
        #send_sticker_message(reply_token,1,2)
        send_text_message(reply_token, eat+"\n\n"+eating_ask)
        self.go_back_eating()   
    def on_enter_dinner(self, event):
        eat=""
        r = random.randrange(1,5)
        if(r==1):eat='泡麵'
        if(r==2):eat='水煮餐'
        if(r==3):eat='人參雞粥'
        if(r==4):eat='牛肉湯'
        if(r==5):eat='自己煮飯'
        reply_token = event.reply_token
        #send_sticker_message(reply_token,1,2)
        send_text_message(reply_token, eat+"\n\n"+eating_ask)
        self.go_back_eating()   
    
    def on_enter_nightsnack(self, event):
        eat=""
        r = random.randrange(1,5)
        if(r==1):eat='泡麵'
        if(r==2):eat='鹹酥雞'
        if(r==3):eat='我是不吃消夜的'
        if(r==4):eat='要減肥不能吃'
        if(r==5):eat='餅乾'
        reply_token = event.reply_token
        #send_sticker_message(reply_token,1,2)
        send_text_message(reply_token, eat+"\n\n"+eating_ask)
        self.go_back_eating()

    def on_enter_exitEating(self, event):
        reply_token = event.reply_token
        send_button_message(reply_token)
        #send_text_message(reply_token,user_ask)
        self.go_back()

    #===============================================================================
    def on_enter_life(self, event):
        print("I'm entering life")
        reply_token = event.reply_token
        send_text_message(reply_token,life_ask)
        #self.go_back() 

    def on_enter_thing(self, event):
        life=""
        r = random.randrange(1,5)
        if(r==1):life='睡覺'
        if(r==2):life='讀書'
        if(r==3):life='寫作業'
        if(r==4):life='思考人生'
        if(r==5):life='不想努力'
        reply_token = event.reply_token
        #send_button_message(reply_token)
        send_text_message(reply_token, life+"\n\n"+life_ask)
        #send_button_message(reply_token)
        self.go_back_life()

    def on_enter_goHome(self, event):
        life=""
        r = random.randrange(1,5)
        if(r==1):life='現在'
        if(r==2):life='明天'
        if(r==3):life='這是個好問題喔'
        if(r==4):life='不知道'
        if(r==5):life='作業寫完就回去'
        reply_token = event.reply_token
        send_text_message(reply_token, life+"\n\n"+life_ask)
        #send_button_message(reply_token)
        self.go_back_life()
    
    def on_enter_entertainment(self, event):
        life=""
        r = random.randrange(1,4)
        if(r==1):life='看電影'
        if(r==2):life='去奇美博物館看展覽'
        if(r==3):life='好累不想出門'
        if(r==4):life='去百貨公司逛街'
        reply_token = event.reply_token
        #send_button_message(reply_token)
        send_text_message(reply_token, life+"\n\n"+life_ask)
        self.go_back_life()
    
    def on_enter_exitLife(self, event):
        print("I'm entering exitLife")
        reply_token = event.reply_token
        send_button_message(reply_token)
        #send_text_message(reply_token,user_ask)
        self.go_back()

    #=====================================================================================================
    def on_enter_cost(self, event):
        print("I'm entering cost")
        reply_token = event.reply_token
        send_text_message(reply_token,cost_ask)
        #self.go_back() 
    def on_enter_buying(self, event):
        cost=""
        r = random.randrange(1,3)
        if(r==1):cost="買衣服"
        if(r==2):cost="沒有買東西"
        if(r==3):cost="買了一雙鞋子"
        reply_token = event.reply_token
        send_text_message(reply_token,cost+"\n\n"+cost_ask)
        self.go_back_cost()

    def on_enter_allowance(self, event):
        print("I'm entering allowance")
        cost="永遠都不嫌多嘻嘻嘻"
        reply_token = event.reply_token
        send_text_message(reply_token,cost+"\n\n"+cost_ask)
        self.go_back_cost()

    def on_enter_parttime(self, event):
        print("I'm entering parttime")
        cost=""
        r = random.randrange(1,3)
        if(r==1):cost='這個月不想努力，沒有賺錢'
        if(r==2):cost='不跟你說'
        if(r==3):cost='賺了5000塊，吃5次海底撈，所以沒錢了嗚嗚'
        reply_token = event.reply_token
        send_text_message(reply_token,cost+"\n\n"+cost_ask)
        self.go_back_cost()
        
    def on_enter_exitCost(self, event):
        print("I'm entering exitCost")
        reply_token = event.reply_token
        send_button_message(reply_token)
        #send_text_message(reply_token,user_ask)
        self.go_back()
    #==========================================================================================
    def on_enter_school(self, event):
        print("I'm entering school")
        reply_token = event.reply_token
        send_text_message(reply_token,school_ask)
        #self.go_back() 
    def on_enter_homework(self, event):
        school=""
        r = random.randrange(1,4)
        if(r==1):school="寫不完"
        if(r==2):school="時間到了自然就會寫完了"
        if(r==3):school="早就寫完了"
        if(r==4):school="想要有人幫"
        reply_token = event.reply_token
        send_text_message(reply_token,school+"\n\n"+school_ask)
        self.go_back_school()

    def on_enter_test(self, event):
        print("I'm entering test")
        r = random.randrange(1,4)
        if(r==1):school="難過的事就別提了"
        if(r==2):school="不想面對"
        if(r==3):school="不跟你說"
        if(r==4):school="還沒考試耶"
        reply_token = event.reply_token
        send_text_message(reply_token,school+"\n\n"+school_ask)
        self.go_back_school()
    
    def on_enter_school_life(self, event):
        print("I'm entering school_life")
        r = random.randrange(1,4)
        if(r==1):school="好累喔不想努力了"
        if(r==2):school="最近常常睡過頭自動停課"
        if(r==3):school="學校好遠不想去上學"
        if(r==4):school="學校附近好吃的店越來越少了"
        reply_token = event.reply_token
        send_text_message(reply_token,school+"\n\n"+school_ask)
        self.go_back_school()
        
    def on_enter_exitSchool(self, event):
        print("I'm entering exitSchool")
        reply_token = event.reply_token
        send_button_message(reply_token)
        #send_text_message(reply_token,user_ask)
        self.go_back()