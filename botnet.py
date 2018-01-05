import pxssh

class Client:

	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		self.session = self.connect()

	def connect(self):
		try:
			s = pxssh.pxssh()
			s.login(self.host, self.user, self.password)
			return s
		except Exception, e:
			print e
			print '[-] Error Connecting!'

	def send_command(self, cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before

def botnetCommand(command):
	for client in botNet:
		output = client.send_command(command)
		print '[*] Output from ' + client.host
		print '[+] ' + output

def addClient(host, user, password):
	client = Client(host, user, password)
	botNet.append(client)

botNet = []

#ADD BOTNET USERS HERE, (USE THE 'addClient' function to do this)
#FORMAT:
#IP ADDRESS, USERNAME, PASSWORD
addClient ('', '', '')

#ADD TO EXECUTE HERE
#SENDS COMMANDS TO USERS IN THE LIST

botnetCommand('')
