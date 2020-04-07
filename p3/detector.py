#ECEN 4133
#Project 3 Network Security
#Part 3
#Liz Parker and Christian Sousa

from scapy.all import *

SYNs = {}
SYNACKs = {}

#Loop through packets cound SYN and SYNACKs
for pkt in PcapReader(sys.argv[1]):
	try:
		#Ignore non TCP packets
		if pkt[IP].proto == 6:
			#Grab source and destination IP addresses
			srcIP = pkt[IP].src
			dstIP = pkt[IP].dst

			#Count SYN packets
			if pkt[TCP].flags == 'S':
				if srcIP in SYNs.keys():	
					SYNs[srcIP] += 1
				else:
					SYNs[srcIP] = 1
			#Counte SYN+ACK Packets
			elif pkt[TCP].flags == 'S''A':
				if dstIP in SYNACKs.keys():	
					SYNACKs[dstIP] += 1
				else:
					SYNACKs[dstIP] = 1
	#Ignore malformed packets
	except:
		pass

#Loop through dictionary and find port scanning IPs
for k in SYNs.keys():
	if k in SYNACKs.keys():
		if SYNs[k] > 3*SYNACKs[k]:
			print(k)
	else:
		print(k)