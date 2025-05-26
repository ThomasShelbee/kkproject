cp flask_app.nginx.conf /etc/nginx/sites-enabled/kkbackend.nginx.conf
certbot --nginx -d kkbackend.silaeder.codingprojects.ru
certbot --nginx -d kk.silaeder.codingprojects.ru
