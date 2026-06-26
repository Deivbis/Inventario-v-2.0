-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-06-2026 a las 07:08:49
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inventario`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cambiar_contraseña`
--

CREATE TABLE `cambiar_contraseña` (
  `id` int(11) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `codigo` varchar(6) NOT NULL,
  `fecha_creacion` datetime NOT NULL DEFAULT current_timestamp(),
  `fecha_expiracion` datetime NOT NULL,
  `uso` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cambiar_contraseña`
--

INSERT INTO `cambiar_contraseña` (`id`, `correo`, `codigo`, `fecha_creacion`, `fecha_expiracion`, `uso`) VALUES
(11, 'deivisbarrios465@gmail.com', '552761', '2026-06-19 03:25:03', '2026-06-19 03:40:03', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `estado` varchar(20) DEFAULT 'Activo',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id`, `nombre`, `descripcion`, `estado`, `fecha_registro`) VALUES
(1, 'Electrónica', 'Dispositivos y gadgets electrónicos', 'Activo', '2025-05-17 14:15:22'),
(2, 'Hogar', 'Artículos para el hogar y decoración', 'Activo', '2025-05-28 12:22:15'),
(3, 'Papelería', 'Artículos de oficina, escolares y suministros de escritura', 'Activo', '2025-05-28 21:28:14'),
(4, 'Ferretería', 'Herramientas y materiales para reparaciones y construcción como clavos, martillos, llaves y tornillos.', 'Activo', '2025-05-30 16:24:55');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `cedula` varchar(20) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `correo` varchar(150) DEFAULT NULL,
  `direccion` text DEFAULT NULL,
  `tipo_cliente` varchar(50) NOT NULL DEFAULT 'normal',
  `estado` varchar(20) DEFAULT 'Activo',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`cedula`, `nombre`, `apellido`, `telefono`, `correo`, `direccion`, `tipo_cliente`, `estado`, `fecha_registro`) VALUES
