From python:3
expose 8080

run apt-get clean && apt-get -y update

workdir /taller2
copy requirements.txt ./
run pip install --no-cache-dir -r requirements.txt

copy . .
cmd ["gunicorn", "_b", "0.0.0.0:5000", "main:app"]
