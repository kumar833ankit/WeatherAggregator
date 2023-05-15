""" This code is a basic example of web scraping using API 
and also GUI mangement and development  with python   """ 






from tkinter import * #import tkinter
from tkinter import messagebox
  
# function to find weather details
# of any area using openweathermap api
def tell_weather() :
  
    # import required modules
    import requests, json
  
    # enter your api key here
    api_key = "97205bc44ad722755e6615dd8fd4e61c"
          
    # base_url variable to store url
    url = "http://api.openweathermap.org/data/2.5/weather?"


        #***************************************************
  
    # take a area name from area_field entry box
    area_name = area_field.get()
  
    # complete_url variable to store complete url address concatination
    complete_url = url + "appid=" + api_key + "&q=" + area_name
                             
  
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
  
    # json method of response object convert
    # json format data into python format data
    x = response.json()
  
    # now x contains list of  nested dictionaries
    # we know dictionary contains key value pair
    # check the value of "cod" key is equal to "404"
    # or not if not that means area is found
    # otherwise area is not found
    if x["cod"] != "404" :#  indicating the server could not find the requested website.
       
        #"main": {
       #"temp": 280.32,
       #"pressure": 1012,
       #"humidity": 81,
       #"temp_min": 279.15,
       #"temp_max": 281.15
     #},
        # store the value of "main" key in variable y
        y = x["main"]
  
        # store the value corresponding to the "temp" key of y
        current_temperature = y["temp"]
  
        # store the value corresponding to the "pressure" key of y
        current_pressure = y["pressure"]
  
        # store the value corresponding to the "humidity" key of y
        current_humidiy = y["humidity"]
  
        # store the value of "weather" key in variable z
        z = x["weather"]
  
        # store the value corresponding to the "description" key
        # at the 0th index of z 
        weather_description = z[0]["description"]
  
        # insert method inserting the 
        # value in the text entry box. 
        temp_field.insert(15, str(current_temperature) + " Kelvin")
        atm_field.insert(10, str(current_pressure) + " hPa")
        humid_field.insert(15, str(current_humidiy) + " %")
        desc_field.insert(10, str(weather_description) )
  
    # if area is not found                   
    else :
  
        # message dialog box appear which
        # shows given Error meassgae
        messagebox.showerror("Error", "City Not Found \n"
                             "Please enter valid area name")
  
        # clear the content of area_field entry box
        area_field.delete(0, END)
  
  
# Function for clearing the 
# contents of all text entry boxes  
def clear_all() : 
    area_field.delete(0, END)  
    temp_field.delete(0, END)
    atm_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)
  
    # set focus on the area_field entry box 
    area_field.focus_set() 
  
  
# Driver code
if __name__ == "__main__" :
  
    # Create a GUI window
    root = Tk()
  
    # set the name of tkinter GUI window
    root.title("Weather App")
  
    # Set the background colour of GUI window 
    root.configure(background = "grey")
  
    # Set the configuration of GUI window 
    root.geometry("425x175")
    root.resizable(0,0) 
    root.minsize(425, 175)
    root.maxsize(425, 175)
  
    # Create a Weather Gui Application label 
    headlabel = Label(root, text = "Weather Gui Application",
                      fg = 'white', bg = 'green')
      
    # Create a City name : label
    label1 = Label(root, text = "City name : ",
                   fg = 'white', bg = 'black')
      
    # Create a City name : label
    label2 = Label(root, text = "Temperature :",
                   fg = 'white', bg = 'black')
  
    # Create a atm pressure : label
    label3 = Label(root, text = "atm pressure :",
                   fg = 'white', bg = 'black')
  
    # Create a humidity : label
    label4 = Label(root, text = "humidity    :",
                   fg = 'white', bg = 'black')
  
    # Create a description :label
    label5 = Label(root, text = "description  :",
                   fg = 'white', bg = 'black')
      
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure .  
    headlabel.grid(row = 0, column = 1) 
    label1.grid(row = 1, column = 0, sticky ="E") 
    label2.grid(row = 3, column = 0, sticky ="E") 
    label3.grid(row = 4, column = 0, sticky ="E") 
    label4.grid(row = 5, column = 0, sticky ="E") 
    label5.grid(row = 6, column = 0, sticky ="E")
  
  
    # Create a text entry box 
    # for filling or typing the information. 
    area_field = Entry(root) 
    temp_field = Entry(root) 
    atm_field = Entry(root) 
    humid_field = Entry(root) 
    desc_field = Entry(root)
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    # ipadx keyword argument set width of entry space . 
    area_field.grid(row = 1, column = 1, ipadx ="100") 
    temp_field.grid(row = 3, column = 1, ipadx ="100") 
    atm_field.grid(row = 4, column = 1, ipadx ="100") 
    humid_field.grid(row = 5, column = 1, ipadx ="100") 
    desc_field.grid(row = 6, column = 1, ipadx ="100")
  
    # Create a Submit Button and attached 
    # to tell_weather function 
    button1 = Button(root, text = "Scrape Data", bg = "black", 
                     fg = "red", command = tell_weather)
  
    # Create a Clear Button and attached 
    # to clear_all function 
    button2 = Button(root, text = "Clear", bg = "red", 
                     fg = "black", command = clear_all)
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    button1.grid(row = 2, column = 1)
    button2.grid(row = 7, column = 1)
      
    # Start the GUI 
    root.mainloop()