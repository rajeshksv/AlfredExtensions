Send Message to your friends from Alfred 2.

### Installation
Grab the extension present in build directory and enjoy. Current Version is 0.3.3 (ALPHA)

### Usage
Just type msg and then start typing contact name or email or phone number. As you start typing, matching contacts will appear. Select one of them and then enter the message you want to send. That's it :)

Optional Tip: Set country code using mcc (in case SMS sending is failing) 

### Features
* Send Gtalk Message/SMS to your contacts
* Multiple Google accounts could be present on the system.
* Search not just contacts, but also buddies whom you already messaged but not present in address book
* Reply to last conversation directly using ..
* Copy last received message using ...

### Note
First time, building indexes will take time. From next time, it will be instant. 

### Special Note
Inspired from my fav extension - IM by NolanChan. But for some reason, he abondoned it. Tried to tinker a bit, but then realized its easier to rewrite. Hence this extension. Expect many many bugs to appear ;)

### Release Notes
#### Sixth Release - 0.3.3 (ALPHA)
* Reply to last conversation using ..
* Copy last received message using ...

#### Fifth Release - 0.3.2 (ALPHA)
* Cmd+Selecting contact will copy contact information to clipboard.
* SMS was failing for some contacts (which doesn't have country code attached to phone number). Fixed the bug by automatically adding country code for such contacts(country code is taken from user input)
* Duplicate Contacts appearing bug fix.

#### Fourth Release - 0.3.1 (ALPHA)
* Small bug fixes. 
* Duplicate Contacts appearing bug Fix - To some extent, duplicate contacts are merged and shown as one
* If conversation doesn't exist, it will be created automatically
* Contact names containing special characters wont cause any issue

#### Third Release - 0.3 (ALPHA)
* Bug Fixes, Code cleanup. Build stabilization
* Multiple Accounts. Full support. Multiple Accounts can be from same domain as well.

#### Second Release - 0.2 (ALPHA)
* Multiple Google Accounts (Limited support - Both accounts shouldn't be from same domain)
* Search not just contacts, but also buddies whom you already messaged but not present in address book

#### Initial Release - 0.1 (ALPHA)
* Send Gtalk Message/SMS to your contacts

### In the pipeline
* Imessage Support
* Non ASCII Character support for contacts
* (Experimental) Whats App (with yowsup client), Facebook, Pushbullet, Mail and others support
* (Experimental) Try decreasing number of steps to send message
* Recommendations of message to be sent (May be current URL of google chrome or clipboard entries etc)
* And more..... :)))

### Bugs
* First time to build database, contacts app must be open already sometimes
