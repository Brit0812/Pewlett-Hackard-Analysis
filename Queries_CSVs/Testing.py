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

CREATE TABLE titles (
  emp_no INT NOT NULL,
  title VARCHAR NOT NULL,
  from_date DATE NOT NULL,
  to_date DATE NOT NULL,
  FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
  PRIMARY KEY (emp_no, from_date)
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

--emp_count by dept_no

SELECT COUNT(ce.emp_no), de.dept_no
--we're getting the emp_no from the current_emp list and the dept_no 
--from the department list- which will be counted 
FROM current_emp as ce 
LEFT JOIN dept_emp as de
--all of the 1st table will be included in the new one
ON ce.emp_no= de.emp_no
GROUP BY de.dept_no;
--we want the people to be grouped by dept/dept_no
--we want the people to be grouped by dept/dept_no
--if we keep running this code- the dept_no will vary in order 
--so below will add to the code to make it uniform

SELECT COUNT(ce.emp_no), de.dept_no
FROM current_emp as ce 
LEFT JOIN dept_emp as de
ON ce.emp_no= de.emp_no
GROUP BY de.dept_no
ORDER BY de.dept_no;
-- pretty and organized! 


SELECT COUNT(ce.emp_no), de.dept_no
INTO Current_emp_Retirement_Count
FROM current_emp as ce 
LEFT JOIN dept_emp as de
ON ce.emp_no= de.emp_no
GROUP BY de.dept_no
ORDER BY de.dept_no;
-- pretty and organized! 
--added the into pull it into a new table and export the CSV

SELECT * FROM salaries
ORDER BY to_date DESC;
--

DROP TABLE emp_info;
SELECT emp_no, first_name, last_name, gender
INTO emp_info
FROM employees
WHERE (birth_date BETWEEN '1952-01-01' AND '1955-12-31')
AND (hire_date BETWEEN '1985-01-01' AND '1988-12-31')

--now make it neat and pretty 
DROP TABLE emp_info;
SELECT e.emp_no, 
	e.first_name,
e.last_name,
	e.gender,
	s.salary, 
	de.to_date
INTO emp_info
FROM employees as e 
INNER JOIN salaries as s 
ON (e.emp_no=s.emp_no)
--adding an addition join- just add it
INNER JOIN dept_emp as de
on(e.emp_no=de.emp_no)
WHERE (e.birth_date BETWEEN '1952-01-01' AND '1955-12-31')
	AND (e.hire_date BETWEEN '1985-01-01' AND '1988-12-31')
	AND (de.to_date= '9999-01-01');



--list of managers per dept
SELECT dm.dept_no,
		d.dept_name,
		dm.emp_no,
		ce.last_name,
		ce.first_name, 
		dm.from_date, 
		dm.to_date
INTO manager_info
FROM dept_manager AS dm
	INNER JOIN departments AS d
		ON (dm.dept_no=d.dept_no)
	INNER JOIN current_emp AS ce 
		ON (dm.emp_no=ce.emp_no)
        
--Deliverable 1
--- we need to collect the data well be using 
SELECT e.emp_no,
       e.first_name,
       e.last_name,
       t.title,
       t.from_date,
       t.to_date
INTO retirement_titles
FROM employees as e
INNER JOIN titles as t 
ON (e.emp_no= t.emp_no)
WHERE (e.birth_date BETWEEN '1952-01-01'AND '1955-12-31')
ORDER BY e.emp_no;

-- Use Dictinct with Orderby to remove duplicate rows
--the dups are on the emp no becasuse theyre apart of 2 depts

SELECT DISTINCT ON (rt.emp_no) 
	rt.emp_no,
	rt.first_name,
	rt.last_name,
	rt.title
    rt.to_date
INTO unique_titles
FROM retirement_titles as rt
WHERE (rt.to_date = '9999-01-01')
--WHERE (t.to_date '9999-01-01')
--do i need the where? the from is pulling already filtered through data
ORDER BY rt.emp_no, rt.to_date DESC;

SELECT COUNT(ut.emp_no),
ut.title
INTO retiring_titles
FROM unique_titles as ut
GROUP BY title 
ORDER BY COUNT(title) DESC;


--Deliverable 2: mentorship
--what makes them qqualifies them for mentorship?
    --born between January 1, 1965 and December 31, 1965
    --is hire date not a factor? only  the actual age?
--whats actually needed?
    --first and last name 
    --birth date
    --hire date
    --current employee 
    --title


SELECT * FROM unique_titles 

SELECT DISTINCT ON (e.emp_no) e.emp_no,
    e.first_name,
    e.last_name,
    e.birth_date,
    de.from_date,
    de.to_date,
    t.title
INTO mentorship_eligibility
FROM employees as e
LEFT OUTER JOIN dept_emp as de
--left outer join is to include unmatched rows from ONE table
ON e.emp_no= de.emp_no
LEFT JOIN titles as t
--returns all rows from the left table, and the matching rows from the right table.
ON e.emp_no= t.emp_no
WHERE (e.birth_date BETWEEN '1965-01-01' AND '1965-12-31')
AND (de.to_date='9999-01-01')
ORDER BY e.emp_no;

SELECT DISTINCT ON (rt.emp_no)
rt.emp_no,
rt.first_name,
rt.last_name,
rt.title,
de.dept_no,
d.dept_name
INTO unique_title_depts
FROM retirement_titles as rt	
INNER JOIN dept_emp as de
ON (rt.emp_no = de.emp_no)
INNER JOIN departments as d 
ON (d.dept_no = de.dept_no)
ORDER BY rt.emp_no, rt.to_date DESC;



SELECT ut.dept_name, ut.title, COUNT(ut.title) 
INTO dept_role_fill 
FROM (SELECT title, dept_name from unique_title_depts) as ut
GROUP BY ut.dept_name, ut.title
ORDER BY ut.dept_name DESC;


SELECT ut.dept_name, ut.title, COUNT(ut.title) 
INTO training_staff
FROM (SELECT title, dept_name from unique_title_depts) as ut
WHERE ut.title IN ('Manager', 'Senior Staff', 'Technique Leader','Senior Engineer')
GROUP BY ut.dept_name, ut.title
ORDER BY ut.dept_name DESC;