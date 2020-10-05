import socket
import re

#Script modified by KnapSec - https://github.com/KnapSec
#Original source: https://gist.github.com/leonjza/f35a7252babdf77c8421 
class Netcat:

	""" Python 'netcat like' module """

	def __init__(self, ip, port):

		self.buff = ""
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((ip, port))

	def read(self, length = 1024):

		""" Read 1024 bytes off the socket """

		return self.socket.recv(length)
 
	def read_until(self, data):

		""" Read data into the buffer until we have data """

		while not data in self.buff:
			self.buff += self.socket.recv(1024)
 
		pos = self.buff.find(data)
		rval = self.buff[:pos + len(data)]
		self.buff = self.buff[pos + len(data):]
 
		return rval
 
	def write(self, data):

		self.socket.send(data)
	
	def close(self):

		self.socket.close()

if __name__ == '__main__':
	nc = Netcat('[ADDRESS]', [PORT]) #Enter the nc address and port here
	nc.buff = b''
	for r in range(523):
		string = nc.read_until(b"\nx = ")
		print(string)
		string = nc.read_until(b"\nx = ")
		print(string)
		string = string[:-5]
		if (re.findall("/", string) and not re.findall("//", string)):
			string = string + '.0'
			string = repr(eval(string))
			#string = string.rstrip('0').rstrip('.') if '.' in string else string
			print(string)
			nc.write(string+'\n')	
		#string = string.decode("utf-8")
		else:
			print(eval(string))
			nc.write(str(eval(string))+'\n')
	string = nc.read()
	print(string)