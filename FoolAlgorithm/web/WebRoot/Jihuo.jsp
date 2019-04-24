<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@page import="com.utils.MD5"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
String mess=(String)request.getAttribute("messages");
	if(mess==null||mess.equals(""))
		mess="<span></span>";
String getAll=new MD5().toMD5("getAll");
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    <title>用户登录</title>
    <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE11">
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="数据博客:大数据从业人员的聚集地，分享大数据知识，请教和回答大数据相关问题。">
	<meta http-equiv="description" content="数据博客:大数据从业人员的聚集地，分享大数据知识，请教和回答大数据相关问题。">
	<link rel="stylesheet" type="text/css" href="<%=basePath%>/css/login.css">
    <link rel="stylesheet" href="css/style.css">

  </head>
  
  <body>
    <div class="header">
  <div class='header1'>
  <img src="image/logo.PNG"  alt="DataAnswer"/>
  </div>
  <div class='header2'>
     <div class='header_nav1'><a href="/FoolAlgorithm/index.jsp">首页</a></div>
     <div class='header_nav2'><a href="/FoolAlgorithm/ExampleService?action=<%=getAll%>">分析案例</a></div>
     <div class='header_nav3'><a href="/FoolAlgorithm/T.jsp">知识图谱</a></div>
      <div class='header_nav4'><a href="/FoolAlgorithm/JobService?action=<%=getAll%>">数据招聘</a></div>
      <div class='header_nav5'><a href="/FoolAlgorithm/Login.jsp">登录</a>
      &nbsp;&nbsp;<a href="/FoolAlgorithm/Register.jsp">注册</a></div>
  </div>
  </div>
    <div class="header_login">
    <div class='login_img'>
     <img src="image/logo_login.PNG" alt="DataAnswer">
     </div>
        <div class="login_part">
           <p>帐号激活</p>
           <div class="user-info">
                
			<div class="error-mess" >
					<font class="font_sty"><%=mess%></font>
			</div>
			<br>
			<div class="error-mess" >
					<a href="/FoolAlgorithm/index.jsp">返回首页<a>
			</div>
					
              </div>
        </div>
    </div>
  </body>
</html>