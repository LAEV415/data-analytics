USE northwind;

-- Write a query to list the product id, product name, and unit price of every product that
-- Northwind sells. (Hint: To help set up your query, look at the schema preview to see
-- what column names belong to each table. Or use SELECT * to query all columns
-- first, then refine your query to just the columns you want.)

SELECT ProductID, ProductName, UnitPrice
FROM products;

-- Write a query to identify the products where the unit price is $7.50 or less.

SELECT ProductID, ProductName, UnitPrice
FROM products
WHERE UnitPrice <= 7.5;

-- What are the products that we carry where we have no units on hand, but 1 or more
-- units are on backorder? Write a query that answers this question.

SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock = 0 AND UnitsOnOrder >= 1;

-- Examine the products table. How does it identify the type (category) of each item
-- sold? Where can you find a list of all categories? Write a set of queries to answer these
-- questions, ending with a query that creates a list of all the seafood items we carry.

SELECT CategoryID -- How products table identifies the type of each item sold
FROM products;

SELECT CategoryID, CategoryName	-- Where we can find the list of all categories
FROM categories;

SELECT ProductName, CategoryID -- Query that creates a list of all seafood items we carry
FROM products
WHERE CategoryID = 8;

-- Examine the products table again. How do you know what supplier each product
-- comes from? Where can you find info on suppliers? Write a set of queries to find the
-- specific identifier for "Tokyo Traders" and then find all products from that supplier.

SELECT SupplierID -- How we know supplier of each product
FROM products;

SELECT *	-- Where we find info on suppliers
FROM suppliers;

SELECT CompanyName, SupplierID -- Finding ID for Company named 'Tokyo Traders'
FROM suppliers
WHERE CompanyName = "Tokyo Traders";

SELECT ProductName, SupplierID
FROM products
WHERE SupplierID = 4;

-- How many employees work at northwind? What employees have "manager"
-- somewhere in their job title? Write queries to answer each question.

SELECT EmployeeID -- 9 employees work at northwind
FROM employees;

SELECT EmployeeID, Title -- 1 employee has manager in their title
FROM employees
WHERE Title LIKE "%manager%";