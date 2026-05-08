<<<<<<< HEAD
# 🚀 EKS Microservices Platform

A cloud-native microservices platform built using **Python, Flask, Docker, Redis, and PostgreSQL**.  
This project demonstrates how modern distributed systems process tasks asynchronously using message queues and background workers.

---

# ✨ Features

- ⚡ Microservices-based architecture
- 🐳 Dockerized services
- 🔄 Asynchronous task processing
- 📬 Redis-based task queue
- 🗄 PostgreSQL persistence layer
- 🌐 Frontend + API communication
- 👷 Background worker processing
- ☁️ Kubernetes & EKS ready structure

---

## Architecture
User → Frontend Service → API Service → Redis Queue → Worker Service → PostgreSQL

---

## 🧩 Services

| Service | Role |
|---|---|
| **🎨 Frontend** | Handles user interaction and displays task status/results |
| **🚀 API** | Receives tasks, persists them to PostgreSQL, and enqueues them in Redis |
| **👷 Worker** | Consumes and processes tasks asynchronously from the Redis queue |
| **📬 Redis** | Lightweight message broker and task queue |
| **🗄 PostgreSQL** | Stores task history, status, and results |

---

## 🐳 Dockerized Microservices

Each service is independently containerized using Docker for:

- portability
- scalability
- environment consistency
- cloud-native deployments

---

## 🔄 Async Workflow

1. User submits a task
2. API stores the task in PostgreSQL
3. API pushes the task into the Redis queue
4. Worker consumes the task asynchronously
5. Worker processes the task and updates the database
6. Frontend displays the latest status and result

---

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **Containerization:** Docker, Docker Compose
- **Queue:** Redis
- **Database:** PostgreSQL
- **Upcoming:** Kubernetes, Helm, AWS EKS, Terraform

---

## 📦 Local Development

```bash
docker compose up --build
```

| Service | URL |
|---|---|
| Frontend | http://localhost:3000 |
| API | http://localhost:8000 |

---

📚 Key Concepts Learned
- Microservices architecture
- Service-to-service communication
- Container networking
- Docker Compose orchestration
- Async background processing
- Redis queue patterns
- Database persistence
- Distributed systems basics

---

## 🚧 Upcoming Improvements

- [ ] Kubernetes manifests
- [ ] Helm chart packaging
- [ ] AWS EKS deployment
- [ ] Terraform infrastructure
- [ ] CI/CD pipeline
- [ ] Monitoring & logging
- [ ] Horizontal scaling

---

## 🎯 Project Goal

The goal of this project is to gain hands-on experience with:

- cloud-native application design
- container orchestration
- scalable backend systems
- modern DevOps workflows

---

## 👨‍💻 Author

Built as part of a cloud-native & DevOps learning journey.
=======
>>>>>>> 920fa48 (feat: deploy microservices platform with kubernetes and helm)
