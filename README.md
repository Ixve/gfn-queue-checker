# gfn-queue-checker
Prerequisites:
*

# Usage
First go to the [GeForce NOW web library](https://play.geforcenow.com/) in a supported browser (Such as vanilla Google Chrome)
Open up DevTools (Three dots in the top right of your browser -> More Tools -> Developer tools) and go to the "Network" tab
Start *any* game you wish - it doesn't matter
Press on the second "session?keyboardLayout=en-US&languageCode=en_US" and go to the "Payload" tab, press "view source", copy it all, and save it to `request.json` (In the same folder as the program)
After that go back to the DevTools, go to Headers and find the "authorization" field, and copy the value (e.g. GFNJWT AieIJfnXjdfje....), then put it in settings.py and save it.
Then just run the program and enjoy!
