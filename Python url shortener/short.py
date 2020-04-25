import requests

def urlShortner(link):
	try:
		url = 'https://rel.ink/api/links/'
		obj = {'url':link}
		response  = requests.post(url,data=obj)
		fin = 'https://rel.ink/'+response.json()['hashid']
		return fin
	except Exception as e:
		return e

link = input('Enter a url: ')
print(urlShortner(link))