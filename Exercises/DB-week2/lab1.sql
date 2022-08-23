CREATE DATABASE College;
CREATE TABLE Devices;

INSERT INTO Devices (ID, device_name, price)
VALUES (1, Samsung, 1400);

UPDATE Students
       SET date_of_birth = '1997-10-07'
       WHERE ID = 02;
DELETE FROM Students
            WHERE ID=02;

SELECT first_name, last_name,
  FROM Students
 WHERE ID = '01';
