docker build -t client .
docker run --network netwrk --name client -v clientvol:/clientdata client