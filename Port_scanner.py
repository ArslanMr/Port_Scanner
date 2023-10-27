import socket
import sys
import threading

usage = "python port_scanner.py Target_IP [Start_Port] [End_Port]"

print("*" * 100)
print("Port Scanner")

if len(sys.argv) < 2:
    print(usage)
    sys.exit()

target = sys.argv[1]  # Get the target IP as the first argument

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Error: Invalid target IP or hostname")
    sys.exit()

# Set default port range (1 to 65535) if not provided by the user
start_port = 1
end_port = 65535

if len(sys.argv) >= 3:
    start_port = int(sys.argv[2])

if len(sys.argv) == 4:
    end_port = int(sys.argv[3])

print("Scanning Target:", target_ip)

print("*" * 100)

print("{:<7} {:<20} {:<10}".format("Port", "Service", "Status"))

def scan_tcp_port(port):
    try:
        service = socket.getservbyport(port)
    except OSError:
        service = "Unknown"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target_ip, port))
    if not conn:
        print("{:<7} {:<20} {:<10}".format(f"{port}/TCP", service, "Open"))
    s.close()

def scan_udp_port(port):
    try:
        service = socket.getservbyport(port, "udp")
    except OSError:
        service = "Unknown"

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.settimeout(2)
    udp_socket.sendto(b'Test Data', (target_ip, port))

    try:
        data, addr = udp_socket.recvfrom(1024)
        if data:
            print("{:<7} {:<20} {:<10}".format(f"{port}/UDP", service, "Open"))
            print("Received Data:", data.decode('utf-8'))
    except socket.timeout:
        pass
    udp_socket.close()

for port in range(start_port, end_port + 1):
    thread_tcp = threading.Thread(target=scan_tcp_port, args=(port,))
    thread_udp = threading.Thread(target=scan_udp_port, args=(port,))
    thread_tcp.start()
    thread_udp.start()
