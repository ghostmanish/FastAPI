# FastAPI
In this repository I have use FastAPI + Docker + Postman. In this you will receive FastAPI application and postman collection to test the API.

To run this application

If you want to run it in docker container the n use these command.

```
git clone https://github.com/ghostmanish/FastAPI.git
cd FastAPI
docker-compose -f .\docker-compose.yml build
docker-compose -f .\docker-compose.yml up
```
If you want to run it in your host machine then use following command.

```
git clone https://github.com/ghostmanish/FastAPI.git
cd FastAPI
pip install -r requirements.txt
uvicorn app:app --reload --host=127.0.0.1 --port=80
```

These are two way to run this application.

And for testing Open the post man import the collection **``FastAPI-Basics-Postman-Collection.postman_collection``**

And Enjoy

# FASTAPI + Docker + Postman
