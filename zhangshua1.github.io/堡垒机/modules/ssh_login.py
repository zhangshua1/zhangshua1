import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import paramiko
from modules.interactive import interactive_shell

def ssh_login(login_user, share_user, server_ip, server_port, password):
    ssh=paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_ip, server_port, share_user, password)

    channel=ssh.invoke_shell()

    interactive_shell(channel, login_user, share_user, server_ip)

    channel.close()
    ssh.close()

if __name__ == "__main__":
    login_user = "xiaoming"
    share_user = "user2"
    password = "123456"
    server_ip = "192.168.107.109"
    server_port = 22
    ssh_login(login_user, share_user, server_ip, server_port, password)
    