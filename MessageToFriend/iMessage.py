import sys
import traceback
import os
import subprocess

contactEntryList = []
name = sys.argv[1]
delimiter = "_^_"
inputfile = "NamesEmailsPhones"

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
		return self.name + "" + self.contact + "" + self.xmlTemplate

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
	for entry in entries:
		if delimiter in entry:
			keyValue = entry.rstrip("\n").split(delimiter)
			contactEntryList.append(ContactEntry(keyValue[0], keyValue[1]))

	for contactEntry in contactEntryList:
		if contactEntry.contains(name):
			XMLString = XMLString + "\n" + contactEntry.xmlTemplate

	print "<items> \n" + XMLString + " \n </items>"
except Exception, e:
	traceback.print_exc()

	print """
	<items>
	  <item uid="NoContacts" arg="None" valid="YES" autocomplete="imu">
	      <title>Your contact list is empty or broken</title>
	      <subtitle>You might need to run keyword 'imu'</subtitle>
	      <icon>icon.png</icon>
	   </item>
	</items>
	"""
