import tkinter as tk
import requests


#background_image=tk.PhotoImage(file='C:\Users\Dell\Documents\Atom projects\GUI APP\bg.jpg')
HEIGHT=500
WIDTH=700


#   d0fa75c06e495a8a7e950726723dc416
#   api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}
def format_response(weather):
    try:
        name= weather['name']
        country= weather['sys']['country']
        desc=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str = 'City: '+ str(name) +'\nCountry Code: '+ str(country)+'\nWeather Description: '+str(desc) +'\nTemperature: '+ str(temp) + '(F)'
    except:
        final_str='There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key= 'd0fa75c06e495a8a7e950726723dc416'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key , 'q':city , 'units':'imperial'}
    response=requests.get(url,params=params)
    weather=response.json()
    label['text']=format_response(weather)


root = tk.Tk()
root.title("Worldwide Weather")
root.iconbitmap("sun.ico")

canvas=tk.Canvas(root, height=HEIGHT , width=WIDTH )
canvas.pack()


#background_label=tk.Label(root,bg=background_image)
#background_label.place(relwidth=1, relheight=1)

welcome = tk.Label(root, text="Welcome to worldwide weather app", bg='yellow')
welcome.pack()

frame=tk.Frame(root, bg='#99ceff',bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(frame, text="Get Weather", bg="gray", font=40, command=lambda:get_weather(entry.get()))
button.place(relx=0.7, rely=0,relwidth=0.3, relheight=1)

entry=tk.Entry(frame, font=40 )
entry.place(relwidth=0.65, relheight=1)

lower_frame= tk.Frame(root,bg='#99ceff',bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('modern',20), anchor='nw', justify='left')
label.place(relx=0, rely=0,relwidth=1, relheight=1)


root.mainloop()
