import requests

url = 'https://en.wikipedia.org/wiki/Special:Random'
r = requests.get(url)
file = open('templates/page.html', 'w')
file.write(r.text)
file.close()

print("I HAVE RUN")
