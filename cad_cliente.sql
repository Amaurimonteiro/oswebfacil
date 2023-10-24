-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Host: [fd77:f3e2:38a5:c000:17:e6d8:b517:2d40]
-- Tempo de geração: 27/11/2022 às 17:06
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
-- Estrutura para tabela `cad_cliente`
--

CREATE TABLE `cad_cliente` (
  `id` int(7) auto_increment primary key,
  `cnpj_cpf_cliente` varchar(18) CHARACTER SET utf8mb4 DEFAULT 'NULL',
  `cnpj_cpf_oficina` varchar(18) CHARACTER SET utf8mb4 DEFAULT NULL,
  `i_estadual` varchar(20) CHARACTER SET utf8mb4 DEFAULT NULL,
  `nome_loja` varchar(100) CHARACTER SET utf8mb4 DEFAULT 'NULL',
  `nome_responsavel` varchar(10) CHARACTER SET utf8mb4 DEFAULT 'NULL',
  `endereco` varchar(100) CHARACTER SET utf8mb4 DEFAULT 'NULL',
  `Bairro` varchar(60) CHARACTER SET utf8mb4 DEFAULT NULL,
  `cidade` varchar(100) CHARACTER SET utf8mb4 DEFAULT NULL,
  `estado` varchar(100) CHARACTER SET utf8mb4 DEFAULT 'NULL',
  `cep` varchar(9) CHARACTER SET utf8mb4 DEFAULT 'NULL',
  `fone_loja` varchar(15) CHARACTER SET utf8mb4 DEFAULT 'NULL',
  `whatsapp_loja` varchar(15) CHARACTER SET utf8mb4 DEFAULT 'NULL',
  `email_loja` varchar(100) CHARACTER SET utf8mb4 DEFAULT 'NULL',
  `Codigo_cliente` varchar(12) CHARACTER SET utf8mb4 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Fazendo dump de dados para tabela `cad_cliente`
--

INSERT INTO `cad_cliente` (`id`, `cnpj_cpf_cliente`, `cnpj_cpf_oficina`, `i_estadual`, `nome_loja`, `nome_responsavel`, `endereco`, `Bairro`, `cidade`, `estado`, `cep`, `fone_loja`, `whatsapp_loja`, `email_loja`, `Codigo_cliente`) VALUES
(12, '43.776.517/0001-80', '47.309.174/0002-85', '12341234', 'CIA DE SANEAMENTO BASICO DO ESTADO DE SAO PAULO SABESP', 'Elzi', 'R COSTA CARVALHO, 300 ', 'PINHEIROS', 'SAO PAULO', 'SAO PAULO', '05429-000', '(11)3388-8000', '()-', 'lei', '2210250813'),
(20, '09.244.426/0002-46', '08.726.829/0001-88', '', 'PADARIA PAES E DOCES SAO PAULO LTDA', '', 'AV PLACIDO PARREIRA LIMA, 118 ', 'PARQUE DOM JOAO NERI', 'SAO PAULO', 'SAO PAULO', '08151-110', '(11)4826-9823', '()-', 'ecianeamorim@hotmail.com', '2210291000');

--
-- Índices de tabelas apagadas
--

--
-- Índices de tabela `cad_cliente`
--
ALTER TABLE `cad_cliente`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas apagadas
--

--
-- AUTO_INCREMENT de tabela `cad_cliente`
--
ALTER TABLE `cad_cliente`
  MODIFY `id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
