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




--Deliverable 3
--Need 2 tables 
---what department and roles need to be fill? 
--whats  needed?
	-- name- first and last 
	-- title 
	-- emp_no 
	-- dept_name
--name of table?
	--dept_roll_fill 
--pull from the retirement_titles 
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
-- to fill would be  different number? 90k vs the retirees which is 70k?



--whos qualified to train?
    --manager 
    -- seniors (staff, engineer, etc)
    --leaders
--are there enough quailed retirees to mentor the next gen emp?

SELECT ut.dept_name, ut.title, COUNT(ut.title) 
INTO training_staff
FROM (SELECT title, dept_name from unique_title_depts) as ut
WHERE ut.title IN ('Manager', 'Senior Staff', 'Technique Leader','Senior Engineer')
GROUP BY ut.dept_name, ut.title
ORDER BY ut.dept_name DESC;
