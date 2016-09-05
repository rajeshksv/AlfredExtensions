on run {targetBuddyContact, targetMessage}
    tell application "Messages"
        if targetBuddyContact contains "@"
        	set targetService to 1st service whose service type = Jabber
	else 
		set targetService to service "SMS"
	end if	
        set targetBuddy to buddy targetBuddyContact of targetService
        send targetMessage to targetBuddy
    end tell
end run
