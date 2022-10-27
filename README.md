# Online Flask Remote Access Trojan

---

## Overview

Online Flask Remote Access Trojan (O.F.R.A.T. for short) is a remote access trojan designed to be used over internet.

Using an easy-to-setup flask server and some tools like ngrok, this tool will let you access any controlled device from anywhere.

---

## Usage

To install this tool, you will need to follow this steps :

- First of all, get a remote server which can be bound on the internet (I personaly apreciate using both [Replit](https://replit.com/) and [UptimeRobot](https://uptimerobot.com/) (there is not sponsored, only personal opinion)).
- Next, install the flask server on this machine :
  - See [this](https://github.com/fxndone/Online-Flask-Remote-Access-Trojan/blob/main/server/README.md) README file and folow the instructions on your server.
- Then, you'll need to infect targets !
  - To do this, get the [infect.py](https://github.com/fxndone/Online-Flask-Remote-Access-Trojan/blob/main/server/infect.py) (you can change the name (not the extension (or to .pyw) !), and/or compile it using PyInstaller, cx_freeze...) script and execute it on target's machine.
  - Once a target opened this script, it is "permanent" :
    - Every time the target reboot, the script restart
    - It's hidden on target system, so removing it, is hard
    - You can remove it by executing [deletme.py](https://fxndone/Online-Flask-Remote-Access-Trojan/blob/main/deletme.py) on target system.
  - Once a target has been infected, it should apear as present on the main system (it will be explained later).
- Once you infected targets, you will be able to control them :
  - Using the script [hackemall.py](https://github.com/fxndone/Online-Flask-Remote-Access-Trojan/blob/main/hackemall.py), you will be able to see all targets, and send them a reverse host.
  - To get a shell, choose your target on [hackemall.py](https://github.com/fxndone/Online-Flask-Remote-Access-Trojan/blob/main/hackemall.py), run `nc -lvnp {your_port}` and send him a couple "reverse_host" "your_port".
  - For the last point, you can use ngrok to get shell over internet :
    - See [here](https://ngrok.com/download), create an account and login on your machine (see [here](https://dashboard.ngrok.com/get-started/setup)), and then, run `ngrok tcp {your_port}`.
    - Send the reverse_host and port shown on the ngrok command.

### WARNING

When using Repl.IT, move from https to http on everything, I don't know why, but currently https isn't supported.

---

## Disclaimer

DO NOT use this tool for any illegal purpose, and be suuuuuure you have permissions before using it

This tool is for educational purpose, fun, and pentesting ONLY.

I'ME NOT RESPONSIBLE for any sh*t you could do with it !!!

---

## TODO

- Add a way to controle targets only over http(s) with flask.
- Improve README files (they are just not looking great).
- Use it to troll friends (forgot I did not have friends (lool, I'me joking, but you should think about going to the shower ;) )).
