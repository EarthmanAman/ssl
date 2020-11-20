from multiprocessing.connection import Listener

address = ('localhost', 8000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey=b'secret password')
conn = listener.accept()
print('connection accepted from', listener.last_accepted)
while True:
	msg = conn.recv()
	print(f"Received: {msg}")
	if msg == 'close':
		conn.close()
		break
listener.close()