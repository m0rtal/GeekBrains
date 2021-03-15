-- Практическое задание по теме “Хранимые процедуры и
-- функции, триггеры"

-- Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от
-- текущего времени суток. С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с
-- 12:00 до 18:00 функция должна возвращать фразу "Добрый день", с 18:00 до 00:00 — "Добрый
-- вечер", с 00:00 до 6:00 — "Доброй ночи".


DROP FUNCTION IF EXISTS hello;
DELIMITER //
CREATE FUNCTION hello()
RETURNS TEXT DETERMINISTIC
BEGIN
	IF HOUR(NOW()) BETWEEN 6 AND 11 THEN
		RETURN "Доброе утро!";
	END IF;
	IF HOUR(NOW()) BETWEEN 12 AND 17 THEN
		RETURN "Добрый день!";
	END IF;	
	IF HOUR(NOW()) BETWEEN 18 AND 23 THEN
		RETURN "Добрый вечер!";
	END IF;	
	IF HOUR(NOW()) BETWEEN 0 AND 5 THEN
		RETURN "Доброй ночи!";
	END IF;	
END//

DELIMITER ;
SELECT hello();



-- В таблице products есть два текстовых поля: name с названием товара и description с его
-- описанием. Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля
-- принимают неопределенное значение NULL неприемлема. Используя триггеры, добейтесь
-- того, чтобы одно из этих полей или оба поля были заполнены. При попытке присвоить полям
-- NULL-значение необходимо отменить операцию.

USE shop;
-- триггер по вставке с пустыми полями
DROP TRIGGER IF EXISTS not_null_insert;
DELIMITER //
CREATE TRIGGER not_null_insert BEFORE INSERT ON products
FOR EACH ROW
BEGIN 
	IF (NEW.name IS NULL) AND (NEW.description IS NULL) THEN
		SET NEW.name = "dummy data";
	END IF;
END//
DELIMITER ;


-- триггер по попытке обновления пустым полем
DROP TRIGGER IF EXISTS not_null_update;
DELIMITER //
CREATE TRIGGER not_null_update BEFORE UPDATE ON products
FOR EACH ROW
BEGIN 
	IF (NEW.name IS NULL) OR (NEW.description IS NULL) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'UPDATE cancelled, field should be NOT NULL';
	END IF;
END//
DELIMITER ;

-- втавим пустые данные
INSERT INTO products (price, catalog_id)
VALUES (100, 1);

-- обновим пустыми данными
UPDATE products 
SET name = NULL
WHERE id = 1;

UPDATE products 
SET description = NULL
WHERE id = 1;


-- проверим
SELECT *
FROM products p ;