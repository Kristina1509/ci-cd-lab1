
# Book Management API

REST API для керування книгами, розроблений на Python із використанням FastAPI.

## Технології

- Python 3.12
- FastAPI
- Pytest
- Docker
- GitHub
- Azure DevOps
- Docker Hub

## Функціональність

- `GET /api/items` — отримати список книг
- `GET /api/items/{book_id}` — отримати книгу за ID
- `POST /api/items` — створити книгу
- `PUT /api/items/{book_id}` — оновити книгу
- `DELETE /api/items/{book_id}` — видалити книгу

## Запуск тестів

```bash
python -m pytest -v
```

## Створення Docker-образу

```bash
docker build -t book-api:latest .
```

## Запуск контейнера

```bash
docker run -d --name book-api-container -p 8000:8000 book-api:latest
```

Документація API доступна за адресою http://localhost:8000/docs.