CREATE TABLE `tkk_test_2016` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `twitid` bigint(32) NOT NULL,
    `date` varchar(128) NOT NULL,
    `text` varchar(256) NOT NULL,
    `beeline` int(11) DEFAULT NULL,
    `mts` int(11) DEFAULT NULL,
    `megafon` int(11) DEFAULT NULL,
    `tele2` int(11) DEFAULT NULL,
    `rostelecom` int(11) DEFAULT NULL,
    `komstar` int(11) DEFAULT NULL,
    `skylink` int(11) DEFAULT NULL,
);
