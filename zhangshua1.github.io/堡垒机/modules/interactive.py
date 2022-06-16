import os,sys
import socket
import termios
import tty
from datetime import datetime
from modules.table_init import *
from modules.db_conn import session

def interactive_shell(channel, login_user, share_user, server_ip):
    import select
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        channel.settimeout(0.0)

        cmd = ''

        tab_key = False
        while True:
            r, w, e = select.select([channel, sys.stdin], [], [])
            if channel in r:
                try:
                    x = channel.recv(1024).decode()
                    if tab_key:
                        if x not in ('\t','\r\n'):
                            cmd += x
                        tab_key = False
                    if len(x) == 0:
                        sys.stdout.write('\r\n*** EOF\r\n')
                        break
                    sys.stdout.write(x)
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                if '\r' != x:
                    cmd +=x
                if '\r' == x and len(cmd) > 0:
                    add_log = Cmd_log(login_user=login_user,
                            share_user=share_user,
                            server_ip=server_ip,
                            shell_command=cmd,
datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    session.add(add_log)
                    session.commit()
                    cmd = ''
                if '\t' == x:
                    tab_key = True
                channel.send(x)
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
    
