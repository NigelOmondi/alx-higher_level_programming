-- Create user_0d_1
--user_0d_1 should have all privileges on MySQL server.
CREATE USER IF NOT USER EXISTS user_0d_1@localhost
IDENTIFIED BY `user_0d_1_pwd`;
GRANT ALL ON *.* TO user_0d_1@localhost
