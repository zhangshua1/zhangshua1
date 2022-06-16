#！/usr/bin/python3.6
import socket
import argparse
import threading

parser = argparse.ArgumentParser()
parser.add_argument("-H", "--hostname", help="hostname or ip", required=True)
args = parser.parse_args()

threads = []
    
def portScanner(host,port):
    with socket.socket() as s:
        s.settimeout(0.1)
        if s.connect_ex((args.hostname, port)) == 0:
            print("%d open" %port)
def main(host):
    for p in range(1, 65535):
        t = threading.Thread(target=portScanner, args=(host, p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    main(args.hostname)
