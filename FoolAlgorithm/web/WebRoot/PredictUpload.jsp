<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title></title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="header">
  <div class='header1'>
  <img src="image/logo.PNG"  alt="DataAnswer"/>
  </div>
  <div class='header2'>
     <div class='header_nav1'><a href="/FoolAlgorithm/index.jsp">首页</a></div>
     <div class='header_nav2'><a href="/FoolAlgorithm/Login.jsp">分析案例</a></div>
     <div class='header_nav3'><a href="/FoolAlgorithm/T.jsp">知识图谱</a></div>
      <div class='header_nav4'><a href="/FoolAlgorithm/Job.jsp">数据招聘</a></div>
      <div class='header_nav5'><a href="/FoolAlgorithm/Login.jsp">登录</a>
      &nbsp;&nbsp;<a href="/FoolAlgorithm/Register.jsp">注册</a></div>
  </div>
  </div>
  <div class="nav_info">确定算法、确定维度下的结果预测<br></div>
  <div class="nav">
  <div class="nav_load">上传训练集：<br><br>上传测试集：</div>
  <div class="nav_load_action">
    <form method="post" action="/FoolAlgorithm/PredictUpload" enctype="multipart/form-data">
    <input type="file" name="upload_Predict_File" />
    <br/><br/>
    <input type="file" name="upload_Train_File" />
    <br/><br/>
    <input type="submit" value="上传" /> 
</form>
  </div>
  </div>
  <div class="radar"></div>
  </body>
</html>
