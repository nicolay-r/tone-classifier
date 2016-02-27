-- Выполняем балансировку для bank задачи
DROP TABLE IF EXISTS bank_train_balanced;
CREATE TABLE bank_train_balanced AS
    SELECT * FROM bank_train_noname;

ALTER TABLE bank_positive DROP COLUMN IF EXISTS rank;
ALTER TABLE bank_positive ADD COLUMN rank INT DEFAULT 1;
ALTER TABLE bank_negative DROP COLUMN IF EXISTS rank;
ALTER TABLE bank_negative ADD COLUMN rank INT DEFAULT -1;
INSERT INTO bank_train_balanced(twitid, text, sberbank)
    SELECT id, text, rank FROM bank_positive limit(3224);
INSERT INTO bank_train_balanced(twitid, text, sberbank)
    SELECT id, text, rank FROM bank_negative limit(2519);

-- Проверяем балансировку
SELECT COUNT(*) FROM bank_train_balanced WHERE
    (sberbank=1 or vtb=1 or gazprom=1 or alfabank=1 or
    bankmoskvy=1 or raiffeisen=1 or uralsib=1 or rshb=1);

SELECT COUNT(*) FROM bank_train_balanced WHERE
    (sberbank=-1 or vtb=-1 or gazprom=1 or alfabank=-1 or
    bankmoskvy=-1 or raiffeisen=-1 or uralsib=-1 or rshb=-1);

SELECT COUNT(*) FROM bank_train_balanced WHERE
    (sberbank=0 or vtb=0 or gazprom=1 or alfabank=0 or
    bankmoskvy=0 or raiffeisen=0 or uralsib=0 or rshb=0);

-- Выполняем балансировку для ttk задачи
DROP TABLE IF EXISTS ttk_train_balanced;
CREATE TABLE ttk_train_balanced AS
    SELECT * FROM ttk_train_noname;

ALTER TABLE ttk_positive DROP COLUMN IF EXISTS rank;
ALTER TABLE ttk_positive ADD COLUMN rank INT DEFAULT 1;
ALTER TABLE ttk_negative DROP COLUMN IF EXISTS rank;
ALTER TABLE ttk_negative ADD COLUMN rank INT DEFAULT -1;
INSERT INTO ttk_train_balanced(twitid, text, mts)
    SELECT id, text, rank FROM ttk_positive limit(1336);
INSERT INTO ttk_train_balanced(twitid, text, mts)
    SELECT id, text, rank FROM ttk_negative limit(660);

-- Проверяем балансировку для ttk
SELECT COUNT(*) FROM ttk_train_balanced WHERE
    (beeline='1' or mts='1' or megafon='1' or tele2='1' or rostelecom='1'
    or komstar='1' or skylink='1');

SELECT COUNT(*) FROM ttk_train_balanced WHERE
    (beeline='0' or mts='0' or megafon='0' or tele2='0' or rostelecom='0'
    or komstar='0' or skylink='0');

SELECT COUNT(*) FROM ttk_train_balanced WHERE
    (beeline='-1' or mts='-1' or megafon='-1' or tele2='-1' or rostelecom='-1'
    or komstar='-1' or skylink='-1');
