-- 1) Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, catalogs и products в таблицу logs 
-- помещается время и дата создания записи, название таблицы, идентификатор первичного ключа и содержимое поля name.

USE shop;
DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
	id SERIAL,
	create_time DATETIME,
	table_name VARCHAR(100),
	pkid BIGINT UNSIGNED,
	name VARCHAR(100)
) ENGINE=Archive;

DROP TRIGGER IF EXISTS users_logging;
DELIMITER //
CREATE TRIGGER users_logging AFTER INSERT ON users
FOR EACH ROW
BEGIN 
	INSERT INTO logs (create_time, table_name, pkid, name)
	VALUES (NEW.created_at , 'users', NEW.id, NEW.name);
END//
DELIMITER ;

DROP TRIGGER IF EXISTS catalogs_logging;
DELIMITER //
CREATE TRIGGER catalogs_logging AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN 
	INSERT INTO logs (create_time, table_name, pkid, name)
	VALUES (NOW(), 'catalogs', NEW.id, NEW.name);
END//
DELIMITER ;

DROP TRIGGER IF EXISTS products_logging;
DELIMITER //
CREATE TRIGGER products_logging AFTER INSERT ON products
FOR EACH ROW
BEGIN 
	INSERT INTO logs (create_time, table_name, pkid, name)
	VALUES (NEW.created_at , 'products', NEW.id, NEW.name);
END//
DELIMITER ;

-- 2) Создайте SQL-запрос, который помещает в таблицу users миллион записей.

DROP PROCEDURE IF EXISTS shop.generate_million;
DELIMITER //
CREATE PROCEDURE shop.generate_million()
BEGIN
	DECLARE cnt INT DEFAULT 0;
	WHILE cnt<1000000 DO
		INSERT INTO users(name, birthday_at) 
		VALUES('dummy user', '1970-01-01' + INTERVAL rand()*10000 DAY);
		SET cnt=cnt+1;
	END WHILE;
END//
DELIMITER ;

CALL shop.generate_million();
