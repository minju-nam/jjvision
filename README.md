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
