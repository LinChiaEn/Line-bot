import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message,push_button_message

load_dotenv()


machine = TocMachine(
    states=["user", "goHome","thing",
            "eating","breakfast", "lunch","dinner","nightsnack","exitEating",
            "life","thing","goHome","entertainment","exitLife",
            "cost","buying","allowance","parttime","exitCost",
            "school","homework","test","school_life","exitSchool"
            ],
    #如果condition return true=>goto dest
    transitions=[
        {"trigger": "advance","source": "user","dest": "eating","conditions": "is_going_to_eating",},
        {"trigger": "advance","source": "eating","dest": "breakfast","conditions": "is_going_to_breakfast",},
        {"trigger": "advance","source": "eating","dest": "lunch","conditions": "is_going_to_lunch",},
        {"trigger": "advance","source": "eating","dest": "dinner","conditions": "is_going_to_dinner",},
        {"trigger": "advance","source": "eating","dest": "nightsnack","conditions": "is_going_to_nightsnack",},
        {"trigger": "advance","source": "eating","dest": "exitEating","conditions": "is_going_to_exitEating",},
        #======================================================================================================
        {"trigger": "advance","source": "user","dest": "life","conditions": "is_going_to_life",},
        {"trigger": "advance","source": "life","dest": "thing","conditions": "is_going_to_thing",},
        {"trigger": "advance","source": "life","dest": "goHome","conditions": "is_going_to_goHome",},
        {"trigger": "advance","source": "life","dest": "entertainment","conditions": "is_going_to_entertainment",},
        {"trigger": "advance","source": "life","dest": "exitLife","conditions": "is_going_to_exitLife",},
        #======================================================================================================
        {"trigger": "advance","source": "user","dest": "cost","conditions": "is_going_to_cost",},
        {"trigger": "advance","source": "cost","dest": "buying","conditions": "is_going_to_buying",},
        {"trigger": "advance","source": "cost","dest": "allowance","conditions": "is_going_to_allowance",},
        {"trigger": "advance","source": "cost","dest": "parttime","conditions": "is_going_to_parttime",},
        {"trigger": "advance","source": "cost","dest": "exitCost","conditions": "is_going_to_exitCost",},
        #################################################################################################
        {"trigger": "advance","source": "user","dest": "school","conditions": "is_going_to_school",},
        {"trigger": "advance","source": "school","dest": "homework","conditions": "is_going_to_homework",},
        {"trigger": "advance","source": "school","dest": "test","conditions": "is_going_to_test",},
        {"trigger": "advance","source": "school","dest": "school_life","conditions": "is_going_to_school_life",},
        {"trigger": "advance","source": "school","dest": "exitSchool","conditions": "is_going_to_exitSchool",},
        #################################################################################################
        {"trigger": "go_back", "source": ["goHome","thing",
            "eating","breakfast", "lunch","dinner","nightsnack","exitEating",
            "life","thing","goHome","entertainment","exitLife",
            "cost","buying","allowance","parttime","exitCost",
            "school","homework","test","school_life","exitSchool"], "dest": "user"},
        {"trigger": "go_back_eating", "source": ["breakfast","lunch","dinner","nightsnack"], "dest": "eating"},
        {"trigger": "go_back_life", "source": ["thing","goHome","entertainment"], "dest": "life"},
        {"trigger": "go_back_cost", "source": ["buying","allowance","parttime"], "dest": "cost"},
        {"trigger": "go_back_school", "source": ["homework","test","school_life"], "dest": "school"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)



@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )
        

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)   #每次while便會呼叫advance()
        if response == False:
            send_text_message(event.reply_token, "輸入錯誤，請重新輸入")
            #machine.go_back()


    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
