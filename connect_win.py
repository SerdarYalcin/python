from getpass import getpass
from telnetlib import SE
from xmlrpc.client import Transport
from requests import Session
import winrm
import getpass
import getpass
from pprint import pprint
import shutil

ask_passwd = getpass.getpass("Enter Password:")
pass_code =  ask_passwd
s = winrm.Session('192.168.100.155', auth= ('test1', pass_code), transport= 'ntlm')
run_command = s.run_cmd('powershell', ['Get-Service'])

print (f"The status is: {run_command.status_code}")
pprint (f" The status 2: {run_command.std_out}")

original = r'C:\Users\Administrator\Desktop\New folder\asd.txt'
target = r'C:\Users\Ron\Desktop\products.txt'

shutil.copyfile(original, target)
