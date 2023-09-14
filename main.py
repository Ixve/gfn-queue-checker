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
        elif r.status_code == 429:
            print("[!] Error refreshing key: Rate limited (429) - waiting 30 seconds...")
            time.sleep(30)
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
            elif 429 in (r1.status_code, r2.status_code):
                flag = 1
                if flag == 1:
                    print("[!] 429 Too Many Requests - waiting 1 minute [!]")
                    time.sleep(60)
                    eu_west()
                else:
                    print("[!] 429 Too Many Requests - waiting 30 seconds... [!]")
                    time.sleep(30)
                    eu_west()
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
            elif 429 in (r1.status_code, r2.status_code):
                flag = 1
                if flag == 1:
                    print("[!] 429 Too Many Requests - waiting 1 minute [!]")
                    time.sleep(60)
                    eu_northwest()
                else:
                    print("[!] 429 Too Many Requests - waiting 30 seconds... [!]")
                    time.sleep(30)
                    eu_northwest()
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
    print("=============== EU NORTHEAST ===============")
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
            elif 429 in (r1.status_code, r2.status_code):
                flag = 1
                if flag == 1:
                    print("[!] 429 Too Many Requests - waiting 1 minute [!]")
                    time.sleep(60)
                    eu_northeast()
                else:
                    print("[!] 429 Too Many Requests - waiting 30 seconds... [!]")
                    time.sleep(30)
                    eu_northeast()
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
            elif 429 in (r1.status_code, r2.status_code):
                flag = 1
                if flag == 1:
                    print("[!] 429 Too Many Requests - waiting 1 minute [!]")
                    time.sleep(60)
                    eu_central()
                else:
                    print("[!] 429 Too Many Requests - waiting 30 seconds... [!]")
                    time.sleep(30)
                    eu_central()
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
            elif 429 in (r1.status_code, r2.status_code):
                flag = 1
                if flag == 1:
                    print("[!] 429 Too Many Requests - waiting 1 minute [!]")
                    time.sleep(60)
                    eu_southwest()
                else:
                    print("[!] 429 Too Many Requests - waiting 30 seconds... [!]")
                    time.sleep(30)
                    eu_southwest()
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
    print("=============== EU SOUTHEAST ===============")
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
            elif 429 in (r1.status_code, r2.status_code):
                flag = 1
                if flag == 1:
                    print("[!] 429 Too Many Requests - waiting 1 minute [!]")
                    time.sleep(60)
                    eu_southeast()
                else:
                    print("[!] 429 Too Many Requests - waiting 30 seconds... [!]")
                    time.sleep(30)
                    eu_southeast()
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

try:
    eu_west()
    flag = 0
except KeyError:
    print("\nKeyError, continuing\n")

try:
    eu_northwest()
    flag = 0
except KeyError:
    print("\nKeyError, continuing\n")

try:
    eu_northeast()
    flag = 0
except KeyError:
    print("\nKeyError, continuing\n")

try:
    eu_central()
    flag = 0
except KeyError:
    print("\nKeyError, continuing\n")

try:
    eu_southwest()
    flag = 0
except KeyError:
    print("\nKeyError, continuing\n")

try:
    eu_southeast()
    flag = 0
except KeyError:
    print("\nKeyError, exitting.\n")
    exit()

print("\n\n\ \ ....... FINAL DATA RESULTS ....... / / ")
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
except FileNotFoundError:
    print("Missing data for EU West... Waiting 60 seconds and retrying")
    time.sleep(60)
    eu_west()

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
except FileNotFoundError:
    print("Missing data for EU Northwest... Waiting 60 seconds and retrying")
    time.sleep(60)
    eu_northwest()

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
except FileNotFoundError:
    print("Missing data for EU Northeast... Waiting 60 seconds and retrying")
    time.sleep(60)
    eu_northeast()

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
except FileNotFoundError:
    print("Missing data for EU Central... Waiting 60 seconds and retrying")
    time.sleep(60)
    eu_central()

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
except FileNotFoundError:
    print("Missing data for EU Southwest... Waiting 60 seconds and retrying")
    time.sleep(60)
    eu_southwest()

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
except FileNotFoundError:
    print("Missing data for EU Southeast... Waiting 60 seconds and retrying")
    time.sleep(60)
    eu_southeast()

    
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

