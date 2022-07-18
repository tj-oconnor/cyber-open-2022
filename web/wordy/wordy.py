import requests
import time

S = requests.Session()

R = S.get("http://localhost:1337/api/game")

game_id = R.json()["game_id"]

#Incorrect guess on purpose
R = S.post("http://localhost:1337/api/guess",json={"guess":"wordy","game_id":game_id})

#Correct guess with old game ID
R = S.post("http://localhost:1337/api/guess",json={"guess":R.json()["correct_word"],"game_id":game_id})

print(R.text)

