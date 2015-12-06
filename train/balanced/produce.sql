DROP TABLE IF EXISTS bank_train_balanced;
CREATE TABLE bank_train_balanced AS SELECT * FROM bank_train_noname;
ALTER TABLE positive ADD COLUMN rank INT DEFAULT 1;
ALTER TABLE negative ADD COLUMN rank INT DEFAULT -1;
INSERT INTO bank_train_balanced(twitid, text, sberbank)
    SELECT id, text, rank FROM positive limit(3230);
INSERT INTO bank_train_balanced(twitid, text, sberbank)
    SELECT id, text, rank FROM negative limit(2519);
