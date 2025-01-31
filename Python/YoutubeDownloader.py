import requests

link = input("Youtube Link (in format https://www.youtube.com/watch?v=ViDeOiDhEre): ")

video_id = link[-11:]
get_video_token_url = "https://www.youtube.com/get_video_info?&video_id={}".format(video_id)

request = requests.get(get_video_token_url)

if request.status_code == 200:
    print(request.text)
else:
    print(f"Try Again. Something wrong. Status Code: {request.status_code}")
    print(get_video_token_url)
    # ill figure out error, need sleep now
    exit()
