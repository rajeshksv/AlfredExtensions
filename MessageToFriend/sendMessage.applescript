on run {targetBuddyContact, targetMessage}
    tell application "Messages"
	set delimiter to "_^_"
	-- targetBuddyContact can be abc@gmail.com_^_Gmail or abc@gmail.com or phone number or abc@gmail.com_^_cde@gmail.com
        if targetBuddyContact contains "@"
		if targetBuddyContact contains delimiter
			set buddyServiceInfo to my split(targetBuddyContact, delimiter)
			set serviceMetaData to item 2 of buddyServiceInfo
			set targetBuddyContact to item 1 of buddyServiceInfo
		end if
		-- To be handled. If delimiter is not present. Just show you can't send message
		set targetService to 1st service whose name is serviceMetaData
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
