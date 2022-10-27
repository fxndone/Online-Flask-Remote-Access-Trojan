# Server installation

---

## Here are the few steps to install the server.

To install the flask app, you will need to run this commands on your dedicated server :

    curl https://raw.githubusercontent.com/fxndone/Online-Flask-Remote-Access-Trojan/main/server/install.py -o install.py
    python install.py

This will install everything which is needed to run your server.

When promped, enter a secure password you only know.

Then, edit the file `hackemall.py` on your attacker machine, and change the value of `PASSWORD` variable from "INSECURE_PASSWORD" to the password you entered.

A few files and directories should have appear.

To run your server, please run `python main.py`

A few infos should appear on your screen.

Get the URL shown, and try accessing it from another place (not your home wi-fi, for example, if you host the server at home).

If you're not able to access it, try searching for another url on the screen (for example, if you use replit, it should appear on your top right).

Once you have the URL, go to the `infect.py` and `infect.sh` scripts that should have appeared, and change the value of variable `URL` from `http://attacker.server:8080/` to the URL you have.

You will also need to do the same for `hackemall.py`.

Once done, be sure that your server will not go down, and enjoy the fact that everythink's all right !
