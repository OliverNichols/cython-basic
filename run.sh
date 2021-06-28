docker rm -f example
docker build -t example .
docker run --name example example