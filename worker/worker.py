import redis
import psycopg2
import json
import os
import time

REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "postgres")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "tasksdb")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")


def get_redis():
    while True:
        try:
            r = redis.Redis(host=REDIS_HOST, port=6379, db=0)
            r.ping()
            print("Connected to Redis")
            return r
        except redis.exceptions.ConnectionError:
            print("Waiting for Redis...")
            time.sleep(2)


def get_postgres():
    while True:
        try:
            conn = psycopg2.connect(
                host=POSTGRES_HOST,
                database=POSTGRES_DB,
                user=POSTGRES_USER,
                password=POSTGRES_PASSWORD
            )
            print("Connected to PostgreSQL")
            return conn
        except psycopg2.OperationalError:
            print("Waiting for PostgreSQL...")
            time.sleep(2)


def process_task(text):
    """
    Simulated task processing
    """
    time.sleep(3)

    result = text.upper()

    return result


def main():
    redis_client = get_redis()
    conn = get_postgres()

    cursor = conn.cursor()

    print("Worker started. Waiting for tasks...")

    while True:
        _, task_data = redis_client.blpop("tasks_queue")

        task = json.loads(task_data)

        task_id = task["id"]
        text = task["text"]

        print(f"Processing task {task_id}")

        result = process_task(text)

        cursor.execute(
            """
            UPDATE tasks
            SET status = %s,
                result = %s
            WHERE id = %s
            """,
            ("completed", result, task_id)
        )

        conn.commit()

        print(f"Completed task {task_id}")


if __name__ == "__main__":
    main()