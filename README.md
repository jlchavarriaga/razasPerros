# razasPerros
Api para gestionar los diferentes nombres de las razas de perros


http://localhost:8000

Desarrollo
>python -m virtualenv venv  
>venv\Scripts\activate
pip install "fastapi[all]"
pip install sqlalchemy
pip freeze > requirements.txt

docker-compose up   //construir y ejecutar el contenedor.
docker-compose up --build

docker build -t fastapi .
docker run -d --name fastapicontainer -p 8081:80 fastapi