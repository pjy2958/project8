import socket
import argparse

def run(host, port, string):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("입력한 문자열 : %s" %string)

        s.sendall(string.encode())              ##입력한 문자열 서버로 전송.

        resp = s.recv(1024)                     ##서버로부터 받은 데이터.
        print("서버로부터 받은 문자열 : %s" %resp.decode())

        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Echo client -p port -i host -s string")
    parser.add_argument("-p", help="port_number", required=True)
    parser.add_argument("-i", help="host_name", required=True)
    parser.add_argument("-s", help="send_string")

    args = parser.parse_args()
    run(host=args.i, port=int(args.p), string=args.s)