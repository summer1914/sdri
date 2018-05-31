SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

DROP DATABASE IF EXISTS sdri;
CREATE DATABASE sdri DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
use sdri;

-- ----------------------------
-- Table structure for exponent
-- ----------------------------
DROP TABLE IF EXISTS `exponent`;
CREATE TABLE `exponent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schoolName` varchar(50) NOT NULL,
  `year` varchar(50) NOT NULL,
  `schoolProvince` varchar(50) DEFAULT NULL,
  `schoolCity` varchar(50) DEFAULT NULL,
  `schoolCounty` varchar(50) DEFAULT NULL,
  `schoolStu` int(11) DEFAULT NULL,
  `schoolPut` float DEFAULT NULL,
  `studentAvg` float DEFAULT NULL,
  `computerSum` int(11) DEFAULT NULL,
  `multiClass` int(11) DEFAULT NULL,
  `classSum` int(11) DEFAULT NULL,
  `broadband` float DEFAULT NULL,
  `effectPrepare` float DEFAULT NULL,
  `pertinencePrepare` float DEFAULT NULL,
  `optimizeTeach` float DEFAULT NULL,
  `turnoverTeach` float DEFAULT NULL,
  `manageCourse` float DEFAULT NULL,
  `communicateCourse` float DEFAULT NULL,
  `I` float DEFAULT NULL,
  `C1` float DEFAULT NULL,
  `C2` float DEFAULT NULL,
  `C3` float DEFAULT NULL,
  `C` float DEFAULT NULL,
  `E1` float DEFAULT NULL,
  `E2` float DEFAULT NULL,
  `E3` float DEFAULT NULL,
  `E` float DEFAULT NULL,
  `final_index` float DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `add_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `add_user_id` (`add_user_id`),
  CONSTRAINT `exponent_ibfk_1` FOREIGN KEY (`add_user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of exponent
