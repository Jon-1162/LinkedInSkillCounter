import requests
from bs4 import BeautifulSoup
# import Scrapy
# import Selenium
# import Playwright

import requests
response = requests.get("https://www.linkedin.com/jobs/search/?currentJobId=4200885089&keywords=Software%20Engineer&origin=JOBS_HOME_KEYWORD_SUGGESTION&refresh=true")
reponse1 = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=SWE&location=United%20States&geoId=100293800&currentJobId=3415227738&position=1&pageNum=0&start=25"
html = response.text
# print(html)

with open('filename.txt', 'w', encoding='utf-8') as fp:
    fp.write(html)

# linkedInURL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=SWE&location=Las%20Vegas,%20Nevada,%20United%20States&geoId=100293800&currentJobId=3415227738&position=1&pageNum=0&start=25"