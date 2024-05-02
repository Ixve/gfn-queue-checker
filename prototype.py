import os
import time
import json
import socket
#   from settings import data

try:
    import requests
except ModuleNotFoundError:
    print("Upgrading pip")
    os.system("python -m pip install --upgrade pip")
    print("\nInstalling requests library")
    os.system("python -m pip install requests")

try:
    from tcppinglib import tcpping
except ModuleNotFoundError:
    print("Upgrading pip")
    os.system("python -m pip install --upgrade pip")
    print("\nInstalling tcppinglib library")
    os.system("python -m pip install tcppinglib")

############################################################################################################################################################
# The following has been ported from the original file and is *not* tested
# This project will be discontinued after this update, which breaks everything
# It is up to you,  the user to fix it.
############################################################################################################################################################
flag = 0
versionflag = 0

def refresh_key():
    try:
        r = requests.post("https://login.nvidia.com/token", data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        if r.status_code == 200:
            k = r.json()
            with open('authorization.json', 'w') as fw:
                x = {"authorization": f'GFNJWT {k["id_token"]}'}
                json.dump(x, fw, indent=4, sort_keys=True)
                fw.close()
            print("[#] Authorization key refreshed - relaunching program [#]\n")
            main()
        elif r.status_code == 429:
            print("[!] Error refreshing key: Rate limited (429) - waiting 30 seconds... [!]")
            time.sleep(30)
        else:
            print(f"An error has occured while POSTing data! \n\n Status Code: {r.status_code}\nReturned Data: {r.text}\n")
            exit()
    except Exception as e:
        print(f"Unknown exception has occured: \n\n {e}")
        exit()

def auth_get():
    try:
        with open('authorization.json', 'r') as tx:
            nx = json.load(tx)
    except:
        refresh_key()

    global headers
    headers = {
        "Accept": "*/*",
        "authorization": f'{nx["authorization"]}',
        "content-type": "application/json",
    }

def version_bump():
    try:
        with open('request.json', 'r') as f:
            x = json.load(f)
            y = json.dumps(x, indent=4)
            z = int(float(x["sessionRequestData"]["clientVersion"]))
            c = y.replace(f'"{z}.0",', f'"{z + 1}.0",')
            f.close()

        with open('request.json', 'w') as f:
            f.write(c)
            f.close()
    except Exception as e:
        print(f"An unknown exception has occured while bumping clientVersion: \n\n{e}")

def grab_ping():
    c = socket.getaddrinfo(f'{x["session"]["sessionControlInfo"]["ip"]}', port=443, family=socket.AF_INET, proto=socket.IPPROTO_TCP)
    print("Testing ping...")
    n = tcpping(c[0][4][0], port=443, timeout=1.5, count=5, interval=1.5)
    print(f"Approximate Server Ping: {n.avg_rtt}ms\n")

############################################################################################################################################################

serverlist = [
    "eu-west",
    "eu-northwest",
    "eu-northeast",
    "eu-central",
    "eu-southwest",
    "eu-southeast"
]

serverlistfull = [
    "=============== EU WEST ===============",
    "============ EU NORTHWAST ============",
    "============ EU NORTHEAST ============",
    "============= EU CENTRAL =============",
    "============ EU SOUTHWEST ============",
    "============ EU SOUTHEAST ============"
]

servertable = {
    "eu-west": "None",
    "eu-northwest": "None",
    "eu-northeast": "None",
    "eu-central": "None",
    "eu-southwest": "None",
    "eu-northeast": "None",
    
}




def server_req():
    for i in serverlist:
        print(serverlistfull[i])
        try:
            with open("request.json", "r") as f:
                x = json.load(f)
                r1 = requests.post(f"https://{serverlist[i]}.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
                r2 = requests.post(f"https://{serverlist[i]}.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
                print(f"Request status code #1: {r1.status_code}")
                print(f"Request status code #2: {r2.status_code}")

                if 403 in (r1.status_code, r2.status_code):
                    if "INVALID_REQUEST_VERSION_OUT_OF_DATE_STATUS" in r2.text:
                        print(statusfull[5])

                elif r2.status_code != 200:
                    for i in statuscodes:
                        if statuscodes[i] in (r1.status_code, r2.status_code):
                            print(statusfull[i])
                    
                elif r2.status_code == 200:
                    parse_data(serverlist[i])
                else:
                    print(f"Unknown error, status code: {r2.status_code}")
                    return None
        except Exception as e:
            print(f"Unknown Exception: \n\n {e}")
            return None



def parse_data(server):
    try:
        vx = json.dumps(r2.json(), indent=4)
        servertable[server] = vx
        print(f"""\n\n
Session ID: {vx["session"]["sessionId"]}
Server: {vx["requestStatus"]["serverId"]}
Current Queue Position: {vx["session"]["seatSetupInfo"]["queuePosition"]}
""")
        print("\nKilling session...")
        try:
            r = requests.delete(f'https://{vx["session"]["sessionControlInfo"]["ip"]}{vx["session"]["sessionControlInfo"]["resourcePath"]}')
            print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
            f.close()
        except Exception as e:
            print(f"Unknown exception occured! \n\n {e} \n Resorting to manual session kill.")
            y0 = input(str("Server: "))
            y1 = input(str("Session ID: "))
            r = requests.delete("https://{y0}.cloudmatchbeta.nvidiagrid.net/v2/session/{y1}")
            print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
            f.close()
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

def main():
    print("""

+==================+
[1] Run queue check
[2] Bump version
[3] Refresh auth
[0] Exit
+==================+
""")
    try:
        choice = int(input(">> "))
    except:
        print("Invalid choice")
        exit()
        
    if choice not in [1, 2, 3, 0]:
        print("Invalid choice, aborting")
        exit()
    elif choice == 1:
        auth_get()
        server_req()
    elif choice == 2:
        version_bump()
    elif choice == 3:
        refresh_key()
    elif choice == 0:
        exit()
    
try:
    main()
except Exception as e:
    print(f"Unknown exception:\n\n{e}")
    exit()
