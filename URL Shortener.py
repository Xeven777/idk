import requests
import json
print()
print("Hi! Let me Shorten your loonnngggg links instantly :)")
print()
print("What do you want?")
print("1. Just shorten my link")
print("2. Shorten my link using my custom code ")

while True :
    choice= int(input("Press 1 or 2 ::  "))
    if choice==1:
        url = input("Enter the long URL: ")
        payload = {'input': url}
        break
    elif choice==2:
        url = input("Enter the long URL: ")
        print("NOTE : Custom codes should consist of 4-32 lowercase letters, numbers, - and/or _ symbols. ")
        print("WHAT IF that custom code has error/ain't available? No worries we got you covered. ")
        print("We'll generate a shortened link normally without errors ! :)")
        cus = input("Enter custom code:")
        payload = { "long": url, "custom": cus, "useFallback": True }
        break
    else:
        print("Wrong Input :( Try again....")

response = requests.post('https://gotiny.cc/api', json=payload)

if response.status_code == 200:
        data = json.loads(response.text)
        short = data[0]['code']
        print("Shortened URL's unique code : ", short)
        print(f"https://gotiny.cc/{short}")
        print("Copy the above URL and paste in the browser and reach your destined page! WooHOO!")
else :
    print("Failed to create short URL. Error code:", response.status_code)
with open("shortened links.txt","a") as f:
    f.write(f"Original : {url}  ---->   Shortened : https://gotiny.cc/{short} \n")
f.close() 
print("Your link has been saved to 'shortened links.txt' in ur files ;) \n")

