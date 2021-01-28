import requests
import eventlet

a = 250
loop = 0

ipv4 = input("ipv4: ")
ipv4 = ipv4[0:9]
print(ipv4)

while loop == 0:	
	
	

	while a < 256:	

		link = str(f"http://{ipv4}.{a}")
		
		print(link)

		a += 1

		try:

			eventlet.monkey_patch()

			with eventlet.Timeout(2):

				response = requests.get(link)

				status = response.status_code

				if status == 200:
						print(f"LINK {link} VALIDADO | STATUS: {status}")

				else:
					loop = 1
		except:
			break