import random, requests, threading, time, os, colorama

colorama.init(convert=True)

threads = int(input('How many threads: '))

def withproxy():
  print('Wait...')
  time.sleep(1)
  time.sleep(2)
  print("Starting please wait while we generate a code and check it")
  with open('proxies.txt', 'r') as proxies:
    for line in proxies:
      proxy = line.rstrip('\n')
  proxy = proxy  
  while True:
    code = ''.join(random.choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890") for x in range(14))
    url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    r = requests.get(url, proxies={ 'http': proxy, 'https': proxy}, headers={    'User-Agent': 'Chrome'    })
    if r.status_code == 204:
       print(colorama.Fore.GREEN+f"{code} is Valid")
       file = open('valid.txt', 'a')
       file.write(f'{code}\n')
    else:
        print(colorama.Fore.RED+f'{code} is invalid')
        file = open('invalid.txt', 'a')
        file.write(f'{code}\n')

    threads = 0

    for _ in range(threads):
        t = threading.Thread(target=withproxy, args=None)
        t.start()
        threads.append(t)

    for thread in threads:
      thread.join()

def normalmode():
  while True:
    code = ''.join(random.choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890") for x in range(14))
    url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    r = requests.get(url, headers={    'User-Agent': 'Chrome'    })
    if r.status_code == 204: # not sure if this is the right status code might be 200
       print(colorama.Fore.GREEN+f"{code} is Valid")
       file = open('valid.txt', 'a')
       file.write(f'{code}\n')
    else:
        print(colorama.Fore.RED+f'{code} is invalid')
        file = open('invalid.txt', 'a')
        file.write(f'{code}\n')

    threads = 0

    for _ in range(threads):
        t = threading.Thread(target=withproxy, args=None)
        t.start()
        threads.append(t)

    

if __name__ == '__main__':
   print("""
 ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████       ▄████ ▓█████  ███▄    █ 
 ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░      ░   ░  ░ ░  ░░ ░░   ░ ▒░
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒     ░ ░   ░    ░      ░   ░ ░ 
         ░  ░              ░         ░ ░           ░    ░  ░         ░ 
                                                                       
 ▄▄▄       ███▄    █ ▓█████▄                                           
▒████▄     ██ ▀█   █ ▒██▀ ██▌                                          
▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌                                          
░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌                                          
 ▓█   ▓██▒▒██░   ▓██░░▒████▓                                           
 ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒                                           
  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒                                           
  ░   ▒      ░   ░ ░  ░ ░  ░                                           
      ░  ░         ░    ░                                              
                      ░                                                
 ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███                 
▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒               
▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒               
▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄                 
▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒               
░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░               
  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░               
░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░                
░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░                    
░                       ░                                              
""")
   yes = ['ye', 'yes', 'sure', 'ok', 'yeah', 'Yes', 'Ye', 'Sure', 'Ok', 'OK', 'Yeah', 'y', 'Y']
   no = ['nah', 'no', 'nope', 'never', 'n', 'N', 'Nah', 'No', 'Never', 'Nope']
   question = input("Proxy support?: ")
   if question in yes:
      file = open('proxies.txt', 'a')
      file.write('Put your proxies here')
      print('Put your proxies in the new created file called proxies.txt: ')
      question2 = input('Have you put your proxies?: : ')
      if question2 in yes:
         withproxy()
      if question2 in no:
         exit()     
   if question in no:
      normalmode()
   else:
      os.system('python main.py')

