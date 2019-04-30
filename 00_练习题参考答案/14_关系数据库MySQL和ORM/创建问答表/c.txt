mysql> create table question (
    -> id int primary key auto_increment,
    -> name varchar(64) not null,
    -> content text,
    -> course_id int not null,
    -> foreign key (course_id) references course(id)
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> desc question;
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| name      | varchar(64) | NO   |     | NULL    |                |
| content   | text        | YES  |     | NULL    |                |
| course_id | int(11)     | NO   | MUL | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
