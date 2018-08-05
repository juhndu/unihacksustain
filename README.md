# unihacksustain: Jord
Unihack project 2018
team Members:
  -Euegene Daily
  -John Du
  -Sindri Ingólfsson
  -Jamie Ramjan
  -Bradley Rego




Deploy instructions:

pip3 install requirements.txt
Install postgresql onto computer
username: postgres, password: password123

Create database named "sustaindb2" in postgresql
at host: 127.0.0.1, port: 5433

python3 manage.py runserver


then in sustain/frontend, either

npm run serve, go to localhost:8080/
or nom run build, go to localhost:8000/
