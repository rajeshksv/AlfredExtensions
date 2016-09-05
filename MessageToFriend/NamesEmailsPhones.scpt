set output to ""
set eoc to "_^_"
set eol to "
"

tell application "Contacts"
	repeat with contact in people
		set contact_name to name of contact
		repeat with phone_entry in phones of contact
			set contact_phone to value of phone_entry
			set output to output & contact_name & eoc & contact_phone & eol
		end repeat
		repeat with email_entry in emails of contact
			set contact_email to value of email_entry
			set output to output & contact_name & eoc & contact_email & eol
		end repeat
	end repeat
end tell
output
