-- Практическое задание по теме “Транзакции, переменные, представления”

-- В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных.
-- Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте
-- транзакции.

START TRANSACTION;
-- вставляем в БД sample, таблицу users...
INSERT INTO sample.users
(
-- ...данные о пользователе с id 1 из БД shop, таблицы users
	SELECT u.id, u.name
	FROM shop.users u
	WHERE u.id=1
);

-- удаляем данные о пользователе с id=1 из shop.users
DELETE FROM shop.users u
WHERE
	u.id = 1;

-- завершаем транзакцию
COMMIT;




-- Создайте представление, которое выводит название name товарной позиции из таблицы
-- products и соответствующее название каталога name из таблицы catalogs.

-- создадим представление
CREATE OR REPLACE VIEW shop.catalogue AS
-- выберем нужные колонки и подпишем их
SELECT p.name AS product, c.name AS `section`
FROM shop.products p 
-- объединим с каталогом так, чтобы видеть все товары
LEFT JOIN shop.catalogs c 
ON p.catalog_id = c.id;

-- проверим, что получилось
SELECT product, `section` FROM shop.catalogue;




-- Пусть имеется таблица с календарным полем created_at. В ней размещены
-- разряженые календарные записи за август 2018 года '2018-08-01', '2016-08-04', '2018-08-16' и
-- 2018-08-17. Составьте запрос, который выводит полный список дат за август, выставляя в
-- соседнем поле значение 1, если дата присутствует в исходном таблице и 0, если она
-- отсутствует.

-- создаём БД
DROP TABLE IF EXISTS example.calendar;
CREATE TABLE example.calendar (
	id SERIAL PRIMARY KEY,
	dates DATE DEFAULT NULL
);
-- наполняем значениями
INSERT INTO example.calendar
VALUES
(NULL, '2018-08-01'), (NULL, '2018-08-04'), (NULL, '2018-08-16'), (NULL, '2018-08-17');

-- создадим представление со всеми датами с 1970 года
CREATE OR REPLACE VIEW example.all_dates AS
SELECT adddate('1970-01-01',t4*10000 + t3*1000 + t2*100 + t1*10 + t0) selected_date FROM
 (SELECT 0 t0 UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9) t0,
 (SELECT 0 t1 UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9) t1,
 (SELECT 0 t2 UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9) t2,
 (SELECT 0 t3 UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9) t3,
 (SELECT 0 t4 UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9) t4
ORDER BY selected_date;

-- дата начала, можно было взять первое значение из таблицы - но чёрт знает, чему оно там может равняться
SET @start_date := '2018-08-01';
-- количество дней в месяце (-1 чтобы не залезть на следующий месяц)
SET @interval_days := DAY(LAST_DAY(@start_date))-1;

-- выбираем все даты
SELECT d.selected_date,
-- и нули/единицы если поле в c.dates не пустое
	CASE
		WHEN c.dates IS NULL THEN 0
		ELSE 1
	END
AS is_in_original_table
-- из таблицы с датами
FROM example.all_dates d
-- объединяем с календарной таблицей так, чтобы остались все даты месяца
LEFT JOIN example.calendar c
ON d.selected_date = c.dates
-- оставляем только даты месяца
WHERE d.selected_date
-- от начальной даты
BETWEEN @start_date 
-- до конечной даты месяца
	AND DATE_ADD(@start_date, INTERVAL @interval_days DAY)
ORDER BY d.selected_date;


-- Пусть имеется любая таблица с календарным полем created_at. Создайте
-- запрос, который удаляет устаревшие записи из таблицы, оставляя только 5 самых свежих
-- записей.

-- на мой взгляд, будет проще создать промежуточную таблицу
DROP TABLE IF EXISTS vk.temp;
CREATE TABLE vk.temp AS
-- знаю, что звёздочку нельзя ))
SELECT * 
FROM vk.messages m 
ORDER BY m.created_at DESC
LIMIT 5;

-- и затем "подставить" её на место оригинальной
ALTER TABLE vk.messages RENAME TO vk.messages_old;  -- переименовываем оригинал в запасную таблицу, хотя можно было и дропнуть
ALTER TABLE vk.temp RENAME TO vk.messages;			-- переименовываем временную таблицу в оригинал

-- либо решить так, но это будет дольше:
USE vk; -- почему-то dbeaver ругался на не выбранную БД, до этого места всё ок было
DELETE m1.* 
FROM vk.messages_old m1 -- удаляем все записи из первой таблицы
LEFT JOIN 				-- которых нет во второй таблице
(
	SELECT * 
	FROM vk.messages 
	LIMIT 5
) AS m2
ON m1.id = m2.id
WHERE m2.id IS NULL;

SELECT *
FROM vk.messages_old; 	-- получаем те же 5 записей, только дольше

