import sys
import traceback
import os
import subprocess

contactEntryList = []
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
	  <item uid="%(uid)s" arg="%(contact)s">
	      <title>%(name)s</title>
	      <subtitle>%(contact)s</subtitle>
	   </item>
	"""

	def __init__(self, name, contact):
		self.name = name
		self.contact = contact
		self.xmlTemplate = self.createXMLfromContact(name, contact)

	def createXMLfromContact(self, name, contact):
		data = {'uid': contact, 'contact': contact, 'name': name}
		return ContactEntry.xmlTemplate % data

	def __str__(self):
		return "Name = " + self.name + "\nContact = " + self.contact + "\nXml=" + self.xmlTemplate

	def __repr__(self):
		return self.__str__()

	def contains(self, substring):
		return substring.lower() in self.name.lower() or substring.lower() in self.contact.lower()
 
try:
	if not os.path.isfile(inputfile):
		cmd = ["osascript",  "NamesEmailsPhones.scpt"]
		with open("NamesEmailsPhones","wb") as out, open("stderr","wb") as err:
			subprocess.Popen(cmd, stdout=out,stderr=err).communicate()

	with open(inputfile) as f:
		entries = f.readlines()

	XMLString = ""
	contactNameMap = {}
	for entry in entries:
		if delimiter in entry:
			keyValue = entry.rstrip("\n").split(delimiter)
			contact = keyValue[1]
			# Remove Facebook, iMessage entries since they are not supported
			# Also merge duplicates
			if "chat.facebook.com" not in contact and not contact.startswith("e:"):
				contactNameMap[contact] = keyValue[0]
	
	for contact, name in contactNameMap.items():
		contactEntryList.append(ContactEntry(name, contact))
        
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

