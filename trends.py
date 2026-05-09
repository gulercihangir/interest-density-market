from pytrends.request import TrendReq
def get_trends(keyword):
    pytrends = TrendReq(hl = 'en-US', tz=0)
    pytrends.build_payload([keyword], timeframe='today 12-m')
    data = pytrends.interest_by_region(resolution='COUNTRY')
    return data.to_dict()

   
import time
from pytrends.request import TrendReq

def get_trends(keyword):
    pytrends = TrendReq(hl='en-US', tz=0)
    pytrends.build_payload([keyword], timeframe='today 12-m')
    time.sleep(2)
    data = pytrends.interest_by_region(resolution='COUNTRY')
    return data.to_dict()          