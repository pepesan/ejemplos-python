CREATE DATABASE  IF NOT EXISTS `test`;
USE `test`;
# EJERCICIO 1
DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `id_user` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(70) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `encmethod` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL DEFAULT 'sha1',
  `active` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `nombre_usuario_user` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Aquí van los usuarios de la aplicación';
# Datos iniciales

INSERT INTO `usuarios` VALUES
    (1,'admin','admin','admin@cursosdedesarrollo.com',NULL,'sha1',0),
    (2,'pepito','pepito','pepito@cursosdedesarrollo.com','Administrador','sha1',1),
    (5,'mery','contraseña','p@p.com',NULL,'sha1',0),
    (6,'bea','contraseña','p@p.com',NULL,'sha1',0);


# EJERCICIO 2
INSERT INTO `usuarios`(
`id_user`,
  `username`,
  `password`,
  `email`,
  `name`,
  `encmethod`,
  `active`)
  VALUES (
    NULL,
    'admin',
    'admin',
    'admin@cursosdedesarrollo.com',
    'administrador',
    'none', '1');
# EJERCICIO 3
SELECT * FROM `usuarios`;
# EJERCICIO 4
INSERT INTO `usuarios`(
`id_user`,
  `username`,
  `password`,
  `email`,
  `name`,
  `encmethod`,
  `active`)
  VALUES (
    NULL,
    'pepesan',
    'contraseña',
    'p@p.com',
    'usuario',
    'none', '1');
# EJERCICIO 5
SELECT * FROM `usuarios` WHERE username="pepesan";

# EJERCICIO 6
UPDATE `usuarios` SET active=true WHERE username="pepesan";

# EJERCICIO 7
DELETE FROM `usuarios`WHERE username="pepesan";

# EJERCICIO 8
INSERT INTO `usuarios`(
`id_user`,
  `username`,
  `password`,
  `email`,
  `name`,
  `encmethod`,
  `active`)
  VALUES (
    NULL,
    'pepesan',
    'comtraseña',
    'p@p.com',
    'usuario',
    'none', '1');
INSERT INTO `usuarios`(
`id_user`,
  `username`,
  `password`,
  `email`,
  `name`,
  `encmethod`,
  `active`)
  VALUES (
    NULL,
    'pepesan2',
    'comtraseña',
    'p2@p.com',
    'usuario2',
    'none', '1');
INSERT INTO `usuarios`(
`id_user`,
  `username`,
  `password`,
  `email`,
  `name`,
  `encmethod`,
  `active`)
  VALUES (
    NULL,
    'pepesan3',
    'comtraseña',
    'p3@p.com',
    'usuario3',
    'none', '1');
INSERT INTO `usuarios`(
`id_user`,
  `username`,
  `password`,
  `email`,
  `name`,
  `encmethod`,
  `active`)
  VALUES (
    NULL,
    'pepesan4',
    'comtraseña',
    'p4@p.com',
    'usuario4',
    'none', '1');

# Ejercicio 9 Consulta los usuarios que están activos""
SELECT * FROM `usuarios` WHERE active=1;

# Ejercicio 10 Consulta los 2 primeros usuarios ordenados por nombre de usuario""
SELECT * FROM `usuarios` ORDER BY `username` ASC LIMIT 0, 2;

# Ejercicio 11 Presenta los usuarios de la segunda página, 2 elementos por página
SELECT * FROM `usuarios` ORDER BY `username` ASC LIMIT 2, 2;

