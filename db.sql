CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL DEFAULT '' COMMENT '用户名称',
  `password` varchar(255) NOT NULL DEFAULT '' COMMENT '密码',
  `email` varchar(100) NOT NULL DEFAULT '' COMMENT '邮箱',
  `phone` varchar(20) NOT NULL DEFAULT '' COMMENT '手机号',
  `avatar` varchar(255) DEFAULT NULL COMMENT '头像地址',
  `status` tinyint(3) unsigned NOT NULL DEFAULT 1 COMMENT '状态：1、正常',
  `created_at` int(10) unsigned NOT NULL DEFAULT 0,
  `updated_at` int(10) unsigned NOT NULL DEFAULT 0,
  `deleted_at` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uk_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;