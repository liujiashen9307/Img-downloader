import os,requests
from bs4 import BeautifulSoup
url = 'http://xkcd.com'              # starting url
os.makedirs('xkcd', exist_ok=True) 
######Another method of url: url.endwith(), it is used to identify the final component of url##
while not url.endswith('#'):
    res = requests.get(url)
    content=res.content
    soup=BeautifulSoup(content,"html.parser")
    comicURL=soup.select("div #comic img")
    if len(comicURL)==0:
        print("No Comic in this page")
    else:
        try:
            URL_Comic="http:"+comicURL[0].get("src")
            request=requests.get(URL_Comic)
            imageFile = open(os.path.join('xkcd', os.path.basename(URL_Comic)), 'wb')
            for chunk in request.iter_content(100000):
                imageFile.write(chunk)                    
        except Exception:
            print("Comic Skipped")
            Previous_link=soup.select('a[rel="prev"]')[0]
            url='http://xkcd.com'+Previous_link.get('href')            
            continue
    Previous_link=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+Previous_link.get('href')
        
    