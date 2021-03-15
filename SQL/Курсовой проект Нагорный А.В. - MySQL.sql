/*
Текстовое описание БД и решаемых ею задач

Разрабатываемая БД предназначена для моего телеграм бота @TRSSP_bot, 
который работает как агрегатор новостей по каналам rss, с расширением стандартных 
функций подписки до возможности учитывания лайков, сохранением постов, 
автоматического парсинга сайтов и автоматического же перевода ключевых новостей
с использованием биржи фрилансеров etxt.ru.     
*/

DROP DATABASE IF EXISTS main;
CREATE DATABASE main;
USE main;


-- Таблица пользователей хранит id пользователя в telegram. 
-- Возможно, в будущем будет расширена дополнительными сведениями о пользователе.
DROP TABLE IF EXISTS users;
CREATE TABLE users (
id SERIAL PRIMARY KEY,
user_name VARCHAR(100));

-- для сохранения RSS-фидов и избегания дублирования записей заведём таблицу с фидами
-- ключ UNIQUE автоматически создаёт индекс по колонке feed
CREATE TABLE IF NOT EXISTS feeds (
id SERIAL PRIMARY KEY, 
feed VARCHAR(255) UNIQUE);

-- для возможности автоматической обработки новостей заведём таблицу с правилами обработки
CREATE TABLE IF NOT EXISTS feed_processing_rules (
id SERIAL PRIMARY KEY, 
rule VARCHAR(255) UNIQUE);

