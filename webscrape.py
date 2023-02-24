from gettext import find
from turtle import clear
import requests
from bs4 import BeautifulSoup
import os

def Get_Prices():
    print("Recieving Prices..")
    if not os.path.exists("PriceZones"):
        os.mkdir("PriceZones")
    
    if not os.path.exists("PriceZones/Tomarrow"):
        os.mkdir("PriceZones/Tomarrow")
        
    
    if not os.path.exists("PriceZones/Tomarrow/SE1"):
        parent_dir = "PriceZones/Tomarrow/"
    
        directory = "SE1"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        with open(parent_dir+directory+"/"+"PriceTable.txt", 'w'): pass
        directory = "SE2"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        with open(parent_dir+directory+"/"+"PriceTable.txt", 'w'): pass
        directory = "SE3"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        with open(parent_dir+directory+"/"+"PriceTable.txt", 'w'): pass
        directory = "SE4"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        with open(parent_dir+directory+"/"+"PriceTable.txt", 'w'): pass
    
    url_path = 'https://www.nordpoolgroup.com/en/Market-data1/Dayahead/Area-Prices/SE/Hourly/?view=table'
    
    def get_marketcap(url_path):
        print("Rendering site..")
        from requests_html import HTMLSession
        session = HTMLSession()
    
        r = session.get(url_path)
    
        r.html.render(wait = 8, sleep = 8)
    
        return r.html
    
    content = get_marketcap(url_path)
    
    sitetext = str(content.html)
    
    tslice = sitetext[sitetext.find("""<div nps-sortable-data-table="" class="ng-scope"><table id="datatable"><thead><tr class="column-headers"><th class="row-name table-time-position sortable-position">"""):sitetext.find("""<div class="dashboard-footer" ng-hide="ctrl.state.loadingTable">""")]
    tslice = tslice[:tslice.find("""<tr class="data-row evenrow extra-row">""")]
    
    
    tslice = tslice.replace("""<div nps-sortable-data-table="" class="ng-scope"><table id="datatable"><thead><tr class="column-headers"><th class="row-name table-time-position sortable-position">""", "" ,1)
    tslice = tslice.replace("""<div class="dashboard-footer" ng-hide="ctrl.state.loadingTable">""", "" ,1)
    tslice = tslice.replace("""</div>""", "")
    tslice = tslice.replace("""<tr class="data-row evenrow">""", "")
    tslice = tslice.replace("""<tr class="data-row oddrow">""", "")
    tslice = tslice.replace("""</th>""", " ")
    tslice = tslice.replace("""<th class="draggable sortable">""", "")
    tslice = tslice.replace("""<td class="row-name">""", "")
    tslice = tslice.replace("""&nbsp;-&nbsp;""", "-")
    tslice = tslice.replace("""</td>""", "")
    tslice = tslice.replace("""<td class="sortable">""", " ")
    tslice = tslice.replace("""</tr>""", " ")
    tslice = tslice.replace("""<tr class="data-row evenrow extra-row">""", "")
    tslice = tslice.replace("""SE1 SE2 SE3 SE4  </thead><tbody>""", "")
    tslice = tslice.replace("00-01", "")
    tslice = tslice.replace("01-02", "")
    tslice = tslice.replace("02-03", "")
    tslice = tslice.replace("03-04", "")
    tslice = tslice.replace("04-05", "")
    tslice = tslice.replace("05-06", "")
    tslice = tslice.replace("06-07", "")
    tslice = tslice.replace("07-08", "")
    tslice = tslice.replace("08-09", "")
    tslice = tslice.replace("09-10", "")
    tslice = tslice.replace("10-11", "")
    tslice = tslice.replace("11-12", "")
    tslice = tslice.replace("12-13", "")
    tslice = tslice.replace("13-14", "")
    tslice = tslice.replace("14-15", "")
    tslice = tslice.replace("15-16", "")
    tslice = tslice.replace("16-17", "")
    tslice = tslice.replace("17-18", "")
    tslice = tslice.replace("18-19", "")
    tslice = tslice.replace("19-20", "")
    tslice = tslice.replace("20-21", "")
    tslice = tslice.replace("21-22", "")
    tslice = tslice.replace("22-23", "")
    tslice = tslice.replace("23-00", "")
    tslice = tslice.replace("""class="future""", "")
    tslice = tslice.replace("""sortable">""", "")
    tslice = tslice.replace("""<td""", "")
    
    SE1 = open("PriceZones/Tomarrow/SE1/PriceTable.txt",'w', encoding="utf-8")
    SE2 = open("PriceZones/Tomarrow/SE2/PriceTable.txt",'w', encoding="utf-8")
    SE3 = open("PriceZones/Tomarrow/SE3/PriceTable.txt",'w', encoding="utf-8")
    SE4 = open("PriceZones/Tomarrow/SE4/PriceTable.txt",'w', encoding="utf-8")
    
    Date = tslice[:10]
    
    tslice = tslice.replace("    ", " ")
    tslice = tslice.replace("   ", " ")
    tslice = tslice.replace("  ", " ")
    tslice = tslice.replace(" ", "", 1)
    
    
    SE1.write(Date+"\n")
    SE2.write(Date+"\n")
    SE3.write(Date+"\n")
    SE4.write(Date+"\n")
    
    Data = tslice[11:]
    
    x = 0
    a = 0
    Zone = 1
    
    while True:
        if a < 10:
            if Zone == 1:
                SE1.write('0'+chr(a+48)+' ')
            if Zone == 2:
                SE2.write('0'+chr(a+48)+' ')
            if Zone == 3:
                SE3.write('0'+chr(a+48)+' ')
            if Zone == 4:
                SE4.write('0'+chr(a+48)+' ')       
        else:
            if Zone == 1:
                SE1.write(str(a)+' ')
            if Zone == 2:
                SE2.write(str(a)+' ')
            if Zone == 3:
                SE3.write(str(a)+' ')
            if Zone == 4:
                SE4.write(str(a)+' ')
            
        while True:
            if Data[x] != ' ':
                if Zone == 1:
                    SE1.write(Data[x])
                if Zone == 2:
                    SE2.write(Data[x])
                if Zone == 3:
                    SE3.write(Data[x])
                if Zone == 4:
                    SE4.write(Data[x])
            x+=1
            if Data[x] == ' ':
                if Zone == 1:
                    SE1.write('\n')
                if Zone == 2:
                    SE2.write('\n')
                if Zone == 3:
                    SE3.write('\n')
                if Zone == 4:
                    SE4.write('\n')
                    a+=1
                Zone+=1
                break
            
            
        if x == (len(Data)-1):
            break
        if Zone == 5:
            Zone = 1
    
    SE1.close()
    SE2.close()
    SE3.close()
    SE4.close()

    print("Prices retrived and stored!")


    

    

    








