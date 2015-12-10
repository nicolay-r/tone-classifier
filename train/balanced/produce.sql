DROP TABLE IF EXISTS bank_train_balanced;
CREATE TABLE bank_train_balanced AS
    SELECT * FROM bank_train_noname;
ALTER TABLE positive ADD COLUMN rank INT DEFAULT 1;
ALTER TABLE negative ADD COLUMN rank INT DEFAULT -1;
INSERT INTO bank_train_balanced(twitid, text, sberbank)
    SELECT id, text, rank FROM positive limit(3224);
INSERT INTO bank_train_balanced(twitid, text, sberbank)
    SELECT id, text, rank FROM negative limit(2519);

DROP TABLE IF EXISTS ttk_train_balanced;
CREATE TABLE ttk_train_balanced AS
    SELECT * FROM ttk_train_noname;
ALTER TABLE ttk_positive ADD COLUMN rank INT DEFAULT 1;
ALTER TABLE ttk_negative ADD COLUMN rank INT DEFAULT -1;
INSERT INTO ttk_train_balanced(twitid, text, mts)
    SELECT id, text, rank FROM ttk_positive limit(2202);
INSERT INTO ttk_train_balanced(twitid, text, mts)
    SELECT id, text, rank FROM ttk_negative limit(1685);
