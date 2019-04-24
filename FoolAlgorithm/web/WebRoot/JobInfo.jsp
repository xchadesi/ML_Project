<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@page import="com.domain.Job"%>
<%@page import="com.utils.MD5"%>
<%@page import="com.domain.User"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
ArrayList al=(ArrayList)request.getAttribute("JobInfo");
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
<meta http-equiv="keywords" content="数据交易,数据服务、数据解读,数据评估，数据招聘">
	<meta http-equiv="description" content="DataAnswer是数据交易/服务入口，集聚了各个数据交易平台和免费的数据源，也为大家提供数据源和数据服务的测评机制，以及大数据视频分析解读和招聘">
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

    
     <!--nav导航-->
      <%
      if(al!=null&&al.size()!=0)
        {
           for(int i=0;i<al.size();i++)
               {
                  Object objects[]=(Object[])al.get(i);
    %>
    <div class='header_jobInfo'><a href="/FoolAlgorithm/ExampleService?action=<%=getAll%>">&nbsp;&nbsp;数据招聘</a>>><%=objects[1] %></div>
    <div class="DA_jobInfo">
    <div class='jobinfo'>
    <div class='jobinfo_style'>
    <div class='jobinfo_title'><font class='job_info_title'></font><%=objects[1] %></div>
    <div class='jobinfo_href'>
    <%=objects[2] %>
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
