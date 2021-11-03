docker network create netwrk
docker build -t server .
docker run --network netwrk -p 5000:5000 --name server -v servervol:/serverdata  server