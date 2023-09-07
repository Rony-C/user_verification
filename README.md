# user_verification
Verify User IDs in bulk

Description
Bulk verify User IDs by opening the browser on a specific page that checks verification status. 
There is a Java and Python version of the script.

Gmail API is used to read emails and check for unopened emails meeting search requirements and to save the the file locally
Pyperclip is used to copy the IDs to an ids.txt file 
ids.txt file is used as a CLI argument
Loop through list of IDs to verify status
