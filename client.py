from multiprocessing.connection import Client

address = ('localhost', 8000)
conn = Client(address, authkey=b'secret password')

# can also send arbitrary objects:
while True:
	msg = input("msg >> ")
	conn.send(msg)
# conn.send(['a', 2.5, None, int, sum])
conn.close()