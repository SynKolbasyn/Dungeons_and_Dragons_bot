from os import getenv

import psycopg
from ujson import load


user = getenv("POSTGRES_USER")
password = getenv("POSTGRES_PASSWORD")
db_name = getenv("POSTGRES_PLAYERS_DB")
PROJECT_DIR = getenv("PROJECT_DIR")


with open(f"{PROJECT_DIR}/game_data/resources/zero_player.json", "r", encoding="utf-8") as file:
    ZERO_PLAYER = load(file)

template = ("{}, " * len(ZERO_PLAYER.keys())).format(*(i for i in ZERO_PLAYER.keys()))[:-2]
template_with_types = ""
for i in template.split(", "):
    template_with_types += f"{i} {ZERO_PLAYER[i]["type"]}, "
template_with_types = template_with_types[:-2]


def generate_data_str(data: dict) -> str:
    res = ""
    for j in data.values():
        res += f"'{j}', "
    return res[:-2]


def generate_data_dict(data: tuple) -> dict:
    res = {}
    for key, val in zip(ZERO_PLAYER.keys(), data):
        res[key] = val
    return res


def generate_zero_player() -> dict:
    res = {}
    for key, val in zip(ZERO_PLAYER.keys(), ZERO_PLAYER.values()):
        res[key] = val["val"]
    return res


def get_data(id: int, first_name: str, last_name: str, full_name: str, username: str) -> dict:
    with psycopg.connect(f"host=players_database port=5432 user={user} password={password} dbname={db_name}") as conn:
        with conn.cursor() as cur:
            cur.execute(f"CREATE TABLE IF NOT EXISTS players ();")
            for k, v in zip(ZERO_PLAYER.keys(), ZERO_PLAYER.values()):
                cur.execute(f"ALTER TABLE players ADD COLUMN IF NOT EXISTS {k} {v["type"]};")

            cur.execute(f"SELECT {template} FROM players WHERE id = {id};")
            res = cur.fetchone()

            if res:
                return generate_data_dict(res)

            result = generate_zero_player() | {
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "full_name": full_name,
                "username": username
            }

            cur.execute(
                f"""
                INSERT INTO players ({template})
                VALUES ({generate_data_str(result)});
                """
            )
            return result


def save_data(data: dict) -> None:
    with psycopg.connect(f"host=players_database port=5432 user={user} password={password} dbname={db_name}") as conn:
        with conn.cursor() as cur:
            data_to_update = ""
            for i in data:
                if i != "id":
                    data_to_update += f"{i} = '{data[i]}', "
            cur.execute(f"UPDATE players SET {data_to_update[:-2]} WHERE id = {data["id"]};")
