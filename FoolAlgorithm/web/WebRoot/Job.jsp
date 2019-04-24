<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@page import="com.utils.MD5"%>
<%@page import="com.domain.User"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
ArrayList al=(ArrayList)request.getAttribute("AllJob");
ArrayList all=(ArrayList)request.getAttribute("AllJobInfo");
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
String JobInfo=MD.toMD5("JobInfo");
String fanye=MD.toMD5("fanye");
String city_jobtype=MD.toMD5("city_jobtype");
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
   
   <div class="DA_job">
    <div class="job_head_choose">
    <div class="job_choose"><a href="/FoolAlgorithm/JobService?action=<%=getAll%>">全部</a></div>
    <div class="job_choose">城市：<select  onchange="window.location=this.value;"><option value="0">请选择</option><option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=北京">北京</option>
    <option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=深圳">深圳</option><option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=上海">上海</option></select></div>
    <div class="job_choose">类型：<select onchange="window.location=this.value;"><option value="0">请选择</option><option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=社招">社招</option>
    <option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=实习">实习</option></select></div>
    <div class="job_chose">职位：<select onchange="window.location=this.value;"><option value="0">请选择</option><option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=数据分析">数据分析师</option>
    <option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=数据架构">大数据架构师</option>
    <option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=数据挖掘">数据挖掘工程师</option>
    <option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=数据库研发">数据库研发工程师</option>
    <option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=数据研发">大数据研发工程师</option>
    <option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=数据爬取">数据爬取工程师</option>
    <option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=数据标注">数据标注</option>
    <option value="/FoolAlgorithm/JobService?action=<%=city_jobtype%>&city_jobtype=数据产品">大数据产品</option>
    </select></div>
    </div>
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
    <div class='time'><%=objects[3] %></div>
    <div class='job_title'><a href="/FoolAlgorithm/JobService?action=<%=JobInfo%>&jobId=<%=objects[0]%>"><%=objects[1] %></a></div>
    <div class='job_href'><a href="/FoolAlgorithm/JobService?action=<%=JobInfo%>&jobId=<%=objects[0]%>">详情</a></div>
    </div>
    <% 
				}
			}else {
				for(int k=(pagenow-1)*size;k<(pagenow-1)*size+size;k++)
				{
				   Object objects[]=(Object[])al.get(k);
    %>
    <div class='job'>
    <div class='time'><%=objects[3] %></div>
    <div class='job_title'><a href="/FoolAlgorithm/JobService?action=<%=JobInfo%>&jobId=<%=objects[0]%>"><%=objects[1] %></a></div>
    <div class='job_href'><a href="/FoolAlgorithm/JobService?action=<%=JobInfo%>&jobId=<%=objects[0]%>">详情</a></div>
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
			<div class="page3"> &nbsp;<a href='/FoolAlgorithm/JobService?action=<%=fanye%>&pagenow=<%=1%>'>首  页 </a>&nbsp;</div>
	    <% 
		}else{
		%>
		    <div class="page3"> &nbsp;<a href='/FoolAlgorithm/JobService?action=<%=fanye%>&pagenow=<%=1%>'>首  页 </a>&nbsp;</div>
		    <div class="page4">&nbsp;<a href='/FoolAlgorithm/JobService?action=<%=fanye%>&pagenow=<%=pagenow-1%>'>上一页    </a>&nbsp;</div>
		<%
		}
		//判断是否为尾页
		if(pagenow==pag)
		{
		%>
			<div class="page6"> &nbsp;<a href='/FoolAlgorithm/JobService?action=<%=fanye%>&pagenow=<%=pagenow%>'>尾  页</a>&nbsp;</div>
		<%
		}else {
		%>
			<div class="page5"> &nbsp;<a href='/FoolAlgorithm/JobService?action=<%=fanye%>&pagenow=<%=pagenow+1%>'>下一页</a>&nbsp;</div>
			<div class="page6"> &nbsp;<a href='/FoolAlgorithm/JobService?action=<%=fanye%>&pagenow=<%=pag%>'>尾  页</a>&nbsp;</div>
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
