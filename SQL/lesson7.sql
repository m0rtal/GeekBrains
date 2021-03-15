USE shop;

-- Составьте список пользователей users, которые осуществили хотя бы один заказ orders в
-- интернет магазине.

-- решаем вложенным запросом 
SELECT
	id, name
FROM
	users
WHERE EXISTS (
	SELECT
		1
	FROM
		orders
	WHERE
		user_id = users.id
);

-- или решаем join'ом
SELECT 
	u.id, u.name, o.updated_at 
FROM 
	users AS u
JOIN
	orders AS o
ON
	u.id = o.user_id;

-- или решаем дедовским способом ))
SELECT
	DISTINCT user_id
FROM orders;



-- Выведите список товаров products и разделов catalogs, который соответствует товару.
SELECT
	p.name AS product, c.name AS 'section' 
FROM
	products p
LEFT JOIN
	catalogs c
ON
	p.catalog_id = c.id;



-- Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label,
-- name). Поля from, to и label содержат английские названия городов, поле name — русское.
-- Выведите список рейсов flights с русскими названиями городов.

DROP TABLE IF EXISTS flights;
CREATE TABLE flights (
id SERIAL PRIMARY KEY,
`from` VARCHAR(100),
`to` VARCHAR(100)
);

INSERT INTO flights (`from`, `to`) VALUES 
('moscow', 'omsk'),
('novgorod', 'kazan'),
('irkutsk', 'moscow'),
('omsk', 'irkutsk'),
('moscow', 'kazan');

DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
`label` VARCHAR(100),
`name` VARCHAR(100)
);

INSERT INTO cities VALUES
('moscow', 'Москва'),
('irkutsk', 'Иркутск'),
('novgorod', 'Новгород'),
('kazan', 'Казань'),
('omsk', 'Омск');

SELECT
-- подставляем города отлёта из справочника
	(SELECT
		name
	FROM
		cities
	WHERE
		`label`=flights.`from`) AS `from`,
-- подставляем города прибытия из справочника
	(SELECT
		name
	FROM
		cities
	WHERE
		`label`=flights.`to`) AS `to`
FROM flights;



-- или решаем джоинами:
SELECT
	c.name AS `from`, c2.name AS `to`
FROM flights f
-- подставляем города отлёта
JOIN cities c 
ON f.`from` = c.label
-- подставляем города прилёта
JOIN cities c2
ON f.`to` = c2.label;

