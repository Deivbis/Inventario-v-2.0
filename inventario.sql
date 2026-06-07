-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-06-2025 a las 22:23:57
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

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
(8, 'deivisbarrios465@gmail.com', '437137', '2025-06-28 19:12:22', '2025-06-28 19:27:22', 0);

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
  `estado` varchar(20) DEFAULT 'Activo',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`cedula`, `nombre`, `apellido`, `telefono`, `correo`, `direccion`, `estado`, `fecha_registro`) VALUES
('0912345678', 'Andrés', 'Mejía', '0999988776', 'andres.mejia@gmail.com', 'Calle 10 de Agosto y Olmedo', 'Activo', '2025-06-08 18:53:14'),
('1122334455', 'Luis', 'Martinez', '555-1111', 'luis.martinez@email.com', 'Av. del Sol 456', 'Inactivo', '2025-06-08 18:47:30'),
('1234567890', 'Juan ', 'Pérez', '555-5678', 'juan.perez@email.com', 'Av. Siempre Viva 742', 'Activo', '2025-05-17 14:15:22');

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
  `estado` varchar(20) DEFAULT 'Activo',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detalle_venta`
--

INSERT INTO `detalle_venta` (`id`, `id_venta`, `id_producto`, `cantidad`, `precio_unitario`, `subtotal`, `estado`, `fecha_registro`) VALUES
(1, 1, 1, 2, 299.99, 599.98, 'Activo', '2025-05-17 14:15:22'),
(2, 5, 2, 5, 1850.50, 9252.50, 'Activo', '2025-06-11 21:37:53'),
(3, 6, 2, 5, 1850.50, 9252.50, 'Activo', '2025-06-11 21:38:29'),
(4, 6, 3, 5, 8.50, 42.50, 'Activo', '2025-06-11 21:38:29'),
(5, 6, 4, 7, 25000.00, 175000.00, 'Activo', '2025-06-11 21:38:29'),
(6, 7, 2, 5, 1850.50, 9252.50, 'Activo', '2025-06-24 07:45:22'),
(7, 8, 2, 3, 1850.50, 5551.50, 'Activo', '2025-06-24 09:16:04'),
(8, 9, 4, 3, 25000.00, 75000.00, 'Activo', '2025-06-27 20:16:23'),
(9, 11, 3, 3, 8.50, 25.50, 'Activo', '2025-06-28 14:15:37'),
(10, 12, 3, 2, 8.50, 17.00, 'Activo', '2025-06-28 14:20:27'),
(11, 13, 4, 3, 25000.00, 75000.00, 'Activo', '2025-06-28 14:21:14'),
(12, 14, 5, 2, 23999.00, 47998.00, 'Activo', '2025-06-28 14:22:12'),
(13, 15, 5, 3, 23999.00, 71997.00, 'Activo', '2025-06-28 14:26:40');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movimientos`
--

