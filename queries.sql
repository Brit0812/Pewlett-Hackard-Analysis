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
        


