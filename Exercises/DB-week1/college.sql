CREATE DATABASE College;
CREATE TABLE Students;

INSERT INTO Students (column_ID,   first_name, last_name, data_of_birth);
VALUES (1, Pedro, Branquinho, 1997-10-08);
INSERT INTO Students (column_ID,   first_name, last_name, data_of_birth);
VALUES (2, Cassandra, Yorker, 1990-03-22);

UPDATE Students
       SET date_of_birth = '1997-10-07'
       WHERE ID = 02;
DELETE FROM Students
            WHERE ID=02;

SELECT first_name, last_name,
  FROM Students
 WHERE ID = '01';
