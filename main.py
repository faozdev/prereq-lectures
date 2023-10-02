import requests
from bs4 import BeautifulSoup
import json
import os

url = 'http://www.bologna.yildiz.edu.tr/index.php?r=program/bachelor'

response = requests.get(url)

html_content = response.content
soup = BeautifulSoup(html_content,"html.parser")
course_code = soup.find("div", {"id": "content"})

data_folder = "public"

dict = {}
data1 = course_code.find('ul')  

for li in data1.find_all("li"):
    inner_ul = li.find('ul')
    if inner_ul:
        inner_li_items = inner_ul.find_all("li")
        for inner_li in inner_li_items:
            a_tag = inner_li.find("a")
            if a_tag and 'href' in a_tag.attrs:
                href_link = a_tag['href']
                department = a_tag.get_text()
                dict.update({department: href_link})
                file_url = os.path.join(data_folder, "url.json")
                with open(file_url, "w", encoding='utf8') as json_file:
                    json_file.write(json.dumps(dict,indent=4, ensure_ascii=False))


data2 = course_code.find('ul')  
dict2 = {}

department = "null"
for index, li in enumerate(data2.find_all("li")):
    if index == 0:
        continue
    for item in li:
        if item.string is not None:
            if "Fakültesi" in item.string:
                faculty = item.string
                if faculty not in dict2:
                    dict2[faculty] = []  
    inner_ul = li.find('ul')
    if inner_ul:
        inner_li_items = inner_ul.find_all("li")
        for item in inner_li_items:
            a_tag = item.find("a")
            if a_tag and 'href' in a_tag.attrs:
                department = a_tag.get_text()
                if department not in dict2.get(faculty, []):
                    dict2.setdefault(faculty, []).append(department)

file_programs = os.path.join(data_folder, "faculty_programs.json")
with open(file_programs, "w", encoding='utf8') as json_file:
    json.dump(dict2, json_file, indent=4, ensure_ascii=False)                

