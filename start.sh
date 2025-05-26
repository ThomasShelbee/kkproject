docker compose up --build -d
sudo docker cp kk:/app/frontend/dist .
sudo chown -R www-data:www-data dist
sudo chmod -R 777 dist
