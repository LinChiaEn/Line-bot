# TOC Project 2020

[![Maintainability](https://api.codeclimate.com/v1/badges/dc7fa47fcd809b99d087/maintainability)](https://codeclimate.com/github/NCKU-CCS/TOC-Project-2020/maintainability)

[![Known Vulnerabilities](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020/badge.svg)](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020)


Template Code for TOC Project 2020

A Line bot based on a finite state machine

More details in the [Slides](https://hackmd.io/@TTW/ToC-2019-Project#) and [FAQ](https://hackmd.io/s/B1Xw7E8kN)

## Setup

### Prerequisite
* Python 3.6
* Pipenv
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)
	* [Note: macOS Install error](https://github.com/pygraphviz/pygraphviz/issues/100)


#### Secret Data
You should generate a `.env` file to set Environment Variables refer to our `.env.sample`.
`LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

#### a. Ngrok installation
* [ macOS, Windows, Linux](https://ngrok.com/download)

or you can use Homebrew (MAC)
```sh
brew cask install ngrok
```

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

#### b. Servo

Or You can use [servo](http://serveo.net/) to expose local servers to the internet.


## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"

## Deploy
Setting to deploy webhooks on Heroku.

### Heroku CLI installation

* [macOS, Windows](https://devcenter.heroku.com/articles/heroku-cli)

or you can use Homebrew (MAC)
```sh
brew tap heroku/brew && brew install heroku
```

or you can use Snap (Ubuntu 16+)
```sh
sudo snap install --classic heroku
```

### Connect to Heroku

1. Register Heroku: https://signup.heroku.com

2. Create Heroku project from website

3. CLI Login

	`heroku login`

### Upload project to Heroku

1. Add local project to Heroku project

	heroku git:remote -a {HEROKU_APP_NAME}

2. Upload project

	```
	git add .
	git commit -m "Add code"
	git push -f heroku master
	```

3. Set Environment - Line Messaging API Secret Keys

	```
	heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
	heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
	```

4. Your Project is now running on Heroku!

	url: `{HEROKU_APP_NAME}.herokuapp.com/callback`

	debug command: `heroku logs --tail --app {HEROKU_APP_NAME}`

5. If fail with `pygraphviz` install errors

	run commands below can solve the problems
	```
	heroku buildpacks:set heroku/python
	heroku buildpacks:add --index 1 heroku-community/apt
	```

	refference: https://hackmd.io/@ccw/B1Xw7E8kN?type=view#Q2-如何在-Heroku-使用-pygraphviz

## Reference
[Pipenv](https://medium.com/@chihsuan/pipenv-更簡單-更快速的-python-套件管理工具-135a47e504f4) ❤️ [@chihsuan](https://github.com/chihsuan)

[TOC-Project-2019](https://github.com/winonecheng/TOC-Project-2019) ❤️ [@winonecheng](https://github.com/winonecheng)

Flask Architecture ❤️ [@Sirius207](https://github.com/Sirius207)

[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)

# NNChatBot

## 前言
在外讀書，媽媽常會透過line的方式關心我的生活，但其實有時候會因為忙碌忘記回復訊息，藉由這個聊天機器人，可以讓媽媽有和女兒聊天的感覺。

## 構想
先藉由使用者點選主題選項後，須入問題代號，再依據提問的問題回答。

## 環境
- window 10
- python 3.6


## 使用說明
- 基本操作
    - 點選按鈕
    - 須入問題數字代號
    - 輸入返回的數字代號，回到按鈕選單
- 架構圖
    1. 點選按鈕進入主題
    2. 輸入問題的數字代號
    3. 回覆問題
    4. 輸入返回數字代號

## 使用示範
### 輸入個人資訊
![](https://i.imgur.com/RAXRooY.jpg)
![](https://i.imgur.com/3VkDy82.jpg)
![](https://i.imgur.com/JhK01qT.jpg)
![](https://i.imgur.com/OCsoSBk.jpg)
### 增肌
![](https://i.imgur.com/OodsURE.jpg)
![](https://i.imgur.com/95lZAGO.jpg)
![](https://i.imgur.com/DOj8yEs.jpg)
![](https://i.imgur.com/bgeHzOf.jpg)
![](https://i.imgur.com/R2vy5FN.jpg)
![](https://i.imgur.com/TfHJx3t.jpg)
![](https://i.imgur.com/6ZEIZzI.jpg)
![](https://i.imgur.com/2iNuLe8.jpg)
### 減脂(生酮飲食)
![](https://i.imgur.com/Aej3bXd.jpg)
![](https://i.imgur.com/shzYGJD.jpg)
![](https://i.imgur.com/nxUfsPP.jpg)
![](https://i.imgur.com/pvibAF1.jpg)
![](https://i.imgur.com/xqbqg5A.jpg)
![](https://i.imgur.com/hsoAJeE.jpg)
![](https://i.imgur.com/7KyAzOK.jpg)
### 隨時畫FSM
![](https://i.imgur.com/kk8b9aa.jpg)
### 聊天機器人
![](https://i.imgur.com/co5NtdJ.jpg)
![](https://i.imgur.com/v0uG700.jpg)


## FSM
![](https://github.com/LinChiaEn/Line-bot/blob/master/fsm.png)
### state說明
- user: 點選按鈕進入主題
- eating: 詢問(1)早餐吃什麼?(2)午餐吃什麼?(3)晚餐吃什麼?(4)最近吃什麼消夜嗎(5)返回
- life: 詢問(1)現在在做什麼呢?(2)什麼時候回家呢?(3)最近有去哪裡玩嗎(4)返回
- cost: 詢問(1)最近買了什麼嗎?(2)零用錢夠花嗎?(3)這個月打工賺多少錢?(4)返回
- school: 詢問(1)作業寫的怎麼樣了(2)考試考得如何(3)學校生活如何(4)返回
- breakfast: 回復早餐吃什麼
- linch: 回復午餐吃什麼
- dinner: 回復晚餐吃什麼
- nightsnack: 回復最近吃什麼消夜
- exitEating: 返回到詢問(1)早餐吃什麼?(2)午餐吃什麼?(3)晚餐吃什麼?(4)最近吃什麼消夜嗎(5)返回
- thing: 回復現在在做什麼
- goHome: 回復什麼時候回家
- entertainment: 回復最近有去哪裡玩
- exitLife: 返回到詢問(1)現在在做什麼呢?(2)什麼時候回家呢?(3)最近有去哪裡玩嗎(4)返回
- allowance: 回復最近買了什麼
- buying: 回復零用錢是否夠花
- parttime:回復這個月打工賺多少錢
- exitCost:返回到詢問(1)最近買了什麼嗎?(2)零用錢夠花嗎?(3)這個月打工賺多少錢?(4)返回
- test:回復作業寫的怎麼樣
- homework:回復考試考得如何
- school_life:回復學校生活
- exitSchool:返回到詢問(1)作業寫的怎麼樣了(2)考試考得如何(3)學校生活如何(4)返回
