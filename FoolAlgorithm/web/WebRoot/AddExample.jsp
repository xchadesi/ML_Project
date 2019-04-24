<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@page import="com.utils.MD5"%>
<%@page import="com.domain.User"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
MD5 MD=new MD5();
User mBean=(User)request.getSession().getAttribute("masterBean");
String quit=MD.toMD5("quit");
String message=(String)request.getAttribute("message");
if (message==null)
{message="";}
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    <title>大数据服务入口</title>
    <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE11">
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
<meta http-equiv="keywords" content="">
	<meta http-equiv="description" content="">
	<link rel="stylesheet" type="text/css" href="<%=path%>/css/style.css">
	<link rel="stylesheet" type="text/css" href="<%=path%>/css/job.css">
	<script type="text/javascript" charset="utf-8" src="<%=basePath%>/ueditor/ueditor.config.js"></script>
    <script type="text/javascript" charset="utf-8" src="<%=basePath%>/ueditor/ueditor.all.min.js"> </script>
    <script type="text/javascript" charset="utf-8" src="<%=basePath%>/ueditor/lang/zh-cn/zh-cn.js"></script>
	<script src="<%=path%>/js/esl.js"></script>
	<script src="js/jquery-1.11.2.js"></script>
  </head>
  <body>
    
<%
String Add=MD.toMD5("Add");
String getAll=MD.toMD5("getAll");
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
 
   <div class='fb_job'>
   <div class='result'>
        <%=message%>
   </div>
   <form id='form_tijiao' method="post" action="/FoolAlgorithm/ExampleService?action=<%=Add%>">
   <table class="altrowstable" id="alternatecolor" width=80%>
   <tr><td align="right">题目</td><td align="left"><input type="text" name="example_title" class="example_title" value=''></td></tr>
    <tr><td align="right">内容</td><td align="left">
    <textarea  rows="30" cols="90" name="example_content" id="compny_desc" value=''>
    </textarea></td></tr>
    </table>
    <input type="text" name="anliId" id="anliId" value='1' style="display:none"> 
    <div class='tijiao_submmit'>
          <input class="example_logging" value="提     交" type="submit"/>
    </div>
    </form>
   </div>
<script>
                   var editor = new UE.ui.Editor({initialFrameWidth:1000,initialFrameHeight:500}); 
                   editor.render('compny_desc');                                      
</script>
   
    
 
 </body>

</html>
