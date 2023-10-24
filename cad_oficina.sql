-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Host: [fd77:f3e2:38a5:c000:17:e6d8:b517:2d40]
-- Tempo de geração: 27/11/2022 às 17:05
-- Versão do servidor: 10.5.10-MariaDB-1:10.5.10+maria~focal-log
-- Versão do PHP: 7.0.33-50+ubuntu16.04.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `fremondata`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cad_oficina`
--

CREATE TABLE `cad_oficina` (
  `id` int(7) auto_increment primary key,
  `cnpj_cpf` varchar(18) CHARACTER SET utf8mb4 DEFAULT NULL,
  `i_estadual` varchar(20) CHARACTER SET utf8mb4 DEFAULT NULL,
  `nome_oficina` varchar(100) CHARACTER SET utf8mb4 DEFAULT NULL,
  `senha` varchar(10) CHARACTER SET utf8mb4 DEFAULT NULL,
  `responsavel` varchar(100) CHARACTER SET utf8mb4 DEFAULT NULL,
  `endereco` varchar(100) CHARACTER SET utf8mb4 DEFAULT NULL,
  `Bairro` varchar(60) CHARACTER SET utf8mb4 DEFAULT NULL,
  `cidade` varchar(100) CHARACTER SET utf8mb4 DEFAULT NULL,
  `estado` varchar(100) CHARACTER SET utf8mb4 DEFAULT NULL,
  `cep` varchar(9) CHARACTER SET utf8mb4 DEFAULT NULL,
  `fone_oficina` varchar(15) CHARACTER SET utf8mb4 DEFAULT 'NULL',
  `whatsapp_oficina` varchar(15) CHARACTER SET utf8mb4 DEFAULT 'NULL',
  `email_oficina` varchar(100) CHARACTER SET utf8mb4 DEFAULT 'NULL',
  `ativo_s_n_susp` varchar(10) CHARACTER SET utf8mb4 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Fazendo dump de dados para tabela `cad_oficina`
--

INSERT INTO `cad_oficina` (`id`, `cnpj_cpf`, `i_estadual`, `nome_oficina`, `senha`, `responsavel`, `endereco`, `Bairro`, `cidade`, `estado`, `cep`, `fone_oficina`, `whatsapp_oficina`, `email_oficina`, `ativo_s_n_susp`) VALUES
(52, '47.309.174/0002-85', '123456789', 'INDUSTRIA DE BALANCAS MICHELETTI LTDA', '1234', 'Elzi de Freitas Monteiro', 'RUA BRIG TOBIAS, 331 ', '', 'SAO PAULO', 'SP', '01032-000', '()-', '()-', 'leidincomp', 'Ativo'),
(53, '08.726.829/0001-88', 'isento', 'SHARECARE BRASIL SERVICOS DE CONSULTORIA LTDA.', '1234', 'Oswaldo', 'AV BRIGADEIRO FARIA LIMA, 1.188 CONJ: 131;', '', 'SAO PAULO', 'SP', '01451-001', '(11)4440-0606', '()-', 'nicolas.toth@healthways.com', 'Ativo');

--
-- Índices de tabelas apagadas
--

--
-- Índices de tabela `cad_oficina`
--
ALTER TABLE `cad_oficina`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas apagadas
--

--
-- AUTO_INCREMENT de tabela `cad_oficina`
--
ALTER TABLE `cad_oficina`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
