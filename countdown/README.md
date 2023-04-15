# countdown
python web page that shows a countdown to a specific date from a file

python app.py
python app.py -p 5000 -f countdown_dates.txt
python app.py --port 5000 --file countdown_dates.txt

# Docker
docker build .
docker run -p 5000:5000 IMAGE_ID

docker-compose up