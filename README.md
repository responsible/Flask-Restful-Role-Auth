#基于Token及用户权限的Flask-Restful的Example
1. 以Token为认证
2. 拥有用户角色权限管理

#主要组成
1. Flask
2. Flask-Restful
3. Flask-SQlAlchemy
4. Flask-Security

#其他可选方案
1. Flask-JWT & Flask-Principal
2. itsdangerous & Flask-Principal
3. Flask-Login & Flask-Principal
4. ...

#运行
```
pip install -r ./requirement.txt
python manage.py
```

#测试
```
$ curl -X POST -H "Content-Type:application/json" -d '{"username":"test1","password":"test1"}' http://localhost:5000/login
{
    "message": "登录成功",
    "token": "WyIxIiwiOThiZmVlMjFlZjljYTU0NzZkYzNmMTUyODUzNDM2MzgiXQ.CgpV7Q.ypduIJefgJAdHAbB_WIrLzfsXYc"
}
```
```
$ curl -H "Content-Type:application/json" -H "Authorization: WyIxIiwiOThiZmVlMjFlZjljYTU0NzZkYzNmMTUyODUzNDM2MzgiXQ.CgpV7Q.ypduIJefgJAdHAbB_WIrLzfsXYc" "http://localhost:5000/protected"
{
    "msg": "这是需要Token的GET方法"
}
```
```
$ curl -X POST -H "Authorization: WyIxIiwiOThiZmVlMjFlZjljYTU0NzZkYzNmMTUyODUzNDM2MzgiXQ.CgpV7Q.ypduIJefgJAdHAbB_WIrLzfsXYc" "http://localhost:5000/protected"
{
    "msg": "这是需要Token和admin权限的POST方法"
}

```