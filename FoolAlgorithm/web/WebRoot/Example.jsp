<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@page import="com.utils.MD5"%>
<%@page import="com.domain.User"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
ArrayList al=(ArrayList)request.getAttribute("AllExample");
ArrayList all=(ArrayList)request.getAttribute("AllExampleInfo");
MD5 MD=new MD5();
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    <title>大数据招聘</title>
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
  <%
String getAll=MD.toMD5("getAll");
String JobInfo=MD.toMD5("ExampleInfo");
String fanye=MD.toMD5("fanye");
%> 
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
      
    <div class="example">
    <%
                 int total=0; //总的条数
		         int size=20;//每页的条数
		         int pag=0;//总的页数
		         int pagenow=1;//默认的当前页数
                  if(al!=null)
                  {
                   if(al.size()!=0)
                   {
                     //从自我刷新的中得到当前页码
		             String now=request.getParameter("pagenow");
		             if(now!=null)
		             {   
			           pagenow=Integer.parseInt(now);
		              }
		               total=al.size();
                     //获得总的页数
			         pag=total%size==0?total/size:total/size+1; 
                     //如果当前页数大于总页数，则置为最后一页
			         if(pagenow>pag)
			         {
				       pagenow=pag;
			          }
			          //判断是否为最后一页
			         if(pagenow==pag)
			        {
                         for(int i=(pagenow-1)*size;i<total;i++)
                      {
                          Object objects[]=(Object[])al.get(i);
             %>
    <div class='job'>
    <div class='time'><%=objects[1] %></div>
    <div class='job_title'><a href="/FoolAlgorithm/ExampleService?action=<%=JobInfo%>&ExampleId=<%=objects[0]%>"><%=objects[2] %></a></div>
    <div class='job_href'><a href="/FoolAlgorithm/ExampleService?action=<%=JobInfo%>&ExampleId=<%=objects[0]%>">详情</a></div>
    </div>
    <% 
				}
			}else {
				for(int k=(pagenow-1)*size;k<(pagenow-1)*size+size;k++)
				{
				   Object objects[]=(Object[])al.get(k);
    %>
    <div class='job'>
    <div class='time'><%=objects[1] %></div>
    <div class='job_title'><a href="/FoolAlgorithm/ExampleService?action=<%=JobInfo%>&ExampleId=<%=objects[0]%>"><%=objects[3] %></a></div>
    <div class='job_href'><a href="/FoolAlgorithm/ExampleService?action=<%=JobInfo%>&ExampleId=<%=objects[0]%>">详情</a></div>
    </div>
     <%
        }}
    %> 
    <div class="page">
        <div class="page2">&nbsp;<%=pagenow%>/<%=pag%>&nbsp;</div>
		<% //判断是否为首页
		if(pagenow==1)
		{
		%>
			<div class="page3"> &nbsp;<a href='/FoolAlgorithm/ExampleService?action=<%=fanye%>&pagenow=<%=1%>'>首  页 </a>&nbsp;</div>
	    <% 
		}else{
		%>
		    <div class="page3"> &nbsp;<a href='/FoolAlgorithm/ExampleService?action=<%=fanye%>&pagenow=<%=1%>'>首  页 </a>&nbsp;</div>
		    <div class="page4">&nbsp;<a href='/FoolAlgorithm/ExampleService?action=<%=fanye%>&pagenow=<%=pagenow-1%>'>上一页    </a>&nbsp;</div>
		<%
		}
		//判断是否为尾页
		if(pagenow==pag)
		{
		%>
			<div class="page6"> &nbsp;<a href='/FoolAlgorithm/ExampleService?action=<%=fanye%>&pagenow=<%=pagenow%>'>尾  页</a>&nbsp;</div>
		<%
		}else {
		%>
			<div class="page5"> &nbsp;<a href='/FoolAlgorithm/ExampleService?action=<%=fanye%>&pagenow=<%=pagenow+1%>'>下一页</a>&nbsp;</div>
			<div class="page6"> &nbsp;<a href='/FoolAlgorithm/ExampleService?action=<%=fanye%>&pagenow=<%=pag%>'>尾  页</a>&nbsp;</div>
		<%
		}
        %>
        </div>
        <%
		} }
        %> 
   </div>      
 </body>

</html>
