
DROP TABLE IF EXISTS bank_positive;
CREATE TABLE IF NOT EXISTS bank_positive (
    id bigint NOT NULL,
    text VARCHAR(512) NOT NULL);

DROP TABLE IF EXISTS bank_negative;
CREATE TABLE IF NOT EXISTS bank_negative (
    id bigint NOT NULL,
    text VARCHAR(512) NOT NULL);

-- Positive Collection
INSERT INTO bank_positive(id, text) (SELECT twitid, text
    FROM bank_train_noname WHERE
    sberbank=1 or vtb=1 or alfabank=1 or
    bankmoskvy=1 or raiffeisen=1 or uralsib=1 or rshb=1);

INSERT INTO bank_positive(id, text) (SELECT twitid, text
    FROM bank_train_2016 WHERE
    sberbank=1 or vtb=1 or alfabank=1 or
    bankmoskvy=1 or raiffeisen=1 or uralsib=1 or rshb=1);

-- Negative Collection
INSERT INTO bank_negative(id, text) (SELECT twitid, text
    FROM bank_train_noname WHERE
    sberbank=-1 or vtb=-1 or alfabank=-1 or
    bankmoskvy=-1 or raiffeisen=-1 or uralsib=-1 or rshb=-1);

INSERT INTO bank_negative(id, text) (SELECT twitid, text
    FROM bank_train_2016 WHERE
    sberbank=-1 or vtb=-1 or alfabank=-1 or
    bankmoskvy=-1 or raiffeisen=-1 or uralsib=-1 or rshb=-1);

SELECT COUNT(*) FROM bank_positive;
SELECT COUNT(*) FROM bank_negative;
