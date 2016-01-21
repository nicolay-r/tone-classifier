
DROP TABLE IF EXISTS bank_train_positive;
DROP TABLE IF EXISTS bank_train_negative;

CREATE TABLE bank_train_positive AS
    SELECT * FROM bank_train_noname WHERE
        sberbank=1 OR gazprom=1 OR raiffeisen=1 OR uralsib=1 OR vtb = 1 OR
        rshb=1 OR bankmoskvy=1 OR alfabank=1;

CREATE TABLE bank_train_negative AS
    SELECT * FROM bank_train_noname WHERE
        sberbank=-1 OR gazprom=-1 OR raiffeisen=-1 OR uralsib=-1 OR vtb = -1 OR
        rshb=-1 OR bankmoskvy=-1 OR alfabank=-1;

DROP TABLE IF EXISTS ttk_train_positive;
DROP TABLE IF EXISTS ttk_train_negative;

CREATE TABLE ttk_train_positive AS
    SELECT * FROM ttk_train_noname WHERE
        beeline='1' OR mts='1' OR megafon='1' OR komstar='1' OR
        rostelecom='1' OR skylink='1' OR tele2='1';

CREATE TABLE ttk_train_negative AS
    SELECT * FROM ttk_train_noname WHERE
        beeline='-1' OR mts='-1' OR megafon='-1' OR komstar='-1' OR
        rostelecom='-1' OR skylink='-1' OR tele2='-1';
