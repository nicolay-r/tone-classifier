-- Для ttk коллекции
DROP TABLE IF EXISTS ttk_train_balanced_2016;
CREATE TABLE ttk_train_balanced_2016 AS
    SELECT * FROM ttk_train_2016;

INSERT INTO ttk_train_balanced_2016(twitid, date, text, beeline, mts,
    megafon, tele2, rostelecom, komstar, skylink) (SELECT
    twitid, date, text, beeline, mts, megafon, tele2, rostelecom,
    komstar, skylink FROM ttk_train_noname WHERE
    beeline='1' or mts='1' or megafon='1' or tele2='1' or rostelecom='1'
    or komstar='1' or skylink='1');

INSERT INTO ttk_train_balanced_2016(twitid, date, text, beeline, mts,
    megafon, tele2, rostelecom, komstar, skylink) (SELECT
    twitid, date, text, beeline, mts, megafon, tele2, rostelecom,
    komstar, skylink FROM ttk_train_noname WHERE
    beeline='-1' or mts='-1' or megafon='-1' or tele2='-1' or rostelecom='-1'
    or komstar='-1' or skylink='-1');

-- Дополняем из автоматически размеченной коллекции
ALTER TABLE ttk_positive DROP COLUMN IF EXISTS rank;
ALTER TABLE ttk_positive ADD COLUMN rank INT DEFAULT 1;
ALTER TABLE ttk_negative DROP COLUMN IF EXISTS rank;
ALTER TABLE ttk_negative ADD COLUMN rank INT DEFAULT '-1';
INSERT INTO ttk_train_balanced_2016(twitid, text, mts)
    SELECT id, text, rank FROM ttk_positive limit(2548);
INSERT INTO ttk_train_balanced_2016(twitid, text, mts)
    SELECT id, text, rank FROM ttk_negative limit(674);

-- Проверяем баллансировку
SELECT COUNT(*) FROM ttk_train_balanced_2016 WHERE
    (beeline='1' or mts='1' or megafon='1' or tele2='1' or rostelecom='1'
    or komstar='1' or skylink='1');

SELECT COUNT(*) FROM ttk_train_balanced_2016 WHERE
    (beeline='0' or mts='0' or megafon='0' or tele2='0' or rostelecom='0'
    or komstar='0' or skylink='0');

SELECT COUNT(*) FROM ttk_train_balanced_2016 WHERE
    (beeline='-1' or mts='-1' or megafon='-1' or tele2='-1' or rostelecom='-1'
    or komstar='-1' or skylink='-1');
