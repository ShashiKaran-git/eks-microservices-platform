from flask import Flask, request, jsonify
import time
import redis
import psycopg2
import os
import json

app = Flask(__name__)

REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "postgres")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "tasksdb")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")

# Redis connection
redis_client = redis.Redis(host=REDIS_HOST, port=6379, db=0)

# PostgreSQL connection
while True:
    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD
        )
        print("Connected to PostgreSQL")
        break
    except psycopg2.OperationalError:
        print("Waiting for PostgreSQL...")
        time.sleep(2)

cursor = conn.cursor()

# Create tasks table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    status TEXT NOT NULL,
    result TEXT
)
""")
conn.commit()


@app.route("/task", methods=["POST"])
def create_task():
    data = request.get_json()
    text = data.get("text")

    cursor.execute(
        "INSERT INTO tasks (text, status) VALUES (%s, %s) RETURNING id",
        (text, "pending")
    )

    task_id = cursor.fetchone()[0]
    conn.commit()

    task_data = {
        "id": task_id,
        "text": text
    }

    redis_client.rpush("tasks_queue", json.dumps(task_data))

    return jsonify({
        "message": "Task created",
        "task_id": task_id
    })


@app.route("/tasks", methods=["GET"])
def get_tasks():
    cursor.execute("SELECT id, text, status, result FROM tasks")
    rows = cursor.fetchall()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "text": row[1],
            "status": row[2],
            "result": row[3]
        })

    return jsonify(tasks)


@app.route("/")
def home():
    return jsonify({"message": "API Service Running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)