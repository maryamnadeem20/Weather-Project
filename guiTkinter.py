import tkinter 
from tkinter import font
import requests
root= tkinter.Tk()



def respond(weather):
	try:
		name =weather['name']
		country =weather['sys']["country"]
		des =weather['weather'][0]['description']
		temp=weather['main']["temp"]
		feel =weather['main']["feels_like"]
		humid=weather['main']["humidity"]
		final= "City: {}\nCountry: {}\nCondition: {}\nTemperature(°C): {}\nFeels Like: {}\nHumidity: {}\n".format(name, country, des, temp, feel, humid)
		return final
	except:
		return "Problem fatching your query :("
		

def getWeather(city):
	key= "f635db97c686d87f399f346e4a975024"
	url="https://api.openweathermap.org/data/2.5/weather"
	parameters={"APPID": key, "q":city, "units": "Metric"}
	response=requests.get(url, params=parameters)
	weather=response.json()
	label['text']=respond(weather)


canvas=tkinter.Canvas(root, height=700, width=700)
canvas.pack()

bgImage=tkinter.PhotoImage(file="landscape.png")
imgLabel=tkinter.Label(root, image=bgImage)
imgLabel.place(relwidth=1, relheight=1)

frame=tkinter.Frame(root, bg='pink', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry=tkinter.Entry(frame, font=('Roman', 20) )
entry.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button=tkinter.Button(frame, text="Check Weather", font=('Roman', 15) , command=lambda: getWeather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

frame2=tkinter.Frame(root, bg="pink", bd=5)
frame2.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75, anchor='n')

label=tkinter.Label(frame2, font=('Roman', 30))
label.place(relx=0, rely=0, relheight=1, relwidth=1)

root.mainloop()