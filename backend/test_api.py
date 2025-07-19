import requests

img_path = 'test_frame.jpg'  # sample image frame
files = {'frame': open(img_path, 'rb')}
res = requests.post('http://localhost:5000/video_feed', files=files)
print(res.json())
