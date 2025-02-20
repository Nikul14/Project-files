 CREATE DATABASE ECommerceSales;
USE ECommerceSales;
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50),
    country VARCHAR(50),
    signup_date DATE
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock_quantity INT
);


CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE OrderDetails (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    subtotal DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Customers VALUES
(1, 'Alice Johnson', 'alice@email.com', 'New York', 'USA', '2023-01-15'),
(2, 'Bob Smith', 'bob@email.com', 'Los Angeles', 'USA', '2022-11-22');

INSERT INTO Products VALUES
(101, 'iPhone 15', 'Electronics', 999.99, 50),
(102, 'MacBook Pro', 'Electronics', 1999.99, 30);

INSERT INTO Orders VALUES
(1001, 1, '2024-02-10', 2999.98),
(1002, 2, '2024-02-11', 999.99);

INSERT INTO OrderDetails VALUES
(1, 1001, 101, 2, 1999.98),
(2, 1002, 102, 1, 999.99);
-- Write SQL Queries for Analysis
SELECT*FROM  Customers ;
SELECT *FROM  Products ;
SELECT*FROM Orders;
SELECT *FROM  OrderDetails;
-- TOTAL SALES PER MONTH
SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
sum(total_amount) as total_sales
from orders
group by month
order by month;

-- best selling products
select p.product_name,
sum(od.quantity) as quantity_sold
from products p 
join OrderDetails od 
on
od.product_id=p.product_id
group by product_name
order by quantity_sold desc
limit 5;

-- Top Customers by Spending:
select c.name,sum(o.total_amount) as total_spending
from Customers c
join  Orders o
on
o.customer_id=c.customer_id
group by c.name
order by total_spending desc
limit 5;

-- Stock Alert for Low Inventory:
select product_name,stock_quantity
from Products 
where stock_quantity<50;

-- Customer Retention Analysis:
select year(signup_date),count(customer_id)
from customers
group by signup_date
order by signup_date;

-- Calculate average order value (AOV)--
select avg(subtotal)
from  OrderDetails
group by order_id
order by order_id;
-- or
select sum(total_amount) / count(order_id) as average_ordervalue
from Orders;

-- Find customers with repeated purchases
select c.name,c.Customer_ID,count(o.order_id) as total_orders
from Orders o
join customers c on o.customer_id=c.Customer_ID
group by c.name,c.Customer_ID
HAVING COUNT(o.order_id) = 1
ORDER BY total_orders DESC;

-- Analyze category-wise sales trends
select  p.product_name,p.category, day(o2.order_date),sum(o.quantity * p.price) as total_sales
from Products p
join OrderDetails o on o.product_id=p.product_id
join  Orders o2 on O.order_id=o.order_id
group by p.category,p.product_name,day(o2.order_date)
order by total_sales desc;

--  Identify Peak Sales Hours
select day(order_date) as sales_day,
count(order_id) as total_orders,
sum(total_amount) as total_sales
from Orders
group by sales_day
order by total_sales;

 

 





















