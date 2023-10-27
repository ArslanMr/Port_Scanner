# Port Scanner

## Overview

This is a Python script for a simple port scanner that can be used to scan open TCP and UDP ports on a target host. The script takes the target IP address, start port, and end port as command-line arguments and scans for open ports within the specified range. It uses multithreading to speed up the scanning process.

## Usage

To use the port scanner, follow these steps:

1. Make sure you have Python installed on your system.

2. Open a terminal or command prompt.

3. Run the script with the following command:

   ```
   python port_scanner.py Target_IP [Start_Port] [End_Port]
   ```

   - `Target_IP` is the IP address or hostname of the target you want to scan for open ports.
   - `Start_Port` (optional) is the first port in the range you want to scan (default is 1).
   - `End_Port` (optional) is the last port in the range you want to scan (default is 65535).

   Example usage:
   
   ```
   python port_scanner.py example.com 80 100
   ```

4. The script will initiate the port scanning process and display the results on the screen.

## How it Works

The script performs the following steps:

1. It resolves the target hostname or IP address using `socket.gethostbyname()`.

2. It creates threads to scan for both TCP and UDP ports within the specified range.

3. For each port in the range, it attempts to establish a TCP connection using `socket.AF_INET` and `socket.SOCK_STREAM`. If the connection is successful, it reports the port as "Open."

4. For UDP ports, it sends a test UDP packet and waits for a response. If it receives a response, it reports the port as "Open" and displays the received data.

## Output

The script provides output in the following format:

```
Port    Service              Status    
80/TCP  http                 Open
53/UDP  domain               Open
```

- "Port" is the port number and its protocol (TCP or UDP).
- "Service" is the service associated with the port.
- "Status" indicates whether the port is open or closed.

## Error Handling

The script handles errors, such as an invalid target IP or hostname, by providing appropriate error messages.

## Note

This script is intended for educational purposes and should only be used with the appropriate permissions. Unauthorized scanning of ports on remote hosts may violate the law and ethical guidelines. Always ensure that you have the necessary permissions before scanning a target.

Please use this tool responsibly and respect the privacy and security of other systems.
