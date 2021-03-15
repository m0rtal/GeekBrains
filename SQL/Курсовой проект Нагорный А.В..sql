/*
Текстовое описание БД и решаемых ею задач

Разрабатываемая БД предназначена для моего телеграм бота @TRSSP_bot, 
который работает как агрегатор новостей по каналам rss, с расширением стандартных 
функций подписки до возможности учитывания лайков, сохранением постов, 
автоматического парсинга сайтов и автоматического же перевода ключевых новостей
с использованием биржи фрилансеров etxt.ru.     
Однако, в связи с текущей загруженностью, на данный момемнт бот умеет только
агрегировать новостные каналы в канал чата с подписчиком, с отслеживанием
отправленных новостей и ведением раздельных чатов с каждым подписчиком.
Также, в связи с необходимостью переносимости проекта и одновременной разработки из
трёх разных точек, было принято согласованное с вами решение о написании БД в SQLite.
*/

-- SQLite не требует создания базы, ею автоматически является файл с таблицами.
-- Но, чтобы показать навык - создадим "виртуальную" базу:
CREATE DATABASE IF NOT EXISTS main;
USE main;


-- Таблица пользователей хранит id пользователя в telegram. 
-- Возможно, в будущем будет расширена дополнительными сведениями о пользователе.
CREATE TABLE IF NOT EXISTS users (
user_id INT PRIMARY KEY);

-- для сохранения RSS-фидов и избегания дублирования записей заведём таблицу с фидами
-- ключ UNIQUE автоматически создаёт индекс по колонке feed
CREATE TABLE IF NOT EXISTS feeds (
id INT PRIMARY KEY, 
feed TEXT UNIQUE);

-- для возможности автоматической обработки новостей заведём таблицу с правилами обработки
CREATE TABLE IF NOT EXISTS feed_processing_rules (
id INT PRIMARY KEY, 
rule TEXT UNIQUE);

