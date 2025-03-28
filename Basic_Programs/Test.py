
from paramiko.client import SSHClient

client = SSHClient()
client.connect('sustaining-01', username='root', password='letmein')
client.close()