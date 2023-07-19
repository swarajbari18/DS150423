CREATE database IF NOT EXISTS EdYoda;
USE Edyoda;

CREATE TABLE department(
dept_id int,
dept_name varchar(20),
location varchar(30)
);
-- desc is used to get the structure of the table
desc department;   

INSERT INTO department VALUES (1, 'Account Department', 'Mumbai');
desc department;
INSERT INTO department VALUES (2, 'Reasearch', 'Delhi');
INSERT INTO department VALUES (1, 'Sales', 'Ahemdabad');
INSERT INTO department VALUES (1, 'Operations', 'Nagpur');

-- to read information we use select
SELECT * FROM department;
SELECT dept_id,dept_name FROM department;

-- AS operator gives aliases only for this query and not change the databse itself
SELECT dept_id AS DEPARTMENT_ID,dept_name AS DEPARTMENT_NAME FROM department;

-- DISTINCT OPERATOR gives the unique values of a coloumn, you can only use distinct for a single coloumn at a time
SELECT DISTINCT dept_id FROM department;
SELECT DISTINCT location FROM department;

USE edyoda;
CREATE TABLE employee(
empid varchar(10) PRIMARY KEY,
ename varchar(40) NOT NULL,
job varchar(15) NOT NULL,
salary numeric(8,2),
dept_id int
);
desc department;

INSERT INTO employee VALUES('1', 'Jay', 'Accountant', 50000.90, '1');
INSERT INTO employee VALUES('2', 'Sushil', 'Data Engineer', 60000, '2');
INSERT INTO employee VALUES('11', 'Sushil', 'Data Eng', 60000, '2');
INSERT INTO employee VALUES('3', 'Vaishali', 'Sales', 40000.90, '3');
INSERT INTO employee VALUES('4', 'Gowri', 'CEO', 67000.90, '4');
INSERT INTO employee VALUES('5', 'Prasad', 'Data Scientist', 70000.90, '2');
INSERT INTO employee VALUES('6', 'Vjay', 'Data Analyst', 53000.90, '1');
INSERT INTO employee VALUES('7', 'Ajay', 'Accountant', 50000.90, '4');
INSERT INTO employee VALUES('10', 'Ajay', 'Accountant', 50000.90, '4');
INSERT INTO employee VALUES('8', 'Suraj', 'CA', NULL, '3');
INSERT INTO employee VALUES('9', 'Suraj', 'CA', NULL, '3');

SELECT * FROM employee;

-- WHERE clause is used to filter the table using conditions, both logical and mathematical operators
-- write a query to get all employee with name sushil
SELECT * 
FROM employee
WHERE ename = 'Sushil';
-- write a query to get all empployee ids with name sushil
SELECT empid
From employee
WHERE ename = 'Sushil';
-- write a query to get emp name except suhil
SELECT empid, ename
FROM employee
WHERE ename != 'Sushil';
-- write a query to get details of all employee with salary > 50000
SELECT *
FROM employee
WHERE salary > 50000;
-- write a query to get details of all employee with salary > 50000 inclusive
SELECT *
FROM employee
WHERE salary >= 50000;
-- write a query to get names only of all employee with salary < 50000 
SELECT ename
FROM employee
WHERE salary < 50000;
--  write a query to get names only of all employee with salary < 50000 inclusive
SELECT ename
FROM employee
WHERE salary <= 50000;
-- query to get all data with nmae jay and sushil, i.e. more than one conditions
SELECT *
FROM employee
WHERE ename IN ('Sushil', 'Jay');
-- alternatively we can also use OR operator 
SELECT *
FROM employee
WHERE ename = 'Sushil' OR ename = 'Jay';
-- query to get all data with nmae sushil and salary > 50000
SELECT *
FROM employee
WHERE ename = 'Sushil' AND salary > 50000;
-- NOT operator, opposite of that condition, get a query where name is not sushil and salry is greater than 50000
SELECT *
FROM employee
WHERE NOT ename = 'Sushil' AND salary > 50000;
-- get detilas of all employee with salriy range of 50000 to 60000
SELECT *
FROM employee
WHERE salary BETWEEN 50000 AND 60000;
-- LIKE clause: whenever we want to specify something like we want the table of employe
-- whose name starts with J then we use a wildcard operator %
SELECT * 
FROM employee
WHERE ename LIKE '%jay%';

SELECT * 
FROM employee
WHERE ename LIKE '_jay%';

SELECT * 
FROM employee
WHERE job LIKE '%data%';

-- MATHEMATICAL FUNCTION----> min, max, count, sum, avg
SELECT MIN(salary) AS min_sal FROM employee;
SELECT MAX(salary) AS max_sal FROM employee;
SELECT COUNT(salary) FROM employee;
SELECT COUNT(empid) FROM employee WHERE ename IN ('Sushil', 'Jay');
-- count(salry) is 9 but count(empid) is 11 because salary coloumn has two NULL values, so count does not count null values
SELECT SUM(salary) FROM employee;
SELECT AVG(salary) FROM employee;
SELECT SUM(salary)/COUNT(salary) FROM employee;
SELECT empid, ename, salary, salary+(10*salary)/100 AS bonus FROM employee;

