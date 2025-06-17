# 📝 MessageBoard — Мини уеб проект с Docker Compose

## 📌 Описание

MessageBoard е малко уеб приложение за публикуване на кратки бележки. Състои се от три отделни компонента, контейнеризирани чрез Docker Compose:
- Flask backend, който обработва заявките
- PostgreSQL база данни, която съхранява бележките
- HTML/JS frontend, който комуникира с API и визуализира съдържание

---

## ⚙️ Стартиране на проекта

```bash
docker compose up --build
Достъп:
🌐 Frontend: http://localhost:8081

🧠 API: http://localhost:5000/api/notes

📁 Структура на проекта
bash
Copy
Edit
messageboard/
├── backend/          # Python Flask + init.sql
├── frontend/         # HTML и JS интерфейс
├── docker-compose.yml
└── README.md
🧠 Как работи проектът
Потребителят въвежда бележка във формата (frontend)

Тя се изпраща като POST заявка до backend API

Flask я записва в база PostgreSQL

Всички бележки се извличат и показват в таблица

🔄 Комуникация между компонентите
frontend → прави HTTP заявки към backend

backend → използва psycopg2 за свързване с database

Всички услуги се свързват чрез Docker мрежа, описана в docker-compose.yml

🐳 Публикувани Docker образи
Backend: https://hub.docker.com/r/kursmado/messageboard-backend

Frontend: https://hub.docker.com/r/kursmado/messageboard-frontend

☁️ GitHub хранилище
🔗 https://github.com/itsnotsimple/docker_messageboard
