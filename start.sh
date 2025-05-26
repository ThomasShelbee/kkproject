docker compose up --build -d
sudo docker cp kk:/app/frontend/dist .
sudo chown -R nikita:nikita dist
sudo usermod -a -G nikita www-data
