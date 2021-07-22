import paramiko
import time

ip_add = ""
username = "admin"
password = "123456"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_add,username=username,password=password)

print("Successful SSH Connection "+ip_add)
remote_connection = ssh_client.invoke_shell()

remote_connection.send("conf ter\n")
remote_connection.send("vlan 2\n")
remote_connection.send("name IT\n")
remote_connection.send("exit\n")

time.sleep(1)
output = remote_connection.recv(65535)
print(output)
ssh_client.close