import requests, urllib.parse, json, os, string, random
from faker import Faker


fake = Faker()
agent = fake.safari()


url_random = 61
session_random = 33
urlrandom = ''.join(random.choices(string.ascii_letters + string.digits, k = url_random))
sessionrandom  = ''.join(random.choices(string.ascii_lowercase + string.digits, k = session_random))


for s in range(100):
  cookie = ("PHPSESSID=" + sessionrandom)
  url = f'https://local-shipstatus-gb.com/Finish.php?session={urlrandom}'
  name = fake.name()
  cnum = fake.credit_card_number()
  cexp = fake.credit_card_expire()
  cvv = fake.credit_card_security_code()
  # f = { 'username' : name, 'password' : cnum, 'client_id' : cexp, 'client_secret' : cvv}
  f = {'form_type': 'cc', 'ccname': name, 'ccnum': cnum, 'ccexp': cexp, 'cccvv': cvv}
  urllib.parse.urlencode(f)
  safe_string = urllib.parse.urlencode(f)

  payload = safe_string
  headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://local-shipstatus-gb.com',
    #  'cookie':'PHPSESSID=134ddeae9b576bc8daa0eb412ced6945',
    'cookie': cookie,
    'content-length': '72',
    'accept-language': 'en-GB,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15',
    # 'user-agent': agent,
    'referer': url,
    'accept-encoding': 'gzip, deflate, br'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  if response.status_code == 200:
    print("ok")
  elif response.status_code != 200:
   print(response.status_code)







