# 数据库

mysql -uroot -p123456
create database wuya character set utf8 collate utf8_bin;


# 查询
后端：views中使用serializers，return使用HttpResponse+json.dumps
前端：
1、返回的数据为string
2、JSON.parse转化
3、eval：由json字符串转换为json对象
4、获取值：jsonOBJ.key
5、组装html：通过str+='标签'
6、填充html：通过 ("#ID").html(str)
7、time转化为格式化字符串
8、字符串转换为格式化time

