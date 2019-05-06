import socket
import argparse

def run_server(port=4000):
    host = ""

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)

        conn, addr = s.accept()
        msg = conn.recv(1024)           ##클라이언트로부터 받은 데이터.
        msg = msg.decode()
        print("입력받은 문자열 : %s" %msg)

        msg = msg[::-1]                 ##문자열을 뒤집어서 저장.

        conn.sendall(msg.encode())               ##클라이언트로 전송.
        print("전송한 문자열 : %s" %msg)

        conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo server -p port")
    parser.add_argument("-p", help="port_number", required=True)

    args = parser.parse_args()
    run_server(port=int(args.p))