-- для хранения подписок пользователя создадим таблицу подписок
-- таблица ссылается на правила обработки, таблицу пользователей и таблицу фидов
-- а также имеет Primary Key из двух полей (user_id и feed_id)
-- для ограничения одного пользователя одной уникальной подпиской
-- и для индексации по этим полям
CREATE TABLE IF NOT EXISTS subscriptions (
user_id INT NOT NULL, 
feed_id INT NOT NULL, 
rule_id INT DEFAULT 1, 
CONSTRAINT ixpk PRIMARY KEY (user_id, feed_id), 
FOREIGN KEY (user_id) REFERENCES users(user_id) 
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
id INT PRIMARY KEY, 
feed_id INT NOT NULL, 
link TEXT, 
FOREIGN KEY (feed_id) REFERENCES feeds(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE);


-- собрав все обновлённые ссылки, бот будет получать их краткое описание для предоставления
-- подписчику, сохраняя описания в таблице описаний и ссылаясь на таблицу ссылок
CREATE TABLE IF NOT EXISTS descriptions (
link_id INT PRIMARY KEY, 
description TEXT, 
FOREIGN KEY (link_id) REFERENCES links(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE);

-- статистика отправленных пользователям сообщений будет вестись в таблице sent_posts,
-- ссылающейся на пользователя и обработанную ссылку
CREATE TABLE IF NOT EXISTS sent_posts (
user_id INT NOT NULL, 
link_id INT NOT NULL, 
is_sent INT DEFAULT 0, 
FOREIGN KEY (user_id) REFERENCES users(user_id) 
ON UPDATE CASCADE 
ON DELETE CASCADE, 
FOREIGN KEY (link_id) REFERENCES links(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE, 
CONSTRAINT ixpk PRIMARY KEY (user_id, link_id));


-- "лайкнутые" новости будем хранить в таблице лайков,
-- ссылающейся на пользователя и ссылку
CREATE TABLE IF NOT EXISTS likes (
id INT PRIMARY KEY, 
user_id INT NOT NULL, 
link_id INT NOT NULL, 
liked INT DEFAULT 0, 
FOREIGN KEY (user_id) REFERENCES users(user_id) 
ON UPDATE CASCADE 
ON DELETE CASCADE, 
FOREIGN KEY (link_id) REFERENCES links(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE);

-- помеченные для дальнейшей работы новости будем также хранить в отдельной таблице,
-- ссылающейся на пользователя и ссылку
CREATE TABLE IF NOT EXISTS marked (
id INT PRIMARY KEY, 
user_id INT NOT NULL, 
link_id INT NOT NULL, 
marked INT DEFAULT 0, 
FOREIGN KEY (user_id) REFERENCES users(user_id) 
ON UPDATE CASCADE 
ON DELETE CASCADE, 
FOREIGN KEY (link_id) REFERENCES links(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE);

-- заведём таблицу для спарсенного контента
-- ссылающуюся на пользователя и ссылку
CREATE TABLE IF NOT EXISTS parsed (
id INT PRIMARY KEY, 
link_id INT NOT NULL, 
raw_html TEXT, 
FOREIGN KEY (link_id) REFERENCES links(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE);

-- а обработанный текстовый контент разобъём на предложения для последующего машинного обучения
CREATE TABLE IF NOT EXISTS sentences (
id INT PRIMARY KEY, 
link_id INT NOT NULL, 
sentence_original TEXT, 
sentence_translated TEXT, 
FOREIGN KEY (link_id) REFERENCES links(id) 
ON UPDATE CASCADE 
ON DELETE CASCADE);


-- ----------------------------------------------------------------------------------------------
-- Поскольку БД написана в SQLite, попытка её импорта в Workbench EER diagram не увенчалась успехом:
-- https://yadi.sk/i/wb1-QFgkgYwLJQ
-- хотя в dbeaver'e всё выглядит неплохо:
-- https://yadi.sk/i/TDTK3l07YdSrKw

-- ----------------------------------------------------------------------------------------------
-- Скрипты наполнения БД данными будут с "?" вместо данных, поскольку БД используется в живом проекте
-- и за наполнение отвечают скрипты python, доступные по адресу https://github.com/m0rtal/t-rss (весь бот)
-- или https://github.com/m0rtal/t-rss/blob/master/utils/db_api/sqlite.py (только скрипты работы с БД).
-- За пакетную вставку отвечает скрипт на питоне, делающий "cursor.execute" когда приходит одно значение
-- и "cursor.executemany" - когда приходит список значений (list в терминах питона).

-- добавление пользователя:
INSERT INTO users (user_id) VALUES(?);

-- добавление правил обработки:
INSERT INTO feed_processing_rules(rule) VALUES(?);

-- добавление RSS фидов:
INSERT INTO feeds(feed) VALUES(?);

-- добавление подписки пользователю:
-- вложенным запросом, поскольку в функцию приходит ссылка, а вставить нужно id
INSERT INTO subscriptions (user_id, feed_id) VALUES(?,(SELECT id FROM feeds WHERE feed=?));

-- добавление ссылки на новость:
-- вложенным запросом по той же причине
INSERT INTO links (feed_id, link) VALUES((SELECT id FROM feeds WHERE feed=?),?);

-- добавление описания ссылке
-- опять со вложенным запросом :)
INSERT INTO descriptions (link_id, description) VALUES ((SELECT id FROM links WHERE link=?),?);


-- добавим запись об отправленном сообщении
INSERT INTO sent_posts (user_id, link_id, is_sent) 
VALUES(?,(SELECT id FROM links WHERE link=?),1);

-- добавим запись о лайкнутом посте
INSERT INTO likes (user_id, link_id, liked) VALUES(?,(SELECT id FROM LINKS WHERE link=?),1)

-- добавим запись о понравившемся посте
INSERT INTO marked (user_id, link_id, marked) VALUES(?,(SELECT id FROM LINKS WHERE link=?),1)


-- ----------------------------------------------------------------------------------------------
-- Скрипты характерных выборок
-- статистика подписок по пользователям
SELECT u.user_id, COUNT(s.feed_id) AS feeds 
FROM users u 
JOIN subscriptions s 
ON u.user_id=s.user_id 
GROUP BY u.user_id;

-- статистика ссылок по подпискам
SELECT f.feed, COUNT(l.id) 
FROM feeds f 
JOIN links l 
ON l.feed_id=f.id 
GROUP BY f.feed;

-- статистика лайкнутых постов
SELECT COUNT(l.link_id)/COUNT(sp.link_id) AS pct_liked 
FROM sent_posts sp 
LEFT JOIN likes l 
ON sp.link_id=l.link_id 
WHERE sp.user_id=?;


-- ----------------------------------------------------------------------------------------------
-- Представления
-- Подписки по пользователям
CREATE VIEW IF NOT EXISTS v_subscriptions AS 
SELECT	s.user_id, f.feed 
FROM subscriptions s 
JOIN feeds f ON 
s.feed_id = f.id;

-- и получение из них только одного пользователя по запросу
SELECT feed 
FROM v_subscriptions 
WHERE user_id=?;

-- все ссылки по пользователям
CREATE VIEW IF NOT EXISTS v_links AS 
SELECT s.user_id, l.link 
FROM subscriptions s 
JOIN links l 
ON s.feed_id=l.feed_id;

-- и получение всех ссылок пользователя для дальнейшей обработки
SELECT link 
FROM v_links 
WHERE user_id=?;

-- все неотправленные сообщения с описаниями - для отправки подписчикам
CREATE VIEW IF NOT EXISTS v_unsent_messages AS 
SELECT s.user_id, l.link, d.description 
FROM subscriptions s 
JOIN links l 
ON l.feed_id=s.feed_id 
JOIN descriptions d 
ON d.link_id=l.id 
LEFT JOIN sent_posts sp 
ON l.id=sp.link_id 
WHERE sp.is_sent IS NULL;

-- и выбор неотправленных сообщений только одного пользователя
SELECT link, description 
FROM v_unsent_messages 
WHERE user_id=?;


-- ----------------------------------------------------------------------------------------------
-- Триггеры
-- Для начала - таблица для бэкапа
CREATE TABLE IF NOT EXISTS backup (
id INT PRIMARY KEY, 
user_id INT, 
record TEXT, 
occured_on DATETIME DEFAULT CURRENT_TIMESTAMP);

-- и триггер по удалению подписки
CREATE TRIGGER IF NOT EXISTS backup_subscription BEFORE DELETE ON subscriptions 
FOR EACH ROW 
BEGIN 
INSERT INTO backup(user_id, record) 
VALUES(OLD.user_id, (SELECT feed FROM feeds WHERE feed.id=OLD.feed_id)); 
END


-- ----------------------------------------------------------------------------------------------
-- Процедуры не поддерживаются SQLite, но написать могу любую - применения пока не вижу.
-- Всё, что необходимо, решается функциями в питоне, а переносить их функционал в БД - такое...

CREATE PROCEDURE test()
BEGIN
	DECLARE var INT DEFAULT 0;
	WHILE var<10 DO
		SELECT "hello";
		SET var=var+1;
	END WHILE;
END
