import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

"""
part 01

| s   | x | y |
|-----|---|---|
| 'g' | 3 | 9 |
| 'v' | 5 | 7 |
| 'f' | 8 | 7 |
"""
data = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

# drop table for fresh run
query_drop = "DROP TABLE IF EXISTS demo;"
curs.execute(query_drop)

# create table
query_create = """
    CREATE TABLE demo (
        s TEXT NOT NULL,
        x TEXT NOT NULL,
        y TEXT NOT NULL
    );
"""

curs.execute(query_create)

# insert data
query_insert = """
    INSERT INTO demo VALUES(?, ?, ?)
"""

curs.executemany(query_insert, data)

# check
query_select = 'SELECT * FROM demo;'

result = curs.execute(query_select).fetchall()
print(result)

# commit
conn.commit()

"""
- Count how many rows you have - it should be 3!
- How many rows are there where both `x` and `y` are at least 5?
- How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
  `DISTINCT`)?
"""

query_1 = "SELECT COUNT(*) FROM demo;"
result_1 = curs.execute(query_1).fetchone()
print('result_1: ', result_1)
# output: result_1:  (3,)

query_2 = """
    SELECT COUNT(*) FROM demo d WHERE d.x >= 5 AND d.y >= 5;
    """
result_2 = curs.execute(query_2).fetchone()
print('result_2: ', result_2)
# output: result_2:  (2,)

query_3 = "SELECT COUNT(DISTINCT y) FROM demo"
result_3 = curs.execute(query_3).fetchone()
print('result_3: ', result_3)
# output: result_3:  (2,)
