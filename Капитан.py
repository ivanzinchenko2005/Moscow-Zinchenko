import sqlite3
import csv


def search_events(place, actor):
    con = sqlite3.connect("cap_events.db")
    cur = con.cursor()
    res = cur.execute("""SELECT * FROM Events""").fetchall()
    res_2 = cur.execute("""SELECT * FROM Crew""").fetchall()
    res_3 = cur.execute("""SELECT * FROM Places""").fetchall()
    answer = []
    for elem in res_2:
        if elem[1] == actor:
            actor_id = elem[0]
    for elem in res_3:
        if elem[1] == place:
            place_id = elem[0]
    for elem in res:
        if elem[2] == place_id and elem[3] == actor_id:
            answer.append([elem[1], elem[4]])
    answer.sort(key=lambda x: x[1], reverse=True)
    answer.sort(key=lambda x: x[0])
    with open("result_events.csv", "w+", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";", quotechar='\"')
        writer.writerow(["event", "damage_profit"])
        writer.writerows(answer)
    con.close()

print('AMOGUS')