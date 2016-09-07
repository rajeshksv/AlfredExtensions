on run {targetBuddyContact, targetMessage}
    tell application "Messages"
        if targetBuddyContact contains "@"
		set domain to item 2 of my split(targetBuddyContact, "@")
		set targetService to my getSenderService(domain)
	else 
		set targetService to service "SMS"
	end if	
        set targetBuddy to buddy targetBuddyContact of targetService
        send targetMessage to targetBuddy
    end tell
end run


on split(theString, theDelimiter)
	-- save delimiters to restore old settings
	set oldDelimiters to AppleScript's text item delimiters
	-- set delimiters to delimiter to be used
	set AppleScript's text item delimiters to theDelimiter
	-- create the array
	set theArray to every text item of theString
	-- restore the old setting
	set AppleScript's text item delimiters to oldDelimiters
	-- return the result
	return theArray
end split

-- Try to get service whose name contains domain. If not return default account
on getSenderService(domain)
	tell application "Messages"
		repeat with svc in services
			set serviceName to name of svc
			if serviceName does not start with "E:" then
				if serviceName contains domain then
					return svc
				end if
			end if
		end repeat
		return 1st service whose service type = Jabber
	end tell
end getSender
