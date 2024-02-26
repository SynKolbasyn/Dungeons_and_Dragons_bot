from os import getenv

import psycopg


user = getenv("POSTGRES_USER")
password = getenv("POSTGRES_PASSWORD")
db_name = getenv("POSTGRES_PLAYERS_DB")


def check_database(cur: psycopg.Cursor | psycopg.ServerCursor) -> None:
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS players
        (id bigint, first_name text, last_name text, full_name text, username text, state text);
        """
    )


def get_data(id: int, first_name: str, last_name: str, full_name: str, username: str) -> dict:
    with psycopg.connect(f"host=players_database port=5432 user={user} password={password} dbname={db_name}") as conn:
        with conn.cursor() as cur:
            check_database(cur)

            cur.execute(
                f"""
                SELECT id, first_name, last_name, full_name, username, state FROM players WHERE id = {id}
                """
            )
            res = cur.fetchone()
            if not res:
                result = {
                    "id": id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "full_name": full_name,
                    "username": username,
                    "state": "Choosing a race"
                }
                cur.execute(
                    f"""
                    INSERT INTO players (id, first_name, last_name, full_name, username, state)
                    VALUES (
                    '{result["id"]}',
                    '{result["first_name"]}',
                    '{result["last_name"]}',
                    '{result["full_name"]}',
                    '{result["username"]}',
                    '{result["state"]}'
                    )
                    """
                )
                return result
            return {
                "id": res[0],
                "first_name": res[1],
                "last_name": res[2],
                "full_name": res[3],
                "username": res[4],
                "state": res[5]
            }
