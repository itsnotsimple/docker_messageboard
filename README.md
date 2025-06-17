
# 📝 MessageBoard — Мини уеб проект с Docker Compose

## 📌 Описание

MessageBoard е уеб приложение, което позволява публикуване на кратки бележки от потребителя. Проектът демонстрира как няколко отделни компонента (уеб интерфейс, backend услуга и база данни) могат да работят заедно в изолирана среда чрез Docker Compose.

---

## ⚙️ Стартиране на проекта

```bash
docker compose up --build
Това ще стартира автоматично:

ui (frontend) – достъпен на http://localhost:8081

web (backend Flask API) – достъпен на http://localhost:5000/api/notes

database (PostgreSQL) – обслужва backend-а

🧱 Структура на проекта
bash
Copy
Edit
messageboard/
├── backend/          # Flask API с SQL скрипт
├── frontend/         # HTML + JS уеб интерфейс
├── docker-compose.yml
└── README.md
🧠 Как работи проектът
Потребителят въвежда бележка в уеб формата

JavaScript я изпраща чрез POST към Flask API

API записва в PostgreSQL база (таблица notes)

Всички записани бележки се визуализират в таблица под формата

🔄 Комуникация между компонентите
ui → говори с web през HTTP

web → използва psycopg2 за достъп до database

Docker Compose управлява мрежата между контейнерите

🐳 Публикувани Docker образи

- Backend: https://hub.docker.com/r/kursmado/messageboard-backend
- Frontend: https://hub.docker.com/r/kursmado/messageboard-frontend


☁️ GitHub хранилище
🔗 https://github.com/itsnotsimple/docker_messageboard

