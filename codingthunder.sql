-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 19, 2024 at 11:47 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` varchar(60) NOT NULL,
  `phone_num` varchar(60) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `email` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(1, 'umer', '12121212', 'Hello Good Morning', '2024-08-03 12:54:09', 'umer@gmail.com'),
(2, 'owais', '9595959595', 'Hello Good Afternoon', '2024-08-03 12:55:00', 'owais@gmail.com'),
(3, 'rehan', '6767676767', 'This is Rehan. I want to learn Python Programming.', '2024-08-03 13:03:53', 'rehan@gmail.com'),
(4, 'Neeraj', '040404040404', 'Hello This is Neeraj from NRCM', '2024-08-05 15:48:05', 'neeraj@gmail.com'),
(5, 'Abdul', '121212121212', 'This is Abdul', '2024-08-08 20:29:20', 'abdul@gmail.com'),
(7, 'Muskan Banu', '9959747039', 'Hi', '2024-08-15 12:41:28', 'muskan@gmail.com'),
(8, 'Muskan Banu', '9959747039', 'wwww', '2024-08-19 12:27:33', 'muskan@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(50) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(60) NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `img_file` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `date`, `img_file`) VALUES
(1, 'birthday', 'My birthday is on 12th may', 'bday-post', 'Hello', '2024-08-19 10:26:18', 'bday.jpg'),
(2, 'Python', 'Learn Python With Umer', 'python-post', 'This is OOP\'s Programming', '2024-08-19 10:30:48', 'contact-bg.jpg'),
(3, 'Web Dev', 'Learn Django and Flask', 'web-post', 'I am web dev', '2024-08-19 10:33:20', 'blog.jpg'),
(4, 'Java DSA', 'learn Java Oops and DSA', 'java-post', 'Learning java and solving Leet codes', '2024-08-19 12:24:23', 'java.jpg'),
(6, 'Full stack', 'front-end + Back-end', 'full-post', 'MERN stack and Fask', '2024-08-19 12:26:36', 'mern.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
