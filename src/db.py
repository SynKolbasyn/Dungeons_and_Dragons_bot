from os import getenv

import psycopg


user = getenv("POSTGRES_USER")
password = getenv("POSTGRES_PASSWORD")
db_name = getenv("POSTGRES_PLAYERS_DB")


def get_data(id: int, first_name: str, last_name: str, full_name: str, username: str) -> dict:
    with psycopg.connect(f"host=players_database port=5432 user={user} password={password} dbname={db_name}") as conn:
        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT id, first_name, last_name, full_name, username FROM players WHERE id = {id}
                """
            )
            res = cur.fetchone()
            if not res:
                result = {
                    "id": id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "full_name": full_name,
                    "username": username
                }
                cur.execute(
                    f"""
                    INSERT INTO players (id, first_name, last_name, full_name, username)
                    VALUES ('{result["id"]}', '{result["first_name"]}', '{result["last_name"]}', '{result["full_name"]}', '{result["username"]}')
                    """
                )
                return result
            return {
                "id": res[0],
                "first_name": res[1],
                "last_name": res[2],
                "full_name": res[3],
                "username": res[4]
            }
