#!/usr/local/bin/python3
import subprocess


def ac_power_status():
    """
    Checks the status if my laptop is charging or not. 
    return: True/False
    """
    ac_status = subprocess.Popen(["pmset -g batt"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = str(ac_status.stdout.readlines()[0])
    return ('AC Power' in result)

def send_text_message():
    """
    Sends a text message by using an Apple Script, telling me to "Check AC Power of home-server..."
    return: subprocess status code
    """
    send_message = subprocess.run(['osascript', '-e', 'tell application "Messages" to send "Check AC Power of home-server..." to buddy "<input phone number here>" of service "SMS"'])
    return (send_message.returncode == 0)

def main():
     if not ac_power_status():
        send_text_message()

if __name__ == "__main__":
    main()
