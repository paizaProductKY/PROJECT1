
import urllib3
import json
import pyperclip

from . import mySetting

def getTweetByText(searchFeild):

    http = urllib3.PoolManager()
    # DeveloperPortalで取得したBearer Token
    key = mySetting.TWITTER_BEARER_TOKEN
    url = 'https://api.twitter.com/2/tweets/search/recent'

    req = http.request('GET',
                    url,
                    headers={'Authorization': 'Bearer '+key},
                    fields=searchFeild
                    )


    result = json.loads(req.data)
    if (req.status == 200):
        if ('meta' in result):
            if(result['meta']['result_count'] > 0):
                txt = result['data'][0]['text'].split('\n')[-4].split(' ')[-2]
                return txt
    else:
        print(req.status)
        print(result['errors'])
