# gfn-queue-checker
Prerequisites:
* `requests` library (`pip install requests`)

# Usage
First go to the [GeForce NOW web library](https://play.geforcenow.com/) in a supported browser (Such as vanilla Google Chrome)<br><br>
Open up DevTools (Three dots in the top right of your browser -> More Tools -> Developer tools) and go to the "Network" tab<br><br>
Start *any* game you wish - it doesn't matter<br><br>
Press on the second "session?keyboardLayout=en-US&languageCode=en_US" and go to the "Payload" tab, press "view source", copy it all, and save it to `request.json` (In the same folder as the program)<br><br>
After that go back to the DevTools, go to Headers and find the "authorization" field, and copy the value (e.g. GFNJWT AieIJfnXjdfje....), then put it in settings.py and save it.<br>
Then just run the program and enjoy!<br><br>
