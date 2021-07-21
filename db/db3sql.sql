-- MySQL dump 10.13  Distrib 8.0.26, for macos11 (x86_64)
--
-- Host: 127.0.0.1    Database: db3
-- ------------------------------------------------------
-- Server version	8.0.25

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
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
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
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
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Prueba',7,'add_prueba'),(26,'Can change Prueba',7,'change_prueba'),(27,'Can delete Prueba',7,'delete_prueba'),(28,'Can view Prueba',7,'view_prueba'),(29,'Can add Sede',8,'add_sede'),(30,'Can change Sede',8,'change_sede'),(31,'Can delete Sede',8,'delete_sede'),(32,'Can view Sede',8,'view_sede'),(33,'Can add Tipo de Identifación',9,'add_tipo_identificacion'),(34,'Can change Tipo de Identifación',9,'change_tipo_identificacion'),(35,'Can delete Tipo de Identifación',9,'delete_tipo_identificacion'),(36,'Can view Tipo de Identifación',9,'view_tipo_identificacion'),(37,'Can add Persona',10,'add_persona'),(38,'Can change Persona',10,'change_persona'),(39,'Can delete Persona',10,'delete_persona'),(40,'Can view Persona',10,'view_persona'),(41,'Can add fecha',11,'add_fecha'),(42,'Can change fecha',11,'change_fecha'),(43,'Can delete fecha',11,'delete_fecha'),(44,'Can view fecha',11,'view_fecha'),(45,'Can add cita',12,'add_cita'),(46,'Can change cita',12,'change_cita'),(47,'Can delete cita',12,'delete_cita'),(48,'Can view cita',12,'view_cita');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_cita`
--

DROP TABLE IF EXISTS `core_cita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_cita` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `otras_indicaciones` varchar(450) DEFAULT NULL,
  `id_fecha_cita_id` bigint NOT NULL,
  `id_persona_id` int NOT NULL,
  `id_prueba_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_fecha_cita_id` (`id_fecha_cita_id`),
  UNIQUE KEY `id_prueba_id` (`id_prueba_id`),
  KEY `core_cita_id_persona_id_4e5968ee_fk_core_tipo` (`id_persona_id`),
  CONSTRAINT `core_cita_id_fecha_cita_id_44855c25_fk_core_fecha_id` FOREIGN KEY (`id_fecha_cita_id`) REFERENCES `core_fecha` (`id`),
  CONSTRAINT `core_cita_id_persona_id_4e5968ee_fk_core_tipo` FOREIGN KEY (`id_persona_id`) REFERENCES `core_tipo_identificacion` (`identificacion`),
  CONSTRAINT `core_cita_id_prueba_id_40ff7dd8_fk_core_prueba_id` FOREIGN KEY (`id_prueba_id`) REFERENCES `core_prueba` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_cita`
--

LOCK TABLES `core_cita` WRITE;
/*!40000 ALTER TABLE `core_cita` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_cita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_fecha`
--

DROP TABLE IF EXISTS `core_fecha`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_fecha` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_disponible` datetime(6) NOT NULL,
  `id_sede_id` bigint NOT NULL,
  `id_prueba_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fecha_disponible` (`fecha_disponible`),
  KEY `core_fecha_id_sede_id_4b285407_fk_core_sede_id` (`id_sede_id`),
  KEY `core_fecha_id_prueba_id_4a9a6e77_fk_core_prueba_id` (`id_prueba_id`),
  CONSTRAINT `core_fecha_id_prueba_id_4a9a6e77_fk_core_prueba_id` FOREIGN KEY (`id_prueba_id`) REFERENCES `core_prueba` (`id`),
  CONSTRAINT `core_fecha_id_sede_id_4b285407_fk_core_sede_id` FOREIGN KEY (`id_sede_id`) REFERENCES `core_sede` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_fecha`
--

LOCK TABLES `core_fecha` WRITE;
/*!40000 ALTER TABLE `core_fecha` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_fecha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_persona`
--

