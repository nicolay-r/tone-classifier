-- Для bank коллекции
DROP TABLE IF EXISTS bank_train_balanced_2016_15k;
CREATE TABLE bank_train_balanced_2016_15k AS
    SELECT * FROM bank_train_2016;

-- Добавляем строки из извлеченных таблиц
ALTER TABLE mtsd_positive DROP COLUMN IF EXISTS rank;
ALTER TABLE mtsd_positive ADD COLUMN rank INT DEFAULT 1;

ALTER TABLE mtsd_negative DROP COLUMN IF EXISTS rank;
ALTER TABLE mtsd_negative ADD COLUMN rank INT DEFAULT -1;

ALTER TABLE mtsd_neutral DROP COLUMN IF EXISTS rank;
ALTER TABLE mtsd_neutral ADD COLUMN rank INT DEFAULT 0;

INSERT INTO bank_train_balanced_2016_15k(twitid, text, sberbank)
    SELECT twitid, text, rank FROM mtsd_positive limit(15600);
INSERT INTO bank_train_balanced_2016_15k(twitid, text, sberbank)
    SELECT twitid, text, rank FROM mtsd_negative limit(14600);
INSERT INTO bank_train_balanced_2016_15k(twitid, text, sberbank)
    SELECT twitid, text, rank FROM mtsd_neutral limit(9600);

-- Проверяем баллансировку
SELECT COUNT(*) FROM bank_train_balanced_2016_15k WHERE
    (sberbank=1 or vtb=1 or gazprom=1 or alfabank=1 or
    bankmoskvy=1 or raiffeisen=1 or uralsib=1 or rshb=1);

SELECT COUNT(*) FROM bank_train_balanced_2016_15k WHERE
    (sberbank=-1 or vtb=-1 or gazprom=1 or alfabank=-1 or
    bankmoskvy=-1 or raiffeisen=-1 or uralsib=-1 or rshb=-1);

SELECT COUNT(*) FROM bank_train_balanced_2016_15k WHERE
    (sberbank=0 or vtb=0 or gazprom=1 or alfabank=0 or
    bankmoskvy=0 or raiffeisen=0 or uralsib=0 or rshb=0);
