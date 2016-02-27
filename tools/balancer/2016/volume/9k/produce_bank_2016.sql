-- Для bank коллекции
DROP TABLE IF EXISTS bank_train_balanced_2016;
CREATE TABLE bank_train_balanced_2016 AS
    SELECT * FROM bank_train_2016;

INSERT INTO bank_train_balanced_2016(twitid, date, text, sberbank, vtb,
    gazprom, alfabank, bankmoskvy, raiffeisen, uralsib, rshb) (SELECT
    twitid, date, text, sberbank, vtb, gazprom, alfabank, bankmoskvy,
    raiffeisen, uralsib, rshb FROM bank_train_noname WHERE
    sberbank=-1 or vtb=-1 or alfabank=-1 or
    bankmoskvy=-1 or raiffeisen=-1 or uralsib=-1 or rshb=-1);

INSERT INTO bank_train_balanced_2016 (twitid, date, text, sberbank, vtb,
    gazprom, alfabank, bankmoskvy, raiffeisen, uralsib, rshb) (SELECT
    twitid, date, text, sberbank, vtb, gazprom, alfabank, bankmoskvy,
    raiffeisen, uralsib, rshb FROM bank_train_noname WHERE
    sberbank=1 or vtb=1 or alfabank=1 or
    bankmoskvy=1 or raiffeisen=1 or uralsib=1 or rshb=1);

-- Добавляем строки из извлеченных таблиц
ALTER TABLE bank_positive DROP COLUMN IF EXISTS rank;
ALTER TABLE bank_positive ADD COLUMN rank INT DEFAULT 1;
ALTER TABLE bank_negative DROP COLUMN IF EXISTS rank;
ALTER TABLE bank_negative ADD COLUMN rank INT DEFAULT -1;

INSERT INTO bank_train_balanced_2016(twitid, text, sberbank)
    SELECT id, text, rank FROM bank_positive limit(5734);
INSERT INTO bank_train_balanced_2016(twitid, text, sberbank)
    SELECT id, text, rank FROM bank_negative limit(3976);

-- Проверяем баллансировку
SELECT COUNT(*) FROM bank_train_balanced_2016 WHERE
    (sberbank=1 or vtb=1 or gazprom=1 or alfabank=1 or
    bankmoskvy=1 or raiffeisen=1 or uralsib=1 or rshb=1);

SELECT COUNT(*) FROM bank_train_balanced_2016 WHERE
    (sberbank=-1 or vtb=-1 or gazprom=1 or alfabank=-1 or
    bankmoskvy=-1 or raiffeisen=-1 or uralsib=-1 or rshb=-1);

SELECT COUNT(*) FROM bank_train_balanced_2016 WHERE
    (sberbank=0 or vtb=0 or gazprom=1 or alfabank=0 or
    bankmoskvy=0 or raiffeisen=0 or uralsib=0 or rshb=0);
