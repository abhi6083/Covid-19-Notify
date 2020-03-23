from plyer import notification
import requests
import time
#to parse the web data
from bs4 import BeautifulSoup

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        #notify function doesn't support the png file
        app_icon="C:\\Users\\abhishek\\PycharmProjects\\corona_notify\\icon (1).ico",
        timeout=6
    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__=="__main__":
    notifyMe("Abhishek Gupta","Lets stop the spread of corona virus together")
    myHtmlData=getData('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(myHtmlData, 'html.parser')

   # print(soup.prettify( ))
    mystrData=""
    for tr in soup.find_all('tbody')[1].find_all('tr'):
        mystrData+=tr.get_text()
    mystrData=mystrData[1:]
    myList=mystrData.split("\n\n")

    states=['Uttar Pradesh','West Bengal','Kerala','Karnataka']
    for item in myList[0:23]:
        datalist=item.split('\n')
        if datalist[1] in states:
            nTitle='Cases of Covid-19'
            nText=f"State {datalist[1]}\n Indian: {datalist[2]} & Foreign: {datalist[3]}\n Cured: {datalist[4]}\n Deaths: {datalist[5]}"
            notifyMe(nTitle,nText)
            time.sleep(6)