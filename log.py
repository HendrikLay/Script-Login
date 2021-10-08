from getpass import getpass
import os
import time
		
def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36m<=================\033[1;37m{\033[1;34mBLACK-CYBER-HENDRIK\033[1;37m}\033[1;36m=================> ')
           print('')
           os.system('date | lolcat')
           print("\033[1;93m")
           print(" \033[1;34m<<<<<<<<<<<<<<<<\033[1;37m{\033[1;36mWELCOME-MASTER-HENDRIK\033[1;37m}\033[1;34m>>>>>>>>>>>>>>>>")
           print("\033[1;93m")
           print("\033[1;36m<~~~~~~~~~~~~~~~~~~~~~\033[1;37m[\033[1;34mLOGIN MASTER\033[1;37m]\033[1;36m~~~~~~~~~~~~~~~~~~~~~>")
           print("")
           try:
                x = str(input('\033[1;34mUsername \033[1;93m: '))
                print("")
                e = getpass('\033[1;36mPassword \033[1;93m: ')
                print ("")
                if x=="Hendrik" and e=="Hendrik09":
                   print('Waiting...')
                   time.sleep(2)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + x + ' | lolcat')
                   time.sleep(2)
                   print('\033[1;92m ────────────────────────────────────── ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Error Password")
                      time.sleep(2)
                      print("")
           except Exception:

                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Error Password")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Error Password")
                      time.sleep(2)
menu()
