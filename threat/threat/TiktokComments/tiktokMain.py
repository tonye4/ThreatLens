from tiktokVideos import get_all_tiktoks
from models import get_reputation_score, comments_analysis
import requests
import json
import time


userLink = "https://www.tiktok.com/@micasousa.pe"

videos = get_all_tiktoks(userLink)


def getComments(videos):
    headers = {
        'accept': '*/**',
        'accept-language': 'en-US,en;q=0.9, fa;q=0.8',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.tiktok.com/explore',
        'sec-ch-ua': '"Google Chrome"; v="129", "Not-A?Brand"; v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }

    all_comments = []

    for post_url in videos:
        post_id = post_url.split("/")[-1]
        comments = []
        comments.append({'post_url': post_url})

        curs = 0

        while True:
            url = f'https://www.tiktok.com/api/comment/list/?WebIdLastTime=1729409061&aid=1988&app_language=en&app_name=tiktok_web&aweme_id={post_id}&browser_language=en-GB&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F128.0.0.0%20Mobile%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=200&cursor={curs}&data_collection_enabled=true&device_id=7427755272205075973&device_platform=web_mobile&focus_state=false&from_page=video&history_len=3&is_fullscreen=true&is_page_visible=true&odinId=7427755310612186117&os=android&priority_region=&referer=&region=CA&screen_height=1146&screen_width=1534&tz_name=America%2FToronto&user_is_login=false&verifyFp=verify_latio6ct_5FzXpKng_5ZAZ_4unS_AkTf_iCW6vWcdOHIQ&webcast_language=en&msToken=qQqwH0ExH-xY6AzFnFs0j_wVEckhRYWRx333JYcTAeFVrG8lEVaWXPdpNNNjLuJEpba7iKL-0zawApLPRqtf5y2izVrEsx1vg5A738_qWf8YDQyUJ7pNcmCvcI9fBer50jhGlZYwgbQHOW3ISBksR6xPhkY=&X-Bogus=DFSzswVuqE0ANJoutQDZ3GhyS0lt&_signature=_02B4Z6wo00001VebAhQAAIDAZDtjuzmji8FXuwaAADL1f2'

            response = requests.get(url=url, headers=headers)
            raw_data = response.json()

            if 'comments' in raw_data:
                for cm in raw_data['comments']:
                    com = cm['share_info']['desc'] if cm['share_info']['desc'] else cm['text']
                    name = cm['user']['nickname'] if cm['user']['nickname'] else "anonymous"
                    comments.append({'name': name, 'comment': com})

            if raw_data.get('has_more') == 1:
                curs += 200
                print('Moving to the next cursor for', post_url)
            else:
                print('No more data available for', post_url)
                break

        all_comments.append({'post_url': post_url, 'comments': comments})

    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(all_comments, f, ensure_ascii=False, indent=4)

    print("\nData has been saved into a JSON file")


getComments(videos)

time.sleep(25)


# Main Execution

# Comments source file
# json_path = 'comments.json'
json_path = 'output.json'

# Run the harmful comment detection: Analyze comments
analyzed_comments = comments_analysis(json_path)
print(analyzed_comments)

# Get the list accounts who are potentially harassing the given account
reputation_scores_df = get_reputation_score(analyzed_comments)
print(reputation_scores_df)
