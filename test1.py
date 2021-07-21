import getpass
import sys
import telnetlib

HOST = ""
user = input("enter username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
	tn.read_until("Password: ")
	tn.write(password + "\n")

tn.write("conf ter\n")

for n in range (2,10):
	tn.write("vlan "+str(n)+"\n")
	tn.write("name Py_VLAN_"+str(n)+"\n")

tn.write("end\n")
tn.write("exit\n")

print tn.read_all()