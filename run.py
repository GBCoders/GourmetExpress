from app.routes import app
import requests

url = 'http://localhost:5001/login'
data = {'email': 'gleice@gmail.com', 'password': 'gleice123'}
response = requests.post(url, json=data)

print(response.json())  
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")