CREATE TABLE `movimientos` (
  `id` int(11) NOT NULL,
  `tipo` text NOT NULL,
  `id_producto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `motivo` text NOT NULL,
  `fecha` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `movimientos`
--

INSERT INTO `movimientos` (`id`, `tipo`, `id_producto`, `cantidad`, `motivo`, `fecha`) VALUES
(1, 'Salida', 2, 5, 'Venta', '2025-06-11 21:37:53'),
(2, 'Salida', 2, 5, 'Venta', '2025-06-11 21:38:29'),
(3, 'Salida', 3, 5, 'Venta', '2025-06-11 21:38:29'),
(4, 'Salida', 4, 7, 'Venta', '2025-06-11 21:38:29'),
(5, 'Salida', 2, 5, 'Venta', '2025-06-24 07:45:23'),
(6, 'Salida', 2, 3, 'Venta', '2025-06-24 09:16:05'),
(7, 'Salida', 4, 3, 'Venta', '2025-06-27 20:16:23'),
(8, 'Salida', 3, 3, 'Venta', '2025-06-28 14:15:37'),
(9, 'Salida', 3, 2, 'Venta', '2025-06-28 14:20:27'),
(10, 'Salida', 4, 3, 'Venta', '2025-06-28 14:21:14'),
(11, 'Salida', 5, 2, 'Venta', '2025-06-28 14:22:12'),
(12, 'Salida', 5, 3, 'Venta', '2025-06-28 14:26:40'),
(13, 'Entrada', 2, 10, 'Compra', '2025-06-28 14:53:19'),
(14, 'Entrada', 2, 10, 'Compra', '2025-06-28 14:54:03'),
(15, 'Entrada', 4, 3, 'Compra', '2025-06-28 15:05:35'),
(16, 'Entrada', 4, 10, 'Compra', '2025-06-28 15:06:38'),
(17, 'Entrada', 2, 2, 'Compra', '2025-06-28 15:10:10'),
(18, 'Entrada', 3, 3, 'Compra', '2025-06-28 15:10:40'),
(19, 'Entrada', 5, 3, 'Compra', '2025-06-28 15:13:08'),
(20, 'Entrada', 5, 2, 'Compra', '2025-06-28 15:18:32'),
(21, 'Entrada', 2, 2, 'Compra', '2025-06-28 15:20:27'),
(22, 'Entrada', 5, 2, 'Compra', '2025-06-28 15:21:38');

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
(1, 'Gestionar Productos', 'Permite agregar, editar y eliminar productos', 'Activo', '2025-05-17 14:15:22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id` int(11) NOT NULL,
  `codigo_producto` varchar(20) DEFAULT NULL,
  `nombre` varchar(150) NOT NULL,
  `imagen_url` varchar(255) DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `categoria_id` int(11) DEFAULT NULL,
  `cantidad_stock` int(11) NOT NULL DEFAULT 0,
  `stock_minimo` int(11) NOT NULL DEFAULT 0,
  `id_proveedor` int(11) DEFAULT NULL,
  `estado` varchar(20) DEFAULT 'Activo',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id`, `codigo_producto`, `nombre`, `imagen_url`, `precio`, `categoria_id`, `cantidad_stock`, `stock_minimo`, `id_proveedor`, `estado`, `fecha_registro`) VALUES
(1, 'PROD001', 'Smartphone XYz', 'https://i2.wp.com/www.socialnews.xyz/wp-content/uploads/2019/07/12/519757509e2186825123d8d572b6a068.jpg?fit=714%2C480&quality=80&zoom=1&ssl=1', 299.99, 1, 50, 7, 1, 'Activo', '2025-05-17 14:15:22'),
(2, 'PROD002', 'Laptop HP 15\"', 'http://d3d71ba2asa5oz.cloudfront.net/52000820/images/15-f233wm%20a.jpg', 1860.50, 1, 26, 5, 3, 'Activo', '2025-06-01 22:21:36'),
(3, 'PROD003', 'Néctar de piña en caja (6x200ml)', 'https://yourspanishcorner.com/1509-large_default/zumo-de-pina-disfruta-6x200ml-juver.jpg\r\n', 8.50, 2, 8, 5, 2, 'Activo', '2025-06-01 22:24:02'),
(4, 'PROD004', 'Impresora Epson L8050', 'https://mediaserver.goepson.com/ImConvServlet/imconv/61dcb6a700968d5fe27870dc9e72d7151805d623/1200Wx1200H?use=banner&hybrisId=B2C&assetDescr=L8050_aberta', 25000.00, 3, 20, 5, 3, 'Activo', '2025-06-11 21:22:12'),
(5, 'PROD005', 'Destornillador Eléctrico', 'https://m.media-amazon.com/images/I/71AbKmbbHwL._AC_SL1500_.jpg', 23999.00, 4, 27, 5, 3, 'Activo', '2025-06-11 21:24:03');

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
(1, 'pbkdf2:sha256:1000000$EZVvVFUCeoIa2IuY$fad3b45c88417ec6bcf63f1b01f6b6622d008dd6a68a2aad7081794a49bdc9f1', 'Activo', '2025-05-20 23:22:56', 1, 'deibis', 'mosquera', '2147483647', 'deivisbarrios465@gmail.com'),
(2, 'pbkdf2:sha256:1000000$WdOTOc0cAINqtZER$055a78cfe21f06514740eddf3003017898ee2977a2efca82172fb3b3347f1706', 'Activo', '2025-05-20 23:34:13', 2, 'mateo', 'peñalosa', '2147483647', 'mateo@gmail.com'),
(4, 'pbkdf2:sha256:1000000$JEgFIZ0jJ1CkiBRB$a095512784cf708b756afed8cbb8f47f2d534a406a9294405ca7cea6d29680f6', 'Inactivo', '2025-05-30 19:54:49', 2, 'Keren', 'Leite', '2147483647', 'mateo123@gmail.com'),
(5, 'pbkdf2:sha256:1000000$jOe7ZXGrPzyNrCsd$9a465c500b0a5dbbcb3de25c1e0e2a95298a31e5f52962788eb18e7ffb4569b5', 'Inactivo', '2025-06-24 16:29:02', 2, 'ana', 'martinez', '3045904433', 'anam@gmail.com'),
(6, 'pbkdf2:sha256:1000000$nVbLEQO0DOjJ5mAO$e674a1a97fc43fbad7e168cdecf60559200fbe954efa3c5493b8c5cdb3b5d6a8', 'Activo', '2025-06-28 16:39:32', 2, 'Duban', 'Perez', '3045893328', 'Dubane@gmail.com');

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
(2, 'vendedor', 'atender a los clientes', 'Activo', '2025-05-20 18:13:54');

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
(1, 1, 1, 'Activo', '2025-05-17 14:15:22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `id` int(11) NOT NULL,
  `cedula_cliente` varchar(20) DEFAULT NULL,
  `fecha` datetime DEFAULT current_timestamp(),
  `total` decimal(10,2) DEFAULT NULL,
  `estado` varchar(20) DEFAULT 'Activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`id`, `cedula_cliente`, `fecha`, `total`, `estado`) VALUES
(1, '1234567890', '2025-05-17 14:15:22', 599.98, 'Activo'),
(5, '1234567890', '2025-06-11 21:37:53', 9252.50, 'Activo'),
(6, '1234567890', '2025-06-11 21:38:29', 184295.00, 'Activo'),
(7, '0912345678', '2025-06-24 07:45:23', 9252.50, 'Activo'),
(8, '0912345678', '2025-06-24 09:16:05', 5551.50, 'Activo'),
(9, '0912345678', '2025-06-27 20:16:23', 75000.00, 'Activo'),
(11, '0912345678', '2025-06-28 14:15:37', 25.50, 'Activo'),
(12, '0912345678', '2025-06-28 14:20:27', 17.00, 'Activo'),
(13, '1234567890', '2025-06-28 14:21:14', 75000.00, 'Activo'),
(14, '1234567890', '2025-06-28 14:22:12', 47998.00, 'Activo'),
(15, '0912345678', '2025-06-28 14:26:39', 71997.00, 'Activo');

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
  ADD KEY `id_producto` (`id_producto`);

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
  ADD KEY `cedula_cliente` (`cedula_cliente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cambiar_contraseña`
--
ALTER TABLE `cambiar_contraseña`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `movimientos`
--
ALTER TABLE `movimientos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `rol_permiso`
--
ALTER TABLE `rol_permiso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

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
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`cedula_cliente`) REFERENCES `cliente` (`cedula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
