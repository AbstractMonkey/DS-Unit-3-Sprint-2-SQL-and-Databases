import sqlite3

import contextlib

import os
os.system("wget 'https://github.com/AbstractMonkey/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true' ")
os.rename("rpg_db.sqlite3?raw=true", "rpg_db.sqlite3")

# connect to sqlite database
conn = sqlite3.connect("rpg_db.sqlite3")

query_1 = '''
SELECT COUNT(character_id) FROM charactercreator_character;
'''
query_2 = '''
SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;
'''
query_3 = '''
SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;
'''
query_4 = '''
SELECT COUNT(character_ptr_id) FROM charactercreator_mage;
'''
query_5 = '''
SELECT COUNT(character_ptr_id) FROM charactercreator_thief;
'''
query_6 = '''
SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;
'''
query_7 = '''
SELECT COUNT(item_id) FROM armory_item;
'''
query_8 = '''
SELECT COUNT(item_ptr_id) FROM armory_weapon;
'''
query_9 = '''
SELECT COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
'''
query_10 = '''
SELECT COUNT(item_id)
FROM charactercreator_character_inventory
WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
GROUP BY character_id
LIMIT 20;
'''
query_11 = '''
SELECT AVG(items) FROM (
SELECT character_id,
COUNT(item_id) AS items
FROM charactercreator_character_inventory
GROUP BY character_id);
'''
query_12 = '''
SELECT AVG(numweps) FROM (
SELECT COUNT(item_id) as numweps
FROM charactercreator_character_inventory
WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
GROUP BY character_id);
'''

with contextlib.closing(conn.cursor()) as cursor:
	cursor.execute(query_1)
	result_1 = cursor.fetchall()
	print("How many total Characters are there?", result_1)

	cursor.execute(query_2)
	result_2 = cursor.fetchall()
	print("How many clerics?", result_2)

	cursor.execute(query_3)
	result_3 = cursor.fetchall()
	print("How many fighters?", result_3)

	cursor.execute(query_4)
	result_4 = cursor.fetchall()
	print("How many mages?", result_4)

	cursor.execute(query_5)
	result_5 = cursor.fetchall()
	print("How many thieves?", result_5)

	cursor.execute(query_6)
	result_6 = cursor.fetchall()
	print("How many necromancers?", result_6)

	cursor.execute(query_7)
	result_7 = cursor.fetchall()
	print("How many total items?", result_7)

	cursor.execute(query_8)
	result_8 = cursor.fetchall()
	print("How many of the Items are weapons?", result_8)

	cursor.execute(query_9)
	result_9 = cursor.fetchall()
	print("How many Items does each character have?", result_9)

	cursor.execute(query_10)
	result_10 = cursor.fetchall()
	print("How many Weapons does each character have?", result_10)

	cursor.execute(query_11)
	result_11 = cursor.fetchall()
	print("On average, how many Items does each Character have?", result_11)

	cursor.execute(query_12)
	result_12 = cursor.fetchall()
	print("On average, how many Weapons does each character have?", result_12)


conn.close()
