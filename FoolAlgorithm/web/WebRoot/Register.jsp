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
    <base>
    
    <title>DataAnswer注册</title>
    <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE11">
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="">
	<meta http-equiv="description" content="">
	<link rel="stylesheet" type="text/css" href="css/register.css">
	 <link rel="stylesheet" href="css/style.css">

  </head>
<%
String register=new MD5().toMD5("register"); 
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
  <div class='register_img'>
     <img src="image/logo_login.PNG" alt="DataAnswer">
     </div>
    <div class="Register_body">
      <div class="Register_header"><font class="font_style2">DataAnswer注册</font>
      </div>
      <div class="register-info">
          <div class="user-info">
            <form id="fm1" name="userform" action="/FoolAlgorithm/RegisterService?action=<%=register%>" method="post">
              <ul>
                <li><span>用户名</span>
                  <input id="name" name="name" tabindex="1" placeholder="不超过20个字符" class="user-name" type="text" value=""/>
                </li>
                <li><span>邮箱</span>
                  <input id="mail" name="mail" tabindex="1" placeholder="请输入有效的邮箱" class="user-name" type="text" value=""/>
                </li>
                <li><span>登录密码</span>
                  <input id="pwd" name="pwd" tabindex="3" placeholder="不超过20个字符" class="main-password" type="password" value=""/>
                </li>
                <li><span>再输入一次</span>
                  <input type="password" tabindex="4" class="password-agin" name="confirmpwd" id="confirmpwd"/>
                </li>  
             </ul>
                <div class="mess_error"><font class="fnt_style"><%=mess%></font></div>
                <div class="next-btn">
                	<input class="next-step" value="确  认"	tabindex="7" type="submit" />
                </div>
             
            </form>
          </div>


      </div>
    </div>
 </body>
</html>
