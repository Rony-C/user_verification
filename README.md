# user_verification
Verify User IDs in bulk

Description
Bulk verify User IDs by opening the browser on a specific page that checks verification status. Ideally this would be a GET request but I am still figuring out the authentication side of this.
The program will take a list of IDs, create the URL and open the URL in the system default browser.
There is a Java and Python version of the script.

How to use
Make sure you are logged in to the site you need to make the calls to. No proper authentication set up yet.
Add your base URL and extension, if required, to wrap around the ID. Set the file the IDs are stored in. Ideally these are just numerical or alphanumerical IDs on separate lines. 
Run the program and see the the browser open the pages.

