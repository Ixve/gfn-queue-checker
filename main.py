import os
import time
import json
import requests
from settings import data

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
            print("[#] Authorization key refreshed - relaunching program [#]")
            main()
        elif r.status_code == 429:
            print("[!] Error refreshing key: Rate limited (429) - waiting 30 seconds...")
            time.sleep(30)
        else:
            print("An error has occured while POSTing data! \n\n Status Code: {r.status_code}\nReturned Data: {r.text}\n")
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

############################################################ EU WEST ############################################################
def eu_west():
    print("\n\n=============== EU WEST ===============")
    try:
        with open("request.json", "r") as f:
            x = json.load(f)
            r1 = requests.post("https://eu-west.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r1.status_code}")
            r2 = requests.post("https://eu-west.cloudmatchbeta.nvidiagrid.net/v2/session?keyboardLayout=en-US&languageCode=en_US", json=x, headers=headers)
            print(f"Request status code #1: {r2.status_code}")
            if 500 in (r1.status_code, r2.status_code):
                print("[!] 500 Internal Server Error - GFN servers are experiencing issues, try again later [!]")
                f.close()
                x = ""
                return None
            elif r2.status_code == 401:
                print("[!] 401 Unauthorized - grabbing new authentication key... [!]")
                refresh_key()
                exit()
            elif 429 in (r1.status_code, r2.status_code):
                global flag
                if flag == 1:
                    print("[!] 429 Too Many Requests - Ratelimited, waiting 1 minute [!]")
                    flag += 1
                    time.sleep(60)
                    eu_west()
                elif flag == 2:
                    flag += 1
                    print("[!] 429 Too Many Requests - Ratelimited, waiting 3 minutes [!]")
                    time.sleep(180)
                    eu_west()
                else:
                    flag += 1
                    print("[!] 429 Too Many Requests - Ratelimited, waiting 30 seconds... [!]")
                    time.sleep(30)
                    eu_west()

            elif 403 in (r1.status_code, r2.status_code):
                if "INVALID_REQUEST_VERSION_OUT_OF_DATE_STATUS" in r2.text:
                    global versionflag
                    if versionflag == 1:
                        versionflag += 1
                        print("[!] VersionBump failed - attempting one last time... [!]")
                        version_bump()
                        eu_west()
                    elif versionflag == 2:
                        versionflag += 1
                        print("[!] VersionBump failed twice - update your request.json [!]")
                        exit()
                    else:
                        versionflag += 1
                        print("[!] 403 Unauthorized - Request clientVersion out of date, attempting VersionBump... [!]")
                        version_bump()
                        eu_west()
                else:
                    print("[!] 403 Unauthorized - Unknown error, send request.json to developer [!]")
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
    print("\n\n=============== EU NORTHWEST ===============")
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
                print("[!] UNAUTHORIZED - GETTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif 429 in (r1.status_code, r2.status_code):
                global flag
                if flag == 1:
                    print("[!] 429 Too Many Requests - waiting 1 minute [!]")
                    flag += 1
                    time.sleep(60)
                    eu_northwest()
                elif flag == 2:
                    flag += 1
                    print("[!] 429 Too Many Requests - waiting 3 minutes [!]")
                    time.sleep(180)
                    eu_northwest()
                else:
                    flag += 1
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
    print("\n\n=============== EU NORTHEAST ===============")
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
                print("[!] UNAUTHORIZED - GETTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif 429 in (r1.status_code, r2.status_code):
                global flag
                if flag == 1:
                    print("[!] 429 Too Many Requests - waiting 1 minute [!]")
                    flag += 1
                    time.sleep(60)
                    eu_northeast()
                elif flag == 2:
                    flag += 1
                    print("[!] 429 Too Many Requests - waiting 3 minutes [!]")
                    time.sleep(180)
                    eu_northeast()
                else:
                    flag += 1
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
    print("\n\n=============== EU CENTRAL ===============")
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
                print("[!] UNAUTHORIZED - GETTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif 429 in (r1.status_code, r2.status_code):
                global flag
                if flag == 1:
                    print("[!] 429 Too Many Requests - waiting 1 minute [!]")
                    flag += 1
                    time.sleep(60)
                    eu_central()
                elif flag == 2:
                    flag += 1
                    print("[!] 429 Too Many Requests - waiting 3 minutes [!]")
                    time.sleep(180)
                    eu_central()
                else:
                    flag += 1
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
    print("\n\n=============== EU SOUTHWEST ===============")
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
                print("[!] UNAUTHORIZED - GETTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif 429 in (r1.status_code, r2.status_code):
                global flag
                if flag == 1:
                    print("[!] 429 Too Many Requests - waiting 1 minute [!]")
                    flag += 1
                    time.sleep(60)
                    eu_southwest()
                elif flag == 2:
                    flag += 1
                    print("[!] 429 Too Many Requests - waiting 3 minutes [!]")
                    time.sleep(180)
                    eu_southwest()
                else:
                    flag += 1
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
    print("\n\n=============== EU SOUTHEAST ===============")
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
                print("[!] UNAUTHORIZED - GETTING NEW AUTH KEY [!]")
                refresh_key()
                exit()
            elif 429 in (r1.status_code, r2.status_code):
                global flag
                if flag == 1:
                    print("[!] 429 Too Many Requests - waiting 1 minute [!]")
                    flag += 1
                    time.sleep(60)
                    eu_southeast()
                elif flag == 2:
                    flag += 1
                    print("[!] 429 Too Many Requests - waiting 3 minutes [!]")
                    time.sleep(180)
                    eu_southeast()
                else:
                    flag += 1
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

def main():
    try:
        auth_get()
    except Exception as e:
        print(f"Error updating headers with authorization key: \n\n {e}")
        
    try:
        eu_west()
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

main()
