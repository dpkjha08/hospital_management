-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 24, 2020 at 03:50 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hosp_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `id` int(11) NOT NULL,
  `patient_id` varchar(10) NOT NULL,
  `patient_name` varchar(100) NOT NULL,
  `doctor_id` varchar(10) NOT NULL,
  `doctor_name` varchar(100) NOT NULL,
  `doctor_fee` varchar(100) NOT NULL,
  `medicine_fee` varchar(100) NOT NULL,
  `is_admitted` tinyint(1) NOT NULL,
  `bed_charge` varchar(100) NOT NULL,
  `no_days` varchar(100) NOT NULL,
  `status` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(15) NOT NULL,
  `pending` varchar(100) NOT NULL,
  `paid` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`id`, `patient_id`, `patient_name`, `doctor_id`, `doctor_name`, `doctor_fee`, `medicine_fee`, `is_admitted`, `bed_charge`, `no_days`, `status`, `date`, `time`, `pending`, `paid`, `total`) VALUES
(5, '13', 'Janhavi Patil', '8', 'Dinanath Jha', '500', '1000', 1, '100', '50', 'Completed', '2020-05-25', '14:40', '1500', '5000', '6500'),
(6, '13', 'Janhavi Patil', '14', 'Deepak Jha', '', '', 0, '', '', 'Pending', '2020-05-25', '16:06', '', '', ''),
(7, '6', 'Aadit  Thanekar', '14', 'Deepak Jha', '1000', '500', 0, '0', '0', 'Completed', '2020-05-27', '09:07', '1400', '100', '1500'),
(8, '6', 'Aadit  Thanekar', '15', 'Dinanath Jha', '', '', 0, '', '', 'Pending', '2020-05-27', '15:40', '', '', ''),
(10, '13', 'Janhavi Patil', '15', 'Dinanath Jha', '1000', '2000', 1, '200', '5', 'Completed', '2020-05-25', '21:00', '1000', '3000', '4000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add sign up form', 1, 'add_signupform'),
(2, 'Can change sign up form', 1, 'change_signupform'),
(3, 'Can delete sign up form', 1, 'delete_signupform'),
(4, 'Can view sign up form', 1, 'view_signupform'),
(5, 'Can add log entry', 2, 'add_logentry'),
(6, 'Can change log entry', 2, 'change_logentry'),
(7, 'Can delete log entry', 2, 'delete_logentry'),
(8, 'Can view log entry', 2, 'view_logentry'),
(9, 'Can add permission', 3, 'add_permission'),
(10, 'Can change permission', 3, 'change_permission'),
(11, 'Can delete permission', 3, 'delete_permission'),
(12, 'Can view permission', 3, 'view_permission'),
(13, 'Can add group', 4, 'add_group'),
(14, 'Can change group', 4, 'change_group'),
(15, 'Can delete group', 4, 'delete_group'),
(16, 'Can view group', 4, 'view_group'),
(17, 'Can add user', 5, 'add_user'),
(18, 'Can change user', 5, 'change_user'),
(19, 'Can delete user', 5, 'delete_user'),
(20, 'Can view user', 5, 'view_user'),
(21, 'Can add content type', 6, 'add_contenttype'),
(22, 'Can change content type', 6, 'change_contenttype'),
(23, 'Can delete content type', 6, 'delete_contenttype'),
(24, 'Can view content type', 6, 'view_contenttype'),
(25, 'Can add session', 7, 'add_session'),
(26, 'Can change session', 7, 'change_session'),
(27, 'Can delete session', 7, 'delete_session'),
(28, 'Can view session', 7, 'view_session'),
(29, 'Can add prescription', 8, 'add_prescription'),
(30, 'Can change prescription', 8, 'change_prescription'),
(31, 'Can delete prescription', 8, 'delete_prescription'),
(32, 'Can view prescription', 8, 'view_prescription'),
(33, 'Can add appointment', 9, 'add_appointment'),
(34, 'Can change appointment', 9, 'change_appointment'),
(35, 'Can delete appointment', 9, 'delete_appointment'),
(36, 'Can view appointment', 9, 'view_appointment');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(2, 'admin', 'logentry'),
(4, 'auth', 'group'),
(3, 'auth', 'permission'),
(5, 'auth', 'user'),
(6, 'contenttypes', 'contenttype'),
(9, 'login', 'appointment'),
(8, 'login', 'prescription'),
(1, 'login', 'signupform'),
(7, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-05-23 15:31:44.679880'),
(2, 'auth', '0001_initial', '2020-05-23 15:31:46.391476'),
(3, 'admin', '0001_initial', '2020-05-23 15:31:54.070228'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-05-23 15:31:56.377958'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-05-23 15:31:56.461731'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-05-23 15:31:57.344993'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-05-23 15:31:58.189346'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-05-23 15:31:58.310024'),
(9, 'auth', '0004_alter_user_username_opts', '2020-05-23 15:31:58.358941'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-05-23 15:31:59.155099'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-05-23 15:31:59.202008'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-05-23 15:31:59.247849'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-05-23 15:31:59.357558'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-05-23 15:31:59.509152'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-05-23 15:31:59.637809'),
(16, 'auth', '0011_update_proxy_permissions', '2020-05-23 15:31:59.693656'),
(17, 'login', '0001_initial', '2020-05-23 15:31:59.994676'),
(18, 'sessions', '0001_initial', '2020-05-23 15:32:00.264919'),
(19, 'login', '0002_signupform_phone_number', '2020-05-23 15:32:55.631941'),
(20, 'login', '0003_auto_20200524_0151', '2020-05-23 20:21:50.823809'),
(21, 'login', '0004_auto_20200524_0154', '2020-05-23 20:24:30.901145'),
(22, 'login', '0005_signupform_blood_group', '2020-05-23 20:30:22.851808'),
(23, 'login', '0006_prescription', '2020-05-23 22:19:23.365659'),
(24, 'login', '0007_appointment', '2020-05-24 00:22:30.383777'),
(25, 'login', '0008_auto_20200524_0553', '2020-05-24 00:23:49.131564'),
(26, 'login', '0009_auto_20200524_0559', '2020-05-24 00:30:02.435533');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('zmpok2qfogfap8gp19sior3tfuczajj4', 'OTZjYzBhZTFkMjNlNGZkNzZkOTkwMzViZWJjZDQ1OWRjYWU5NzFkZDp7ImVtYWlsX3N1Y2Nlc3MiOiJFbWFpbCBTZW50IFN1Y2Nlc3NmdWxseSB0byBKYW5oYXZpIFBhdGlsISEhIn0=', '2020-06-07 13:28:26.817147');

-- --------------------------------------------------------

--
-- Table structure for table `prescription`
--

CREATE TABLE `prescription` (
  `user_id` int(11) NOT NULL,
  `patient_id` varchar(10) NOT NULL,
  `patient_name` varchar(100) NOT NULL,
  `doctor_id` varchar(10) NOT NULL,
  `doctor_name` varchar(100) NOT NULL,
  `symptoms` varchar(100) NOT NULL,
  `prescription` varchar(400) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `prescription`
--

INSERT INTO `prescription` (`user_id`, `patient_id`, `patient_name`, `doctor_id`, `doctor_name`, `symptoms`, `prescription`, `date`) VALUES
(5, '6', 'Aadit  Thanekar', '14', 'Deepak Jha', 'Fever ', 'hgqwctyqdw ytt yudv2 uvy21ef1e u1ev12e wuv12ey2eye2  uyyy12ef6', '2020-05-24'),
(6, '13', 'Janhavi Patil', '14', 'Deepak Jha', 'Cough', 'Drink Warm Water', '2020-05-24'),
(7, '6', 'Aadit  Thanekar', '14', 'Deepak Jha', 'Cold, Fever', 'Bed rest for two weeks', '2020-05-24'),
(8, '6', 'Aadit  Thanekar', '14', 'Deepak Jha', 'High Fever, Weakness', 'Bed rest for two weeks', '2020-05-24'),
(12, '13', 'Janhavi Patil', '14', 'Deepak Jha', 'Cough', 'Bed rest for two weeks', '2020-05-24'),
(13, '13', 'Janhavi Patil', '14', 'Deepak Jha', 'qwdjvh3', 'hgqwctyqdw ytt yudv2 uvy21ef1e u1ev12e wuv12ey2eye2  uyyy12ef6', '2020-05-24');

-- --------------------------------------------------------

--
-- Table structure for table `signup`
--

CREATE TABLE `signup` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `phone_number` varchar(10) NOT NULL,
  `address` varchar(200) DEFAULT NULL,
  `age` varchar(4) NOT NULL,
  `case_paper` varchar(10) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `blood_group` varchar(5) NOT NULL,
  `department` varchar(100) NOT NULL DEFAULT '',
  `salary` varchar(10) NOT NULL DEFAULT '',
  `status` varchar(10) NOT NULL DEFAULT 'Active',
  `attendance` varchar(20) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `signup`
--

INSERT INTO `signup` (`user_id`, `first_name`, `last_name`, `email`, `user_type`, `password`, `phone_number`, `address`, `age`, `case_paper`, `gender`, `blood_group`, `department`, `salary`, `status`, `attendance`) VALUES
(6, 'Aadit ', 'Thanekar', 'aadit@gmail.com', 'patient', '1234567890', '7826712546', 'wdej', '20', '90786758', 'male', 'AB-', '', '', 'Active', ''),
(9, 'Hospital', 'Receptionist', 'recep@gmail.com', 'receptionist', '1234567890', '1029384756', 'Rehti hai kidar toh yeh madam', '30', 'None', 'female', 'A+', '', '', 'Active', ''),
(11, 'Human ', 'Resources', 'hr@gmail.com', 'hr', '1234567890', '0987654321', 'Nako Nako', '50', '', 'female', 'AB-', '', '', 'Active', ''),
(13, 'Janhavi', 'Patil', 'foodpoker16@gmail.com', 'patient', '1234567890', '2351273412', 'wdej', '20', '9090', 'female', 'AB-', '', '0', 'Active', ''),
(14, 'Deepak', 'Jha', 'dnjha1387@gmail.com', 'doctor', '1234567890', '9594665337', 'jvewuy', '90', '9090', 'male', 'A-', 'Neurologist', '50000', 'Inactive', '35'),
(15, 'Dinanath', 'Jha', 'dnjha@gmail.com', 'doctor', '1234567890', '9594665337', 'gvdxyv8t', '20', '', 'male', 'AB+', 'Neurologist', '50000000', 'Active', '60'),
(18, 'First ', 'User', 'first@gmail.com', 'patient', '1234567890', '9594665337', 'jvewuy', '20', '97897', 'male', 'AB+', '', '0', 'Active', ''),
(20, 'qtwwer', 'wejfgy', 'decode@gmail.com', 'patient', '1234567890', '9594665765', 'hhxfoy', '90', '87675', 'male', 'AB-', '', '0', 'Active', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `prescription`
--
ALTER TABLE `prescription`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `signup`
--
ALTER TABLE `signup`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `prescription`
--
ALTER TABLE `prescription`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `signup`
--
ALTER TABLE `signup`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
