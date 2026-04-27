USE northwind;

-- 1.Create a single query to list the product id, product name, unit price and category
-- name of all products. Order by category name and within that, by product name.

SELECT ProductID, ProductName, UnitPrice, CategoryName -- only mainly acceptable when column names unique
FROM products
JOIN categories
ON products.CategoryID = categories.CategoryID
ORDER BY CategoryName, ProductName;

-- 2.Create a single query to list the product id, product name, unit price and supplier
-- name of all products that cost more than $75. Order by product name.

SELECT ProductID, ProductName, UnitPrice, CompanyName
FROM products
JOIN suppliers
ON products.SupplierID = suppliers.SupplierID
WHERE UnitPrice > 75
ORDER BY ProductName;

-- 3.Create a single query to list the product id, product name, unit price, category name,
-- and supplier name of every product. Order by product name.

SELECT ProductID, ProductName, UnitPrice, CompanyName, CategoryName,
FROM products p
JOIN suppliers s
ON p.SupplierID = s.SupplierID
JOIN categories c
ON p.CategoryID = c.CategoryID
ORDER BY ProductName;

-- 4.Create a single query to list the order id, ship name, ship address, and shipping
-- company name of every order that shipped to Germany. Assign the shipping company
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
-- shipped to.

SELECT OrderID, ShipName, ShipAddress, CompanyName Shipper
FROM orders o
JOIN shippers s
ON o.Shipvia = s.ShipperID
WHERE ShipCountry = "Germany"
ORDER BY CompanyName, ShipName;

-- 5.Start from the same query as above (#4), but omit OrderID and add logic to group by
-- ship name, with a count of how many orders were shipped for that ship name.

SELECT ShipName, ShipAddress, CompanyName Shipper, Count(ShipName) OrdersPlaced
FROM orders o
JOIN shippers s
ON o.Shipvia = s.ShipperID
WHERE ShipCountry = "Germany"
GROUP BY ShipName, ShipAddress, Shipper
ORDER BY ShipName;

-- 6.Create a single query to list the order id, order date, ship name, ship address of all
-- orders that included Sasquatch Ale.

SELECT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
FROM orders o
JOIN `order details` o2
ON o.OrderID = o2.OrderID
JOIN products p
ON o2.ProductID = p.ProductID
WHERE ProductName LIKE "%Sasquatch Ale%"

