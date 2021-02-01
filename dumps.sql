-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: data_model_manager
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.19.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add ai model',7,'add_aimodel'),(26,'Can change ai model',7,'change_aimodel'),(27,'Can delete ai model',7,'delete_aimodel'),(28,'Can view ai model',7,'view_aimodel'),(29,'Can add data',8,'add_data'),(30,'Can change data',8,'change_data'),(31,'Can delete data',8,'delete_data'),(32,'Can view data',8,'view_data'),(33,'Can add data category',9,'add_datacategory'),(34,'Can change data category',9,'change_datacategory'),(35,'Can delete data category',9,'delete_datacategory'),(36,'Can view data category',9,'view_datacategory'),(37,'Can add permission',10,'add_permission'),(38,'Can change permission',10,'change_permission'),(39,'Can delete permission',10,'delete_permission'),(40,'Can view permission',10,'view_permission'),(41,'Can add role',11,'add_role'),(42,'Can change role',11,'change_role'),(43,'Can delete role',11,'delete_role'),(44,'Can view role',11,'view_role'),(45,'Can add role has permisson',12,'add_rolehaspermisson'),(46,'Can change role has permisson',12,'change_rolehaspermisson'),(47,'Can delete role has permisson',12,'delete_rolehaspermisson'),(48,'Can view role has permisson',12,'view_rolehaspermisson'),(49,'Can add model train data',13,'add_modeltraindata'),(50,'Can change model train data',13,'change_modeltraindata'),(51,'Can delete model train data',13,'delete_modeltraindata'),(52,'Can view model train data',13,'view_modeltraindata');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_model_manager_app_aimodel`
--

