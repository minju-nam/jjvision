# 전주비전대 Project 

## Install DHT11 sensor 
```
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install
cd Adafruit_Python_DHT/examples 
```
  - run
  ```
  python AdafruitDHT.py 11 4 
  ```
## 1초에 한 번씩 뜨게 하려면
```
1초에 한 번씩 온도와 습도가 나오게 하고 싶으면 vim simpletest.py 입력 후 코드를 수정한다 (pin번호, 센서 번호, 위에 import time을 넣어주고 밑에 코드를 첫 줄에 while(true):, 마지막 줄에 time.sleep(1)를 삽입해준다 (들여쓰기 필수)
```
## InfluxDB installation

## 1. Repository의 GPG key를 더하기
```
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
```
## 2. Repository를 더하기
```
echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
```
## 3. 프로그램 설치
```
sudo apt update
sudo apt install influxdb
```
## 4. 프로그램 실행
```
sudo service influxdb start
```
## 5. 데이터 베이스 만들기
```
>create database 데이터베이스이름(본인: mindata)
```
## 6. 데이터 베이스 확인 명령 
```
>show databases
```
# Grafana Installation

## 1. Repository의 GPG key를 더하기
```
curl https://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -
```
## 2. Repository를 더하기
```
echo "deb https://dl.bintray.com/fg2it/deb stretch main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```
## 3. 프로그램 설치
```
sudo apt update
sudo apt install grafana
```
## 4. 프로그램 실행
```
sudo service grafana-server start
```
# influxdb import with python
```
sudo pip install influxdb
```
# gpio pin map
```
cd /tmp
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
```
## 기타 지식
```
22번 포트는 ssh 접속을 허락해 주는 포트
.vimrc(설정 파일)

vim 설정에서 자주 쓰이는 것(vim설정 들어가는 법=vim .vimrc)
set number = 번호 표시
set ai = auto indent
set si = smart indent
set cindent = c style indent
set shiftwidth=4 = 자동 공백 채움 시 4칸
set tabstop=4 = tab을 4칸 공백으로
set ignorecase = 검색 시 대소문자 무시
set hlsearch = 검색 시 하이라이트
set nocompatible = 방향키로 이동 가능
set fileencodings=utf-8,euc-kr = 파일 저장 인코딩 : utf-8, euc-kr
set fencs=ucs-bom,utf-8,euc-kr = 한글 파일은 euc-kr, 유니코드는 유니코드
set bs=indent,eol,start = backspace 사용가능
set ruler = 상태 표시줄에 커서 위치 표시
set title = 제목 표시
set showmatch = 다른 코딩 프로그램처럼 매칭되는 괄호 보여줌
set wmnu = tab 을 눌렀을 때 자동완성 가능한 목록
syntax on = 문법 하이라이트 on
filetype indent on = 파일 종류에 따른 구문 강조
set mouse=a = 커서 이동을 마우스로 가능하도록

<python 명령어>
set softtabstop=4 = Tab 키를 눌렀을 때 4개 space로
set bg=dark
set expandtab = 탭을 스페이스로 바꾸는 설정
let python_version_2=1 = python 2 문법을 따름(플러그 인)
let pythin_highlight_all=1 = 모든 강조(색상) on
filetype indent plugin on
```
## pir 센서 감지 vim 설정 코드
```
  1 #1/usr/bin/python
  2
  3 import time
  4 import RPi.GPIO as GPIO
  5
  6 print GPIO.VERSION
  7 GPIO.setmode(GPIO.BCM)
  8 GPIO.setup(4,GPIO.IN)
  9
 10 def interrupt_fired(channel):
 11     print("interrupt Fired")
 12     print(channel)
 13
 14 GPIO.add_event_detect(4,GPIO.FALLING, callback=interrupt_fired)
 15
 16 while(True):
 17     time.sleep(1)
 18     print("timer fired")
 19
```

