-- Для ttk коллекции
DROP TABLE IF EXISTS ttk_train_balanced_2016_15k;
CREATE TABLE ttk_train_balanced_2016_15k AS
    SELECT * FROM ttk_train_2016;

-- Дополняем из автоматически размеченной коллекции
ALTER TABLE mtsd_positive DROP COLUMN IF EXISTS rank;
ALTER TABLE mtsd_positive ADD COLUMN rank INT DEFAULT 1;

ALTER TABLE mtsd_negative DROP COLUMN IF EXISTS rank;
ALTER TABLE mtsd_negative ADD COLUMN rank INT DEFAULT '-1';

ALTER TABLE mtsd_neutral DROP COLUMN IF EXISTS rank;
ALTER TABLE mtsd_neutral ADD COLUMN rank INT DEFAULT '0';

--
INSERT INTO ttk_train_balanced_2016_15k(twitid, text, mts)
    SELECT twitid, text, rank FROM mtsd_positive limit(15000);
INSERT INTO ttk_train_balanced_2016_15k(twitid, text, mts)
    SELECT twitid, text, rank FROM mtsd_negative limit(13800);
INSERT INTO ttk_train_balanced_2016_15k(twitid, text, mts)
    SELECT twitid, text, rank FROM mtsd_neutral limit(11500);

-- Проверяем баллансировку
SELECT COUNT(*) FROM ttk_train_balanced_2016_15k WHERE
    (beeline='1' or mts='1' or megafon='1' or tele2='1' or rostelecom='1'
    or komstar='1' or skylink='1');

SELECT COUNT(*) FROM ttk_train_balanced_2016_15k WHERE
    (beeline='0' or mts='0' or megafon='0' or tele2='0' or rostelecom='0'
    or komstar='0' or skylink='0');

SELECT COUNT(*) FROM ttk_train_balanced_2016_15k WHERE
    (beeline='-1' or mts='-1' or megafon='-1' or tele2='-1' or rostelecom='-1'
    or komstar='-1' or skylink='-1');
