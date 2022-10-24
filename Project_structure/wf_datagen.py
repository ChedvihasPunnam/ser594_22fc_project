import requests
from bs4 import BeautifulSoup
import regex as re
import pandas as pd

url = 'https://aws.amazon.com/sitemaps/sitemap_blogs/'

r = requests.get(url)

page_data_soup = BeautifulSoup(r.text, 'lxml')

links = []
for i in page_data_soup.find_all('loc'):
    links.append(i.text)


def check_reg(rgx, text):
    if re.search(rgx, text):
        return True
    else:
        return False


allow_rules = [r"https://aws.amazon.com/blogs/aws/.+"]
deny_rules = [r".+/author/.*", ".+/page/.*", r".+/tag/.*", r".+/category/.*"]
new_links = []
for link in links:
    out = True
    for rule in allow_rules:
        out = out and check_reg(rule, link)
    for rule in deny_rules:
        out = out and not (check_reg(rule, link))
    if out:
        new_links.append(link)


data = []
for link in new_links:
    temp = {}
    r = requests.get(link)
    page_data_soup = BeautifulSoup(r.text, 'html.parser')
#     print(i.text)
    temp['Website'] = 'AWS'
    temp['Title'] = page_data_soup.find(class_="lb-h2 blog-post-title").text
    temp['Link'] = link

    for blog_data in page_data_soup.findAll(class_="blog-post-content"):
        temp_data = ''
        for i in blog_data.findAll('p'):
            temp_data = temp_data + i.text

        temp['content'] = temp_data
        data.append(temp)

#########################################################Facebook Data########################################33
url = 'https://engineering.fb.com/sitemap-1.xml'

r = requests.get(url)

page_data_soup = BeautifulSoup(r.text, 'lxml')

links = []
for i in page_data_soup.find_all('loc'):
    links.append(i.text)

allow_rules = [r"https://engineering.fb.com/.+"]
deny_rules = [r"https://engineering.fb.com/codeofconduct/"]
new_links = []
for link in links:
    out =True
    for rule in allow_rules:
        out = out and check_reg(rule,link)

    for rule in deny_rules:
        out = out and not(check_reg(rule,link))
    if out:
 
        new_links.append(link)
        
#data = []
for link in new_links:
    
    temp = {}
    r = requests.get(link)
    page_data_soup = BeautifulSoup(r.text, 'html.parser')
    temp['Website'] = 'Facebook'
    temp['Title'] = page_data_soup.find(class_='entry-title').text
    
    temp['Link'] = link
    
    for blog_data in page_data_soup.findAll(class_ = "entry-content" ):
        temp_data = ''
        for i in blog_data.findAll('p'):
            temp_data = temp_data + i.text
        
    
        temp['content'] = temp_data
        data.append(temp)        





df = pd.json_normalize(data)

df.to_csv('data_original/Blog-data-original.csv',index=False)





