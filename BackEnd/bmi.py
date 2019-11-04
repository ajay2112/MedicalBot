import requests
from bs4 import BeautifulSoup 

#height =input("Enter the height :")
#weight=input("Enter the weight :")
#gender=input("Enter the gender :")
#age=input("Enter age :")
#target_weight=input("Enter the targer weight :")
def bmi(height,weight,gender,age):
    gen=0
    if gen=="male":
        gen=1
    url=("https://www.smartbmicalculator.com/result.html?unit=0&hc={0}&wk={1}&us={2}&ua={3}&ue=1&gk=".format(height,weight,gen,age))
    page = requests.get(url)
    if (page.status_code == 200):
        html = page.content
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find(id="maincol")
        a=soup.find_all("p",{"class":"subhead"})
        b=soup.find_all("p",{"class":"subhead2"})
        flag=1
        flag2=1
        output=""
    for tag in a:
        if (flag<=6):
            output+=(tag.text).upper()
            n=tag.nextSibling.text
            output+="\n"
            output+=n
            output+="\n"
            flag=flag+1
    for tag2 in b:
        if (flag2<=4):
            output+=(tag2.text).upper()
            n=tag2.nextSibling.text
            output+="\n"
            output+=n
            output+="\n"
            flag2=flag2+1
    return output
