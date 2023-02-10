import requests
import time

url = "http://192.168.2.105:8080/locatorcommand"

data = {
    "network":  "hydra",
    "locator":  "a85b36200037",
    "command":  "start_update",
    "api": "192.168.2.105"
}

count = 0

while True:
    with open("request_log.txt", "a") as log_file:
        response = requests.post(url, json=data)
        count += 1
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if response.status_code == 200:
            log_message = str(count) + " - " + current_time + " - Successful\n"
            log_file.write(log_message)
            print("Successful request")
        else:
            log_message = str(count) + " - " + current_time + " - Failed\n"
            log_file.write(log_message)
            print("Request failed")
    time.sleep(600)
