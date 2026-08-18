# 사용자 계정 등록 

# create user '사용자아이디'@'호스트' inentified by 'password';
# '호스트' 자리에 들어갈 수 있는 내용
#		'%' : 모든 ip에서 접속허용
#		'localhost' : 내부망에서만 허용(보안)

create user 'dbuser01'@'%' identified by 'pw12341234' ;
create user 'dbuser02'@'%' identified by 'pw12341234' ;

# 권한 부여
# grant 권한목록 on 데이터베이스 to '사용자계정':
# 권한목록 :
#		select, insert, delete, updata
#		create, alter, drop
#		app privileages

grant all privileges on testdb2.* to 'dbuser01'@'%';
grant select, delete, insert, update on testdb2.* to 'dbuser02'@'%';

# 권한 반영
flush privileges;

# 권한 확인
show grants for 'dbuser01'@'%';
show grants for 'dbuser02'@'%';










