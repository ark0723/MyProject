drop table if exists employee cascade; 
drop table if exists takes cascade;
drop table if exists class cascade;
drop table if exists student cascade;
drop table if exists professor cascade;
drop table if exists department cascade;
drop table if exists course cascade;

create table department 
(
dept_id varchar(10) not null,
dept_name varchar(20) not null,
office varchar(20),
constraint pk_department primary key(dept_id)
);

create table student 
(
stu_id varchar(10) not null,
resident_id varchar(14) unique not null,
name varchar(10) not null,
year int,
address varchar(10),
dept_id varchar(10),
constraint pk_student primary key(stu_id),
constraint fk_student foreign key(dept_id) references department(dept_id)
);

create table professor 
(
prof_id varchar(10) not null,
resident_id varchar(14) unique not null,
name varchar(10) not null,
dept_id varchar(10),
position varchar(10),
year_emp int,
constraint pk_professor primary key(prof_id),
constraint fk_professor foreign key(dept_id) references department(dept_id)
);

create table course 
(
course_id varchar(10) not null,
title varchar(20) not null,
credit int,
constraint pk_course primary key(course_id)
);

create table class 
(
class_id varchar(10) not null,
course_id varchar(10),
year int,
semester int,
division char(1),
prof_id varchar(10),
classroom varchar(9),
enroll int,
constraint pk_class primary key(class_id),
constraint fk_class1 foreign key(course_id) references course(course_id),
constraint fk_class2 foreign key(prof_id) references professor(prof_id)
);

create table takes 
(
stu_id varchar(10) not null,
class_id varchar(10),
grade char(5),
constraint pk_takes primary key(stu_id, class_id),
constraint fk_takes1 foreign key(stu_id) references student(stu_id),
constraint fk_takes2 foreign key(class_id) references class(class_id)
);

insert into department values('920', '컴퓨터공학과', '201호');
insert into department values('923', '산업공학과', '207호');
insert into department values('925', '전자공학과', '308호');

insert into student 
values('1292001', '900424-1825409', '김광식', 3, '서울', 920);
insert into student 
values('1292002', '900305-1730021', '김정현', 3, '서울', 920);
insert into student 
values('1292003', '891021-2308302', '김현정', 4, '대전', 920);
insert into student 
values('1292301', '890902-2704012', '김현정', 2, '대구', 923);
insert into student 
values('1292303', '910715-1524390', '박광식', 3, '광주', 923);
insert into student 
values('1292305', '921011-1809003', '김우주', 4, '부산', 923);
insert into student 
values('1292501', '900825-1506390', '박철수', 3, '대전', 925);
insert into student 
values('1292502', '911011-1809003', '백태성', 3, '서울', 925);
insert into student 
values('1292503', '901024-2409325', '최성희', 4, '전주', 925);

insert into professor 
values('92001', '590327-2839240', '이태연', '920', '교수', 1997);
insert into professor 
values('92002', '690702-1350026', '고희석', '920', '부교수', 2003);
insert into professor 
values('92301', '741011-2765501', '최성희', '923', '부교수', 2004);
insert into professor 
values('92302', '750728-1102458', '김태석', '923', '교수', 1999);
insert into professor 
values('92501', '620505-1200546', '박철재', '925', '조교수', 2012);
insert into professor 
values('92502', '740101-1830264', '장민석', '925', '부교수', 2005);

insert into course values('C101', '전산개론', 3);
insert into course values('C102', '자료구조', 3);
insert into course values('C103', '데이터베이스', 4);
insert into course values('C301', '운영체제', 3);
insert into course values('C302', '컴퓨터구조', 3);
insert into course values('C303', '이산수학', 4);
insert into course values('C304', '객체지향언어', 4);
insert into course values('C501', '인공지능', 3);
insert into course values('C502', '알고리즘', 2);

insert into class values('C101-01', 'C101', 2012, 1, 'A', '92301', '301호', 40);
insert into class values('C102-01', 'C102', 2012, 1, 'A', '92001', '209호', 30);
insert into class values('C103-01', 'C103', 2012, 1, 'A', '92501', '208호', 30);
insert into class values('C103-02', 'C103', 2012, 1, 'B', '92301', '301호', 30);
insert into class values('C501-01', 'C501', 2012, 1, 'A', '92501', '103호', 45);
insert into class values('C501-02', 'C501', 2012, 1, 'B', '92502', '204호', 25);
insert into class values('C301-01', 'C301', 2012, 2, 'A', '92502', '301호', 30);
insert into class values('C302-01', 'C302', 2012, 2, 'A', '92501', '209호', 45);
insert into class values('C502-01', 'C502', 2012, 2, 'A', '92001', '209호', 30);
insert into class values('C502-02', 'C502', 2012, 2, 'B', '92301', '103호', 26);

insert into takes values('1292001', 'C101-01', 'B+');
insert into takes values('1292001', 'C103-01', 'A+');
insert into takes values('1292001', 'C301-01', 'A');
insert into takes values('1292002', 'C102-01', 'A');
insert into takes values('1292002', 'C103-01', 'B+');
insert into takes values('1292002', 'C502-01', 'C+');
insert into takes values('1292003', 'C103-02', 'C');
insert into takes values('1292003', 'C501-02', 'A+');
insert into takes values('1292301', 'C102-01', 'C+');
insert into takes values('1292303', 'C102-01', 'C');
insert into takes values('1292303', 'C103-02', 'B+');
insert into takes values('1292303', 'C501-01', 'A+');
insert into takes values('1292303', 'C302-01', 'B');

create table employee
(
ename varchar(20),
rank varchar(10),
sal int,
bonus int,
dept_id varchar(10),
constraint pk_emp primary key(ename),
constraint fk_emp foreign key(dept_id) references department(dept_id)
);


insert into employee
values('김광성', '사원', 2800, 20, '920');
insert into employee
values('김홍식', '사원', 3000, 20, '920');
insert into employee
values('최대호', '대리', 3500, 10, '920');
insert into employee
values('박철수', '과장', 5500, 10, '920');


insert into employee
values('안성수', '사원', 2500, 20, '923');
insert into employee
values('최수진', '대리', 2700, 10, '923');
insert into employee
values('신길수', '대리', 2800, 10, '923');
insert into employee
values('양대진', '과장', 4000, 10, '923');

insert into employee
values('김영철', '사원', 2800, 20, '925');
insert into employee
values('최보혜', '사원', 3500, 15, '925');
insert into employee
values('윤길중', '대리', 3800, 20, '925');
insert into employee
values('이인석', '과장', 5500, 20, '925');