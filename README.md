# CI-CD-REDES
docker --version

mkdir ci-cd-network-demo
cd ci-cd-network-demo


#Construa a imagem Docker
docker build -t network-demo .
obs:
ls

cd ..
ls
=
"Dockerfile
network_test.py
.github/"

docker build -t network-demo .

docker run network-demo



#Execute o container
docker run network-demo

#Teste com falha
result = subprocess.run(["ping", "-c", "2", "10.0.0.2"], capture_output=True, text=True)

docker build -t network-demo .
docker run network-demo