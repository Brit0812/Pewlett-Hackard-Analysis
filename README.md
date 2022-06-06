# Pewlett-Hackard-Analysis

## Overview

The purpose of this analysis is to help Pewlett Hackard get back on track with the organization of their employees, especially those who will be retiring soon. After cleaning and organizing the data, the large company will be able to prepare for the upcoming opening positions, in turn providing clarity on future promotions.  The human resources (HR) department and upper management needs to be aware this information, especially: the identity of the retiring employees and their title(s), the influx of job openings that will need to be filled, once those eligible for retirement retire, and find out who qualifies for their mentorship program. 


To create a schema QuickDBD, allows one to create an ERD (Entity-Relationship Diagram), which is a tool used to depict the relationships within the provided data. The visual provides an outline or a “blueprint” of the correlating relationships between the data.  The ERD assists in the creation of the schema, which is created in PostgreSQL and pgAdmin. The schema creates new tables or CSV, where the data it was cleaned and organized by, that would then be exported and utilized by HR and management. 

(image)

## Results

The first schema to be run, creates a list of the employees who will be retiring soon. When creating a list of the retiring employees the important data to include is: their employee number, their first and last name, their title, and their birth date. The two CSVs/tables that were joined together to create the retirement table was a list of employees and a list of the employees’ titles.

•	 The common denominator between the two tables would be the employee number, which easily visible due to the ERD.  The new table that was created now had 133,776 rows of potential retirees, all of whom have a birth year of 1952 and 1955.

•	 While this data is a great starting point for gathering a list of retirees, there are some issues with the data: duplicate employee numbers. There are duplicate employee numbers because some people received a promotion or changed departments. 

•	Since we have a list of the potential retirees in a CSV, named, retirement_titles, we can now utilize that information to filter or clean the data. The removal of the duplicate employees was done so by using SELECT DISTINCT ON (rt.emp_no) was used since the duplicates were caused by the employee number. The removal of the duplicate employee numbers reduced the total number of retirees significantly, as the duplicates were removed, leaving the new total at 72458.

(image)

•	 The other table created shows each departments retirement count, which would prove useful as HR and management would know the amount of people they’d need to hire in each department.

(image)

The mentorship programs eligible employees need to be collected to begin their new training as people begin to retire. After creating a new schema for its found that there are 1549 eligible mentees, who were born in 1965. 

(image)

## Summary 

The information gathered should provide a lot of clarity into what should be done in regards to future positions that needs to be filled. The number of retirees could be the demise of the company, if a hiring process doesn’t occur to counter the loss of employees. 

The mentorship program would allow those working at the company to gain more experience through the retirees. This would provide immense benefits across the board as employees would understand their roles, equipment, software, and more. 

In the table below (image #) shows the departments that need to be filled as employees begin to retire. The table groups the retirees into their perspective departments and their roles, which would allow HR a visual on the departments that would be impacted. Some departments will suffer more significantly than others, for example: production and development senior engineers total a loss of nearly 26,000 employees.

(image)

When looking for retiring employees to mentor the upcoming generation and their endeavors with the company the data was filters by people with the following titles: managers, senior (staff, engineers, etc.), and leaders. After their titles were pulled, which would, in theory, make them the most qualified they were them grouped by their department and a count. There is a great number of potential mentors, to assist in the development of the future employees. 

(image)
 
