create database project_python
default character set utf8
default collate utf8_general_ci;

use project_python;

create table user (
	id int(11) not null auto_increment,
    name varchar(50) not null,
    sex enum('M', 'F') not null,
    email varchar(254) not null,
    password varchar(25) not null,
    creation timestamp not null,
    constraint pk_user
		primary key (id)
);


-- PROCEDURES
delimiter $$

-- Verify if e-mail exists in table 'user'
create procedure p_EmailExists(in _email varchar(254))
begin
	select exists (select * from user where email = _email);
end $$

-- Register a new user
create procedure p_RegisterUser (
	in _name varchar(50), in _sex enum('M', 'F'),
    in _email varchar(254), in _password varchar(25))
begin
	insert into user (name, sex, email, password) 
		values (_name, _sex, _email, _password);
end $$

-- Select user's data by e-mail
create procedure p_SelectByEmail (in _email varchar(254))
begin
	select email, password, name, sex, id from user where email = _email;
end $$

-- Update the user's informations (name, email, sex)
create procedure p_UpdateUserInformations (
	in _name varchar(50), in _email varchar(254),
    in _sex enum('M', 'F'), in _id int(11))
begin
	update user 
		set name = _name, email = _email, sex = _sex
			where id = _id;
end $$

-- Update the user password
create procedure p_UpdateUserPassword (in _id int(11), in _password varchar(25))
begin
	update user
		set password = _password
			where id = _id;
end $$

-- Verify if password in parameter is equals in the user table
create procedure p_VerifyPassword (in _id int(11), in _password varchar(25))
begin
	declare userPassword int(25);
    
	set userPassword = (select password from user where id = _id);
    
    if userPassword = _password then
		select 'true';
        
	else
		select null;
	end if;

end $$

-- Delete user's data
create procedure p_DeleteAccount (in _id int(11))
begin
	delete from user where id = _id;
end $$

delimiter ;