import os
from dotenv import load_dotenv
from flask import Flask
import os,requests

app = Flask(__name__)
  
@app.route('/<name>', methods =['GET'])
def home(name):
    api=os.getenv('API-KEY')
    print(api)
    construct_url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api}"
    response = requests.get(construct_url)
    print(response.status_code)

    list_of_data = response.json()
    print(list_of_data)
    
    html_data = f"""
    <table border="1">
    <tr>
        <td>country_code</td>
        <td>coordinate</td>
        <td>temp</td>
        <td>pressure</td>
        <td>humidity</td>
        <td>name</td>
    </tr>
    <tr>
        <td>{str(list_of_data['sys']['country'])}</td>
        <td>{str(list_of_data['coord']['lon']) + ' ' 
                    + str(list_of_data['coord']['lat'])}</td>
        <td>{str(list_of_data['main']['temp']) + 'k'}</td>
        <td>{str(list_of_data['main']['pressure'])}</td>
        <td>{str(list_of_data['main']['humidity'])}</td>
        <td>{str(list_of_data['name'])}</td>
    </tr>

</table>
    """
    return html_data

if __name__ == "__main__":
    app.run(port = 5000,debug=True)
