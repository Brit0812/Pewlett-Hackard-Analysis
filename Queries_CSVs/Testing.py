--DROP TABLE departments 

CREATE TABLE departments (
	 PRIMARY KEY (dept_no),
     dept_no VARCHAR(4) NOT NULL,
     dept_name VARCHAR(40) NOT NULL,
     UNIQUE (dept_name)
);

CREATE TABLE employees (
	 emp_no INT NOT NULL,
     birth_date DATE NOT NULL,
     first_name VARCHAR NOT NULL,
     last_name VARCHAR NOT NULL,
     gender VARCHAR NOT NULL,
     hire_date DATE NOT NULL,
     PRIMARY KEY (emp_no)
);


CREATE TABLE dept_emp (
	 emp_no INT NOT NULL,
     dept_no VARCHAR(4) NOT NULL,
     from_date DATE NOT NULL,
     to_date DATE NOT NULL,
FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
FOREIGN KEY (dept_no) REFERENCES departments (dept_no),
    PRIMARY KEY (emp_no, dept_no)
);

CREATE TABLE dept_manager (
dept_no VARCHAR(4) NOT NULL,
    emp_no INT NOT NULL,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
FOREIGN KEY (dept_no) REFERENCES departments (dept_no),
    PRIMARY KEY (emp_no, dept_no)
);

CREATE TABLE salaries (
  emp_no INT NOT NULL,
  salary INT NOT NULL,
  from_date DATE NOT NULL,
  to_date DATE NOT NULL,
  FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
  PRIMARY KEY (emp_no)
);


SELECT * FROM departments;

--issues importing manager 
--import the columns and then the not null- then itll import 
SELECT * FROM dept_manager;

SELECT * FROM employees;

SELECT * FROM salaries;

SELECT first_name, last_name
FROM employees
WHERE birth_date BETWEEN '1952-01-01' AND '1955-12-31';
--90,000 in the list 

--same as above, but narrowing the range 
SELECT first_name, last_name
FROM employees
WHERE birth_date BETWEEN '1952-01-01' AND '1952-12-31';
--around 21,000 in the list 

--This is the group eligable for reterinment AND add hire date
SELECT first_name, last_name
FROM employees
WHERE (birth_date BETWEEN '1952-01-01' AND '1955-12-31')
AND(hire_date between '1985-01-01' AND '1988-12-31');
--41000 elig for ret.

-- Number of employees retiring
--easier than scrolling through the names OR looking at the bottom by the success output 
SELECT COUNT(first_name)
FROM employees
WHERE (birth_date BETWEEN '1952-01-01' AND '1955-12-31')
AND (hire_date BETWEEN '1985-01-01' AND '1988-12-31');

SELECT first_name, last_name
INTO retirement_info
--this is creating a new table from the info gathered 
--create table is more for inital use to import the collected data?
FROM employees
WHERE (birth_date BETWEEN '1952-01-01' AND '1955-12-31')
AND (hire_date BETWEEN '1985-01-01' AND '1988-12-31');

SELECT * FROM retirement_info;

--originally created this table from a query,
--we haven’t formed any connections to other tables 
--and the CASCADE constraint isn’t needed.

DROP TABLE retirement_info;

--new table for ret.info- including emp_no


SELECT emp_no, first_name, last_name
INTO retirement_info
-- into a new table- ret. info
FROM employees 
--where are we pulling the info from
WHERE (birth_date BETWEEN '1952-01-01' AND '1955-12-31')
AND (hire_date BETWEEN '1985-01-01' AND '1988-12-31');
--CHECK the table 
SELECT * FROM retirement_info;

--unite the depts and managers 

SELECT departments.dept_name,
	dept_manager.emp_no,
	dept_manager.from_date, 
	dept_manager.to_date
FROM departments
--1st table joining
INNER JOIN dept_manager 
--the 2nd table joining
ON departments.dept_no= dept_manager.dept_no;
--this is where post will look for matches
--this one doesnt really work because a lot of people 
--dont work with the company anymore 

--use the abv on this code 
SELECT d.dept_name,
	dm.emp_no,
	dm.from_date,
	dm.to_date
FROM departments as d
INNER JOIN dept_manager as dm
ON d.dept_no= dm.dept_no

--join ret.info with dept_emp
--needed to create a dept_emp OR should i have made made my own 
--query? does it matter?
SELECT retirement_info.emp_no,
    retirement_info.first_name,
retirement_info.last_name,
    dept_emp.to_date
FROM retirement_info 
LEFT JOIN dept_emp
--merging to the left- so dept_emp is table 2
ON retirement_info.emp_no= dept_emp.emp_no
--link them on the ON CLAUSE 


--using nicknames= temp so its just less typing 
--practice ret.info
--its the same as above but cleaner and nicer 
SELECT ri.emp_no,
    ri.first_name,
ri.last_name,
    de.to_date
--define the shorter names 
FROM retirement_info as ri
LEFT JOIN dept_emp as de
ON ri.emp_no = de.emp_no;

--new table to hold the info from the retirement table and dep_emp
--this table will show poeple elig. for ret. and CURRENTLY work for the comp

SELECT ri.emp_no, 
	ri.first_name, 
	ri.last_name,
	de.to_date
INTO current_emp
--making the new table
FROM retirement_info as ri 
LEFT JOIN dept_emp as de
ON ri.emp_no= de.emp_no
WHERE de.to_date=('9999-01-01');
--9999-01-01 means we want ALL the current emp
--CANT see the table in the data output- but its perfect on the export


