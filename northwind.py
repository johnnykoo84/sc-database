import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

"""
- What are the ten most expensive items (per unit price) in the database?
- What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
- (Stretch) How does the average age of employee at hire vary by city?
"""

query_1 = """
    SELECT DISTINCT(p.ProductName) FROM OrderDetail od
    INNER JOIN Product p on od.ProductId = p.id
    ORDER BY od.UnitPrice LIMIT 10;
"""

result_1 = curs.execute(query_1).fetchall()
print('question 1: ', result_1)

query_2 = """
    SELECT AVG(strftime('%Y', 'now') - strftime('%Y', BirthDate)) 
     - (strftime('%m-%d', 'now') < strftime('%m-%d', BirthDate) )
     FROM employee;
"""

result_2 = curs.execute(query_2).fetchone()
str = float(''.join(str(ele) for ele in result_2))
print('\nquestion 2: ', f'{str:.2f}')
