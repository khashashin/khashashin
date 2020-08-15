#!/bin/bash
COMPOSE="/usr/local/bin/docker-compose --no-ansi"
DOCKER="/usr/bin/docker"

cd /home/khashashin/khashashin/

$COMPOSE run certbot renew && $COMPOSE kill -s SIGHUP nginx
$DOCKER system prune -af

# create following cron job
# 0 12 * * * /home/khashashin/khashashin/nginx/ssl_renew.sh >> /home/khashashin/khashashin/nginx/logs/cert-renew.log 2>&1