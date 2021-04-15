import requests
import os
DIR_PATH = '/usr/games/notify_birthday'
try:
    r = requests.get('https://docs.google.com/document/u/4/export?format=txt&id=1MaetdIy3yDCVHEzmD87SGyHquNavWJo3k-RVU7tYE6Q&token=AC4w5Vg4qq7bqDhwXOwmXKAyzpZr7afLzg%3A1586228079190&includes_info_params=true')
    b = r.text
    with open(os.path.join(DIR_PATH,'birthday'), 'w') as f:
            f.write(b)
except Exception as e:
    print(e)
