create database devopsroles;
use devopsroles;

CREATE TABLE test_table (
  name VARCHAR(20),
  color VARCHAR(10)
);

CREATE TABLE register (
  username VARCHAR(20),
  password VARCHAR(10)
);

INSERT INTO test_table
  (name, color)
VALUES
  ('dev', 'blue'),
  ('pro', 'yellow');

INSERT INTO register
  (username, password)
VALUES
  ('admin', 'admin123');