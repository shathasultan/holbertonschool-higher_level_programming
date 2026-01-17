-- check if database exist and create second_table
CREATE TABLE IF NOT EXISTS second_table

(id INT PRIMARY KEY,
name VARCHAR(250),
score INT
);

-- insert into second_table
insert into second_table(id, name, score)
values(1,'John',10),(2,'Alex',3),(3,'Bob',14),(4,'George',8)
