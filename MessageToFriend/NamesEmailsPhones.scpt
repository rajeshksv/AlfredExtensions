set contact_entries to ""
set eoc to "_^_"
set eol to "
"
-- Get Contacts from Chat History
tell application "Messages"
	repeat with current_service in services
		repeat with current_buddy in every buddy of current_service
			if status of current_buddy is not equal to unknown
				set contact_email to handle of current_buddy
				set contact_name to name of current_buddy
				set service_name to name of current_service
				set contact_entries to contact_entries & contact_name & eoc & contact_email & eoc & service_name & eol
			end if	
		end repeat
	end repeat
end tell

-- Get Contacts from Address Book
tell application "Contacts"
	repeat with current_buddy in people
		set contact_name to name of current_buddy
		repeat with email_entry in emails of current_buddy
			set contact_email to value of email_entry
			set contact_entries to contact_entries & contact_name & eoc & contact_email & eol
		end repeat
		
		repeat with phone_entry in phones of current_buddy
			set contact_phone to value of phone_entry
			set contact_entries to contact_entries & contact_name & eoc & contact_phone & eol
		end repeat
	end repeat
end tell

contact_entries
