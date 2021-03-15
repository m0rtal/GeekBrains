/*
2. Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, числового id и строкового name.
*/

CREATE DATABASE IF NOT EXISTS example;

USE example;

CREATE TABLE IF NOT EXISTS users (
	id INT,
	name VARCHAR(100)
);


/*
 3. Создайте дамп базы данных example из предыдущего задания, разверните содержимое дампа в новую базу данных sample.
 */

SYSTEM mysqldump.exe example > example.sql;
DROP TABLE IF EXISTS sample;
CREATE DATABASE IF NOT EXISTS sample;
SYSTEM mysql sample < example.sql;

/*
4. (по желанию) Ознакомьтесь более подробно с документацией утилиты mysqldump. Создайте дамп единственной таблицы help_keyword
базы данных mysql. Причем добейтесь того, чтобы дамп содержал только первые 100 строк таблицы.
*/

-- не понял со 100 записями, на всякий случай сделал 2 варианта
SYSTEM mysqldump.exe --where="true limit 100" mysql help_keyword > help100_1.sql;
SYSTEM mysqldump.exe --where="help_keyword_id < 100" mysql help_keyword > help100_2.sql;