DROP TABLE IF EXISTS `data_model_manager_app_aimodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_model_manager_app_aimodel` (
  `model_id` int NOT NULL AUTO_INCREMENT,
  `model_name` varchar(512) NOT NULL,
  `model_owner_id` int DEFAULT NULL,
  PRIMARY KEY (`model_id`),
  KEY `data_model_manager_a_model_owner_id_8e619d0e_fk_data_mode` (`model_owner_id`),
  CONSTRAINT `data_model_manager_a_model_owner_id_8e619d0e_fk_data_mode` FOREIGN KEY (`model_owner_id`) REFERENCES `data_model_manager_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_model_manager_app_aimodel`
--

LOCK TABLES `data_model_manager_app_aimodel` WRITE;
/*!40000 ALTER TABLE `data_model_manager_app_aimodel` DISABLE KEYS */;
INSERT INTO `data_model_manager_app_aimodel` VALUES (1,'1',1),(2,'2',1),(3,'3',1),(4,'4',1),(5,'5',1),(6,'6',1),(7,'7',1),(8,'8',1),(10,'00000',1),(11,'1234564',2);
/*!40000 ALTER TABLE `data_model_manager_app_aimodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_model_manager_app_data`
--

DROP TABLE IF EXISTS `data_model_manager_app_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_model_manager_app_data` (
  `data_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(512) NOT NULL,
  `size_on_disk` int unsigned NOT NULL,
  `directory_of_data` varchar(512) DEFAULT NULL,
  `number_of_images` int unsigned NOT NULL,
  `number_of_classes` int unsigned DEFAULT NULL,
  `iqa_0` int unsigned DEFAULT NULL,
  `iqa_1` int unsigned DEFAULT NULL,
  `iqa_2` int unsigned DEFAULT NULL,
  `iqa_3` int unsigned DEFAULT NULL,
  `iqa_4` int unsigned DEFAULT NULL,
  `shape_0` int unsigned DEFAULT NULL,
  `shape_1` int unsigned DEFAULT NULL,
  `shape_2` int unsigned DEFAULT NULL,
  `shape_3` int unsigned DEFAULT NULL,
  `shape_4` int unsigned DEFAULT NULL,
  `analyzed` tinyint(1) NOT NULL,
  `best_result` double DEFAULT NULL,
  `data_avatar` varchar(100) DEFAULT NULL,
  `best_analyzed_model_id` int DEFAULT NULL,
  `data_category_id` int NOT NULL,
  `data_owner_id` int DEFAULT NULL,
  PRIMARY KEY (`data_id`),
  KEY `data_model_manager_a_data_category_id_ed4e6ff4_fk_data_mode` (`data_category_id`),
  KEY `data_model_manager_a_best_analyzed_model__7908c80b_fk_data_mode` (`best_analyzed_model_id`),
  KEY `data_model_manager_a_data_owner_id_66be1bd6_fk_data_mode` (`data_owner_id`),
  CONSTRAINT `data_model_manager_a_best_analyzed_model__7908c80b_fk_data_mode` FOREIGN KEY (`best_analyzed_model_id`) REFERENCES `data_model_manager_app_aimodel` (`model_id`),
  CONSTRAINT `data_model_manager_a_data_category_id_ed4e6ff4_fk_data_mode` FOREIGN KEY (`data_category_id`) REFERENCES `data_model_manager_app_datacategory` (`data_category_id`),
  CONSTRAINT `data_model_manager_a_data_owner_id_66be1bd6_fk_data_mode` FOREIGN KEY (`data_owner_id`) REFERENCES `data_model_manager_app_user` (`id`),
  CONSTRAINT `data_model_manager_app_data_chk_1` CHECK ((`size_on_disk` >= 0)),
  CONSTRAINT `data_model_manager_app_data_chk_10` CHECK ((`shape_1` >= 0)),
  CONSTRAINT `data_model_manager_app_data_chk_11` CHECK ((`shape_2` >= 0)),
  CONSTRAINT `data_model_manager_app_data_chk_12` CHECK ((`shape_3` >= 0)),
  CONSTRAINT `data_model_manager_app_data_chk_13` CHECK ((`shape_4` >= 0)),
  CONSTRAINT `data_model_manager_app_data_chk_2` CHECK ((`number_of_images` >= 0)),
  CONSTRAINT `data_model_manager_app_data_chk_3` CHECK ((`number_of_classes` >= 0)),
  CONSTRAINT `data_model_manager_app_data_chk_4` CHECK ((`iqa_0` >= 0)),
  CONSTRAINT `data_model_manager_app_data_chk_5` CHECK ((`iqa_1` >= 0)),
  CONSTRAINT `data_model_manager_app_data_chk_6` CHECK ((`iqa_2` >= 0)),
  CONSTRAINT `data_model_manager_app_data_chk_7` CHECK ((`iqa_3` >= 0)),
  CONSTRAINT `data_model_manager_app_data_chk_8` CHECK ((`iqa_4` >= 0)),
  CONSTRAINT `data_model_manager_app_data_chk_9` CHECK ((`shape_0` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_model_manager_app_data`
--

LOCK TABLES `data_model_manager_app_data` WRITE;
/*!40000 ALTER TABLE `data_model_manager_app_data` DISABLE KEYS */;
INSERT INTO `data_model_manager_app_data` VALUES (1,'1',1,'1',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'',NULL,1,1),(2,'2',2,'2',2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'',NULL,1,2),(3,'3',3,'3',3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'data/data_avatar/jack_of_heart_c5FvKjH.jpg',NULL,1,1),(4,'4',4,'4',4,4,4,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'data/data_avatar/TFboard_VS_code.jpg',NULL,1,2),(5,'5',5,'5',5,5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'data/data_avatar/screen_qK9dwQ3.jpg',NULL,1,2),(6,'6',6,'May nay',6,6,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'data/data_avatar/screen.jpg',NULL,1,2),(7,'7',7,'7',7,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,'data/data_avatar/2.jpg',NULL,4,1),(8,'8',8,'8',8,8,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'',NULL,2,2),(9,'9',9,'9',9,9,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'',NULL,2,1),(10,'333',333,'3333',3333,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'',NULL,3,2),(11,'0',0,'0',0,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'',NULL,1,2),(12,'0000',9999,'999',99999,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'data/data_avatar/jack_of_heart.jpg',NULL,4,1),(13,'23123123',3213123,'12312312',312312312,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'data/data_avatar/ace_of_heart.jpg',NULL,2,2),(15,'11111',11111,'1213123123',343434,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'data/data_avatar/ace_of_spade.jpg',NULL,2,1),(16,'1000',1112,'2222222222222',2222222,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,'data/data_avatar/queen_of_heart.jpg',NULL,2,1),(17,'00',111111,'22222222222222',11,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,'data/data_avatar/king_of_diamonds.jpg',NULL,3,2);
/*!40000 ALTER TABLE `data_model_manager_app_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_model_manager_app_datacategory`
--

DROP TABLE IF EXISTS `data_model_manager_app_datacategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_model_manager_app_datacategory` (
  `data_category_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(512) NOT NULL,
  PRIMARY KEY (`data_category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_model_manager_app_datacategory`
--

LOCK TABLES `data_model_manager_app_datacategory` WRITE;
/*!40000 ALTER TABLE `data_model_manager_app_datacategory` DISABLE KEYS */;
INSERT INTO `data_model_manager_app_datacategory` VALUES (1,'1'),(2,'2'),(3,'222'),(4,'3232'),(5,'789');
/*!40000 ALTER TABLE `data_model_manager_app_datacategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_model_manager_app_modeltraindata`
--

DROP TABLE IF EXISTS `data_model_manager_app_modeltraindata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_model_manager_app_modeltraindata` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data_id` int NOT NULL,
  `model_id` int NOT NULL,
  `added_by_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `data_model_manager_a_data_id_9c528fc8_fk_data_mode` (`data_id`),
  KEY `data_model_manager_a_model_id_65db1e23_fk_data_mode` (`model_id`),
  KEY `data_model_manager_a_added_by_id_21045f9a_fk_data_mode` (`added_by_id`),
  CONSTRAINT `data_model_manager_a_added_by_id_21045f9a_fk_data_mode` FOREIGN KEY (`added_by_id`) REFERENCES `data_model_manager_app_user` (`id`),
  CONSTRAINT `data_model_manager_a_data_id_9c528fc8_fk_data_mode` FOREIGN KEY (`data_id`) REFERENCES `data_model_manager_app_data` (`data_id`),
  CONSTRAINT `data_model_manager_a_model_id_65db1e23_fk_data_mode` FOREIGN KEY (`model_id`) REFERENCES `data_model_manager_app_aimodel` (`model_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_model_manager_app_modeltraindata`
--

LOCK TABLES `data_model_manager_app_modeltraindata` WRITE;
/*!40000 ALTER TABLE `data_model_manager_app_modeltraindata` DISABLE KEYS */;
INSERT INTO `data_model_manager_app_modeltraindata` VALUES (1,1,1,NULL);
/*!40000 ALTER TABLE `data_model_manager_app_modeltraindata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_model_manager_app_permission`
--

DROP TABLE IF EXISTS `data_model_manager_app_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_model_manager_app_permission` (
  `permission_id` int NOT NULL AUTO_INCREMENT,
  `permission_name` varchar(512) NOT NULL,
  `method` varchar(20) NOT NULL,
  `permission_url_name` varchar(512) NOT NULL,
  PRIMARY KEY (`permission_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_model_manager_app_permission`
--

LOCK TABLES `data_model_manager_app_permission` WRITE;
/*!40000 ALTER TABLE `data_model_manager_app_permission` DISABLE KEYS */;
INSERT INTO `data_model_manager_app_permission` VALUES (1,'delete_data','DELETE','data_detail'),(2,'delete_model','DELETE','ai_model_detail'),(3,'update_model','POST','ai_model_detail'),(4,'change_password','POST','change_password'),(5,'update_data_category','POST','update_data_category'),(7,'create_data','POST','data_page'),(8,'create_model','POST','ai_model'),(9,'create_data_category','POST','data_category'),(10,'update_data','POST','data_detail');
/*!40000 ALTER TABLE `data_model_manager_app_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_model_manager_app_role`
--

DROP TABLE IF EXISTS `data_model_manager_app_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_model_manager_app_role` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(512) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_model_manager_app_role`
--

LOCK TABLES `data_model_manager_app_role` WRITE;
/*!40000 ALTER TABLE `data_model_manager_app_role` DISABLE KEYS */;
INSERT INTO `data_model_manager_app_role` VALUES (1,'user'),(2,'guest');
/*!40000 ALTER TABLE `data_model_manager_app_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_model_manager_app_rolehaspermisson`
--

DROP TABLE IF EXISTS `data_model_manager_app_rolehaspermisson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_model_manager_app_rolehaspermisson` (
  `id` int NOT NULL AUTO_INCREMENT,
  `permission_id` int NOT NULL,
  `role_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `data_model_manager_a_permission_id_af133401_fk_data_mode` (`permission_id`),
  KEY `data_model_manager_a_role_id_89100bef_fk_data_mode` (`role_id`),
  CONSTRAINT `data_model_manager_a_permission_id_af133401_fk_data_mode` FOREIGN KEY (`permission_id`) REFERENCES `data_model_manager_app_permission` (`permission_id`),
  CONSTRAINT `data_model_manager_a_role_id_89100bef_fk_data_mode` FOREIGN KEY (`role_id`) REFERENCES `data_model_manager_app_role` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_model_manager_app_rolehaspermisson`
--

LOCK TABLES `data_model_manager_app_rolehaspermisson` WRITE;
/*!40000 ALTER TABLE `data_model_manager_app_rolehaspermisson` DISABLE KEYS */;
INSERT INTO `data_model_manager_app_rolehaspermisson` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,7,1),(9,8,1),(10,9,1),(12,10,1),(13,4,2);
/*!40000 ALTER TABLE `data_model_manager_app_rolehaspermisson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_model_manager_app_user`
--

DROP TABLE IF EXISTS `data_model_manager_app_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_model_manager_app_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `last_login` datetime(6) DEFAULT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(512) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `token` varchar(512) DEFAULT NULL,
  `role_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `data_model_manager_a_role_id_54e85c9c_fk_data_mode` (`role_id`),
  CONSTRAINT `data_model_manager_a_role_id_54e85c9c_fk_data_mode` FOREIGN KEY (`role_id`) REFERENCES `data_model_manager_app_role` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_model_manager_app_user`
--

LOCK TABLES `data_model_manager_app_user` WRITE;
/*!40000 ALTER TABLE `data_model_manager_app_user` DISABLE KEYS */;
INSERT INTO `data_model_manager_app_user` VALUES (1,'2021-02-01 09:40:28.874643','sonthanhnguyen','pbkdf2_sha256$216000$Oeob9BHt2BCF$ZygQQ3ti1lxBWTD84PSOPb58BcAxFJtD2A2mM1z5CVw=',1,1,1,NULL,1),(2,'2021-02-01 09:46:28.715394','son1','pbkdf2_sha256$216000$Ayz47bgaml7K$Xw9nlbPBGega7t5ryhhbT5uKk2PvJbBBorbJLlxzKE0=',1,0,1,NULL,1),(3,'2021-02-01 09:37:58.300073','son2','pbkdf2_sha256$216000$unczXpL6r2SF$/VVL39gKSPJJgg92uGja4mUiLbRqidktnDnlcHvIcgE=',1,0,1,NULL,2);
/*!40000 ALTER TABLE `data_model_manager_app_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_model_manager_app_user_groups`
--

DROP TABLE IF EXISTS `data_model_manager_app_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_model_manager_app_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `data_model_manager_app_u_user_id_group_id_52acc387_uniq` (`user_id`,`group_id`),
  KEY `data_model_manager_a_group_id_70b431fd_fk_auth_grou` (`group_id`),
  CONSTRAINT `data_model_manager_a_group_id_70b431fd_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `data_model_manager_a_user_id_247ac569_fk_data_mode` FOREIGN KEY (`user_id`) REFERENCES `data_model_manager_app_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_model_manager_app_user_groups`
--

LOCK TABLES `data_model_manager_app_user_groups` WRITE;
/*!40000 ALTER TABLE `data_model_manager_app_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `data_model_manager_app_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_model_manager_app_user_user_permissions`
--

DROP TABLE IF EXISTS `data_model_manager_app_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_model_manager_app_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `data_model_manager_app_u_user_id_permission_id_c9f23276_uniq` (`user_id`,`permission_id`),
  KEY `data_model_manager_a_permission_id_6e48f15c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `data_model_manager_a_permission_id_6e48f15c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `data_model_manager_a_user_id_f828e389_fk_data_mode` FOREIGN KEY (`user_id`) REFERENCES `data_model_manager_app_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_model_manager_app_user_user_permissions`
--

LOCK TABLES `data_model_manager_app_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `data_model_manager_app_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `data_model_manager_app_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_data_mode` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_data_mode` FOREIGN KEY (`user_id`) REFERENCES `data_model_manager_app_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-01-29 04:06:11.244354','1','delete_data',1,'[{\"added\": {}}]',10,1),(2,'2021-01-29 04:06:19.408211','2','delete_model',1,'[{\"added\": {}}]',10,1),(3,'2021-01-29 04:06:30.989827','3','update_model',1,'[{\"added\": {}}]',10,1),(4,'2021-01-29 04:06:40.096188','4','change_password',1,'[{\"added\": {}}]',10,1),(5,'2021-01-29 04:07:20.486672','5','update_data_category',1,'[{\"added\": {}}]',10,1),(6,'2021-01-29 04:07:48.812587','6','add_model',1,'[{\"added\": {}}]',10,1),(7,'2021-01-29 04:09:04.263642','7','create_data',1,'[{\"added\": {}}]',10,1),(8,'2021-01-29 04:09:15.409217','8','create_model',1,'[{\"added\": {}}]',10,1),(9,'2021-01-29 04:09:20.719905','6','add_model',3,'',10,1),(10,'2021-01-29 04:09:39.768252','9','create_data_category',1,'[{\"added\": {}}]',10,1),(11,'2021-01-29 04:10:44.334126','10','update_data',1,'[{\"added\": {}}]',10,1),(12,'2021-01-29 04:10:53.004082','1','RoleHasPermisson object (1)',1,'[{\"added\": {}}]',12,1),(13,'2021-01-29 04:10:58.204214','2','RoleHasPermisson object (2)',1,'[{\"added\": {}}]',12,1),(14,'2021-01-29 04:11:03.025731','3','RoleHasPermisson object (3)',1,'[{\"added\": {}}]',12,1),(15,'2021-01-29 04:11:08.286197','4','RoleHasPermisson object (4)',1,'[{\"added\": {}}]',12,1),(16,'2021-01-29 04:11:13.289236','5','RoleHasPermisson object (5)',1,'[{\"added\": {}}]',12,1),(17,'2021-01-29 04:11:19.647550','6','RoleHasPermisson object (6)',1,'[{\"added\": {}}]',12,1),(18,'2021-01-29 04:11:31.660985','7','RoleHasPermisson object (7)',1,'[{\"added\": {}}]',12,1),(19,'2021-01-29 04:11:38.758417','8','RoleHasPermisson object (8)',1,'[{\"added\": {}}]',12,1),(20,'2021-01-29 04:11:45.065381','8','RoleHasPermisson object (8)',3,'',12,1),(21,'2021-01-29 04:12:29.689751','7','RoleHasPermisson object (7)',3,'',12,1),(22,'2021-01-29 04:12:38.566748','9','RoleHasPermisson object (9)',1,'[{\"added\": {}}]',12,1),(23,'2021-01-29 04:12:45.138963','10','RoleHasPermisson object (10)',1,'[{\"added\": {}}]',12,1),(24,'2021-01-29 04:12:53.084072','11','RoleHasPermisson object (11)',1,'[{\"added\": {}}]',12,1),(25,'2021-01-29 04:12:57.639800','11','RoleHasPermisson object (11)',3,'',12,1),(26,'2021-01-29 04:13:04.253028','12','RoleHasPermisson object (12)',1,'[{\"added\": {}}]',12,1),(27,'2021-01-29 04:15:02.192279','2','son1',1,'[{\"added\": {}}]',6,1),(28,'2021-02-01 04:26:32.379769','12','Data object (12)',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(29,'2021-02-01 06:46:54.528267','1','ModelTrainData object (1)',1,'[{\"added\": {}}]',13,1),(30,'2021-02-01 07:07:08.092066','13','Data object (13)',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(31,'2021-02-01 08:01:32.947922','11','0',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(32,'2021-02-01 08:01:38.207675','11','0',2,'[]',8,1),(33,'2021-02-01 08:01:43.232477','10','333',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(34,'2021-02-01 08:01:48.523553','9','9',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(35,'2021-02-01 08:01:52.818007','8','8',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(36,'2021-02-01 08:01:59.215262','5','5',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(37,'2021-02-01 08:02:04.563344','7','7',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(38,'2021-02-01 08:02:09.330691','6','6',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(39,'2021-02-01 08:02:24.418857','2','guest',1,'[{\"added\": {}}]',11,1),(40,'2021-02-01 08:02:30.456388','3','son2',1,'[{\"added\": {}}]',6,1),(41,'2021-02-01 08:03:05.642650','13','RoleHasPermisson object (13)',1,'[{\"added\": {}}]',12,1),(42,'2021-02-01 08:04:44.319297','3','son2',2,'[{\"changed\": {\"fields\": [\"Role id\"]}}]',6,1),(43,'2021-02-01 08:09:02.752915','4','4',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(44,'2021-02-01 08:09:08.176752','3','3',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(45,'2021-02-01 08:09:15.156534','2','2',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(46,'2021-02-01 08:09:20.157924','1','1',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1),(47,'2021-02-01 08:10:31.666749','4','4',2,'[{\"changed\": {\"fields\": [\"Data owner\"]}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(7,'data_model_manager_app','aimodel'),(8,'data_model_manager_app','data'),(9,'data_model_manager_app','datacategory'),(13,'data_model_manager_app','modeltraindata'),(10,'data_model_manager_app','permission'),(11,'data_model_manager_app','role'),(12,'data_model_manager_app','rolehaspermisson'),(6,'data_model_manager_app','user'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-01-29 04:04:28.892512'),(2,'contenttypes','0002_remove_content_type_name','2021-01-29 04:04:29.082952'),(3,'auth','0001_initial','2021-01-29 04:04:29.235025'),(4,'auth','0002_alter_permission_name_max_length','2021-01-29 04:04:29.623923'),(5,'auth','0003_alter_user_email_max_length','2021-01-29 04:04:29.642702'),(6,'auth','0004_alter_user_username_opts','2021-01-29 04:04:29.662296'),(7,'auth','0005_alter_user_last_login_null','2021-01-29 04:04:29.680834'),(8,'auth','0006_require_contenttypes_0002','2021-01-29 04:04:29.688497'),(9,'auth','0007_alter_validators_add_error_messages','2021-01-29 04:04:29.707884'),(10,'auth','0008_alter_user_username_max_length','2021-01-29 04:04:29.725293'),(11,'auth','0009_alter_user_last_name_max_length','2021-01-29 04:04:29.736979'),(12,'auth','0010_alter_group_name_max_length','2021-01-29 04:04:29.756539'),(13,'auth','0011_update_proxy_permissions','2021-01-29 04:04:29.770538'),(14,'auth','0012_alter_user_first_name_max_length','2021-01-29 04:04:29.780390'),(15,'data_model_manager_app','0001_initial','2021-01-29 04:04:30.556768'),(16,'admin','0001_initial','2021-01-29 04:04:31.478627'),(17,'admin','0002_logentry_remove_auto_add','2021-01-29 04:04:31.690430'),(18,'admin','0003_logentry_add_action_flag_choices','2021-01-29 04:04:31.714322'),(19,'sessions','0001_initial','2021-01-29 04:04:31.747804'),(20,'data_model_manager_app','0002_data_data_owner','2021-01-30 06:44:34.330250'),(21,'data_model_manager_app','0003_auto_20210201_0715','2021-02-01 07:16:01.638654'),(22,'data_model_manager_app','0004_auto_20210201_0717','2021-02-01 07:17:37.910365'),(23,'data_model_manager_app','0005_modeltraindata_added_by','2021-02-01 07:19:02.860451'),(24,'data_model_manager_app','0006_auto_20210201_0846','2021-02-01 08:47:01.240074');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8ecatgg9qehx0lqgzpz7brullzwjwsqm','.eJxVjEEOwiAQRe_C2hCgMFCX7j0DGZhBqoYmpV0Z765NutDtf-_9l4i4rTVunZc4kTiLQZx-t4T5wW0HdMd2m2We27pMSe6KPGiX15n4eTncv4OKvX7rBKDyiI68HoxmUgTOjxZ0MFRCMYaNQ9TFpOI1OyZmBChsVQZrgxbvD-AFOAQ:1l6Veg:9j34SfZgmzz3sH0eVPht2pH9mpw63vB_5CgziimDz3Y','2021-02-15 09:37:58.304445'),('n4zkvi1s6nypvvrzkzfjnf8irdqgabyy','.eJxVjEEOwiAQRe_C2pAWGIou3fcMZIYZpGpoUtqV8e7apAvd_vfef6mI21ri1mSJE6uLMur0uxGmh9Qd8B3rbdZprusykd4VfdCmx5nleT3cv4OCrXxr2xGE7AyBPxP1A2ZIQNKDY-7EcfaJBzQBDUvw2eZkLQewzvicxAf1_gD6aTib:1l6Vmu:JkpWKUmPBGmbOl75xdVjfdhn4REU9PT1DFc3ikezbCQ','2021-02-15 09:46:28.719507');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-01 17:10:27
