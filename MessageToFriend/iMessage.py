import sys
import traceback
import os
import subprocess

contactEntryList = []
countryCodeConfigFile = "countryCode"
searchTerm = sys.argv[1]
delimiter = "_^_"
inputfile = "NamesEmailsPhones"

def noContactsFound():
	print """
	<items>
	  <item uid="NoContacts" arg="None" valid="YES" autocomplete="imu">
	      <title>No Contacts found :(</title>
	      <subtitle>Tip: Try reducing search terms</subtitle>
	      <icon>icon.png</icon>
	   </item>
	</items>
	"""

class ContactEntry:
	xmlTemplate = """
	  <item uid="%(uid)s" arg="%(arg)s">
	      <title>%(name)s</title>
	      <subtitle>%(contact)s</subtitle>
	   </item>
	"""

	def __init__(self, name, contact, service):
		self.name = name
		self.contact = contact
		self.xmlTemplate = self.createXMLfromContact(name, contact, service)

	def createXMLfromContact(self, name, contact, service):
		arg = contact
		if service is not None:
			arg = contact + delimiter + service
		data = {'uid': contact, 'arg': arg, 'name': name, 'contact': contact}
		return ContactEntry.xmlTemplate % data

	def __str__(self):
		return "Name = " + self.name + "\nContact = " + self.contact + "\nXml=" + self.xmlTemplate

	def __repr__(self):
		return self.__str__()

	def contains(self, substring):
		return substring.lower() in self.name.lower() or substring.lower() in self.contact.lower()
 
try:
	if not os.path.isfile(inputfile):
		# Generate the contacts database. Will happen only on first time run.
		cmd = ["osascript",  "NamesEmailsPhones.scpt"]
		with open("NamesEmailsPhones","wb") as out, open("stderr","wb") as err:
			subprocess.Popen(cmd, stdout=out,stderr=err).communicate()

	with open(inputfile) as f:
		lines = f.readlines()

	XMLString = ""
	contactNameMap = {}
	contactServiceMap = {}

	# Parsing lines, removing duplicates
	for line in lines:
		if delimiter in line:
			# Format will be name_^_abc@gmail.com_^_Gmail or name_^_abc@gmail.com_^_ghf@gmail.com or name_^_7251467389_^_SMS
			keyValue = line.rstrip("\n").split(delimiter)
			contact = keyValue[1]

			# Parsing and cleaning up phone numbers
			if "@" not in contact:
				contact = keyValue[1].translate(None, " !#$%^&*()-=[]\{};'<>/?,.?:")
				if not contact.startswith("+") and os.path.isfile(countryCodeConfigFile):
					with open(countryCodeConfigFile) as cc:
						countryCode = cc.readlines()
						contact = ''.join(countryCode).strip("\n") + contact.lstrip("0") 


			# Remove Facebook, iMessage lines since they are not supported
			# Also merge duplicates
			if "chat.facebook.com" not in contact and not contact.startswith("e:"):
				contactNameMap[contact] = keyValue[0]
				if len(keyValue) == 3:
					contactServiceMap[contact] = keyValue[2]
        
	# Preparing list of contacts - ContactEntry objects
	for contact, name in contactNameMap.items():
		contactEntryList.append(ContactEntry(name, contact, contactServiceMap.get(contact)))
        
	# Filtering list of contacts
	for contactEntry in contactEntryList:
		if contactEntry.contains(searchTerm):
			XMLString = XMLString + "\n" + contactEntry.xmlTemplate

	if XMLString == "":
		noContactsFound()
	else:
		print "<items> \n" + XMLString + " \n </items>"
except Exception, e:
	traceback.print_exc()
	noContactsFound()

