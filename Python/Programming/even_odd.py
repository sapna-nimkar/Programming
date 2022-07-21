'''
select * from tablename order by salary desc limit 1,1;

select max(sal) from employee where sal not in (select max(sal) from employee);

select max(sal) from employee where sal< (select max(sal) from employee);
'''