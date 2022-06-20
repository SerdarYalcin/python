from importlib.util import spec_from_file_location
from sys import stderr, stdout
from turtle import home
from paramiko import SSHClient, AutoAddPolicy
import getpass
import os
from threading import Timer

ask_pass = getpass.getpass()
pass_code = ask_pass
connect_ssh = SSHClient()
connect_ssh.set_missing_host_key_policy(AutoAddPolicy)
connect_ssh.connect(username='test', hostname='192.168.111.111', password=pass_code, port='22')

sft_client = connect_ssh.open_sftp()
sft_client.get('/home/test/password.key', 'password.key') # Downloading a file from remote machine
# sft_client.put('/home/ec2/file.txt', '/etc/ansible/group_vars/key.key')  Upload a file from local to remote

sft_client.close()
connect_ssh.close()
