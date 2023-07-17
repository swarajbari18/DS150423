CREATE DATABASE IF NOT EXISTS assignment_1;
USE assignment_1;
CREATE TABLE SalesPeople (
Snum int,
Sname char(20),
City char(10),
Comm int,
PRIMARY KEY(Snum)
);

CREATE TABLE Customers (
Cnum int,
City char(10),
Snum int,
PRIMARY KEY(Cnum),
FOREIGN KEY(Snum) REFERENCES SalesPeople(Snum)
);
-- forgot to add a colomn here, so that's why I did the below steps
-- Sir if you have a better way to rectify this then please share it with us
ALTER TABLE Customers
ADD COLUMN Cname char(10) NOT NULL AFTER Cnum;


CREATE TABLE orders (
Onum int PRIMARY KEY,
Cnum int,
Snum int,
FOREIGN KEY(Cnum) REFERENCES Customers(Cnum),
FOREIGN KEY(Snum) REFERENCES SalesPeople(Snum)
);

INSERT INTO SalesPeople VALUES (1001,'Peel','London',12);
INSERT INTO SalesPeople VALUES (1002,'Serres','Sanjose',13);
INSERT INTO SalesPeople VALUES (1004,'Motika','London',11);
INSERT INTO SalesPeople VALUES (1007,'Rifkin','Barcelona',15);
INSERT INTO SalesPeople VALUES (1003,'Axelrod','Newyork',10);
SELECT * FROM SalesPeople;

INSERT INTO Customers VALUES (2001,'Hoffman','London',1001);
INSERT INTO Customers VALUES (2002,'Giovanni','Rome ',1003);
INSERT INTO Customers VALUES (2003,'Liu','Sanjose ',1002);
INSERT INTO Customers VALUES (2004,'Grass','Berlin ',1002);
INSERT INTO Customers VALUES (2006,'Clemens ','London',1001);
INSERT INTO Customers VALUES (2008,'Cisneros ','Sanjose ',1007);
INSERT INTO Customers VALUES (2007,'Pereira ','Rome ',1004);

ALTER TABLE Orders
ADD Odate varchar(10) AFTER Amt;
DESCRIBE Orders;
INSERT INTO Orders VALUES (3001,18.69,'3-10-1990',2008,1007);
INSERT INTO Orders VALUES (3003,767.19,'3-10-1990',2001,1001);
INSERT INTO Orders VALUES (3002,1900.10,'3-10-1990',2007,1004);
INSERT INTO Orders VALUES (3005,5160.45,'3-10-1990',2003,1002);
INSERT INTO Orders VALUES (3006,1098.16,'3-10-1990',2008,1007);
INSERT INTO Orders VALUES (3009,1713.23,'4-10-1990',2002,1003);
INSERT INTO Orders VALUES (3007,75.75,'4-10-1990',2004,1002);
INSERT INTO Orders VALUES (3008,4273.00,'5-10-1990',2006,1001);
INSERT INTO Orders VALUES (3010,1309.95,'6-10-1990',2004,1002);
INSERT INTO Orders VALUES (3011,9891.88,'6-10-1990',2006,1001);
SELECT * FROM Orders;

-- Q1)  no of sales person whose name begins with a/A
SELECT Sname FROM SalesPeople WHERE Sname LIKE 'a%' OR Sname LIKE 'A%';

-- Q2) salesperson whose orders is more than 2000
SELECT Sname, SUM(Amt) AS all_orders 
FROM SalesPeople AS sa 
JOIN Orders AS orr 
ON sa.Snum = orr.Snum 
GROUP BY Sname;

SELECT Sname,all_orders 
FROM (SELECT Sname, SUM(Amt) AS all_orders 
FROM SalesPeople AS sa JOIN Orders AS orr 
ON sa.Snum = orr.Snum 
GROUP BY Sname) AS tab1
WHERE all_orders >= 2000; -- this query will give the answer

-- Q3) salesperson from newyork
SELECT Sname,City FROM SalesPeople WHERE City LIKE 'Newyork';

-- Q4) salespeople belonging to london and paris, there was no paris city sio i also took bacelona
SELECT City,COUNT(Sname) FROM SalesPeople WHERE City IN ('London','Paris') GROUP BY City;

SELECT City,COUNT(Sname) FROM SalesPeople WHERE City IN ('London','Barcelona') GROUP BY City;

-- Q5) no of orders taken by salespeople and thier date
SELECT Sname, Odate, COUNT(Onum) 
FROM Salespeople AS sa
JOIN Orders as orr
ON sa.Snum = orr.Snum
GROUP BY Sname, Odate;
