DROP TABLE IF EXISTS `core_persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_persona` (
  `numero_identificacion_id` int NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `primer_apellido` varchar(30) NOT NULL,
  `segundo_apellido` varchar(30) NOT NULL,
  PRIMARY KEY (`numero_identificacion_id`),
  CONSTRAINT `core_persona_numero_identificacio_51d190dc_fk_core_tipo` FOREIGN KEY (`numero_identificacion_id`) REFERENCES `core_tipo_identificacion` (`identificacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_persona`
--

LOCK TABLES `core_persona` WRITE;
/*!40000 ALTER TABLE `core_persona` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_prueba`
--

DROP TABLE IF EXISTS `core_prueba`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_prueba` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo_prueba` varchar(9) NOT NULL,
  `tipo_licencia` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_prueba` (`tipo_prueba`),
  UNIQUE KEY `tipo_licencia` (`tipo_licencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_prueba`
--

LOCK TABLES `core_prueba` WRITE;
/*!40000 ALTER TABLE `core_prueba` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_prueba` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_sede`
--

DROP TABLE IF EXISTS `core_sede`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_sede` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ubicacion` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ubicacion` (`ubicacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_sede`
--

LOCK TABLES `core_sede` WRITE;
/*!40000 ALTER TABLE `core_sede` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_sede` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_tipo_identificacion`
--

DROP TABLE IF EXISTS `core_tipo_identificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_tipo_identificacion` (
  `identificacion` int NOT NULL,
  `tipo` varchar(50) NOT NULL,
  PRIMARY KEY (`identificacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_tipo_identificacion`
--

LOCK TABLES `core_tipo_identificacion` WRITE;
/*!40000 ALTER TABLE `core_tipo_identificacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_tipo_identificacion` ENABLE KEYS */;
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
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(12,'core','cita'),(11,'core','fecha'),(10,'core','persona'),(7,'core','prueba'),(8,'core','sede'),(9,'core','tipo_identificacion'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-07-21 23:17:47.875196'),(2,'auth','0001_initial','2021-07-21 23:17:48.001470'),(3,'admin','0001_initial','2021-07-21 23:17:48.036489'),(4,'admin','0002_logentry_remove_auto_add','2021-07-21 23:17:48.042506'),(5,'admin','0003_logentry_add_action_flag_choices','2021-07-21 23:17:48.047465'),(6,'contenttypes','0002_remove_content_type_name','2021-07-21 23:17:48.076880'),(7,'auth','0002_alter_permission_name_max_length','2021-07-21 23:17:48.094359'),(8,'auth','0003_alter_user_email_max_length','2021-07-21 23:17:48.111839'),(9,'auth','0004_alter_user_username_opts','2021-07-21 23:17:48.117004'),(10,'auth','0005_alter_user_last_login_null','2021-07-21 23:17:48.133193'),(11,'auth','0006_require_contenttypes_0002','2021-07-21 23:17:48.134517'),(12,'auth','0007_alter_validators_add_error_messages','2021-07-21 23:17:48.140157'),(13,'auth','0008_alter_user_username_max_length','2021-07-21 23:17:48.157594'),(14,'auth','0009_alter_user_last_name_max_length','2021-07-21 23:17:48.176848'),(15,'auth','0010_alter_group_name_max_length','2021-07-21 23:17:48.191733'),(16,'auth','0011_update_proxy_permissions','2021-07-21 23:17:48.198229'),(17,'auth','0012_alter_user_first_name_max_length','2021-07-21 23:17:48.214210'),(18,'core','0001_initial','2021-07-21 23:17:48.306292'),(19,'core','0002_alter_sede_options','2021-07-21 23:17:48.311843'),(20,'core','0003_auto_20210721_2245','2021-07-21 23:19:47.122777'),(21,'core','0004_remove_fecha_id_prueba','2021-07-21 23:19:47.153226'),(22,'core','0005_fecha_id_prueba','2021-07-21 23:19:47.175136'),(23,'core','0006_alter_fecha_id_prueba','2021-07-21 23:19:47.179926'),(24,'sessions','0001_initial','2021-07-21 23:19:47.194991');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
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

-- Dump completed on 2021-07-21 17:27:05