-- ----------------------------
BEGIN;
INSERT INTO `exponent` VALUES (13, '汉口一中', '2016', '湖北', '武汉', '汉口', 762, 300000, 20, 133, 122, 433, 1024, 0.5, 0.5, 0.5, 0.92, 0.5, 0.5, 1, 0.17, 0.16, 1, 0.3, 0.5, 0.78, 0.5, 0.58, 0.56, '2017-12-15 12:29:48', 45);
INSERT INTO `exponent` VALUES (15, '青山二中', '2015', '湖北', '武汉', '青山', 762, 300000, 20, 333, 123, 444, 1024, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.44, 0.16, 1, 0.41, 0.5, 0.5, 0.5, 0.5, 0.57, '2017-12-15 12:32:10', 46);
INSERT INTO `exponent` VALUES (16, '青山二中', '2016', '湖北', '武汉', '青山', 762, 250000, 20, 122, 45, 234, 1024, 0.5, 0.5, 0.5, 0.5, 0.9, 0.92, 1, 0.16, 0.06, 1, 0.21, 0.5, 0.5, 0.91, 0.61, 0.53, '2017-12-15 12:33:01', 46);
INSERT INTO `exponent` VALUES (17, '青山一中', '2015', '湖北', '武汉', '青山', 762, 300000, 14, 11, 45, 700, 1024, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 1, 0.01, 0.06, 1, 0.08, 0.5, 0.5, 0.67, 0.55, 0.39, '2017-12-15 12:34:35', 47);
INSERT INTO `exponent` VALUES (18, '青山一中', '2016', '湖北', '武汉', '青山', 888, 200000, 20, 123, 45, 345, 1024, 0.5, 0.5, 0.88, 0.92, 0.9, 0.91, 1, 0.14, 0.05, 1, 0.19, 0.5, 0.91, 0.9, 0.74, 0.57, '2017-12-15 12:35:23', 47);
INSERT INTO `exponent` VALUES (21, '汉口一中', '2017', '湖北', '武汉', '汉口', 762, 300000, 20, 133, 122, 433, 1024, 0.5, 0.5, 0.5, 0.92, 0.5, 0.5, 1, 0.17, 0.16, 1, 0.3, 0.5, 0.78, 0.5, 0.58, 0.56, '2018-01-02 11:00:20', 45);
INSERT INTO `exponent` VALUES (22, '汉口一中', '2018', '湖北', '武汉', '汉口', 762, 20, 20, 11, 6, 123, 1024, 0.5, 0.25, 0.5, 0.92, 0.98, 0.91, 0, 0.01, 0.01, 1, 0.05, 0.42, 0.78, 0.96, 0.68, 0, '2018-01-02 11:02:03', 45);
INSERT INTO `exponent` VALUES (23, '汉口二中', '2015', '湖北', '武汉', '汉口', 762, 200000, 500, 123, 49, 234, 1024, 0.8, 0.25, 0.88, 0.5, 0.5, 0.92, 0.52, 0.16, 0.21, 1, 0.32, 0.62, 0.63, 0.64, 0.63, 0.51, '2018-01-02 19:46:15', 44);
INSERT INTO `exponent` VALUES (24, '汉口二中', '2016', '湖北', '武汉', '汉口', 888, 333000, 500, 78, 99, 233, 1024, 0.8, 0.25, 0.5, 0.5, 0.5, 0.91, 0.75, 0.09, 0.42, 1, 0.34, 0.62, 0.5, 0.64, 0.58, 0.54, '2018-01-02 19:47:33', 44);
INSERT INTO `exponent` VALUES (25, '汉口二中', '2017', '湖北', '武汉', '汉口', 762, 300000, 500, 243, 211, 565, 1024, 1, 0.5, 0.88, 0.5, 0.5, 0.92, 0.79, 0.32, 0.37, 1, 0.49, 0.84, 0.63, 0.64, 0.7, 0.66, '2018-01-02 19:48:32', 44);
INSERT INTO `exponent` VALUES (26, '汉口三中', '2015', '湖北', '武汉', '汉口', 1088, 300000, 500, 122, 211, 333, 1024, 1, 0.5, 0.5, 0.5, 0.5, 0.92, 0.55, 0.11, 0.19, 1, 0.28, 0.84, 0.5, 0.64, 0.65, 0.51, '2018-01-02 19:58:59', 74);
INSERT INTO `exponent` VALUES (27, '汉口三中', '2016', '湖北', '武汉', '汉口', 762, 300000, 202, 144, 89, 211, 1024, 0.5, 0.5, 0.5, 0.92, 0.5, 0.5, 1, 0.19, 0.12, 1, 0.28, 0.5, 0.78, 0.5, 0.58, 0.55, '2018-01-02 19:59:43', 74);
INSERT INTO `exponent` VALUES (28, '汉口三中', '2017', '湖北', '武汉', '汉口', 645, 300000, 500, 211, 111, 555, 1024, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.93, 0.33, 0.17, 1, 0.38, 0.5, 0.5, 0.5, 0.5, 0.55, '2018-01-02 20:00:37', 74);
INSERT INTO `exponent` VALUES (29, '青山二中', '2017', '湖北', '武汉', '青山', 888, 300000, 500, 211, 211, 555, 1024, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.68, 0.24, 0.38, 1, 0.45, 0.5, 0.5, 0.5, 0.5, 0.53, '2018-01-02 20:03:29', 46);
INSERT INTO `exponent` VALUES (30, '青山三中', '2015', '湖北', '武汉', '青山', 762, 300000, 500, 111, 111, 333, 1024, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.79, 0.15, 0.33, 1, 0.37, 0.5, 0.5, 0.5, 0.5, 0.52, '2018-01-02 20:04:35', 76);
INSERT INTO `exponent` VALUES (31, '青山三中', '2016', '湖北', '武汉', '青山', 762, 300, 20, 111, 111, 333, 1024, 0.5, 0.5, 0.5, 0.5, 1, 0.91, 0.02, 0.15, 0.33, 1, 0.37, 0.5, 0.5, 0.97, 0.62, 0.23, '2018-01-02 20:05:23', 76);
INSERT INTO `exponent` VALUES (32, '青山三中', '2017', '湖北', '武汉', '青山', 762, 200, 20, 121, 12, 322, 1024, 0.5, 0.5, 0.5, 0.7, 0.8, 0.9, 0.01, 0.16, 0.04, 1, 0.19, 0.5, 0.63, 0.83, 0.64, 0.17, '2018-01-02 20:06:18', 76);
INSERT INTO `exponent` VALUES (33, '青山一中', '2017', '湖北', '武汉', '青山', 762, 300, 20, 111, 22, 321, 1024, 0.5, 0.5, 0.5, 0.5, 0.5, 0.92, 0.02, 0.15, 0.07, 1, 0.22, 0.5, 0.5, 0.64, 0.54, 0.19, '2018-01-02 20:07:32', 47);
INSERT INTO `exponent` VALUES (34, '武昌一中', '2015', '湖北', '武汉', '武昌', 762, 300, 20, 100, 12, 222, 1024, 0.5, 0.25, 0.5, 0.5, 0.5, 0.91, 0.02, 0.13, 0.02, 1, 0.14, 0.42, 0.5, 0.64, 0.51, 0.16, '2018-01-02 20:09:26', 77);
INSERT INTO `exponent` VALUES (35, '武昌一中', '2016', '湖北', '武汉', '武昌', 1000, 300, 20, 111, 22, 333, 1024, 0.5, 0.25, 0.5, 0.5, 1, 1, 0.01, 0.11, 0.02, 1, 0.13, 0.42, 0.5, 1, 0.59, 0.15, '2018-01-02 20:10:11', 77);
INSERT INTO `exponent` VALUES (36, '武昌一中', '2017', '湖北', '武汉', '武昌', 762, 202, 20, 111, 222, 333, 1024, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.01, 0.15, 0.29, 1, 0.35, 0.5, 0.5, 0.5, 0.5, 0.17, '2018-01-02 20:11:22', 77);
INSERT INTO `exponent` VALUES (37, '武昌二中', '2015', '湖北', '武汉', '武昌', 1000, 222, 20, 122, 22, 333, 1024, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.01, 0.12, 0.07, 1, 0.2, 0.5, 0.5, 0.67, 0.55, 0.16, '2018-01-02 20:15:09', 78);
INSERT INTO `exponent` VALUES (38, '武昌二中', '2016', '湖北', '武汉', '武昌', 1000, 200, 11, 211, 22, 333, 1024, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.02, 0.21, 0.02, 1, 0.16, 0.5, 0.5, 0.5, 0.5, 0.17, '2018-01-02 20:16:07', 78);
INSERT INTO `exponent` VALUES (39, '武昌二中', '2017', '湖北', '武汉', '武昌', 762, 200, 40, 111, 67, 342, 1024, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.01, 0.15, 0.2, 1, 0.31, 0.5, 0.5, 0.67, 0.55, 0.17, '2018-01-02 20:17:48', 78);
INSERT INTO `exponent` VALUES (40, '武昌三中', '2015', '湖北', '武汉', '武昌', 1000, 3000, 233, 111, 222, 444, 1024, 0.8, 0.25, 0.5, 0.5, 0.5, 0.91, 0.01, 0.11, 0.5, 1, 0.38, 0.62, 0.5, 0.64, 0.58, 0.19, '2018-01-02 20:20:38', 79);
INSERT INTO `exponent` VALUES (41, '武昌三中', '2016', '湖北', '武汉', '武昌', 762, 5002, 200, 211, 22, 333, 1024, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.03, 0.28, 0.03, 1, 0.2, 0.5, 0.5, 0.67, 0.55, 0.21, '2018-01-02 20:21:31', 79);
INSERT INTO `exponent` VALUES (42, '武昌三中', '2017', '湖北', '武汉', '武昌', 762, 2023, 211, 221, 33, 455, 1024, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.01, 0.29, 0.04, 1, 0.23, 0.5, 0.5, 0.67, 0.55, 0.16, '2018-01-02 20:22:35', 79);
INSERT INTO `exponent` VALUES (43, '汉口二中', '2018', '湖北', '武汉', '汉口', 776, 300000, 30, 122, 56, 233, 1024, 0.6, 0.9, 1, 1, 0.6, 0.9, 1, 0.16, 0.24, 1, 0.34, 0.7, 1, 0.7, 0.79, 0.68, '2018-05-10 15:45:48', 44);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `desc` varchar(200) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `permission` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of role
-- ----------------------------
BEGIN;
INSERT INTO `role` VALUES (1, '教师', '教师权限，查看本校指数,修改个人信息。', '2017-12-05 22:26:09', 1);
INSERT INTO `role` VALUES (2, '学校管理者', '学校管理者权限，修改个人信息，查看本校指数，学校排名与分析，学校诊断报告，数据录入与修改，注册教师角色用户', '2017-12-05 22:26:09', 2);
INSERT INTO `role` VALUES (3, '区域管理员', '区域管理者的权限，修改个人信息，查看学校排名与分析，学校检索，注册学校管理者角色用户。', '2017-12-05 22:26:09', 4);
INSERT INTO `role` VALUES (4, '系统开发者', '开发人员管理角色，管理维护系统，注册区域管理员用户。', '2017-12-05 22:26:09', 8);
INSERT INTO `role` VALUES (5, '专家', '随机对学校就绪指数进行诊断。', '2018-05-16 14:57:21', 16);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `join_time` datetime DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `school_name` varchar(100) DEFAULT NULL,
  `district_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (40, 'admin', '111111', '409322382@qq.com', '2017-12-06 21:04:11', 4, NULL, NULL, NULL);
INSERT INTO `user` VALUES (42, '汉口区管理', '111111', 'quyuguanli1@qq.com', '2017-12-06 21:06:46', 3, 40, NULL, '汉口');
INSERT INTO `user` VALUES (43, '青山区管理', '111111', 'quyuguanli2@qq.com', '2017-12-06 21:07:26', 3, 40, NULL, '青山');
INSERT INTO `user` VALUES (44, '汉口二中学校管理', '111111', 'xuexiaoguanli1@qq.com', '2017-12-06 21:08:41', 2, 42, '汉口二中', NULL);
INSERT INTO `user` VALUES (45, '汉口一中学校管理', '111111', 'xuexiaoguanli2@qq.com', '2017-12-06 21:09:05', 2, 42, '汉口一中', NULL);
INSERT INTO `user` VALUES (46, '青山二中学校管理', '111111', 'xuexiaoguanli3@qq.com', '2017-12-06 21:10:06', 2, 43, '青山二中', NULL);
INSERT INTO `user` VALUES (47, '青山一中学校管理', '111111', 'xuexiaoguanli4@qq.com', '2017-12-06 21:10:24', 2, 43, '青山一中', NULL);
INSERT INTO `user` VALUES (65, '汉口二中教师一', '111111', 'jiaoshi7@qq.com', '2018-01-01 23:55:08', 1, 44, NULL, NULL);
INSERT INTO `user` VALUES (74, '汉口三中学校管理', '111111', 'xuexiaoguanli5@qq.com', '2018-01-02 17:49:38', 2, 42, '汉口三中', NULL);
INSERT INTO `user` VALUES (75, '武昌区管理', '111111', 'quyuguanli3@qq.com', '2018-01-02 17:53:35', 3, 40, '', '武昌');
INSERT INTO `user` VALUES (76, '青山三中学校管理', '111111', 'xuexiaoguanli6@qq.com', '2018-01-02 18:01:08', 2, 43, '青山三中', NULL);
INSERT INTO `user` VALUES (77, '武昌一中学校管理', '111111', 'xuexiaoguanli7@qq.com', '2018-01-02 18:01:58', 2, 75, '武昌一中', NULL);
INSERT INTO `user` VALUES (78, '武昌二中学校管理', '111111', 'xuexiaoguanli8@qq.com', '2018-01-02 18:02:21', 2, 75, '武昌二中', NULL);
INSERT INTO `user` VALUES (79, '武昌三中学校管理', '111111', 'xuexiaoguanli9@qq.com', '2018-01-02 18:02:44', 2, 75, '武昌三中', NULL);
INSERT INTO `user` VALUES (80, '武昌四中学校管理', '111111', 'xuexiaoguanli10@qq.com', '2018-01-02 18:03:55', 2, 75, '武昌四中', NULL);
INSERT INTO `user` VALUES (81, '汉口四中学校管理', '111111', 'xuexiaoguanli11@qq.com', '2018-01-02 18:05:23', 2, 42, '汉口四中', NULL);
INSERT INTO `user` VALUES (82, '汉口一中教师一', '111111', 'jiaoshi5@qq.com', '2018-01-02 18:15:23', 1, 45, '', NULL);
INSERT INTO `user` VALUES (83, '汉口一中教师二', '111111', 'jiaoshi6@qq.com', '2018-01-02 18:16:21', 1, 45, '', NULL);
INSERT INTO `user` VALUES (84, '青山一中教师一', '111111', 'jiaoshi9@qq.com', '2018-01-02 18:19:55', 1, 47, '', NULL);
INSERT INTO `user` VALUES (85, '青山一中教师二', '111111', 'jiaoshi10@qq.com', '2018-01-02 18:20:17', 1, 47, '', NULL);
INSERT INTO `user` VALUES (86, '汉口三中教师一', '111111', 'jiaoshi11@qq.com', '2018-01-02 18:21:12', 1, 74, '', NULL);
INSERT INTO `user` VALUES (87, '汉口三中教师二', '111111', 'jiaoshi12@qq.com', '2018-01-02 18:21:38', 1, 74, '', NULL);
INSERT INTO `user` VALUES (88, '青山三中教师一', '111111', 'jiaoshi13@qq.com', '2018-01-02 18:22:35', 1, 76, '', NULL);
INSERT INTO `user` VALUES (89, '青山三中教师二', '111111', 'jiaoshi14@qq.com', '2018-01-02 18:23:00', 1, 76, '', NULL);
INSERT INTO `user` VALUES (90, '武昌一中教师一', '111111', 'jiaoshi15@qq.com', '2018-01-02 18:24:22', 1, 77, '', NULL);
INSERT INTO `user` VALUES (91, '武昌一中教师二', '111111', 'jiaoshi16@qq.com', '2018-01-02 18:24:48', 1, 77, '', NULL);
INSERT INTO `user` VALUES (92, '武昌二中教师一', '111111', 'jiaoshi17@qq.com', '2018-01-02 18:25:45', 1, 78, '', NULL);
INSERT INTO `user` VALUES (93, '武昌二中教师二', '111111', 'jiaoshi18@qq.com', '2018-01-02 18:26:26', 1, 78, '', NULL);
INSERT INTO `user` VALUES (94, '武昌三中教师一', '111111', 'jiaoshi19@qq.com', '2018-01-02 18:27:44', 1, 79, '', NULL);
INSERT INTO `user` VALUES (95, '武昌三中教师二', '111111', 'jiaoshi20@qq.com', '2018-01-02 18:28:03', 1, 79, '', NULL);
INSERT INTO `user` VALUES (96, '汉口四中教师一', '111111', 'jiaoshi21@qq.com', '2018-01-02 18:29:31', 1, 81, '', NULL);
INSERT INTO `user` VALUES (97, '汉口四中教师二', '111111', 'jiaoshi22@qq.com', '2018-01-02 18:29:51', 1, 81, '', NULL);
INSERT INTO `user` VALUES (98, '青山四中学校管理', '111111', 'xuexiaoguanli12@qq.com', '2018-01-02 18:31:04', 2, 43, '青山四中', NULL);
INSERT INTO `user` VALUES (99, '青山四中教师一', '111111', 'jiaoshi23@qq.com', '2018-01-02 18:31:52', 1, 98, '', NULL);
INSERT INTO `user` VALUES (100, '青山四中教师二', '111111', 'jiaoshi24@qq.com', '2018-01-02 18:32:13', 1, 98, '', NULL);
INSERT INTO `user` VALUES (104, '青山二中教师一', '111111', 'jiaoshi25@qq.com', '2018-01-02 19:18:50', 1, 46, '', '');
INSERT INTO `user` VALUES (105, '青山二中教师二', '111111', 'jiaoshi26@qq.com', '2018-01-02 19:19:32', 1, 46, '', '');
INSERT INTO `user` VALUES (106, '专家1', '111111', 'zhuanjia1@qq.com', '2018-05-16 15:12:54', 5, 40, '', '');
INSERT INTO `user` VALUES (107, '专家2', '111111', 'zhuanjia2@qq.com', '2018-05-16 15:13:41', 5, 40, '', '');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
