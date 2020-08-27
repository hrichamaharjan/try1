-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 23, 2020 at 10:39 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `register`
--

-- --------------------------------------------------------

--
-- Table structure for table `book_flight`
--

CREATE TABLE `book_flight` (
  `id` int(11) NOT NULL,
  `destination` varchar(100) NOT NULL,
  `source` varchar(100) NOT NULL,
  `dpt` date NOT NULL,
  `date` date NOT NULL,
  `combo` varchar(100) NOT NULL,
  `count_no` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `price` int(11) NOT NULL,
  `flight_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book_flight`
--

INSERT INTO `book_flight` (`id`, `destination`, `source`, `dpt`, `date`, `combo`, `count_no`, `user_id`, `price`, `flight_name`) VALUES
(21, 'Jnakpur', 'Kathmandu', '2020-08-04', '2020-08-10', 'Adult', 3, 14, 4000, 'Nepal Airlines'),
(22, 'Kathmandu', 'Lumbini', '2020-08-04', '2020-08-05', 'Old age', 3, 13, 4000, 'Tara Airlines'),
(23, 'Biratnagar', 'Dhangadi', '2020-09-10', '2020-09-11', 'Adult', 4, 7, 6000, 'Tara Airlines'),
(24, 'Bhadrapur', 'Kathmandu', '2020-08-04', '2020-08-05', 'Old age', 3, 10, 6000, 'Yeti Airlines'),
(25, 'kathmandu', 'Biratnagar', '2020-08-07', '2020-08-10', 'Adult', 2, 8, 6000, 'Surya Airline'),
(26, 'Dharan', 'Dhangadi', '2020-08-05', '2020-08-14', 'Infant', 2, 8, 4000, 'Surya Airline');

-- --------------------------------------------------------

--
-- Table structure for table `oneway`
--

CREATE TABLE `oneway` (
  `id` int(11) NOT NULL,
  `destination` varchar(100) NOT NULL,
  `source` varchar(100) NOT NULL,
  `dpt` date NOT NULL,
  `combo` varchar(100) NOT NULL,
  `count_no` int(11) NOT NULL,
  `class_selection` varchar(100) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `flight_name` varchar(100) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `oneway`
--

INSERT INTO `oneway` (`id`, `destination`, `source`, `dpt`, `combo`, `count_no`, `class_selection`, `user_id`, `flight_name`, `price`) VALUES
(14, 'Kathmandu', 'Janakpur', '2020-08-04', 'Adult', 3, 'Premium Economy', 14, 'Surya Airline', 4000),
(15, 'Dhangadi', 'Biratnagar', '2020-10-23', 'Adult', 4, 'First Class', 7, 'Tara Airlines', 6000),
(16, 'RasuwA', 'Dang', '2020-08-04', 'Adult', 3, 'Economy', 11, 'Buddha Air', 3000),
(17, 'Pokhara', 'Kaski', '2020-08-04', 'Infant', 3, 'Premium Economy', 12, 'Nepal Airlines', 4000),
(18, 'janakpur', 'Kathmandu', '2020-08-17', 'Infant', 2, 'Premium Economy', 8, 'Yeti Airlines', 4000),
(20, 'Jumla', 'Pokhara', '2020-09-15', 'Adult', 6, 'Premium Economy', 8, 'Tara Airlines', 4000),
(22, 'Kathmandu', 'Pokhara', '2020-09-24', 'Adult', 4, 'Premium Economy', 8, 'Yeti Airlines', 4000),
(28, 'Dang', 'Mustang', '2020-08-17', 'Infant', 2, 'Premium Economy', 8, 'Yeti Airlines', 4000),
(29, 'Pokhara', 'Dang', '2020-08-21', 'Adult', 3, 'Premium Economy', 8, 'Surya Airline', 4000);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(20) NOT NULL,
  `f_name` varchar(30) NOT NULL,
  `l_name` varchar(40) NOT NULL,
  `contact` int(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(20) NOT NULL,
  `question` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `f_name`, `l_name`, `contact`, `email`, `password`, `question`, `answer`) VALUES
(7, 'Rita', 'maharjan', 777887, 'rita@gmail.com', '6', 'Your First Pet Name?', 'tommy'),
(8, 'richa', 'mrj', 2147483647, 'ri@gmail.com', 'qrt', 'Your Birth Place?', 'kathmandu'),
(10, 'Shreya', 'Shrestha', 2147483647, 'shrey123@gmail.com', '128', 'Your Birth Place?', 'bhaktapur'),
(11, 'Ram', 'Prasad', 2147483647, 'ram@gmail.com', 'iu', 'Your Birth Place?', 'baitadi'),
(12, 'Sita', 'giri', 2147483647, 'sita@hotmail.com', 'siti', 'Your First Pet Name?', 'tommy'),
(13, 'Rose', 'Shah', 2147483647, 'rosy@live.com', 'r', 'Your First Pet Name?', 'sheru'),
(14, 'Gaurav', 'Jha', 2147483647, 'gauri@gmail.com', '6', 'Your NickName?', 'gauri'),
(15, 'maya', 'maharjan', 2147483647, 'maya@hotmail.com', 'a', 'Your Birth Place?', 'bhadrapur'),
(16, 'r', 'R', 66666, 'l@gmail.com', 'l', 'Your NickName?', 'u'),
(17, 'test_fname', 'test_lname', 0, 'test_email', 'test_password', 'test_question', 'test_answer');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book_flight`
--
ALTER TABLE `book_flight`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `oneway`
--
ALTER TABLE `oneway`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book_flight`
--
ALTER TABLE `book_flight`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `oneway`
--
ALTER TABLE `oneway`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `book_flight`
--
ALTER TABLE `book_flight`
  ADD CONSTRAINT `book_flight_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `oneway`
--
ALTER TABLE `oneway`
  ADD CONSTRAINT `oneway_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
