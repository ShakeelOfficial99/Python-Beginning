import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.azadchaiwala.com/')

soup = BeautifulSoup(response.content, 'html.parser')

# find title 
# print(soup.html.head.title)


# find a tags
# print(soup.find_all('a'))



# 

for d in soup.find_all("div", class_= "course-title"):
    print(d)

