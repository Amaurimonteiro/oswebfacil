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

comando_SQL = "INSERT INTO cad_os (
,,
cod_peca_2,quant_2,Descri_2,valor_unit_2,valor_tot_2,
cod_peca_3,quant_3,Descri_3,valor_unit_3,valor_tot_3,
cod_peca_4,quant_4,Descri_4,valor_unit_4,valor_tot_4,
cod_peca_5,quant_5,Descri_5,valor_unit_5,valor_tot_5,



CREATE TABLE `cad_os` (
  `id` int(7) auto_increment primary key,
  `num_os` varchar(10) CHARACTER SET utf8mb4 DEFAULT NULL,
  `cnpj_cpf_oficina` varchar(18) CHARACTER SET utf8mb4 DEFAULT NULL,
  `cnpj_cpf_cliente` varchar(18) CHARACTER SET utf8mb4 DEFAULT NULL,
  `nome_cliente` varchar(100) CHARACTER SET utf8mb4 DEFAULT NULL,
  `nome_tecnico` varchar(100) CHARACTER SET utf8mb4 DEFAULT NULL,
  `rg_tecnico` varchar(15) CHARACTER SET utf8mb4 DEFAULT NULL,
  `val_mao_de_obra` decimal(14,2) DEFAULT NULL,
  `defeitos_informados` varchar(200) CHARACTER SET utf8mb4 DEFAULT NULL,
  `defeitos_constatados` varchar(200) CHARACTER SET utf8mb4 DEFAULT NULL,
  `medidas_corretivas` varchar(200) CHARACTER SET utf8mb4 DEFAULT NULL,
  `observacoes` varchar(200) CHARACTER SET utf8mb4 DEFAULT NULL,
  `valor_hora_tecnica` decimal(16,2) DEFAULT NULL,
  `tempo_gasto` varchar(8) CHARACTER SET utf8mb4 DEFAULT NULL,
  `inventario` varchar(30) CHARACTER SET utf8mb4 DEFAULT NULL,
  `equip_fabricante` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  `modelo` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  `n_serie` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  `portaria` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  `carga_maxima` varchar(20) CHARACTER SET utf8mb4 DEFAULT NULL,
  `divisao` varchar(20) CHARACTER SET utf8mb4 DEFAULT NULL,
  `h_entrada` varchar(8) CHARACTER SET utf8mb4 DEFAULT NULL,
  `h_saida` varchar(8) CHARACTER SET utf8mb4 DEFAULT NULL,
  `n_lacre_antigo` varchar(15) CHARACTER SET utf8mb4 DEFAULT NULL,
  `n_lacre_atual` varchar(15) CHARACTER SET utf8mb4 DEFAULT NULL,
  `selo_reparado_antigo` varchar(15) CHARACTER SET utf8mb4 DEFAULT NULL,
  `selo_reparado_atual` varchar(15) CHARACTER SET utf8mb4 DEFAULT NULL,
  `cod_peca_1` int(5) DEFAULT NULL,
  `quant_1` numeric(5) DEFAULT NULL,
  `Descri_1` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  `valor_unit_1` decimal (10,2) DEFAULT NULL,
  `valor_tot_1` decimal(10,2) DEFAULT NULL,  
  `cod_peca_2` int(5) DEFAULT NULL,
  `quant_2` numeric(5) DEFAULT NULL,
  `Descri_2` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  `valor_unit_2` decimal (10,2) DEFAULT NULL,
  `valor_tot_2` decimal(10,2) DEFAULT NULL,
  `cod_peca_3` int(5) DEFAULT NULL,
  `quant_3` numeric(5) DEFAULT NULL,
  `Descri_3` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  `valor_unit_3` decimal (10,2) DEFAULT NULL,
  `valor_tot_3` decimal(10,2) DEFAULT NULL,
  `cod_peca_4` int(5) DEFAULT NULL,
  `quant_4` numeric(5) DEFAULT NULL,
  `Descri_4` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  `valor_unit_4` decimal (10,2) DEFAULT NULL,
  `valor_tot_4` decimal(10,2) DEFAULT NULL,
  `cod_peca_5` int(5) DEFAULT NULL,
  `quant_5` numeric(5) DEFAULT NULL,
  `Descri_5` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  `valor_unit_5` decimal (10,2) DEFAULT NULL,
  `valor_tot_5` decimal(10,2) DEFAULT NULL,
  `data_abertura` datetime DEFAULT NULL,
  `data_fechamento` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;












CREATE TABLE `cad_oficina1` (
  `id` int(5) NOT NULL,
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
