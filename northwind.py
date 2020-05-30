import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

"""
Part 2
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

"""
Part 3
What are the ten most expensive items (per unit price) in the database and their suppliers?
What is the largest category (by number of unique products in it)?
(Stretch) Who's the employee with the most territories? Use TerritoryId (not name, region, or other fields) as the unique identifier for territories.
"""

# To be honest, I'm not understanding this question exactly
# expecially at the end, 'and their suppliers'
query_4 = """
    SELECT DISTINCT(p.ProductName), s.CompanyName FROM OrderDetail od
    INNER JOIN Product p on od.ProductId = p.id
    INNER JOIN Supplier s on p.SupplierId = s.id
    ORDER BY od.UnitPrice LIMIT 10;
"""

result_4 = curs.execute(query_4).fetchall()
print('result_4: ', result_4)

query_5 = """
        SELECT p.ProductName, COUNT(DISTINCT p.ProductName) FROM Product p
        INNER JOIN Category c on p.CategoryId = c.id
        GROUP BY c.CategoryName ORDER BY 2 DESC LIMIT 1
"""

result_5 = curs.execute(query_5).fetchone()
print('result 5', result_5)
