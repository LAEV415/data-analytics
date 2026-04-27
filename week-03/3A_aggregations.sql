USE northwind;

-- 1.Write a query to find the price of the cheapest item that Northwind sells. Then write a
-- second query to find the name of the product that has that price.

SELECT min(DISTINCT UnitPrice) -- finding lowest price
FROM products;

SELECT ProductName, UnitPrice -- pulling product name of lowest priced item
FROM products
WHERE UnitPrice = (
	SELECT min(DISTINCT UnitPrice)
	FROM products
    );
    
-- 2.Write a query to find the average price of all items that Northwind sells.
-- (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
-- using the ROUND function to round the average price to the nearest cent.)

SELECT avg(UnitPrice) -- calculating avg price of all items
FROM products;

SELECT ROUND(AVG(UnitPrice), 2) -- rounding to the nearest cent
FROM products;

-- 3.Write a query to find the price of the most expensive item that Northwind sells. Then
-- write a second query to find the name of the product with that price, plus the name of
-- the supplier for that product.

SELECT max(UnitPrice)
FROM products;

SELECT ProductName, CompanyName Supplier, UnitPrice
FROM products p
JOIN suppliers s
ON p.SupplierID = s.SupplierID
WHERE UnitPrice = (
	SELECT max(UnitPrice)
	FROM products
	);
    
-- 4.Write a query to find total monthly payroll (the sum of all the employees’ monthly
-- salaries).

SELECT sum(Salary)
FROM employees;

-- 5.Write a query to identify the highest salary and the lowest salary amounts which any
-- employee makes. (Just the amounts, not the specific employees!)

SELECT max(salary), min(salary)
FROM employees;

-- 6.Write a query to find the name and supplier ID of each supplier and the number of
-- items they supply. Hint: Join is your friend here.

SELECT p.SupplierID, ContactName, count(Distinct ProductName) AS numOfItems -- by using distinct we avoid repeated items
FROM suppliers s
JOIN products p
ON s.SupplierID = p.SupplierID
GROUP BY ContactName, SupplierID;

-- 7.Write a query to find the list of all category names and the average price for items in
-- each category.

SELECT CategoryName Category, avg(UnitPrice) avgPrice
FROM categories c
JOIN products p
ON c.CategoryID = p.CategoryID
GROUP BY CategoryName;

-- 8.Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
-- is the name of each supplier and the number of items they supply.

SELECT ContactName, count(Distinct ProductName) AS numOfItems -- by using distinct we avoid repeated items
FROM suppliers s
JOIN products p
ON s.SupplierID = p.SupplierID
GROUP BY ContactName
HAVING count(Distinct ProductName) >= 5;

-- 9.Write a query to list products currently in inventory by the product id, product name,
-- and inventory value (calculated by multiplying unit price by the number of units on
-- hand). Sort the results in descending order by value. If two or more have the same
-- value, order by product name. If a product is not in stock, leave it off the list.

SELECT ProductID, ProductName, (unitPrice * UnitsInStock) AS inventoryValue
FROM products
WHERE UnitsInStock > 0
ORDER BY inventoryValue DESC, ProductName;