('0912345678', 'Andrés', 'Mejía', '0999988776', 'andres.mejia@gmail.com', 'Calle 10 de Agosto y Olmedo', 'frecuente', 'Activo', '2025-06-08 18:53:14'),
('1122334455', 'Luis', 'Martinez', '555-1111', 'luis.martinez@email.com', 'Av. del Sol 456', 'frecuente', 'Inactivo', '2025-06-08 18:47:30'),
('1234567890', 'Juan ', 'Pérez', '555-5678', 'juan.perez@email.com', 'Av. Siempre Viva 742', 'frecuente', 'Activo', '2025-05-17 14:15:22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_venta`
--

CREATE TABLE `detalle_venta` (
  `id` int(11) NOT NULL,
  `id_venta` int(11) DEFAULT NULL,
  `id_producto` int(11) DEFAULT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `descuento` int(11) NOT NULL,
  `estado` varchar(20) DEFAULT 'Activo',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detalle_venta`
--

INSERT INTO `detalle_venta` (`id`, `id_venta`, `id_producto`, `cantidad`, `precio_unitario`, `subtotal`, `descuento`, `estado`, `fecha_registro`) VALUES
(1, 1, 1, 2, 299.99, 599.98, 0, 'Activo', '2025-05-17 14:15:22'),
(2, 5, 2, 5, 1850.50, 9252.50, 0, 'Activo', '2025-06-11 21:37:53'),
(3, 6, 2, 5, 1850.50, 9252.50, 0, 'Activo', '2025-06-11 21:38:29'),
(4, 6, 3, 5, 8.50, 42.50, 0, 'Activo', '2025-06-11 21:38:29'),
(5, 6, 4, 7, 25000.00, 175000.00, 0, 'Activo', '2025-06-11 21:38:29'),
(6, 7, 2, 5, 1850.50, 9252.50, 0, 'Activo', '2025-06-24 07:45:22'),
(7, 8, 2, 3, 1850.50, 5551.50, 0, 'Activo', '2025-06-24 09:16:04'),
(8, 9, 4, 3, 25000.00, 75000.00, 0, 'Activo', '2025-06-27 20:16:23'),
(9, 11, 3, 3, 8.50, 25.50, 0, 'Activo', '2025-06-28 14:15:37'),
(10, 12, 3, 2, 8.50, 17.00, 0, 'Activo', '2025-06-28 14:20:27'),
(11, 13, 4, 3, 25000.00, 75000.00, 0, 'Activo', '2025-06-28 14:21:14'),
(12, 14, 5, 2, 23999.00, 47998.00, 0, 'Activo', '2025-06-28 14:22:12'),
(13, 15, 5, 3, 23999.00, 71997.00, 0, 'Activo', '2025-06-28 14:26:40'),
(15, 18, 1, 5, 299.99, 1499.95, 0, 'Activo', '2026-06-23 23:46:42'),
(16, 19, 1, 2, 300.99, 601.98, 0, 'Activo', '2026-06-26 05:01:57'),
(17, 20, 1, 2, 300.99, 601.98, 0, 'Activo', '2026-06-26 05:04:40'),
(18, 21, 1, 2, 300.99, 601.98, 0, 'Activo', '2026-06-26 05:06:08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movimientos`
--

CREATE TABLE `movimientos` (
  `id` int(11) NOT NULL,
  `tipo` text NOT NULL,
  `id_producto` int(11) NOT NULL,
  `registro_usuario_id` int(11) NOT NULL,
  `stock_anterior` int(11) NOT NULL DEFAULT 0,
  `stock_nuevo` int(11) NOT NULL DEFAULT 0,
  `observacion` varchar(50) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `motivo` text NOT NULL,
  `fecha` datetime DEFAULT current_timestamp(),
  `estado` varchar(20) NOT NULL DEFAULT 'Activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `movimientos`
--

INSERT INTO `movimientos` (`id`, `tipo`, `id_producto`, `registro_usuario_id`, `stock_anterior`, `stock_nuevo`, `observacion`, `cantidad`, `motivo`, `fecha`, `estado`) VALUES
(24, 'Salida', 1, 1, 50, 45, 'Venta registrada', 5, 'Venta', '2026-06-23 23:46:42', 'Activo'),
(25, 'Salida', 1, 1, 45, 43, 'Venta registrada', 2, 'Venta', '2026-06-26 00:01:57', 'Activo'),
(26, 'Salida', 1, 1, 43, 41, 'Venta registrada', 2, 'Venta', '2026-06-26 00:04:40', 'Activo'),
(27, 'Salida', 1, 1, 41, 39, 'Venta registrada', 2, 'Venta', '2026-06-26 00:06:08', 'Activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permisos`
--

CREATE TABLE `permisos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `estado` varchar(20) DEFAULT 'Activo',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `permisos`
--

INSERT INTO `permisos` (`id`, `nombre`, `descripcion`, `estado`, `fecha_registro`) VALUES
(2, 'ver_productos', 'Puede visualizar productos', 'Activo', '2026-06-20 00:14:57'),
(3, 'crear_productos', 'Puede crear productos', 'Activo', '2026-06-20 00:14:57'),
(4, 'editar_productos', 'Puede editar productos', 'Activo', '2026-06-20 00:14:57'),
(5, 'eliminar_productos', 'Puede eliminar productos', 'Activo', '2026-06-20 00:14:57'),
(6, 'ver_clientes', 'Puede visualizar clientes', 'Activo', '2026-06-20 00:14:57'),
(7, 'crear_clientes', 'Puede crear clientes', 'Activo', '2026-06-20 00:14:57'),
(8, 'editar_clientes', 'Puede editar clientes', 'Activo', '2026-06-20 00:14:57'),
(9, 'realizar_ventas', 'Puede registrar ventas', 'Activo', '2026-06-20 00:14:57'),
(10, 'ver_ventas', 'Puede visualizar ventas', 'Activo', '2026-06-20 00:14:57'),
(11, 'registrar_compras', 'Puede registrar compras', 'Activo', '2026-06-20 00:14:57'),
(12, 'ver_movimientos', 'Puede visualizar movimientos', 'Activo', '2026-06-20 00:14:57'),
(13, 'registrar_movimientos', 'Puede registrar movimientos', 'Activo', '2026-06-20 00:14:57'),
(14, 'ver_reportes', 'Puede visualizar reportes', 'Activo', '2026-06-20 00:14:57'),
(15, 'ver_usuarios', 'Puede visualizar usuarios', 'Activo', '2026-06-20 00:14:57'),
(16, 'crear_usuarios', 'Puede crear usuarios', 'Activo', '2026-06-20 00:14:57'),
(17, 'editar_usuarios', 'Puede editar usuarios', 'Activo', '2026-06-20 00:14:57'),
(18, 'ver_roles', 'Puede visualizar roles', 'Activo', '2026-06-20 00:14:57'),
(19, 'administrar_roles', 'Puede administrar roles', 'Activo', '2026-06-20 00:14:57'),
(20, 'ver_proveedores', 'Puede administrar proveedores\r\n', 'Activo', '2026-06-22 23:42:45'),
(21, 'crear_proveedores', 'Puede crear proveedores', 'Activo', '2026-06-22 23:42:45'),
(22, 'editar_proveedores', 'Puede editar proveedores', 'Activo', '2026-06-22 23:42:45'),
(23, 'ver_categorias', 'Puede administrar categorías\r\n', 'Activo', '2026-06-22 23:42:45'),
(24, 'crear_categorias', 'Puede crear categorías', 'Activo', '2026-06-22 23:42:45'),
(25, 'editar_categorias', 'Puede editar categorías', 'Activo', '2026-06-22 23:42:45');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id` int(11) NOT NULL,
  `codigo_producto` varchar(20) DEFAULT NULL,
  `nombre` varchar(150) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `imagen_url` varchar(255) DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `categoria_id` int(11) DEFAULT NULL,
  `cantidad_stock` int(11) NOT NULL DEFAULT 0,
  `stock_minimo` int(11) NOT NULL DEFAULT 0,
  `stock_maximo` int(11) NOT NULL DEFAULT 0,
  `unidad_medida` varchar(100) NOT NULL,
  `id_proveedor` int(11) DEFAULT NULL,
  `estado` varchar(20) DEFAULT 'Activo',
  `fecha_registro` datetime DEFAULT current_timestamp(),
  `fecha_actualizacion` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id`, `codigo_producto`, `nombre`, `descripcion`, `imagen_url`, `precio`, `categoria_id`, `cantidad_stock`, `stock_minimo`, `stock_maximo`, `unidad_medida`, `id_proveedor`, `estado`, `fecha_registro`, `fecha_actualizacion`) VALUES
(1, 'PROD001', 'Smartphone XYz', '', 'https://i2.wp.com/www.socialnews.xyz/wp-content/uploads/2019/07/12/519757509e2186825123d8d572b6a068.jpg?fit=714%2C480&quality=80&zoom=1&ssl=1', 300.99, 1, 39, 7, 0, '', 1, 'Activo', '2025-05-17 14:15:22', '2026-06-26 05:06:08'),
(2, 'PROD002', 'Laptop HP 15\"', '', 'http://d3d71ba2asa5oz.cloudfront.net/52000820/images/15-f233wm%20a.jpg', 1860.50, 1, 26, 5, 0, '', 3, 'Activo', '2025-06-01 22:21:36', '2026-06-18 22:50:35'),
(3, 'PROD003', 'Néctar de piña en caja (6x200ml)', '', 'https://sparlapalma.com/documents/10180/12821/600785_G.jpg', 8.50, 2, 8, 5, 0, '', 2, 'Activo', '2025-06-01 22:24:02', '2026-06-18 22:50:35'),
(4, 'PROD004', 'Impresora Epson L8050', '', 'https://mediaserver.goepson.com/ImConvServlet/imconv/61dcb6a700968d5fe27870dc9e72d7151805d623/1200Wx1200H?use=banner&hybrisId=B2C&assetDescr=L8050_aberta', 25000.00, 3, 20, 5, 0, '', 3, 'Activo', '2025-06-11 21:22:12', '2026-06-18 22:50:35'),
(5, 'PROD005', 'Destornillador Eléctrico', '', 'https://m.media-amazon.com/images/I/71AbKmbbHwL._AC_SL1500_.jpg', 23999.00, 4, 27, 5, 0, '', 3, 'Activo', '2025-06-11 21:24:03', '2026-06-18 22:50:35');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proovedores`
--

CREATE TABLE `proovedores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `direccion` text DEFAULT NULL,
  `correo` varchar(150) DEFAULT NULL,
  `estado` varchar(20) DEFAULT 'Activo',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proovedores`
--

INSERT INTO `proovedores` (`id`, `nombre`, `telefono`, `direccion`, `correo`, `estado`, `fecha_registro`) VALUES
(1, 'Proveedor XYZ', '554-456-2346', 'Calle Falsa 123', 'contacto@proveedorxyz.com', 'Activo', '2025-05-17 14:15:22'),
(2, 'Alimentos del Valle', '3208741230', 'Cl 34 #15-44, Bucaramanga', 'contacto@alimentosdelvalle.com', 'Activo', '2025-05-31 19:46:50'),
(3, 'Suministros Tecnológicos', '3129988776', 'Av. Siempre Viva 123, Bogotá', 'soporte@suministrostec.com', 'Activo', '2025-05-31 19:57:40');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_usuarios`
--

CREATE TABLE `registro_usuarios` (
  `id` int(11) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `estado` varchar(20) DEFAULT 'Activo',
  `fecha_registro` datetime DEFAULT current_timestamp(),
  `id_rol` int(11) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `correo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registro_usuarios`
--

INSERT INTO `registro_usuarios` (`id`, `contraseña`, `estado`, `fecha_registro`, `id_rol`, `nombre`, `apellido`, `telefono`, `correo`) VALUES
(1, 'pbkdf2:sha256:1000000$Z8WQVr2s2byeTsjC$de0e8fa3e317f776ceea6770759b53f7a1d31ce631b8ccc4eccdb21b4843c044', 'Activo', '2026-06-19 03:31:41', 1, 'Deibis', 'Mosquera', '3045903327', 'deivisbarrios465@gmail.com'),
(2, 'pbkdf2:sha256:1000000$64bcEwqo92Ht4GBN$b066c1201f7c495da80791d1b54192780526da87bac48393dc3e75fe35aad721', 'Activo', '2026-06-20 04:48:43', 2, 'carlos', 'sanchez', '3256325548', 'sanchez@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `estado` varchar(20) DEFAULT 'Activo',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `nombre`, `descripcion`, `estado`, `fecha_registro`) VALUES
(1, 'Administrador', 'Acceso total al sistema', 'Activo', '2025-05-17 14:15:22'),
(2, 'vendedor', 'atender a los clientes', 'Activo', '2025-05-20 18:13:54'),
(3, 'Supervisor', 'Supervisa movimientos, reportes y estadísticas', 'Activo', '2026-06-19 16:51:30'),
(4, 'Bodeguero', 'Gestiona entradas, vencimientos y stock', 'Activo', '2026-06-19 16:51:30');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol_permiso`
--

CREATE TABLE `rol_permiso` (
  `id` int(11) NOT NULL,
  `id_rol` int(11) DEFAULT NULL,
  `id_permiso` int(11) DEFAULT NULL,
  `estado` varchar(20) DEFAULT 'Activo',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol_permiso`
--

INSERT INTO `rol_permiso` (`id`, `id_rol`, `id_permiso`, `estado`, `fecha_registro`) VALUES
(2, 1, 19, 'Activo', '2026-06-20 00:17:47'),
(3, 1, 7, 'Activo', '2026-06-20 00:17:47'),
(4, 1, 3, 'Activo', '2026-06-20 00:17:47'),
(5, 1, 16, 'Activo', '2026-06-20 00:17:47'),
(6, 1, 8, 'Activo', '2026-06-20 00:17:47'),
(7, 1, 4, 'Activo', '2026-06-20 00:17:47'),
(8, 1, 17, 'Activo', '2026-06-20 00:17:47'),
(9, 1, 5, 'Activo', '2026-06-20 00:17:47'),
(11, 1, 9, 'Activo', '2026-06-20 00:17:47'),
(12, 1, 11, 'Activo', '2026-06-20 00:17:47'),
(13, 1, 13, 'Activo', '2026-06-20 00:17:47'),
(14, 1, 6, 'Activo', '2026-06-20 00:17:47'),
(15, 1, 12, 'Activo', '2026-06-20 00:17:47'),
(16, 1, 2, 'Activo', '2026-06-20 00:17:47'),
(17, 1, 14, 'Activo', '2026-06-20 00:17:47'),
(18, 1, 18, 'Activo', '2026-06-20 00:17:47'),
(19, 1, 15, 'Activo', '2026-06-20 00:17:47'),
(20, 1, 10, 'Activo', '2026-06-20 00:17:47'),
(33, 2, 2, 'Activo', '2026-06-20 00:18:17'),
(34, 2, 6, 'Activo', '2026-06-20 00:18:17'),
(35, 2, 7, 'Activo', '2026-06-20 00:18:17'),
(36, 2, 9, 'Activo', '2026-06-20 00:18:17'),
(37, 2, 10, 'Activo', '2026-06-20 00:18:17'),
(38, 3, 2, 'Activo', '2026-06-20 00:18:39'),
(39, 3, 6, 'Activo', '2026-06-20 00:18:39'),
(40, 3, 10, 'Activo', '2026-06-20 00:18:39'),
(41, 3, 12, 'Activo', '2026-06-20 00:18:39'),
(42, 3, 14, 'Activo', '2026-06-20 00:18:39'),
(43, 4, 2, 'Activo', '2026-06-20 00:19:08'),
(44, 4, 3, 'Activo', '2026-06-20 00:19:08'),
(45, 4, 4, 'Activo', '2026-06-20 00:19:08'),
(46, 4, 11, 'Activo', '2026-06-20 00:19:08'),
(47, 4, 12, 'Activo', '2026-06-20 00:19:08'),
(48, 4, 13, 'Activo', '2026-06-20 00:19:08'),
(49, 1, 20, 'Activo', '2026-06-22 23:49:02'),
(50, 1, 21, 'Activo', '2026-06-22 23:49:02'),
(51, 1, 22, 'Activo', '2026-06-22 23:49:02'),
(52, 1, 23, 'Activo', '2026-06-22 23:49:02'),
(53, 1, 24, 'Activo', '2026-06-22 23:49:02'),
(54, 1, 25, 'Activo', '2026-06-22 23:49:02'),
(55, 3, 20, 'Activo', '2026-06-22 23:49:12'),
(56, 3, 23, 'Activo', '2026-06-22 23:49:12'),
(57, 4, 20, 'Activo', '2026-06-22 23:49:24'),
(58, 4, 21, 'Activo', '2026-06-22 23:49:24'),
(59, 4, 22, 'Activo', '2026-06-22 23:49:24'),
(60, 4, 23, 'Activo', '2026-06-22 23:49:24'),
(61, 4, 24, 'Activo', '2026-06-22 23:49:24'),
(62, 4, 25, 'Activo', '2026-06-22 23:49:24');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `id` int(11) NOT NULL,
  `cedula_cliente` varchar(20) DEFAULT NULL,
  `usuario_id` int(11) NOT NULL DEFAULT 2,
  `subtotal` decimal(10,2) NOT NULL,
  `descuento` decimal(10,0) NOT NULL,
  `metodo_pago` varchar(50) NOT NULL,
  `fecha` datetime DEFAULT current_timestamp(),
  `total` decimal(10,2) DEFAULT NULL,
  `estado` varchar(20) DEFAULT 'Activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`id`, `cedula_cliente`, `usuario_id`, `subtotal`, `descuento`, `metodo_pago`, `fecha`, `total`, `estado`) VALUES
(1, '1234567890', 1, 0.00, 0, '', '2025-05-17 14:15:22', 599.98, 'Activo'),
(5, '1234567890', 1, 0.00, 0, '', '2025-06-11 21:37:53', 9252.50, 'Activo'),
(6, '1234567890', 1, 0.00, 0, '', '2025-06-11 21:38:29', 184295.00, 'Activo'),
(7, '0912345678', 1, 0.00, 0, '', '2025-06-24 07:45:23', 9252.50, 'Activo'),
(8, '0912345678', 1, 0.00, 0, '', '2025-06-24 09:16:05', 5551.50, 'Activo'),
(9, '0912345678', 1, 0.00, 0, '', '2025-06-27 20:16:23', 75000.00, 'Activo'),
(11, '0912345678', 1, 0.00, 0, '', '2025-06-28 14:15:37', 25.50, 'Activo'),
(12, '0912345678', 1, 0.00, 0, '', '2025-06-28 14:20:27', 17.00, 'Activo'),
(13, '1234567890', 1, 0.00, 0, '', '2025-06-28 14:21:14', 75000.00, 'Activo'),
(14, '1234567890', 1, 0.00, 0, '', '2025-06-28 14:22:12', 47998.00, 'Activo'),
(15, '0912345678', 1, 0.00, 0, '', '2025-06-28 14:26:39', 71997.00, 'Activo'),
(18, '0912345678', 1, 0.00, 0, 'Efectivo', '2026-06-23 23:46:42', 1499.95, 'Activo'),
(19, '1234567890', 1, 0.00, 0, 'Efectivo', '2026-06-26 00:01:57', 601.98, 'Activo'),
(20, '1234567890', 1, 0.00, 0, 'Efectivo', '2026-06-26 00:04:40', 601.98, 'Activo'),
(21, '1234567890', 1, 0.00, 0, 'Efectivo', '2026-06-26 00:06:08', 601.98, 'Activo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cambiar_contraseña`
--
ALTER TABLE `cambiar_contraseña`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`cedula`);

--
-- Indices de la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_venta` (`id_venta`),
  ADD KEY `id_producto` (`id_producto`);

--
-- Indices de la tabla `movimientos`
--
ALTER TABLE `movimientos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_producto` (`id_producto`),
  ADD KEY `usuario_id` (`registro_usuario_id`);

--
-- Indices de la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo_producto` (`codigo_producto`),
  ADD KEY `categoria_id` (`categoria_id`),
  ADD KEY `id_proveedor` (`id_proveedor`);

--
-- Indices de la tabla `proovedores`
--
ALTER TABLE `proovedores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `registro_usuarios`
--
ALTER TABLE `registro_usuarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_rol` (`id_rol`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `rol_permiso`
--
ALTER TABLE `rol_permiso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_rol` (`id_rol`),
  ADD KEY `id_permiso` (`id_permiso`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cedula_cliente` (`cedula_cliente`),
  ADD KEY `fk_ventas_usuario` (`usuario_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cambiar_contraseña`
--
ALTER TABLE `cambiar_contraseña`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `movimientos`
--
ALTER TABLE `movimientos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `proovedores`
--
ALTER TABLE `proovedores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `registro_usuarios`
--
ALTER TABLE `registro_usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `rol_permiso`
--
ALTER TABLE `rol_permiso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD CONSTRAINT `detalle_venta_ibfk_1` FOREIGN KEY (`id_venta`) REFERENCES `ventas` (`id`),
  ADD CONSTRAINT `detalle_venta_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id`);

--
-- Filtros para la tabla `movimientos`
--
ALTER TABLE `movimientos`
  ADD CONSTRAINT `fk_movimiento_usuario` FOREIGN KEY (`registro_usuario_id`) REFERENCES `registro_usuarios` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `movimientos_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`id`),
  ADD CONSTRAINT `producto_ibfk_2` FOREIGN KEY (`id_proveedor`) REFERENCES `proovedores` (`id`);

--
-- Filtros para la tabla `registro_usuarios`
--
ALTER TABLE `registro_usuarios`
  ADD CONSTRAINT `registro_usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id`);

--
-- Filtros para la tabla `rol_permiso`
--
ALTER TABLE `rol_permiso`
  ADD CONSTRAINT `rol_permiso_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id`),
  ADD CONSTRAINT `rol_permiso_ibfk_2` FOREIGN KEY (`id_permiso`) REFERENCES `permisos` (`id`);

--
-- Filtros para la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `fk_ventas_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `registro_usuarios` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`cedula_cliente`) REFERENCES `cliente` (`cedula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
