# -*- coding: utf-8 -*-

from selenium import webdriver
import csv
                                            
driver = webdriver.Edge(executable_path=r"D:\edgedriver_win64\edgedriver_win64\msedgedriver.exe")
driver.get("https://www.amazon.in/gp/bestsellers/books/")
products = driver.find_elements_by_xpath("//div[@class='a-cardui _p13n-zg-list-grid-desktop_style_grid-cell__1uMOS p13n-grid-content']")

mylist = []
with open("books.csv",'w',encoding='utf-8',newline='') as csvfile:
    writing = csv.writer(csvfile, delimiter=',')
    writing.writerow(['book','price'])
    for i in products:
        if len((i.text).split("\n")) > 5:
            mylist = (i.text).split("\n")
            writing.writerow([mylist[1],mylist[5]])

                
