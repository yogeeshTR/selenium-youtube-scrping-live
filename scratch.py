response =requests.get(YOUTUBE_TRENDING_URL )

print("status code:",response.status_code)

print("Output:" ,response.text)

with open ("trending.html",'w' )as f:
  f.write(response.text)

from bs4 import BeautifulSoup

doc = BeautifulSoup(response.text , 'html.parser')

print("page title:",doc.title.text)

video_divs =doc.find_all("div",class_ = "ytd-video-renderer")

print(f'Found{len(video_divs)} videos')

print(video_divs)

print("hello")