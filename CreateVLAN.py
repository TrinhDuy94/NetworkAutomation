import getpass
import sys
import telnetlib

HOST = ""
user = input("enter username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf ter\n")

for n in range (2,10):
	tn.write(b"vlan "+str(n).encode('ascii')+b"\n")
	tn.write(b"name Py_VLAN_"+str(n).encode('ascii')+b"\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print (tn.read_all().decode('ascii'))