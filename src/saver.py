import psycopg2



def create_database(params: dict, db_name: str) -> None:
    """Создание новой базы данных PostgreSQL с защитой от SQL-инъекций."""
    conn = None
    try:
        # Подключаемся
        conn = psycopg2.connect(**params)
        conn.autocommit = True

        # Формирование запроса
        with conn.cursor() as cur:

            # Закрываем все активные соединения с БД
            cur.execute(f"""
                SELECT pg_terminate_backend(pg_stat_activity.pid)
                FROM pg_stat_activity
                WHERE pg_stat_activity.datname = '{db_name}'
                  AND pid <> pg_backend_pid();
            """)

            cur.execute(f"DROP DATABASE IF EXISTS {db_name}")  # Удаляем БД
            cur.execute(f"CREATE DATABASE {db_name}")  # Создаём БД
        print(f"База '{db_name}' успешно пересоздана!")

    except psycopg2.Error as e:
        print(f"Ошибка при создании БД: {e}")
        raise

    finally:
        if conn:
            conn.close()  # Закрываем соединение


