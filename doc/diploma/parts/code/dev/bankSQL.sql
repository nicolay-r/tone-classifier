CREATE TABLE `bank_test_2016` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `twitid` bigint(32) NOT NULL,
    `date` varchar(128) DEFAULT NULL,
    `text` varchar(256) DEFAULT NULL,
    `sberbank` int(10) DEFAULT NULL,
    `vtb` int(10) DEFAULT NULL,
    `gazprom` int(10) DEFAULT NULL,
    `alfabank` int(10) DEFAULT NULL,
    `bankmoskvy` int(10) DEFAULT NULL,
    `raiffeisen` int(10) DEFAULT NULL,
    `uralsib` int(10) DEFAULT NULL,
    `rshb` int(10) DEFAULT NULL
);
