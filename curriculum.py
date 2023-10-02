import requests
from bs4 import BeautifulSoup
import json
import sys
import os

if len(sys.argv) < 2:
    print("Using: python script.py <URL anahtarı>")
    sys.exit(1)

input = sys.argv[1]
data_folder = "public"
json_data = os.path.join(data_folder, "url.json")


with open(json_data, "r", encoding='utf8') as json_file:
    parsed_data = json.load(json_file) 

url = parsed_data.get(input)

url = 'http://www.bologna.yildiz.edu.tr' + url

response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content,"html.parser")


f = open("courses.json", "r")

courses = soup.find("div", {"id": "semesters"})

curriculum = []
 

b = 1   
for semester in courses.find_all("tr"):

    if "table_semester_heading" in semester.get("class", []):
        donem = {
            "donem_adi": f'{b}.Dönem' ,
            "dersler": []
        }
        b += 1 

    a = 0
    ders = {}
    for columns in semester.find_all("td"):
        
        if a == 0:
            ders["kodu"] = columns.text.strip()
            #print("Ders Kodu:",columns.text.strip())
        elif a == 1:
            img_tag = columns.find("img")
            if img_tag and 'title' in img_tag.attrs:
                columns = img_tag['title']
                ders["onkosul"] = columns.split(' ')[0]
                print("Bağlı Ders Adı:",columns.split(' ')[0])
        elif a == 2:    
            ders["adi"] = columns.text.strip()
            #print("Ders Adı:",columns.text.strip()) 
        elif a == 3:
            ders["saati"] = columns.text.strip()
            #print("Ders Saati:",columns.text.strip())
        elif a == 4:
            ders["uygulama"] = columns.text.strip()
            #print("Uygulama:",columns.text.strip())
        elif a == 5:
            ders["laboratuvar"] = columns.text.strip()
            #print("Laboratuar:",columns.text.strip())
        elif a == 6:
            ders["kredi"] = columns.text.strip()
            #print("Yerel Kredi:",columns.text.strip())
        elif a == 7:
            ders["akts"] = columns.text.strip()
            #print("AKTS:",columns.text.strip())
            donem["dersler"].append(ders)
            ders = {}
        a += 1             
        
    if "total_ects" in semester.get("class", []):
        curriculum.append(donem) 

    if "program_total_ects" in semester.get("class", []):
        #print("Toplam AKTS bulundu.")
        break
       
lectures = json.dumps(curriculum, indent=4, ensure_ascii=False) 
with open("courses.json", "w", encoding='utf8') as json_dosyasi:
    json_dosyasi.write(lectures)
