# ATHMAN HASHIM ABDALLA
# P15 / 81781 / 2017

from multiprocessing.connection import Listener

"""
Purpose
--------
	* To create a server to accept ssl

Method of encryption
----------------------
	* I used a simple encryption techniques just for demostration 
	* The master key is appended at the end of each string.
"""

# Creating a server process
print("Server listening ... \n")
address = ('localhost', 8000)     # family is deduced to be 'AF_INET'
listener = Listener(address)
conn = listener.accept()

# The keys of the server
pk = 3
secret_key = 24 / pk

print('connection accepted from', listener.last_accepted)

# Receiving the first message which is "client_hello"
msg = conn.recv()
print("Receiving client request... \n")

# Check if it the client_hello i.e. a request by client to connect
if msg == "client_hello":
	conn.send("server_hello")
	conn.send(pk) # Send public key to client
	print("Sending Server Public Key... \n")

# Receiving Pre master encrypted message from client	
pre_master_encrypt_msg = conn.recv()
print("Receiving pre master key")
split_msg = pre_master_encrypt_msg.split()
k = round(int(split_msg[-1]) / secret_key * pk) # extract the pre master key
print("Pre master key is: " + str(k))

# I used a constant figure 8 as the master key for simplicity
master_key = 8

# Encrypting the master key with the pre master key 
encryt_master_key_value = k * master_key

# Send the encrypted master key
print("\nSending master key")
conn.send("master {}".format(encryt_master_key_value))


print("\n\nHandshake complete \n\n")

# Start receiving 

	
msg_recv = conn.recv()
msg_split = msg_recv.split()

if float(msg_split[-1]) == float(master_key):
	print("Received >> {} {}".format(msg_split[0], msg_split[1]))
	
else:
	print("Corrupted data. Initiate the processes again")
	conn.close()

conn.close()

listener.close()