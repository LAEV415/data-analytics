USE northwind;

-- 1. What is the product name(s) of the most expensive products?

SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT max(Distinct UnitPrice) FROM products);

-- 2. What is the product name(s) and categories of the least expensive products?

SELECT ProductName, UnitPrice, CategoryName Category -- pulling product name of lowest priced item
FROM products p
JOIN categories c
ON p.CategoryID = c.CategoryID
WHERE UnitPrice = (
	SELECT min(DISTINCT UnitPrice)
	FROM products
    );
    
-- 3.What is the order id, shipping name and shipping address of all orders shipped via
-- "Federal Shipping"?

SELECT OrderID, ShipName, ShipAddress, CompanyName
FROM orders o
JOIN shippers s
ON o.ShipVia = s.ShipperID
WHERE ShipVia = (
	SELECT ShipperID
    FROM shippers
    WHERE CompanyName = "Federal Shipping"
    );
    
-- 4. What are the order ids of the orders that included "Sasquatch Ale"?

SELECT OrderID, products.ProductName
FROM `order details`
JOIN products
ON `order details`.ProductID = products.ProductID
WHERE `order details`.ProductID = (
	SELECT ProductID
    FROM products
    WHERE ProductName LIKE "%Sasquatch Ale%"
    );
    
-- What is the name of the employee that sold order 10266?
SELECT FirstName
FROM employees
WHERE EmployeeID = (
	SELECT EmployeeID
    FROM orders
    WHERE orderID = 10266
    );
    
-- 6. What is the name of the customer that bought order 10266?

SELECT ContactName
FROM customers
WHERE CustomerID = (
	SELECT CustomerID
    FROM orders
    WHERE orderID = 10266
    );

