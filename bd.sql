-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: rdr
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Aplicacion_aplicacion`
--

DROP TABLE IF EXISTS `Aplicacion_aplicacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Aplicacion_aplicacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(128) DEFAULT NULL,
  `descripcion` varchar(256) DEFAULT NULL,
  `archivo` varchar(256) DEFAULT NULL,
  `fecha` datetime(6) NOT NULL,
  `autor` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Aplicacion_aplicacion`
--

LOCK TABLES `Aplicacion_aplicacion` WRITE;
/*!40000 ALTER TABLE `Aplicacion_aplicacion` DISABLE KEYS */;
INSERT INTO `Aplicacion_aplicacion` VALUES (4,'Filtros','Aplicacion con STP implementado y politicas de aceptacion y rechazo de paquetes','/media/App-4.py','2018-07-05 16:51:12.000000','Javier Barroso'),(5,'Simple switch','Aplicacion para imbuir el comportamiento de un conmutador ','/media/App-5.py','2018-07-05 16:52:25.000000','Git Ryu');
/*!40000 ALTER TABLE `Aplicacion_aplicacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Configuracion_configuracion`
--

DROP TABLE IF EXISTS `Configuracion_configuracion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Configuracion_configuracion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(128) DEFAULT NULL,
  `nota` varchar(256) DEFAULT NULL,
  `archivo` varchar(256) DEFAULT NULL,
  `fecha` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Configuracion_configuracion`
--

LOCK TABLES `Configuracion_configuracion` WRITE;
/*!40000 ALTER TABLE `Configuracion_configuracion` DISABLE KEYS */;
INSERT INTO `Configuracion_configuracion` VALUES (3,'Configuracion HP-1','Primera configuracion propuesta para el switch HP-1','/media/Conf-3.conf','2018-07-05 16:47:13.000000'),(4,'Configuracion HP-2','Primera configuracion propuesta para el switch HP-2','/media/Conf-4.conf','2018-07-05 16:47:44.000000'),(5,'Configuracion MikroTik','Primera configuracion propuesta para el switch de MikroTik','/media/Conf-5.conf','2018-07-05 16:49:38.000000');
/*!40000 ALTER TABLE `Configuracion_configuracion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Conmutador_conmutador`
--

DROP TABLE IF EXISTS `Conmutador_conmutador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Conmutador_conmutador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(128) DEFAULT NULL,
  `version` varchar(256) NOT NULL,
  `controlador` varchar(256) DEFAULT NULL,
  `instancia` varchar(256) DEFAULT NULL,
  `fabricante` varchar(256) DEFAULT NULL,
  `ip` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip` (`ip`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Conmutador_conmutador`
--

