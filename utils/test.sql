create database `test_python` default character set utf8;

use test_python;
CREATE TABLE `t_test_insert` (
    `id` bigint not null,
    `name` varchar(100) not null,
    `gender` varchar(20) not null,
    `price` decimal(24,4) not null,
    `create_time` bigint not null,
    `extra_str1` varchar(200) not null,
    `extra_str2` varchar(200) not null,
    `extra_int1` bigint not null,
    `extra_int2` bigint not null,
    PRIMARY KEY (`id`),
    KEY `I_create_time` (`create_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
