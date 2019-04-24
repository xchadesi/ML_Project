<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@page import="com.utils.MD5"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
String mess=(String)request.getAttribute("messages");
	if(mess==null||mess.equals(""))
		mess="<span></span>";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    <title>找回密码</title>
    <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE11">
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<link rel="stylesheet" type="text/css" href="<%=basePath%>/css/login.css">
	<link rel="stylesheet" href="css/style.css">
  </head>
  
<%
String getpwd=new MD5().toMD5("getpwd");
String toRegister=new MD5().toMD5("toRegister");
String getAll=new MD5().toMD5("getAll");
%>    
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
           <p>找回密码</p>
           <div class="user-info">
                <div class="user-pass">
                  <form id="fm1" action="/FoolAlgorithm/LoginService?action=<%=getpwd%>" method="post">
                    <div class="user-name">
                    <input id="name" name="name"  placeholder="输入用户名"  type="text" value=""/>
                    </div>
                    <div class="pass-word">
                    <input id="mail" name="mail"  placeholder="输入邮箱"  type="text" value="" />
                    </div>
					<div class="error-mess" >
						<font class="font_sty"><%=mess%></font>
					</div>
					<input class="logging" value="找回密码" type="submit"/> 
                  </form>
                </div>
              <div class="third-part">
                <div class="register-now"><span>还没有帐号？</span>
	                <span class="register">
	                	<a href="/FoolAlgorithm/RegisterService?action=<%=toRegister%>">立即注册</a>
	                </span>
               	</div>
              </div>
              </div>
        </div>
    </div>
  </body>
</html>