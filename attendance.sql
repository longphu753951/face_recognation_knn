create database attendance;

create table `attendance`.`employee`(
	`employee_id` bigint not null auto_increment,
    `name`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `image_path` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    primary key (`employee_id`)
);

select employee_id from  `attendance`.`employee` where image_path = 'Long_Phu';

create table `attendance`.`attendance`(
	`checkin_id` bigint not null auto_increment,
    `attendance_status` bigint not null ,
    `employee_id` bigint not null,
	`attendance_date` date NOT NULL,
	`attendance_time` time NOT NULL,
    primary key(`checkin_id`,`employee_id`),
    CONSTRAINT `employee_id` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`) ON DELETE RESTRICT ON UPDATE CASCADE
)


