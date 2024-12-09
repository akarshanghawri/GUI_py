from tkinter import *  
import requests  
import json  

# Create the main window  
root = Tk()  
root.title("Weather Report")  
root.geometry("400x400")  
root.configure(bg="#f0f0f0")  

# Convert temperature from Kelvin to Celsius  
def kelvin_to_celsius(kelvin):  
    return round(kelvin - 273.15, 2)  

# Fetch and display weather data  
def get_weather():  
    global e  
    city = e.get()  
    e.delete(0, END)  

    if not city:  # Check for empty input  
        result_label.config(text="Please enter a city name.", fg="red")  
        return  

    api_key = "YOUR_API_KEY_HERE"  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"  

    try:  
        api_requests = requests.get(url)  
        api = json.loads(api_requests.content)  

        # Extract and display relevant weather details  
        country = api['sys']['country']  
        temp = kelvin_to_celsius(api['main']['temp'])  
        weather_desc = api['weather'][0]['description'].capitalize()  

        result_label.config(  
            text=f"{city.capitalize()}, {country}\n{temp}°C\n{weather_desc}", fg="black"  
        )  

    except Exception:  # Handle API errors  
        result_label.config(text="City not found or invalid API key.", fg="red")  

# Create input field and buttons  
e = Entry(root, font=("Helvetica", 20), width=30)  
e.pack(pady=20)  

display = Button(root, text="Get Weather", command=get_weather)  
display.pack(pady=20)  

result_label = Label(root, font=("Helvetica", 16), bg="#f0f0f0")  
result_label.pack(pady=20)  

root.mainloop()  
