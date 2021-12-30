from transitions.extensions import GraphMachine

from utils import send_text_message
import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "1" 

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "2"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "3" 


    def on_enter_state1(self, event):
        print("I'm entering state1")
        eat=""
        r = random.randrange(1,5)
        if(r==1):eat='泡麵'
        if(r==2):eat='水煮餐'
        if(r==3):eat='人參雞粥'
        if(r==4):eat='牛肉湯'
        if(r==5):eat='自己煮飯'
        reply_token = event.reply_token
        send_text_message(reply_token, eat)
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        thing=""
        r = random.randrange(1,5)
        if(r==1):thing='睡覺'
        if(r==2):thing='讀書'
        if(r==3):thing='寫作業'
        if(r==4):thing='思考人生'
        if(r==5):thing='不想努力'

        reply_token = event.reply_token
        send_text_message(reply_token, thing)
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
    
    def on_enter_state3(self, event):
        goHome=""
        r = random.randrange(1,5)
        if(r==1):goHome='現在'
        if(r==2):goHome='明天'
        if(r==3):goHome='這是個好問題喔'
        if(r==4):goHome='不知道'
        if(r==5):goHome='作業寫完就回去'

        reply_token = event.reply_token
        send_text_message(reply_token, goHome)
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")
