# gfn-queue-checker
Prerequisites:
* `requests` library (`pip install requests`)

# Usage
Open up a supported browser - such as vanilla Google Chrome<br><br>
Open DevTools by pressing the three dots in the top left -> More Tools -> Developer Tools<br>(MAKE SURE TO DO THIS IN A NEW TAB / BEFORE LOADING GFN WEB)<br><br>
Navigate over to the Network tab in the DevTools<br><br>
Navigate over to the [GeForce NOW web library (play.geforcenow.com)](https://play.geforcenow.com/) in your browser<br><br>
Find and press on the `token` request, go to the payload tab, press view source, select it all and copy it<br><br>
After copying the token request, open up settings.py and put it in the `data = ""` (between the quotation marks) (make sure to wipe the text beforehand.. obviously..)<br><br>
Go back to the network tab in DevTools, start any game you want (it does not matter which)<br><br>
Find and press the second `session?keyboardLayout=en-US&languageCode=en_US` request, go to the payload tab, press view source, select it all and copy it<br><br>
Open up any text editor of your liking (notepad works too), paste the previously obtained data in there and save it as `request.json` (it's important that it's a json file.. obviously..)<br><br>
Now just run main.py for EU and main_us.py for US and let the program do its thing.

<br><br><br><br>(*I will work on automating all of this eventually*)
