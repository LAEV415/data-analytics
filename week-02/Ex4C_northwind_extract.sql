-- a) The name of the table that holds the items that northwind sells is 'products'
-- b) The name of the table that holds the types/categories of the items Northwind sells is 'categories'

SELECT * FROM employees;
-- The Northwind employee whose name makes it look like she is a bird is 'Peacock'

SELECT * FROM products;
-- My query returns 77 records. I can change my query to retrieve only 10 rows by clicking the dropdown menu and selecting 'Limit to 10 rows'

SELECT * FROM categories;
-- The category ID for seafood is 8.

SELECT OrderID, OrderDate, ShipName, ShipCountry 
FROM orders
ORDER BY OrderID DESC
LIMIT 50;