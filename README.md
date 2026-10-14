# Basic Network Sniffer

## What it does
This program captures live network packets as they pass through the interface and prints out basic details about each one.

## How it works
It uses Scapy to capture packets, and the sniff function calls show_packet on every packet it catches, which pulls out the info and prints it.

## What it shows for each packet
- Source IP
- Destination IP
- Protocol (TCP, UDP, ICMP, etc.)
- Source and destination ports
- Payload (the first 60 bytes of the actual data, if the packet carries any) 

## How to run it
```
sudo python3 sniffer.py
```
It needs sudo because capturing raw network traffic requires admin privileges. Press Ctrl+C to stop it.

## Sample Output
 ```
10.0.2.15 -> 10.105.127.59 UDP 38036 -> 53
10.0.2.15 -> 104.20.23.154 TCP 48034 -> 80
payload: b'GET / HTTP/1.1\r\nHost: example.com\r\nUser-Agent: curl/8.20.0\r\n'
104.20.23.154 -> 10.0.2.15 TCP 80 -> 48034
payload: b'HTTP/1.1 200 OK\r\nDate: Tue, 13 Oct 2026 13:47:22 GMT\r\nConten'
```
Port 53 is DNS and port 80 is HTTP. The first payload is the web request my machine sent, and the second is the server's reply. Both are readable because HTTP is not encrypted.


## What I learned
I noticed that HTTP traffic shows up completely in plain text, so anyone sniffing the network could read the actual request. It made it a lot clearer why HTTPS and encryption actually matter.

## Note
This was only tested on my own lab network, not a live public one

