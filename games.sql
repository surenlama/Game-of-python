-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 27, 2020 at 03:23 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `games`
--

-- --------------------------------------------------------

--
-- Table structure for table `game`
--

CREATE TABLE `game` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `id` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `game`
--

INSERT INTO `game` (`username`, `password`, `id`) VALUES
('amarsir', '123', 1),
('vim', '123', 888),
('dixit', '123', 999),
('tashi', '123', 9870),
('dixit', '123', 758934);

-- --------------------------------------------------------

--
-- Table structure for table `game1`
--

CREATE TABLE `game1` (
  `name` varchar(50) NOT NULL,
  `email` varchar(15) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `game1`
--

INSERT INTO `game1` (`name`, `email`, `phone`, `username`, `password`) VALUES
('kohil', 'nkjsd@gmail.com', '758934', 'dixit', '123'),
('mahendran', 'njlwefekj', '76812', 'suren', '123'),
('sangeet', 'surenkdsf', '788', 'suren', '123'),
('vim', 'vim@123', '888', 'vim', '123'),
('akhilesh', 'anil@123', '9803939647', 'akhilesh', '123'),
('raju', 'suren@gmail.com', '98093939647', 'dixit', '123'),
('bikash', 'bikash@gmal.com', '9870', 'tashi', '123');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('dixit', '123'),
('suren', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `game`
--
ALTER TABLE `game`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `game1`
--
ALTER TABLE `game1`
  ADD PRIMARY KEY (`phone`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
