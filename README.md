# 🚀 EKS Microservices Platform

A production-style cloud-native microservices platform built using Docker, Kubernetes, Helm, Terraform, AWS EKS, GitHub Actions, Redis, and PostgreSQL.

This project demonstrates modern DevOps workflows including:
- containerization
- Kubernetes orchestration
- Infrastructure as Code (IaC)
- CI/CD automation
- autoscaling
- cloud-native deployments

---

# 🏗 Architecture

```text
GitHub Actions
        ↓
Docker Hub
        ↓
AWS EKS
        ↓
Frontend Service
        ↓
API Service
        ↓
Redis Queue
        ↓
Worker Service
        ↓
PostgreSQL
```

---

# ✨ Features

- ⚡ Microservices architecture
- 🐳 Dockerized services
- ☸ Kubernetes orchestration
- 📦 Helm templating
- 🏗 Terraform infrastructure provisioning
- ☁ AWS EKS deployment
- 🔄 GitHub Actions CI/CD pipeline
- 📬 Redis-based async task queue
- 🗄 PostgreSQL persistence layer
- 📈 Horizontal Pod Autoscaling (HPA)
- 📊 Kubernetes metrics monitoring
- 🌐 Public LoadBalancer deployment

---

# 🧩 Services Overview

| Service | Purpose |
|---|---|
| Frontend | User interface |
| API Service | Backend REST API |
| Worker | Background task processor |
| Redis | Queue/message broker |
| PostgreSQL | Persistent database |

---

# 🔄 Async Processing Workflow

1. User submits task
2. API stores task in PostgreSQL
3. API pushes task into Redis queue
4. Worker consumes task asynchronously
5. Worker processes task
6. Database updates status/result
7. Frontend displays latest result

---

# ⚙ Tech Stack

- Python
- Flask
- Docker
- Kubernetes
- Helm
- Terraform
- AWS EKS
- GitHub Actions
- Redis
- PostgreSQL

---

# 🚀 CI/CD Workflow

```text
git push
    ↓
GitHub Actions
    ↓
Docker image build
    ↓
Push to Docker Hub
    ↓
Connect to AWS EKS
    ↓
Helm deployment
    ↓
Automatic Kubernetes rollout
```

---

# 📈 Horizontal Pod Autoscaling

Implemented Kubernetes HPA using Metrics Server.

The API service automatically scales based on CPU utilization.

Example:
- CPU load increased beyond threshold
- Kubernetes scaled API replicas from 1 → 3 automatically

---

# 📸 Screenshots

## Application Running on AWS EKS

![Application UI](screenshots/app-ui.png)

---

## GitHub Actions CI/CD Pipeline

![GitHub Actions](screenshots/github-actions.png)

---

## Kubernetes Horizontal Pod Autoscaling

![HPA](screenshots/hpa-autoscaling.png)

---

## AWS EKS Cluster

![EKS Cluster](screenshots/eks-cluster.png)

---

# 🧠 Challenges Faced & Lessons Learned

- Managed resource constraints on t3.small infrastructure
- Solved Kubernetes networking and service discovery issues
- Handled Helm ownership conflicts
- Debugged Git rebase and merge conflicts
- Optimized monitoring stack for low-resource clusters
- Resolved Terraform dependency cleanup issues
- Implemented autoscaling under generated load

---

# 🎯 Key Learnings

- Kubernetes orchestration
- Infrastructure as Code (Terraform)
- Helm templating
- GitHub Actions CI/CD
- AWS EKS deployments
- Horizontal Pod Autoscaling
- Distributed systems architecture
- Cloud-native networking
- Infrastructure optimization

---

# 👨‍💻 Author

Built as part of a cloud-native & DevOps engineering learning journey.