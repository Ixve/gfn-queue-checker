import os
import time
import json
import requests
from settings import data

def refresh_key():
    try:
        r = requests.post("https://login.nvidia.com/token", data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        if r.status_code == 200:
            k = r.json()
            with open('authorization.json', 'w') as fw:
                x = {"authorization": f'GFNJWT {k["id_token"]}'}
                json.dump(x, fw, indent=4, sort_keys=True)
                fw.close()
            print("[#] AUTHORIZATION KEY REFRESHED - RELAUNCH PROGRAM [#]")
            exit()
        else:
            print("An error has occured while POSTing data! \n\n Status Code: {r.status_code}\nReturned Data: {r.text}\n")
            exit()
    except Exception as e:
        print(f"Unknown exception has occured: \n\n {e}")
        exit()

try:
    with open('authorization.json', 'r') as tx:
        nx = json.load(tx)
except:
    refresh_key()

headers = {
    "Accept": "*/*",
    "authorization": f'{nx["authorization"]}',
    "content-type": "application/json",
}


############################################################ US WEST ############################################################
def us_west():
    print("=============== US WEST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://us-west.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://us-west.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r2.status_code}")
            if r2.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            elif r2.status_code == 401:
                print("[!] UNAUTHORIZED - PRINTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif r2.status_code == 200:
                with open("response_uswest.json", "w") as fw:
                    print("Dumping to response_uswest.json")
                    json.dump(r2.json(), fw, indent=4)
                    fw.close()
                f.close()
                x = ""
            else:
                print(f"Unknown error, status code: {r2.status_code}")
                return None
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

    try:
        with open("response_uswest.json", "r") as f:
            x = json.load(f)
            print(f"""\n\n
Session ID: {x["session"]["sessionId"]}
Server: {x["requestStatus"]["serverId"]}
Current Queue Position: {x["session"]["seatSetupInfo"]["queuePosition"]}
""")
            print("\nKilling session...")
            try:
                r = requests.delete(f'https://{x["session"]["sessionControlInfo"]["ip"]}{x["session"]["sessionControlInfo"]["resourcePath"]}')
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
            except Exception as e:
                print(f"Unknown exception occured! \n\n {e} \n Resorting to manual session kill.")
                y0 = input(str("Server: "))
                y1 = input(str("Session ID: "))
                r = requests.delete("https://{y0}.cloudmatchbeta.nvidiagrid.net/v2/session/{y1}")
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

############################################################ US NORTHWEST ############################################################

def us_northwest():
    print("=============== US NORTHWEST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://us-northwest.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://us-northwest.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r2.status_code}")
            if r2.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            elif r2.status_code == 401:
                print("[!] UNAUTHORIZED - PRINTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif r2.status_code == 200:
                with open("response_usnorthwest.json", "w") as fw:
                    print("Dumping to response_usnorthwest.json")
                    json.dump(r2.json(), fw, indent=4)
                    fw.close()
                f.close()
                x = ""
            else:
                print(f"Unknown error, status code: {r2.status_code}")
                return None
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

    try:
        with open("response_usnorthwest.json", "r") as f:
            x = json.load(f)
            print(f"""\n\n
Session ID: {x["session"]["sessionId"]}
Server: {x["requestStatus"]["serverId"]}
Current Queue Position: {x["session"]["seatSetupInfo"]["queuePosition"]}
""")
            print("\nKilling session...")
            try:
                r = requests.delete(f'https://{x["session"]["sessionControlInfo"]["ip"]}{x["session"]["sessionControlInfo"]["resourcePath"]}')
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
            except Exception as e:
                print(f"Unknown exception occured! \n\n {e} \n Resorting to manual session kill.")
                y0 = input(str("Server: "))
                y1 = input(str("Session ID: "))
                r = requests.delete("https://{y0}.cloudmatchbeta.nvidiagrid.net/v2/session/{y1}")
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

############################################################ US NORTHEAST ############################################################
def us_northeast():
    print("=============== US NORTHEAST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://us-northeast.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://us-northeast.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r2.status_code}")
            if r2.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            elif r2.status_code == 401:
                print("[!] UNAUTHORIZED - PRINTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif r2.status_code == 200:
                with open("response_usnortheast.json", "w") as fw:
                    print("Dumping to response_usnortheast.json")
                    json.dump(r2.json(), fw, indent=4)
                    fw.close()
                f.close()
                x = ""
            else:
                print(f"Unknown error, status code: {r2.status_code}")
                return None
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

    try:
        with open("response_usnortheast.json", "r") as f:
            x = json.load(f)
            print(f"""\n\n
Session ID: {x["session"]["sessionId"]}
Server: {x["requestStatus"]["serverId"]}
Current Queue Position: {x["session"]["seatSetupInfo"]["queuePosition"]}
""")
            print("\nKilling session...")
            try:
                r = requests.delete(f'https://{x["session"]["sessionControlInfo"]["ip"]}{x["session"]["sessionControlInfo"]["resourcePath"]}')
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
            except Exception as e:
                print(f"Unknown exception occured! \n\n {e} \n Resorting to manual session kill.")
                y0 = input(str("Server: "))
                y1 = input(str("Session ID: "))
                r = requests.delete("https://{y0}.cloudmatchbeta.nvidiagrid.net/v2/session/{y1}")
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""

    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

############################################################ US CENTRAL ############################################################
def us_central():
    print("=============== US CENTRAL ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://us-central.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://us-central.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r2.status_code}")
            if r2.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            elif r2.status_code == 401:
                print("[!] UNAUTHORIZED - PRINTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif r2.status_code == 200:
                with open("response_uscentral.json", "w") as fw:
                    print("Dumping to response_uscentral.json")
                    json.dump(r2.json(), fw, indent=4)
                    fw.close()
                f.close()
                x = ""
            else:
                print(f"Unknown error, status code: {r2.status_code}")
                return None
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

    try:
        with open("response_uscentral.json", "r") as f:
            x = json.load(f)
            print(f"""\n\n
Session ID: {x["session"]["sessionId"]}
Server: {x["requestStatus"]["serverId"]}
Current Queue Position: {x["session"]["seatSetupInfo"]["queuePosition"]}
""")
            print("\nKilling session...")
            try:
                r = requests.delete(f'https://{x["session"]["sessionControlInfo"]["ip"]}{x["session"]["sessionControlInfo"]["resourcePath"]}')
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
            except Exception as e:
                print(f"Unknown exception occured! \n\n {e} \n Resorting to manual session kill.")
                y0 = input(str("Server: "))
                y1 = input(str("Session ID: "))
                r = requests.delete("https://{y0}.cloudmatchbeta.nvidiagrid.net/v2/session/{y1}")
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""

    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

############################################################ US SOUTHWEST ############################################################            
def us_southwest():
    print("=============== US SOUTHWEST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://us-southwest.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://us-southwest.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r2.status_code}")
            if r2.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            elif r2.status_code == 401:
                print("[!] UNAUTHORIZED - PRINTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif r2.status_code == 200:
                with open("response_ussouthwest.json", "w") as fw:
                    print("Dumping to response_ussouthwest.json")
                    json.dump(r2.json(), fw, indent=4)
                    fw.close()
                f.close()
                x = ""
            else:
                print(f"Unknown error, status code: {r2.status_code}")
                return None
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

    try:
        with open("response_ussouthwest.json", "r") as f:
            x = json.load(f)
            print(f"""\n\n
Session ID: {x["session"]["sessionId"]}
Server: {x["requestStatus"]["serverId"]}
Current Queue Position: {x["session"]["seatSetupInfo"]["queuePosition"]}
""")
            print("\nKilling session...")
            try:
                r = requests.delete(f'https://{x["session"]["sessionControlInfo"]["ip"]}{x["session"]["sessionControlInfo"]["resourcePath"]}')
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
            except Exception as e:
                print(f"Unknown exception occured! \n\n {e} \n Resorting to manual session kill.")
                y0 = input(str("Server: "))
                y1 = input(str("Session ID: "))
                r = requests.delete("https://{y0}.cloudmatchbeta.nvidiagrid.net/v2/session/{y1}")
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""

    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

############################################################ US SOUTHEAST ############################################################
def us_southeast():
    print("=============== US SOUTHEAST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://us-southeast.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://us-southeast.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r2.status_code}")
            if r2.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            elif r2.status_code == 401:
                print("[!] UNAUTHORIZED - PRINTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif r2.status_code == 200:
                with open("response_ussoutheast.json", "w") as fw:
                    print("Dumping to response_ussoutheast.json")
                    json.dump(r2.json(), fw, indent=4)
                    fw.close()
                f.close()
                x = ""
            else:
                print(f"Unknown error, status code: {r2.status_code}")
                return None
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

    try:
        with open("response_ussoutheast.json", "r") as f:
            x = json.load(f)
            print(f"""\n\n
Session ID: {x["session"]["sessionId"]}
Server: {x["requestStatus"]["serverId"]}
Current Queue Position: {x["session"]["seatSetupInfo"]["queuePosition"]}
""")
            print("\nKilling session...")
            try:
                r = requests.delete(f'https://{x["session"]["sessionControlInfo"]["ip"]}{x["session"]["sessionControlInfo"]["resourcePath"]}')
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
            except Exception as e:
                print(f"Unknown exception occured! \n\n {e} \n Resorting to manual session kill.")
                y0 = input(str("Server: "))
                y1 = input(str("Session ID: "))
                r = requests.delete("https://{y0}.cloudmatchbeta.nvidiagrid.net/v2/session/{y1}")
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""

    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None


############################################################ US SOUTH ############################################################
def us_south():
    print("=============== US SOUTH ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://us-south.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://us-south.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r2.status_code}")
            if r2.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            elif r2.status_code == 401:
                print("[!] UNAUTHORIZED - PRINTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif r2.status_code == 200:
                with open("response_ussouth.json", "w") as fw:
                    print("Dumping to response_ussouth.json")
                    json.dump(r2.json(), fw, indent=4)
                    fw.close()
                f.close()
                x = ""
            else:
                print(f"Unknown error, status code: {r2.status_code}")
                return None
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

    try:
        with open("response_ussouth.json", "r") as f:
            x = json.load(f)
            print(f"""\n\n
Session ID: {x["session"]["sessionId"]}
Server: {x["requestStatus"]["serverId"]}
Current Queue Position: {x["session"]["seatSetupInfo"]["queuePosition"]}
""")
            print("\nKilling session...")
            try:
                r = requests.delete(f'https://{x["session"]["sessionControlInfo"]["ip"]}{x["session"]["sessionControlInfo"]["resourcePath"]}')
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
            except Exception as e:
                print(f"Unknown exception occured! \n\n {e} \n Resorting to manual session kill.")
                y0 = input(str("Server: "))
                y1 = input(str("Session ID: "))
                r = requests.delete("https://{y0}.cloudmatchbeta.nvidiagrid.net/v2/session/{y1}")
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""

    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None


############################################################ US MIDWEST ############################################################
def us_midwest():
    print("=============== US MIDWEST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://us-midwest.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://us-midwest.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r2.status_code}")
            if r2.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            elif r2.status_code == 401:
                print("[!] UNAUTHORIZED - PRINTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif r2.status_code == 200:
                with open("response_usmidwest.json", "w") as fw:
                    print("Dumping to response_usmidwest.json")
                    json.dump(r2.json(), fw, indent=4)
                    fw.close()
                f.close()
                x = ""
            else:
                print(f"Unknown error, status code: {r2.status_code}")
                return None
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

    try:
        with open("response_usmidwest.json", "r") as f:
            x = json.load(f)
            print(f"""\n\n
Session ID: {x["session"]["sessionId"]}
Server: {x["requestStatus"]["serverId"]}
Current Queue Position: {x["session"]["seatSetupInfo"]["queuePosition"]}
""")
            print("\nKilling session...")
            try:
                r = requests.delete(f'https://{x["session"]["sessionControlInfo"]["ip"]}{x["session"]["sessionControlInfo"]["resourcePath"]}')
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
            except Exception as e:
                print(f"Unknown exception occured! \n\n {e} \n Resorting to manual session kill.")
                y0 = input(str("Server: "))
                y1 = input(str("Session ID: "))
                r = requests.delete("https://{y0}.cloudmatchbeta.nvidiagrid.net/v2/session/{y1}")
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""

    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None


############################################################ US EAST ############################################################
def us_east():
    print("=============== US EAST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://us-east.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://us-east.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r2.status_code}")
            if r2.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            elif r2.status_code == 401:
                print("[!] UNAUTHORIZED - PRINTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif r2.status_code == 200:
                with open("response_useast.json", "w") as fw:
                    print("Dumping to response_useast.json")
                    json.dump(r2.json(), fw, indent=4)
                    fw.close()
                f.close()
                x = ""
            else:
                print(f"Unknown error, status code: {r2.status_code}")
                return None
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

    try:
        with open("response_useast.json", "r") as f:
            x = json.load(f)
            print(f"""\n\n
Session ID: {x["session"]["sessionId"]}
Server: {x["requestStatus"]["serverId"]}
Current Queue Position: {x["session"]["seatSetupInfo"]["queuePosition"]}
""")
            print("\nKilling session...")
            try:
                r = requests.delete(f'https://{x["session"]["sessionControlInfo"]["ip"]}{x["session"]["sessionControlInfo"]["resourcePath"]}')
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
            except Exception as e:
                print(f"Unknown exception occured! \n\n {e} \n Resorting to manual session kill.")
                y0 = input(str("Server: "))
                y1 = input(str("Session ID: "))
                r = requests.delete("https://{y0}.cloudmatchbeta.nvidiagrid.net/v2/session/{y1}")
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""

    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None


############################################################ US MOUNTAIN ############################################################
def us_mountain():
    print("=============== US MOUNTAIN ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://us-mountain.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://us-mountain.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r2.status_code}")
            if r2.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            elif r2.status_code == 401:
                print("[!] UNAUTHORIZED - PRINTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif r2.status_code == 200:
                with open("response_usmountain.json", "w") as fw:
                    print("Dumping to response_usmountain.json")
                    json.dump(r2.json(), fw, indent=4)
                    fw.close()
                f.close()
                x = ""
            else:
                print(f"Unknown error, status code: {r2.status_code}")
                return None
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None




    try:
        with open("response_ussoutheast.json", "r") as f:
            x = json.load(f)
            print(f"""\n\n
Session ID: {x["session"]["sessionId"]}
Server: {x["requestStatus"]["serverId"]}
Current Queue Position: {x["session"]["seatSetupInfo"]["queuePosition"]}
""")
            print("\nKilling session...")
            try:
                r = requests.delete(f'https://{x["session"]["sessionControlInfo"]["ip"]}{x["session"]["sessionControlInfo"]["resourcePath"]}')
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
            except Exception as e:
                print(f"Unknown exception occured! \n\n {e} \n Resorting to manual session kill.")
                y0 = input(str("Server: "))
                y1 = input(str("Session ID: "))
                r = requests.delete("https://{y0}.cloudmatchbeta.nvidiagrid.net/v2/session/{y1}")
                print(f"DELETE Request sent!\nStatus Code: {r.status_code}")
                f.close()
                x = ""
    except Exception as e:
        print(f"Unknown Exception: \n\n {e}")
        return None

try:
    us_west()
except KeyError:
    print("\nKeyError, continuing\n")

try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    us_northwest()
except KeyError:
    print("\nKeyError, continuing\n")

try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    us_northeast()
except KeyError:
    print("\nKeyError, continuing\n")

try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    us_central()
except KeyError:
    print("\nKeyError, continuing\n")

try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    us_southwest()
except KeyError:
    print("\nKeyError, continuing\n")

try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    us_southeast()
except KeyError:
    print("\nKeyError, exitting.\n")
    exit()
    
try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    us_south()
except KeyError:
    print("\nKeyError, exitting.\n")
    exit()

try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    us_east()
except KeyError:
    print("\nKeyError, exitting.\n")
    exit()
    
try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    us_midwest()
except KeyError:
    print("\nKeyError, exitting.\n")
    exit()
    
try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    us_mountain()
except KeyError:
    print("\nKeyError, exitting.\n")
    exit()

print("\n\n\ \ ....... FINAL DATA RESULTS ....... / / ")
try:
    with open("response_uswest.json") as f:
        x = json.load(f)
        print(f'US WEST ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for US WEST... Continuing")
    x = ""
    f.close()

try:
    with open("response_usnorthwest.json") as f:
        x = json.load(f)
        print(f'US NORTHWEST ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for US NORTHWEST... Continuing")
    x = ""
    f.close()

try:
    with open("response_usnortheast.json") as f:
        x = json.load(f)
        print(f'US NORTHEAST ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for US NORTHEAST... Continuing")
    x = ""
    f.close()

try:
    with open("response_uscentral.json") as f:
        x = json.load(f)
        print(f'US CENTRAL ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for US CENTRAL... Continuing")
    x = ""
    f.close()

try:
    with open("response_ussouthwest.json") as f:
        x = json.load(f)
        print(f'US SOUTHWEST ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for US SOUTHWEST... Continuing")
    x = ""
    f.close()

try:
    with open("response_ussoutheast.json") as f:
        x = json.load(f)
        print(f'US SOUTHEAST ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for US SOUTHEAST... Continuing")
    x = ""
    f.close()

try:
    with open("response_ussouth.json") as f:
        x = json.load(f)
        print(f'US SOUTH ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for US SOUTH... Continuing")
    x = ""
    f.close()


try:
    with open("response_useast.json") as f:
        x = json.load(f)
        print(f'US EAST ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for US EAST... Continuing")
    x = ""
    f.close()


try:
    with open("response_usmidwest.json") as f:
        x = json.load(f)
        print(f'US MIDWEST ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for US MIDWEST... Continuing")
    x = ""
    f.close()


try:
    with open("response_usmountain.json") as f:
        x = json.load(f)
        print(f'US MOUNTAIN ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for US MOUNTAIN... Continuing")
    x = ""
    f.close()
  
try:
    os.remove("response_uscentral.json")    # Central
    os.remove("response_ussoutheast.json")  # South East
    os.remove("response_ussouthwest.json")  # South West
    os.remove("response_usnortheast.json")  # North East
    os.remove("response_usnorthwest.json")  # North West
    os.remove("response_ussouth.json")      # South
    os.remove("response_useast.json")       # East
    os.remove("response_usmidwest.json")    # Midwest
    os.remove("response_usmountain.json")   # Mountain
    os.remove("response_uswest.json")       # West
except Exception as e:
    print(f"Unknown exception whilst removing files: \n\n {e}")
exit()

