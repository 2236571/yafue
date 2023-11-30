from flask import Flask, render_template
import requests
from dotenv import load_dotenv,dotenv_values
from sqlalchemy import create_engine,Integer,MetaData,Table,Column,String


metaData=MetaData()

#definicion de tablas
cities = Table ('cities',metaData,
                Column('id',Integer(),primary_key=True,autoincrement=True),
                Column('nombre',String(100),nullable=True,unique=True)
                )

config= dotenv_values('.env')
app = Flask(__name__)
engine= create_engine("sqlite:///wheather.db")



#app = Flask(__name__)
#config = dotenv_values ('.env')

def get_weather_data(city):
    API_KEY = config['API_KEY']
    url=f'https://api.openweathermap.org/data/2.5/weather?q={ city }&appid={API_KEY}&units=metric&lang=es'
    r = requests.get(url).json()
    return r 

@app.route('/clima')
def prueba():
    clima = get_weather_data('Cuenca')
    temperatura = str(clima['main']['temp'])
    descripcion= str(clima['weather'][0]['description'])
    icono= str(clima['weather'][0]['icon'])

    weather = {
            'ciudad':'Cuenca',
            'temperatura': temperatura,
             'descripcion':descripcion,
             'icono':icono
             }  
    return render_template('weather.html',clima=weather)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/clima')
def clima():
    return 'obtener todo la informacion del clima'

if __name__ == '__main__':
    app.run(debug=True)













