<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@page import="com.utils.MD5"%>
<%@page import="com.domain.User"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
ArrayList al=(ArrayList)request.getAttribute("ExampleInfo");
MD5 MD=new MD5();
String getAll=MD.toMD5("getAll");
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    <title>数据招聘</title>
    <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE11">
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
<meta http-equiv="keywords" content="">
	<meta http-equiv="description" content="">
	<link rel="stylesheet" type="text/css" href="<%=path%>/css/style.css">
    <link rel="stylesheet" type="text/css" href="<%=path%>/css/job.css">
   
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


    <%
      if(al!=null&&al.size()!=0)
        {
           for(int i=0;i<al.size();i++)
               {
                  Object objects[]=(Object[])al.get(i);
    %>
    <div class='header_jobInfo'><a href="/FoolAlgorithm/ExampleService?action=<%=getAll%>">&nbsp;&nbsp;分析案例</a>>><%=objects[1] %></div>
     <div class="DA_jobInfo">
    <div class='jobinfo'>
    <div class='jobinfo_style'>
    <div class='jobinfo_title'><font class='job_info_title'></font><%=objects[2] %></div>
    <div class='jobinfo_href'>
    <%=objects[3] %>
    </div>
    </div>
    </div>
     <%
        }}
         %> 
     </div>    
     
    <div class='jobinfo_foot'>
    </div>

 </body>

</html>
