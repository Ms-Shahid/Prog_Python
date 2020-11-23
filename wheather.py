from tkinter import *
import tkinter as tk 
from datetime import datetime
from PIL import ImageTk , Image 
import requests 
from tkinter import messagebox

class Weather():
    def weather_report(self):

        self.url = "https://community-open-weather-map.p.rapidapi.com/weather"
        self.cityname = self.loc.get(1.0, END)
        self.api_key = '30cb71aff0msh5657a19eb32f5cdp149f50jsndc1d9b047ce9'
        self.data = requests.get(self.url+ self.cityname + '&appid=' + self.api_key).json()


        if self.data['cod'] == '404':
            messagebox.showerror('Error', 'City Not Found !!')

        else:

            self.location['text'] = self.data['name'] + "," +
            self.data['sys']['country']
            self.c = self.data['main']['temp_max'] - 273.15
            self.f = self.c*9/5+32
            self.weather['text'] = self.data['weather'][0]['main']
            self.weather['font'] = ('verdana',20,'bold')
            self.temperature['text'] = f'{self.c}.C \n {self.f}.F'
            self.temperature['font'] = ('verdana', 15, 'bold')
            self.humidity['text'] = self.data['main']['humidity']
            self.humidity['font'] = ('verdana', 15, 'bold')
            self.pressure['text'] = self.data['main']['pressure']
            self.pressure['font'] = ('verdana', 15, 'bold')