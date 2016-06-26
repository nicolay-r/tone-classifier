
DROP TABLE IF EXISTS ttk_positive;
CREATE TABLE IF NOT EXISTS ttk_positive (
    id bigint NOT NULL,
    text VARCHAR(512) NOT NULL);

DROP TABLE IF EXISTS ttk_negative;
CREATE TABLE IF NOT EXISTS ttk_negative (
    id bigint NOT NULL,
    text VARCHAR(512) NOT NULL);

-- Positive Collection
INSERT INTO ttk_positive(id, text) (SELECT twitid, text
    FROM ttk_train_noname WHERE
    beeline='1' or mts='1' or megafon='1' or tele2='1' or rostelecom='1'
    or komstar='1' or skylink='1');

INSERT INTO ttk_positive(id, text) (SELECT twitid, text
    FROM ttk_train_2016 WHERE
    beeline='1' or mts='1' or megafon='1' or tele2='1' or rostelecom='1'
    or komstar='1' or skylink='1');

-- Negative Collection
INSERT INTO ttk_negative(id, text) (SELECT twitid, text
    FROM ttk_train_noname WHERE
    beeline='-1' or mts='-1' or megafon='-1' or tele2='-1' or rostelecom='-1'
    or komstar='-1' or skylink='-1');

INSERT INTO ttk_negative(id, text) (SELECT twitid, text
    FROM ttk_train_2016 WHERE
    beeline='-1' or mts='-1' or megafon='-1' or tele2='-1' or rostelecom='-1'
    or komstar='-1' or skylink='-1');

SELECT COUNT(*) FROM ttk_positive;
SELECT COUNT(*) FROM ttk_negative;
