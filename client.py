# ATHMAN HASHIM ABDALLA
# P15 / 81781 / 2017


from multiprocessing.connection import Client
"""
Purpose
--------
	* Creating a client which will be using ssl to communicate with server

"""

# Creating client
address = ('localhost', 8000)
conn = Client(address)

# Initializing handshake

print("Sending Request to server...\n")
conn.send("client_hello")


# Receiing server response
rep = conn.recv()
print("Receiving server acceptance... \n")
server_pk = conn.recv()
k = 2

# Calculating pre master using the server public key
pre_master_key = server_pk * k
print("Sending pre master key ... \n")
msg1 = "sending pre_master_key encoded text {}".format(pre_master_key)
conn.send(msg1)

# Receiving master key
recv_master = conn.recv()
print("Receiving master key ... \n")
received_master = recv_master.split()
master_key = int(received_master[-1]) / k

print("Master key", master_key)

# Sending hello world
hello = "Hello world {}".format(master_key)
conn.send(hello)

conn.close()	