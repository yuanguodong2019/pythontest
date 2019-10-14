from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
import json
import pymysql
# Create your views here.

def list(request):
    db = pymysql.connect(host="localhost", user="root", password="sasa", db="myblog", port=3306)
    cur = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from user"
    try:
        cur.execute(sql)  # 执行sql语句  
        list = cur.fetchall()  # 获取查询的所有记录  
        return render(request, 'index.html', {'list':list})
    except Exception as e:
        return 0
    finally:
        db.close()  # 关闭连接  

def add(request):
    if request.method=="GET":
        return render(request,'add.html')
    else:
        print ("1")
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print (name,email,password)
        db = pymysql.connect(host="localhost", user="root", password="sasa", db="myblog", port=3306)
        cur = db.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute("insert into user(name,email,password)values (%s,%s,%s)",[name,email,password])  # 执行sql语句  
        db.commit()
        cur.close()
        db.close()  # 关闭连接  
        return redirect('/user/list/')

def delete(request):
    nid=request.GET.get('id')
    db = pymysql.connect(host="localhost", user="root", password="sasa", db="myblog", port=3306)
    cur = db.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute("delete from user where id = %s", [nid,])  # 执行sql语句  
    db.commit()
    cur.close()
    db.close()  # 关闭连接  
    return redirect('/user/list/')

def edit(request):
    if request.method == "GET":
        nid=request.GET.get('id')
        db = pymysql.connect(host="localhost", user="root", password="sasa", db="myblog", port=3306)
        cur = db.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute("select * from user  where id = %s", [nid,])  # 执行sql语句  
        list = cur.fetchone()
        cur.close()
        db.close()  # 关闭连接  
        return render(request, 'edit.html', {'list': list})
    else:
        id =request.GET.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        db = pymysql.connect(host="localhost", user="root", password="sasa", db="myblog", port=3306)
        cur = db.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute("update user set name = %s, email =%s,password = %s where id = %s", [name,email,password,id])  # 执行sql语句  
        db.commit()
        cur.close()
        db.close()  # 关闭连接  
        return redirect('/user/list/')
