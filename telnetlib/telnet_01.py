from telnetlib import Telnet

tn = Telnet("192.168.10.1")

tn.write(b"admin\n")
tn.write(b"cisco\n")
tn.write(b"show ip int bri\n")
tn.write(b"exit\n")
print(tn.read_all().decode("ascii"))
