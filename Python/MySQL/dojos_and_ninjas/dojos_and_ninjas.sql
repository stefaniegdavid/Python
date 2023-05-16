SELECT * 
from dojos;

INSERT INTO dojos (id, name, created_at, updated_at)
VALUES ('1', 'Stefanie', NOW(), NOW());

INSERT INTO dojos (id, name, created_at, updated_at)
VALUES ('2', 'David', NOW(), NOW());

INSERT INTO dojos (id, name, created_at, updated_at)
VALUES ('3', 'Gucci', NOW(), NOW());

SET SQL_SAFE_UPDATES = 0;
DELETE FROM `dojos_and_ninjas_schema`.`dojos` WHERE (`id` = '1');
DELETE FROM `dojos_and_ninjas_schema`.`dojos` WHERE (`id` = '2');
DELETE FROM `dojos_and_ninjas_schema`.`dojos` WHERE (`id` = '3');

SELECT * 
from dojos;

INSERT INTO dojos (id, name, created_at, updated_at)
VALUES ('1', 'Jake', NOW(), NOW());

INSERT INTO dojos (id, name, created_at, updated_at)
VALUES ('2', 'Emma', NOW(), NOW());

INSERT INTO dojos (id, name, created_at, updated_at)
VALUES ('3', 'Rose', NOW(), NOW());

SELECT *
from ninjas;

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('Kelsea', 'Rogers', '31', NOW(), NOW(), 1);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('Joanna', 'Morales', '50', NOW(), NOW(), 1);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('Sherisa', 'Valdez', '32', NOW(), NOW(), 1);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('Jamile', 'Garcia', '52', NOW(), NOW(), 2);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('Amber', 'Chai', '25', NOW(), NOW(), 2);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('Fatima', 'Flores', '28', NOW(), NOW(), 2);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('Valeria', 'Salazar', '28', NOW(), NOW(), 3);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('Viviana', 'Zendejas', '29', NOW(), NOW(), 3);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('Sergio', 'Lopez', '32', NOW(), NOW(), 3);

SET SQL_SAFE_UPDATES = 0;
DELETE FROM `dojos_and_ninjas_schema`.`dojos` WHERE (`id` = '7');
DELETE FROM `dojos_and_ninjas_schema`.`dojos` WHERE (`id` = '8');
DELETE FROM `dojos_and_ninjas_schema`.`dojos` WHERE (`id` = '9');

SELECT * 
from ninjas 
WHERE dojo_id=1;

SELECT *
from ninjas
WHERE dojo_id=3;

SELECT dojos.*
FROM dojos, ninjas
WHERE ninjas.dojo=dojo_id

SELECT * 
from ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas.id=6;
