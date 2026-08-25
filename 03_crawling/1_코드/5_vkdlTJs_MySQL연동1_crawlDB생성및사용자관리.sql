# mysql workbench에서 crawlDB 스키마 생성 후 crawluser 계정 생성
drop database if exists crawlDB;
create schema crawlDB default character set utf8mb4;

# 사용자 계정 등록
create user 'crawluser'@'%' identified by 'acorn1234';

# 권한 부여
grant all privileges on crawldb.* to 'crawluser'@'%';

# 권한 부여하는 기준 
-- 개발환경 : all privileges(모든 권한)
-- 운영 : select, delete, insert, update
-- 배포/관리 : create, alter, drop 별도 계정


# 권한 반영 
flush privileges;

# 권한 확인
show grants for 'crawluser'@'%';