-- для хранения подписок пользователя создадим таблицу подписок
-- таблица ссылается на правила обработки, таблицу пользователей и таблицу фидов
-- а также имеет Primary Key из двух полей (user_id и feed_id)
-- для ограничения одного пользователя одной уникальной подпиской
-- и для индексации по этим полям
CREATE TABLE IF NOT EXISTS subscriptions (
user_id BIGINT UNSIGNED NOT NULL, 
feed_id BIGINT UNSIGNED NOT NULL, 
rule_id BIGINT UNSIGNED DEFAULT 1, 
CONSTRAINT ixpk PRIMARY KEY (user_id, feed_id), 
FOREIGN KEY (user_id) REFERENCES users(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE, 
FOREIGN KEY (feed_id) REFERENCES feeds(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE, 
FOREIGN KEY (rule_id) REFERENCES feed_processing_rules(id) 
ON UPDATE CASCADE 
ON DELETE SET NULL);

-- бот, получая данные из RSS фида, будет сохранять ссылки на новости в таблице ссылок
-- которая ссылается на таблицу RSS фидов
CREATE TABLE IF NOT EXISTS links (
id SERIAL PRIMARY KEY, 
feed_id BIGINT UNSIGNED NOT NULL, 
link VARCHAR(255), 
FOREIGN KEY (feed_id) REFERENCES feeds(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE);


-- собрав все обновлённые ссылки, бот будет получать их краткое описание для предоставления
-- подписчику, сохраняя описания в таблице описаний и ссылаясь на таблицу ссылок
CREATE TABLE IF NOT EXISTS descriptions (
link_id BIGINT UNSIGNED PRIMARY KEY, 
description VARCHAR(2550), 
FOREIGN KEY (link_id) REFERENCES links(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE);

-- статистика отправленных пользователям сообщений будет вестись в таблице sent_posts,
-- ссылающейся на пользователя и обработанную ссылку
CREATE TABLE IF NOT EXISTS sent_posts (
user_id BIGINT UNSIGNED NOT NULL, 
link_id BIGINT UNSIGNED NOT NULL, 
is_sent BIT DEFAULT 0, 
FOREIGN KEY (user_id) REFERENCES users(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE, 
FOREIGN KEY (link_id) REFERENCES links(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE, 
CONSTRAINT ixpk PRIMARY KEY (user_id, link_id));

-- "лайкнутые" новости будем хранить в таблице лайков,
-- ссылающейся на пользователя и ссылку
CREATE TABLE IF NOT EXISTS likes (
id SERIAL PRIMARY KEY, 
user_id BIGINT UNSIGNED NOT NULL, 
link_id BIGINT UNSIGNED NOT NULL, 
liked BIT DEFAULT 0, 
FOREIGN KEY (user_id) REFERENCES users(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE, 
FOREIGN KEY (link_id) REFERENCES links(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE);

-- помеченные для дальнейшей работы новости будем также хранить в отдельной таблице,
-- ссылающейся на пользователя и ссылку
CREATE TABLE IF NOT EXISTS marked (
id SERIAL PRIMARY KEY, 
user_id BIGINT UNSIGNED NOT NULL, 
link_id BIGINT UNSIGNED NOT NULL, 
marked BIT DEFAULT 0, 
FOREIGN KEY (user_id) REFERENCES users(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE, 
FOREIGN KEY (link_id) REFERENCES links(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE);

-- заведём таблицу для спарсенного контента
-- ссылающуюся на пользователя и ссылку
CREATE TABLE IF NOT EXISTS parsed (
id SERIAL PRIMARY KEY, 
link_id BIGINT UNSIGNED NOT NULL, 
raw_html TEXT(1000000), 
FOREIGN KEY (link_id) REFERENCES links(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE);

-- а обработанный текстовый контент разобъём на предложения для последующего машинного обучения
CREATE TABLE IF NOT EXISTS sentences (
id SERIAL PRIMARY KEY, 
link_id BIGINT UNSIGNED NOT NULL, 
sentence_original TEXT(1000), 
sentence_translated TEXT(1000), 
FOREIGN KEY (link_id) REFERENCES links(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE);

-- таблица для бэкапа
CREATE TABLE IF NOT EXISTS backup (
id SERIAL, 
user_id BIGINT UNSIGNED, 
record TEXT(10000), 
occured_on DATETIME DEFAULT CURRENT_TIMESTAMP) ENGINE=Archive;


-- ----------------------------------------------------------------------------------------------
-- Скрипты наполнения БД данными - в отдельном файле, в оригинале - 
-- будут с "?" вместо данных, поскольку БД используется в живом проекте
-- и за наполнение отвечают скрипты python, доступные по адресу https://github.com/m0rtal/t-rss (весь бот)
-- или https://github.com/m0rtal/t-rss/blob/master/utils/db_api/sqlite.py (только скрипты работы с БД).
-- За пакетную вставку отвечает скрипт на питоне, делающий "cursor.execute" когда приходит одно значение
-- и "cursor.executemany" - когда приходит список значений (list в терминах питона).

-- добавление пользователя:
-- INSERT INTO users (user_id) VALUES(?);

-- добавление правил обработки:
-- INSERT INTO feed_processing_rules(rule) VALUES(?);
-- 
-- добавление RSS фидов:
-- INSERT INTO feeds(feed) VALUES(?);
-- 
-- добавление подписки пользователю:
-- вложенным запросом, поскольку в функцию приходит ссылка, а вставить нужно id
-- INSERT INTO subscriptions (user_id, feed_id) VALUES(?,(SELECT id FROM feeds WHERE feed=?));
-- 
-- добавление ссылки на новость:
-- вложенным запросом по той же причине
-- INSERT INTO links (feed_id, link) VALUES((SELECT id FROM feeds WHERE feed=?),?);
-- 
-- добавление описания ссылке
-- опять со вложенным запросом :)
-- INSERT INTO descriptions (link_id, description) VALUES ((SELECT id FROM links WHERE link=?),?);
-- 
-- 
-- добавим запись об отправленном сообщении
-- INSERT INTO sent_posts (user_id, link_id, is_sent) 
-- VALUES(?,(SELECT id FROM links WHERE link=?),1);
-- 
-- добавим запись о лайкнутом посте
-- INSERT INTO likes (user_id, link_id, liked) VALUES(?,(SELECT id FROM LINKS WHERE link=?),1)
-- 
-- добавим запись о понравившемся посте
-- INSERT INTO marked (user_id, link_id, marked) VALUES(?,(SELECT id FROM LINKS WHERE link=?),1)


-- ----------------------------------------------------------------------------------------------
-- Скрипты характерных выборок
-- статистика подписок по пользователям
SELECT u.id, COUNT(s.feed_id) AS feeds 
FROM users u 
JOIN subscriptions s 
ON u.id=s.user_id 
GROUP BY u.id;


-- статистика ссылок по подпискам
SELECT f.feed, COUNT(l.id) 
FROM feeds f 
JOIN links l 
ON l.feed_id=f.id 
GROUP BY f.feed;


-- ----------------------------------------------------------------------------------------------
-- Представления
-- Подписки по пользователям
CREATE OR REPLACE VIEW v_subscriptions AS 
SELECT	s.user_id , f.feed 
FROM subscriptions s 
JOIN feeds f ON 
s.feed_id = f.id;

-- просмотр
SELECT user_id, feed
FROM v_subscriptions
WHERE user_id = 1;

-- все ссылки по пользователям
CREATE OR REPLACE VIEW v_links AS 
SELECT s.user_id, l.link 
FROM subscriptions s 
JOIN links l 
ON s.feed_id=l.feed_id;

-- и получение всех ссылок пользователя для дальнейшей обработки
SELECT * 
FROM v_links 
WHERE user_id=1;

-- все неотправленные сообщения с описаниями - для отправки подписчикам
CREATE OR REPLACE VIEW v_unsent_messages AS 
SELECT s.user_id, l.link, d.description 
FROM subscriptions s 
JOIN links l 
ON l.feed_id=s.feed_id 
JOIN descriptions d 
ON d.link_id=l.id 
LEFT JOIN sent_posts sp 
ON l.id=sp.link_id 
WHERE sp.is_sent=0;

-- и выбор неотправленных сообщений только одного пользователя
SELECT user_id, link, description
FROM v_unsent_messages
WHERE user_id=1;


-- ----------------------------------------------------------------------------------------------
-- Триггеры
-- триггер по удалению подписки
DROP TRIGGER IF EXISTS backup_subscription;
DELIMITER //
CREATE TRIGGER backup_subscription BEFORE DELETE ON subscriptions 
FOR EACH ROW 
BEGIN 
INSERT INTO backup (user_id, record)
VALUES (OLD.user_id, (SELECT feed FROM feeds WHERE feeds.id=OLD.feed_id)); 
END//
DELIMITER ;


-- ----------------------------------------------------------------------------------------------
-- Функция подсчёта статистики лайков
DROP FUNCTION IF EXISTS main.likes_stats;

DELIMITER //
CREATE FUNCTION main.likes_stats()
RETURNS FLOAT(5,2) READS SQL DATA -- float(5,2) выдаст всего 5 цифр, из которых 2 будут десятичной дробью 
BEGIN
	DECLARE liked INT; -- сколько записей лайкнуто
	DECLARE total INT; -- всего записей

	SELECT COUNT(*)
	INTO liked
	FROM likes l
	WHERE l.liked=1; 
	
	SELECT COUNT(*)
	INTO total
	FROM likes l;

	RETURN liked / total * 100; -- вернём процент лайкнутых записей
END//
DELIMITER ;

SELECT likes_stats();
