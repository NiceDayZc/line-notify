import httpx
import threading
import os

bearer_token = input("bearer_token > ")
Message = input("Message > ")
Thread = input(int("Thread > "))

def a():
    x = httpx.post("https://notify-api.line.me/api/notify",headers={"content-type":"application/x-www-form-urlencoded","Authorization":"Bearer " + bearer_token},data={"message": Message})
    s = [200, 201, 204]
    if x.status_code in s:
        print("cool")
    elif x.status_code == 400:
        print(F"rate limit")

try:
    while True:
        if threading.active_count() < Thread:
            threading.Thread(target=a).start()
except KeyboardInterrupt: os._exit(0)
