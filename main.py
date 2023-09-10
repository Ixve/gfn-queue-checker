import os
import time
import json
import requests
from settings import headers
from settings import data

############################################################ EU WEST ############################################################
def eu_west():
    print("=============== EU WEST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://eu-west.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://eu-west.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
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
                with open("response_euwest.json", "w") as fw:
                    print("Dumping to response_euwest.json")
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
        with open("response_euwest.json", "r") as f:
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

############################################################ EU NORTHWEST ############################################################

def eu_northwest():
    print("=============== EU NORTHWEST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://eu-northwest.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://eu-northwest.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
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
                with open("response_eunorthwest.json", "w") as fw:
                    print("Dumping to response_eunorthwest.json")
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
        with open("response_eunorthwest.json", "r") as f:
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

############################################################ EU NORTHEAST ############################################################
def eu_northeast():
    print("=============== EU WEST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://eu-northeast.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://eu-northeast.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
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
                with open("response_eunortheast.json", "w") as fw:
                    print("Dumping to response_eunortheast.json")
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
        with open("response_eunortheast.json", "r") as f:
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

############################################################ EU CENTRAL ############################################################
def eu_central():
    print("=============== EU CENTRAL ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://eu-central.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://eu-central.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
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
                with open("response_eucentral.json", "w") as fw:
                    print("Dumping to response_eucentral.json")
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
        with open("response_eucentral.json", "r") as f:
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

############################################################ EU SOUTHWEST ############################################################            
def eu_southwest():
    print("=============== EU SOUTHWEST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://eu-southwest.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://eu-southwest.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
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
                with open("response_eusouthwest.json", "w") as fw:
                    print("Dumping to response_eusouthwest.json")
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
        with open("response_eusouthwest.json", "r") as f:
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

############################################################ EU SOUTHEAST ############################################################
def eu_southeast():
    print("=============== EU WEST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://eu-southeast.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            if r1.status_code == 500:
                print("[!] INTERNAL SERVER ERROR [!]")
                f.close()
                x = ""
                return None
            r2 = requests.post("https://eu-southeast.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
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
                with open("response_eusoutheast.json", "w") as fw:
                    print("Dumping to response_eusoutheast.json")
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
        with open("response_eusoutheast.json", "r") as f:
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

def refresh_key():
    try:
        r = requests.post("https://login.nvidia.com/token", data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        k = r.json()
        print(f'\n\nNew auth key (replace the one in settings.py):\n\nGFNJWT {k["id_token"]}')
        exit()
    except Exception as e:
        print(f"Unknown exception has occured: \n\n {e}")
        exit()

try:
    eu_west()
except KeyError:
    print("\nKeyError, continuing\n")

try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    eu_northwest()
except KeyError:
    print("\nKeyError, continuing\n")

try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    eu_northeast()
except KeyError:
    print("\nKeyError, continuing\n")

try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    eu_central()
except KeyError:
    print("\nKeyError, continuing\n")

try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    eu_southwest()
except KeyError:
    print("\nKeyError, continuing\n")

try:
    print("Waiting 10 seconds in-case of ratelimit...")
    time.sleep(10)
    eu_southeast()
except KeyError:
    print("\nKeyError, exitting.\n")
    exit()

print("\n\n \ \ ....... FINAL DATA RESULTS ....... / / ")
try:
    with open("response_euwest.json") as f:
        x = json.load(f)
        print(f'EU West ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for EU West... Continuing")
    x = ""
    f.close()    

try:
    with open("response_eunorthwest.json") as f:
        x = json.load(f)
        print(f'EU Northwest ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for EU Northwest... Continuing")
    x = ""
    f.close()  

try:
    with open("response_eunortheast.json") as f:
        x = json.load(f)
        print(f'EU Northeast ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for EU Northeast... Continuing")
    x = ""
    f.close()  

try:
    with open("response_eucentral.json") as f:
        x = json.load(f)
        print(f'EU Central ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for EU Central... Continuing")
    x = ""
    f.close()  

try:
    with open("response_eusouthwest.json") as f:
        x = json.load(f)
        print(f'EU Southwest ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for EU Southwest... Continuing")
    x = ""
    f.close()  

try:
    with open("response_eusoutheast.json") as f:
        x = json.load(f)
        print(f'EU Southeast ({x["requestStatus"]["serverId"]}): {x["session"]["seatSetupInfo"]["queuePosition"]}')
        x = ""
        f.close()
except KeyError:
    print("Missing queue position data for EU Southeast... Continuing")
    x = ""
    f.close()  
    
try:
    os.remove("response_eucentral.json")
    os.remove("response_eusoutheast.json")
    os.remove("response_eusouthwest.json")
    os.remove("response_eunortheast.json")
    os.remove("response_eunorthwest.json")
    os.remove("response_euwest.json")
except Exception as e:
    print(f"Unknown exception whilst removing files: \n\n {e}")
exit()

