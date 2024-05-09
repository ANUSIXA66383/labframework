import os
import time
import sys
import requests
import os
import random
import art
import socket
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def scan_website(url):
    try:
        # Resolve the URL to an IP address
        ip = socket.gethostbyname(url)
        
        # Resolve the IP address to a hostname
        hostname = socket.gethostbyaddr(ip)[0]
        
        # Get the HTTP response code
        response = requests.get(url)
        response_code = response.status_code
        
        # Get the server header
        server_header = response.headers.get('Server')
        
        # Get the content type
        content_type = response.headers.get('Content-Type')
        
        # Get the content length
        content_length = response.headers.get('Content-Length')
        
        # Print the results
        print(f"IP address: {ip}")
        print(f"Hostname: {hostname}")
        print(f"HTTP response code: {response_code}")
        print(f"Server header: {server_header}")
        print(f"Content type: {content_type}")
        print(f"Content length: {content_length}")
        
    except socket.gaierror:
        print("Error: Unable to resolve URL.")


def send_email():
    # Prompt the user for their email address and password
    print("enter email:")
    from_email = input("lab>")
    print("enter your email password")
    from_password = input("lab>")

    # Prompt the user for the recipient's email address and the text to send
    print("email to send:")
    to_email = input("lab>")
    print("text to send:")
    text = input("lab>")

    # Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Email sent from Python"
    msg.attach(MIMEText(text, 'plain'))

    # Send the email using the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

    print("Email sent successfully!")

def resolve_url(url):
    try:
        # Resolve the URL to an IP address
        ip = socket.gethostbyname(url)
        
        # Resolve the IP address to a hostname
        hostname = socket.gethostbyaddr(ip)[0]
        
        return ip, hostname
    except socket.gaierror:
        return None, "Error: Unable to resolve URL."

# 


def spinner():
    print("LoadingLab...")
    spinner_chars = ["-", "\\", "|", "/"]
    for _ in range(10):
        for char in spinner_chars:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")  # backspace
print("WELCOME TO THE LAB:)")
def print_menu():
    print("commands:")
    print("  echo to just test console it print pon to the console")
    print("  clean to clean console")
    print("  help to print it ")
    print("  gennumber to  Generate Random Number")
    print("  dos to  DOS Website")
    print("  textascii to  Text to ASCII Art")
    print("  exit to  Exit")
    print("  ipurl url to ip")
    print("  emailsend send email ")
    print("  scan to print info about website (mini scan website but for penetration testing you need nmap)")
    print("  console to enter linux console. (without zsh or bash its just sh )")
    print("  renamefile to rename file")
    print("  touchfile to create file")
    print("  mkdir to create dir")

print_menu()
def laborotory():
    
    while True:
        
        choice = input("lab>")
        if choice == "gennumber":
            print("Random Number: ", random.randint(1, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
            input("Press Enter to continue...")
        elif choice == "dos":
            print("Enter website to DOS (example: https://example.com): ")
            website = input("lab>")
            while True:
                w = requests.get(website)
                print("Status Code: ", w.status_code)
                time.sleep(1)
        elif choice == "textascii":
            print("Enter text to convert to ASCII Art: ")
            text = input("lab>")
            print(art.text2art(text))
            input("Press Enter to continue...")
        elif choice == "exit":
            print("Exiting...")
            sys.exit()
        elif choice == "ipurl":
            print("enter URL (without http or https)")
            urli = input("lab>")
            ip, hostname = resolve_url(urli)
            if ip and hostname:
                print(f"IP addres: {ip}")
            else:
             print("unable to resolve url")   
        elif choice == "emailsend":
            send_email()
        elif choice == "scan":
            weburlsite = input("lab>")
            scan_website(weburlsite)
        elif choice == "help":
            print_menu()
        elif choice == "clean":
            os.system('clear' if os.name == 'posix' else 'cls')
        elif choice == "console":
            print("enter command, when want to exit, enter exitconsole")
            while True:
                console_command = input("console>")
                if console_command == "exitconsole":
                    laborotory()
                os.system(console_command)
        elif choice == "echo":
            print('pon')
        elif choice == "renamefile":
            print("enter file to rename (path or file in directory where start this program)")
        elif choice == "touchfile":
            print("enter file name:")
            filename = input("lab>")
            os.system("touch " + filename)
        elif choice == "mkdir":
            print("enter dir name:") 
            dirname = input("lab>")
            os.system("mkdir " + dirname)
        


            path1 = input("lab>")
            print("enter new file name")
            path2 = input("lab>")
            os.rename(path1, path2)


        else:
            print("Unknown command. Try again!")
            input("Press Enter to continue...")
        

if __name__ == "__main__":
    spinner()
    laborotory()