-- DELETE 
DELETE FROM employee WHERE empid = '11';
SELECT * FROM employee;
DELETE FROM employee WHERE ename = 'suraj';
SELECT * FROM employee;
-- to disable the safe mode we can also use this code
SET sql_safe_updates = 0; 
TRUNCATE TABLE employee;
SELECT * FROM employee;
DROP TABLE employee;
SELECT * FROM employee;


-- SORTING-----> we use ORDER BY to sort
-- ascending
SELECT *
FROM employee
ORDER BY salary;
-- desecnding
SELECT *
FROM employee
WHERE salary > 50000
ORDER BY salary desc;
-- this desc here is desecnding and not describe

SELECT *
FROM employee
ORDER BY dept_id, ename, empid;
-- you can specify multiple coloumns in ORDER bY

-- LIMITS and OFFSETS
-- the hiearchy of queries is

-- SELECT coloumn_names
-- FROM table_name
-- WHERE condition
-- ORDER coloumn_names
-- LIMIT a_number
-- OFFSET a_number
SELECT *
FROM employee
ORDER BY dept_id , ename
LIMIT 5 ;
-- only shows the staring 5 rows as mentioned
SELECT *
FROM employee
ORDER BY dept_id desc, ename
LIMIT 5 ;
-- shows ending 5 rows

-- OFFSET---> give me the second maximum salary
SELECT salary FROM employee ORDER BY salary desc LIMIT 1;
-- above query will give us the maximum salary, offseting it to oneplace will give us the second maximum salary
SELECT salary FROM employee ORDER BY salary desc LIMIT 1 OFFSET 1;
-- third highest salary
SELECT salary FROM employee ORDER BY salary desc LIMIT 1 OFFSET 2;
-- what offset does is that it omits the given no of rows from the data from the start


-- GROUP BY---> will group the table with similiar values w.r.t. a coloumn
-- hierarchy with group by is
-- -----------------------------
-- SELECT coloumn_names
-- FROM table_name
-- WHERE condition
-- GROUP BY coloumn_names
-- ORDER coloumn_names
-- LIMIT a_number
-- OFFSET a_number
-- ----------------------------------
-- ----------------------------------
SELECT *
FROM employee
GROUP BY dept_id;
-- this will not run as it canoot aggregate other coloumns to a single cloumn,
-- to use group by funcctions we alwys SELECT coloumns with some mathematical function so that it can be reduced to a single entity in that group
SELECT COUNT(empid)
FROM employee
GROUP BY dept_id; 
-- as you can see the above code/query runs successfully, but it is not showing us the dept_id
-- ----------
SELECT dept_id,COUNT(empid) AS no_of_employee
FROM employee
GROUP BY dept_id; 
-- so the coloumn you group by can be SELECT directly without a aggregate function as group by is thre
-- run the above two queries and see the difference

SELECT salary, COUNT(empid)
FROM employee
WHERE salary IN (50000.90, 60000, 70000.90)
GROUP BY salary;

SELECT dept_id, MAX(salary)
FROM employee
GROUP BY dept_id;

SELECT dept_id, MIN(salary)
FROM employee
GROUP BY dept_id;

SELECT dept_id, sum(salary) AS total_salary_expenses_per_dept
FROM employee
GROUP BY dept_id;
-- multiple group by
SELECT dept_id, salary, COUNT(salary)
FROM employee
-- WHERE salary IN (50000.90, 60000)
GROUP BY dept_id, salary;

-- KEYS ---------------------------------------------------------------------------------------------------
-- Index is a unique value which represents every row of a table
-- Primary Key----> it is a coloumn which has all unique and NOT NULL values
-- whenever we create a table with a primary key, table by default considers the primary key as your index
-- but if  we don't have a primary key and have a very big data then we have to create an index, we do that by
SHOW INDEX FROM department;
CREATE INDEX deptindex on department(dept_id, dept_name, location);  -- will crete index on all coloumns, I did'nt want that
SHOW INDEX FROM department;
DROP INDEX deptindex on department;
CREATE INDEX deptindex on department(dept_id);
SHOW INDEX FROM department;
SELECT * FROM department;
SHOW INDEX FROM employee;  -- took primary key as our index automatically

-- UPDATE statement
-- whnever you have to modify the row data
UPDATE employee
SET job = 'Accountant'
WHERE empid = 8;
SELECT * FROM employee;

-- UPDATE is a command to make change inside the table, i.e. the data
-- ALTER is the command to change the structure of the table, i.e. coloumn, Keys, etc
ALTER TABLE employee
ADD location varchar(20);

ALTER TABLE employee
DROP location;

ALTER TABLE employee
RENAME COLUMN location to city ; -- will show some erroe but runs fine

ALTER TABLE employee
MODIFY COLUMN city char(20);

