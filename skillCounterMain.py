import requests
from bs4 import BeautifulSoup
import math
import pandas as pd
import time

# response = requests.get("https://www.linkedin.com/jobs/search/?currentJobId=4200885089&keywords=Software%20Engineer&origin=JOBS_HOME_KEYWORD_SUGGESTION&refresh=true")
# reponse1 = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=SWE&location=United%20States&geoId=100293800&currentJobId=3415227738&position=1&pageNum=0&start=25"

# with open('job.txt', 'w', encoding='utf-8') as fp:
#     fp.write(html)


# linkedInURL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=SWE&location=Las%20Vegas,%20Nevada,%20United%20States&geoId=100293800&currentJobId=3415227738&position=1&pageNum=0&start=25"


l=[]
o={}
k=[]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
target_url='https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python%20%28Programming%20Language%29&location=Las%20Vegas%2C%20Nevada%2C%20United%20States&geoId=100293800&currentJobId=3415227738&start={}'
for i in range(0,math.ceil(117/25)):

    res = requests.get(target_url.format(i))
    soup=BeautifulSoup(res.text,'html.parser')
    alljobs_on_this_page=soup.find_all("li")
    print(len(alljobs_on_this_page))
    for x in range(0,len(alljobs_on_this_page)):
        jobid = alljobs_on_this_page[x].find("div",{"class":"base-card"}).get('data-entity-urn').split(":")[3]
        l.append(jobid)

target_url='https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/'

print(l)




for j in range(0, len(l)):
    # time.sleep(2)
    jobID = l[j]
    checkingURL = target_url+jobID
    res=requests.get(checkingURL)
    soup=BeautifulSoup(res.text, 'html.parser')
    jobListing=soup.find_all("section")
    # jobDesc = soup.find("section",{"class":"show-more-less-html"})
    jobDesc = soup.find("div",{"class":"show-more-less-html__markup show-more-less-html__markup--clamp-after-5 relative overflow-hidden"})
    o["jobID"]=jobID
    o["jobDesc"]=jobDesc
    k.append(o)
    o = {}
    


df = pd.DataFrame(k)
df.to_csv('linkedinjobs.csv', index=False, encoding='utf-8')
print(k)



# for j in range(0,len(l)):

#     resp = requests.get(target_url.format(l[j]))
#     soup=BeautifulSoup(resp.text,'html.parser')

#     try:
#         o["company"]=soup.find("div",{"class":"top-card-layout__card"}).find("a").find("img").get('alt')
#     except:
#         o["company"]=None

#     try:
#         o["job-title"]=soup.find("div",{"class":"top-card-layout__entity-info"}).find("a").text.strip()
#     except:
#         o["job-title"]=None

#     try:
#         o["level"]=soup.find("ul",{"class":"description__job-criteria-list"}).find("li").text.replace("Seniority level","").strip()
#     except:
#         o["level"]=None



#     k.append(o)
#     o={}

# df = pd.DataFrame(k)
# df.to_csv('linkedinjobs.csv', index=False, encoding='utf-8')
# print(k)