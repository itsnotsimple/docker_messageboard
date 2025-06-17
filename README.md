# 📝 MessageBoard — Мини приложение с Docker Compose

## 📌 Описание

MessageBoard е уеб приложение, съставено от три компонента, които работят заедно чрез Docker Compose:
- Python Flask API за управление на бележки
- HTML/JavaScript интерфейс
- PostgreSQL база за съхранение на данни

---

## 🚀 Стартиране на проекта

```bash
docker compose up --build
```

Услугите ще се стартират автоматично:
- UI: http://localhost:8081
- API: http://localhost:5000/api/notes

---

## 📁 Структура

- `backend/` – Python Flask + SQL скрипт
- `frontend/` – HTML и JS
- `docker-compose.yml` – стартира всички контейнери
- `README.md` – документация

---

## 🧠 Компоненти и комуникация

- `ui` (frontend) праща HTTP заявки към `web` (backend)
- `web` записва и чете данни от `database` (PostgreSQL)
- Всички контейнери са в една Docker мрежа и комуникират чрез имената си

---

## 🐳 Docker образи (примерно)

- `docker build -t <user>/messageboard-backend ./backend`
- `docker build -t <user>/messageboard-frontend ./frontend`

---

## ✅ Готово за качване в:
- GitHub (сорс код и конфигурация)
- Docker Hub (публични образи)

📅 Краен срок: **20.06.2025**