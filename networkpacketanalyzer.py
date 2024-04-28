import socket

# Create a raw socket to listen for packets
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

# Loop to receive and analyze packets
while True:
    packet = s.recvfrom(65565)  # Receive a packet
    packet_data = packet[0]  # Extract packet data
    print(packet_data)  # Print packet data