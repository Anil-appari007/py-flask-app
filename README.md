

# py-flask-app
Sample Web Application with Python Flask

##  Run on local
```bash
pip install flask
```
```bash
python3 app.py
```

## To Run with Docker
```bash
docker build -t flask-app:v1.03 .
```
```bash
docker run --rm -p 5000:5000 --name sample-app flask-app:v1.03
```


### Expected Ouput:
```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000

Press CTRL+C to quit.
192.168.0.112 - - [12/Feb/2023 05:21:25] "GET / HTTP/1.1" 200 -
```