<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@page import="com.utils.MD5"%>
<%@page import="com.domain.User"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
MD5 MD=new MD5();
String getAll=MD.toMD5("getAll");
String JobInfo=MD.toMD5("ExampleInfo");
String fanye=MD.toMD5("fanye");
String tologin=MD.toMD5("toLogin");
String quit=MD.toMD5("quit");
User mBean=(User)request.getSession().getAttribute("masterBean");
%>   

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title></title>
 <link rel="stylesheet" href="css/style.css">
</head>
<style> 
a{ text-decoration:none} 
</style> 
<body>
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
      <%
   if(mBean!=null)
   {
   %>
   <div class='header_nav5'><%=mBean.getUserName()%></div>
   <%
      if(mBean.getUserName().equals("dataanswer")){
    %>
   <div class='header_nav6'><a href="/FoolAlgorithm/AddExample.jsp">发布</a></div>
   <%
   }
    %>
   <div class='header_nav7'><a href="/FoolAlgorithm/LoginService?action=<%=quit%>">退出</a></div>
   <%
   }else{
    %>
      <div class='header_nav5'><a href="/FoolAlgorithm/Login.jsp?action=<%=tologin%>">登录</a>
      &nbsp;&nbsp;<a href="/FoolAlgorithm/Register.jsp">注册</a></div>
      <%
      }
       %>
  </div>
  </div>
  <div class="nav_info">傻瓜式算法预测<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <span >地球人都会用的算法工具!</span></div>
  <div class="nav">
    <div class="nav_func"><a href="/FoolAlgorithm/AlgorithmUpload.jsp">调节算法</a></div>
	<div class="nav_func"><a href="/FoolAlgorithm/DimUpload.jsp">调节维度</a></div>
	<div class="nav_func"><a href="/FoolAlgorithm/PredictUpload.jsp">预测结果</a></div>
  </div>
  <div class="radar"></div>
</body>
</body>
</html>
