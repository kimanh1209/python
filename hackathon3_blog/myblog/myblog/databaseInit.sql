CREATE DATABASE blog_mysql;
USE blog_mysql;

DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `content` VARCHAR(1000) NULL,
  `author` INT NULL,
  `created` datetime,
  PRIMARY KEY (`id`));
  
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(32) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);