LOCK TABLES `Conmutador_conmutador` WRITE;
/*!40000 ALTER TABLE `Conmutador_conmutador` DISABLE KEYS */;
INSERT INTO `Conmutador_conmutador` VALUES (17,'HP-1','1.0','172.18.1.5','aggregate','HP','172.18.1.2'),(18,'HP-2','1.0','172.18.1.6','aggregate','HP','172.18.1.3'),(21,'Mikrotik','1.0','172.18.1.7','aggregate','MikroTik','172.18.1.4');
/*!40000 ALTER TABLE `Conmutador_conmutador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Grafico_grafico`
--

DROP TABLE IF EXISTS `Grafico_grafico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Grafico_grafico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `trafico` int(11) DEFAULT NULL,
  `tipo` varchar(256) DEFAULT NULL,
  `ip` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=318 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Grafico_grafico`
--

LOCK TABLES `Grafico_grafico` WRITE;
/*!40000 ALTER TABLE `Grafico_grafico` DISABLE KEYS */;
INSERT INTO `Grafico_grafico` VALUES (304,'2018-06-29 11:33:38.000000',0,'entrada','172.18.1.4'),(305,'2018-06-29 11:33:38.000000',0,'salida','172.18.1.4'),(306,'2018-06-30 17:03:02.000000',0,'entrada','172.18.1.4'),(307,'2018-06-30 17:03:02.000000',0,'salida','172.18.1.4'),(308,'2018-06-30 17:03:02.000000',0,'entrada','172.18.1.3'),(309,'2018-06-30 17:03:02.000000',0,'salida','172.18.1.3'),(310,'2018-06-30 17:03:02.000000',0,'entrada','172.18.1.2'),(311,'2018-06-30 17:03:02.000000',0,'salida','172.18.1.2'),(312,'2018-07-05 08:38:05.000000',0,'entrada','172.18.1.4'),(313,'2018-07-05 08:38:05.000000',0,'salida','172.18.1.4'),(314,'2018-07-05 08:38:05.000000',0,'entrada','172.18.1.3'),(315,'2018-07-05 08:38:05.000000',0,'salida','172.18.1.3'),(316,'2018-07-05 08:38:05.000000',0,'entrada','172.18.1.2'),(317,'2018-07-05 08:38:05.000000',0,'salida','172.18.1.2');
/*!40000 ALTER TABLE `Grafico_grafico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Politica_politica`
--

DROP TABLE IF EXISTS `Politica_politica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Politica_politica` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `politica` int(11) NOT NULL,
  `origen` int(11) DEFAULT NULL,
  `destino` int(11) DEFAULT NULL,
  `accion` varchar(256) DEFAULT NULL,
  `switch` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `politica` (`politica`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Politica_politica`
--

LOCK TABLES `Politica_politica` WRITE;
/*!40000 ALTER TABLE `Politica_politica` DISABLE KEYS */;
INSERT INTO `Politica_politica` VALUES (12,1,2,3,'Rechazar','172.18.1.3'),(13,13,4,5,'Aceptar','172.18.1.4');
/*!40000 ALTER TABLE `Politica_politica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Politica_politica_usuario`
--

DROP TABLE IF EXISTS `Politica_politica_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Politica_politica_usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `politica` int(11) NOT NULL,
  `usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Politica_politica_usuario`
--

LOCK TABLES `Politica_politica_usuario` WRITE;
/*!40000 ALTER TABLE `Politica_politica_usuario` DISABLE KEYS */;
INSERT INTO `Politica_politica_usuario` VALUES (1,1,12),(2,1,10),(3,2,10);
/*!40000 ALTER TABLE `Politica_politica_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuario_usuario`
--

DROP TABLE IF EXISTS `Usuario_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Usuario_usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(128) DEFAULT NULL,
  `apellidos` varchar(128) DEFAULT NULL,
  `correo` varchar(256) NOT NULL,
  `usuario` varchar(256) DEFAULT NULL,
  `credencial` varchar(256) DEFAULT NULL,
  `es_admin` tinyint(1) NOT NULL,
  `ultima_sesion` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `apellidos` (`apellidos`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario_usuario`
--

LOCK TABLES `Usuario_usuario` WRITE;
/*!40000 ALTER TABLE `Usuario_usuario` DISABLE KEYS */;
INSERT INTO `Usuario_usuario` VALUES (7,'root','root','root@email.com','root','$6$rounds=656000$0hMtvuHupJ59QD1P$BxVrDJUssPKvtVKmLbPu.PcJFJGMmBWR2/CkNnZXDHwARd4eVn4qoPUvZvkWKMNZCphhKv5PWHjoM7Kvvpbzl/',1,'2018-07-05 16:30:05.000000');
/*!40000 ALTER TABLE `Usuario_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add conmutador',7,'add_conmutador'),(20,'Can change conmutador',7,'change_conmutador'),(21,'Can delete conmutador',7,'delete_conmutador'),(22,'Can add aplicacion',8,'add_aplicacion'),(23,'Can change aplicacion',8,'change_aplicacion'),(24,'Can delete aplicacion',8,'delete_aplicacion'),(25,'Can add usuario',9,'add_usuario'),(26,'Can change usuario',9,'change_usuario'),(27,'Can delete usuario',9,'delete_usuario'),(28,'Can add configuracion',10,'add_configuracion'),(29,'Can change configuracion',10,'change_configuracion'),(30,'Can delete configuracion',10,'delete_configuracion'),(31,'Can add politica',11,'add_politica'),(32,'Can change politica',11,'change_politica'),(33,'Can delete politica',11,'delete_politica'),(34,'Can add politica_ usuario',12,'add_politica_usuario'),(35,'Can change politica_ usuario',12,'change_politica_usuario'),(36,'Can delete politica_ usuario',12,'delete_politica_usuario'),(37,'Can add grafico',13,'add_grafico'),(38,'Can change grafico',13,'change_grafico'),(39,'Can delete grafico',13,'delete_grafico');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(8,'Aplicacion','aplicacion'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(10,'Configuracion','configuracion'),(7,'Conmutador','conmutador'),(5,'contenttypes','contenttype'),(13,'Grafico','grafico'),(11,'Politica','politica'),(12,'Politica','politica_usuario'),(6,'sessions','session'),(9,'Usuario','usuario');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Aplicacion','0001_initial','2018-06-08 07:38:52.685979'),(2,'Configuracion','0001_initial','2018-06-08 07:38:52.710491'),(3,'Conmutador','0001_initial','2018-06-08 07:38:52.743536'),(4,'Politica','0001_initial','2018-06-08 07:38:52.803337'),(5,'Usuario','0001_initial','2018-06-08 07:38:52.847920'),(6,'contenttypes','0001_initial','2018-06-08 07:38:52.901607'),(7,'auth','0001_initial','2018-06-08 07:38:53.356617'),(8,'admin','0001_initial','2018-06-08 07:38:53.489915'),(9,'admin','0002_logentry_remove_auto_add','2018-06-08 07:38:53.528442'),(10,'contenttypes','0002_remove_content_type_name','2018-06-08 07:38:53.617105'),(11,'auth','0002_alter_permission_name_max_length','2018-06-08 07:38:53.644149'),(12,'auth','0003_alter_user_email_max_length','2018-06-08 07:38:53.671844'),(13,'auth','0004_alter_user_username_opts','2018-06-08 07:38:53.683330'),(14,'auth','0005_alter_user_last_login_null','2018-06-08 07:38:53.721155'),(15,'auth','0006_require_contenttypes_0002','2018-06-08 07:38:53.727863'),(16,'auth','0007_alter_validators_add_error_messages','2018-06-08 07:38:53.762576'),(17,'auth','0008_alter_user_username_max_length','2018-06-08 07:38:53.786796'),(18,'sessions','0001_initial','2018-06-08 07:38:53.814189'),(19,'Politica','0002_remove_politica_protocolo','2018-06-19 10:50:51.713031'),(20,'Aplicacion','0002_aplicacion_fichero','2018-06-20 08:01:22.472103'),(21,'Grafico','0001_initial','2018-06-28 07:26:25.399994'),(22,'Grafico','0002_auto_20180628_0730','2018-06-28 07:30:33.311725'),(23,'Aplicacion','0003_remove_aplicacion_fichero','2018-06-28 17:20:43.735641'),(24,'Conmutador','0002_auto_20180628_1720','2018-06-28 17:20:43.871236'),(25,'Grafico','0003_auto_20180628_1720','2018-06-28 17:20:44.005946'),(26,'Politica','0003_politica_switch','2018-06-28 17:20:44.081260'),(27,'Politica','0004_auto_20180702_1424','2018-07-03 06:14:57.837699');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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

-- Dump completed on 2018-07-05 17:04:08