desc employee; -- city has varchar(20)
ALTER TABLE employee
ADD COLUMN location varchar(20);
desc employee; -- now city has char(20)

ALTER TABLE employee
ADD COLUMN location varchar(20);

-- CONSTRAINS
-- --------> NOT NULL
-- --------> UNIQUE
-- --------> PRIMARY KEY
-- --------> FORIEGN KEY

-- VIEW
-- -------> To crate an abstract table of the data
-- -------> To give the access of a table of data without giving the access to the database, for security purposes
-- --------CRATE A VIEW---- of all employee odf dept_id 1 and 2

CREATE VIEW view_employee AS
SELECT * FROM employee WHERE dept_id IN (1,2);

SELECT * FROM view_employee;

-- will replaacee1,2 with 3,4
CREATE OR REPLACE VIEW view_employee AS
SELECT * FROM employee WHERE dept_id IN (3,4);
SELECT * FROM view_employee;

-- will drop the view
DROP VIEW view_employee;

-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
-- ----------- JOINS ---------------------------------------------------------------------------------------------------------------
-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
CREATE TABLE student (
rollno varchar(10) PRIMARY KEY,
sname varchar(10),
age int,
city varchar(10)
);

CREATE TABLE subject (
subid varchar(10),
rollno varchar(10)
);

INSERT INTO subject VALUES ('1','1');
INSERT INTO subject VALUES ('3','2');
INSERT INTO subject VALUES ('2','3');
INSERT INTO subject VALUES ('2','4');
INSERT INTO subject VALUES ('1','5');
INSERT INTO subject VALUES ('3','6');
INSERT INTO subject VALUES ('4',NULL);
INSERT INTO subject VALUES ('5',NULL);


INSERT INTO student VALUES ('1','jay','12','mumbai');
INSERT INTO student VALUES ('2','ajay','12','surat');
INSERT INTO student VALUES ('3','vijay','10','nagpur');
INSERT INTO student VALUES ('4','sanjay','11','jaipur');
INSERT INTO student VALUES ('5','jaya','13','mumbai');
INSERT INTO student VALUES ('6','jayesh','12','kalyan');
INSERT INTO student VALUES ('7','vijaya','13','goa');
INSERT INTO student VALUES ('8','jaywanti','11','bangaluru');

SELECT * FROM student;
SELECT * FROM subject;

-- INNER
SELECT *
FROM student JOIN subject
WHERE student.rollno = subject.rollno;

SELECT *
FROM student as s JOIN subject as su  -- giving aliases is mandatory when using ON instead of WHERE
ON s.rollno = su.rollno;
-- CARTESIAN JOIN
SELECT *
FROM student as s JOIN subject as su; 
-- full join ---------- WE WILL HAVE TO USE UNION like campusx or we can simply use full join
SELECT *
FROM student FULL JOIN subject; -- this works, don't aliasize the table is a mandatory condition here

SELECT *
FROM student FULL JOIN subject
WHERE student.rollno = subject.rollno;  -- full mai where aur on clauses nahi chalte  hai

-- WHERE OR ON KE SATH KARNE KE LIYE HUM LEFT JOIN AUR RIGHT JOIN ALAD ALAG KARKE UN DONO MEI UNION KAR DENGE---campuwsx method


-- NORMALIZATION --------------------------------------------------------------------------------------------------------------------------
-- normalization is a database design technique which help us reduce the data redundncy
-- helpls us eliminate unneccessary/undesired characterset of insertion updation and deletion
-- normalization ensures data is stored logically
-- 1NF
-- 2NF
-- 3NF
-- BCNF(boyes codd normalization Form) 
-- 4NF
-- 5NF
-- ---------   1NF  --------------------
-- each table cell should contain a single value, 
-- each record needs to be unique(combination of all values in a row should not be repeating)
-- ----------------------------- 2NF  ---------------------------------------
-- shold follow all the rules of 1NF
-- should also have a PRIMARY KEY
-- we may have to divide the table into two to make that happen
-- --------------------------- 3NF(third normal form) ------------------------------------
-- first let's see transitive functional dependency--- it means when you change a non-key coloumn then it also demands changes in another non-key coloumn
-- that is non-key members ccannot have a transitive functional dependency
-- for this we create another table to break the dependency
-- 3NF -- always follow 2NF and no transitive functional dependencies
-- ------------------ BCNF(Boyees Codd normalization form) -------------------------------------------------------------------
-- follows 3NF
-- There should not be more than one candidate key
-- nowadys we ignore bcnf as we want two candidate keys to remove duplicate account


-- ------------------------------------------------------------------------------------------------------------------------------------------------------
-- if 1nf had 1 table then 2 nf probably will have more table than that, and similiarly the no of tables will increaase as we go on upto BCNF
-- also when we inner union 2nf tables we get 1nf table, when we inner join 3nf we get 2nf tabkle and so on
-- ------------------------------------------------------------------------------------------------------------------------------------------------------










