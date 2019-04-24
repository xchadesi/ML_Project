<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
String testPath = (String)request.getAttribute("testPath");
String trainPath = (String)request.getAttribute("trainPath");
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>文件上传结果</title>
<link rel="stylesheet" href="css/style.css">
</head>
<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
<script src="http://code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
<style>
   .div{
       width:380px;
       margin-top: 10px;
       line-height:30px;
       border:2px solid #0AF546;}
       
     .div td{
       font-family:"\5FAE\8F6F\96C5\9ED1";
	   font-size: 15px; 
	   color:#FFFFFF;}
</style>

<body>
    <center>
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
 <div id="div_Parameters">
<form method="post" action="/FoolAlgorithm/PredictParameter" name="form">
<input type="text" name="testPath" value=<%=testPath %> style="display:none"/>
<input type="text" name="trainPath" value=<%=trainPath %> style="display:none"/>
<table>
<tr><td class="div_td">选择作为预测变量的列名称：</td>
<td><select name="column" class="div_select">
    <option value='-1'>请选择列名称</option>
    <% 
   String[] message =(String[]) request.getAttribute("message");
   for (int j = 0; j < message.length; j++) { 
    
    %>
	<option value=<%=message[j]%>><%=message[j]%></option>
	<% }%>
	</select></td></tr>
<tr><td class="div_td">选择测试数据的比例：</td>
<td><select name="ratio"  class="div_select">
	<option value='-1'>请选择比例</option>
	<option value='0.1'>0.1</option>
	<option value='0.2'>0.2</option>
	<option value='0.3'>0.3</option>
	<option value='0.4'>0.4</option>
	<option value='0.5'>0.5</option>
	</select></td></tr>
<tr><td class="div_td">降维方法：</td>
<td><select name="dim_reduce" class="div_select">
	<option value='-1'>请选择降维的方法</option>
	<option value='PCA'>PCA</option>
	<option value='Chi2'>Chi2</option>
	<option value='No'>无需选择</option>
	</select>
	<select name="dims" class="div_select">
	<option value='-1'>请选择维数</option>
	<%
	 for (int n = 1; n < message.length-1; n++) { 
	 %>
	<option value=<%=n%>><%=n%></option>
	<%} %>
	</select>
	</td></tr>
<tr><td class="div_td">选择算法：</td>
<td></td></tr>
<tr><td><input type="radio" id="id1" traget="div1" name="Algorithm" value="GBDT">
   <label for="id1" class="div_label">GBDT</label></td>
   <td>
   <div class="div" id="div1" style="display:none">
   <table>
   <tr><td>learning_rate:</td><td><input type="text" name="learning_rate"  value= "0.1" onfocus="javascript:if(this.value=='0.1')this.value='';" onblur="javascript:if(this.value=='')this.value='0.1';"/></td></tr>
   <tr><td>n_estimators:</td><td><input type="text" name="n_estimators"  value= "100" onfocus="javascript:if(this.value=='100')this.value='';" onblur="javascript:if(this.value=='')this.value='100';"/></td></tr>
   <tr><td>max_depth:</td><td><input type="text" name="max_depth"  value= "" onfocus="javascript:if(this.value=='')this.value='';" onblur="javascript:if(this.value=='')this.value='';"/></td></tr>
   <tr><td>min_samples_split:</td><td><input type="text" name="min_samples_split"  value= "2" onfocus="javascript:if(this.value=='2')this.value='';" onblur="javascript:if(this.value=='')this.value='2';"/></td></tr>
   <tr><td>min_samples_leaf:</td><td><input type="text" name="min_samples_leaf"  value= "1" onfocus="javascript:if(this.value=='1')this.value='1';" onblur="javascript:if(this.value=='')this.value='1';"/></td></tr>
   <tr><td>max_features:</td><td><input type="text" name="max_features"  value= "" onfocus="javascript:if(this.value=='')this.value='';" onblur="javascript:if(this.value=='')this.value='';"/></td></tr>
   <tr><td>subsample:</td><td><input type="text" name="subsample"  value= "1.0" onfocus="javascript:if(this.value=='1.0')this.value='';" onblur="javascript:if(this.value=='')this.value='1.0';"/></td></tr>
   </table>
   </div>
   </td></tr>
   
   
<tr><td><input type="radio" id="id2" traget="div2" name="Algorithm" value="RF">
   <label for="id2" class="div_label">RF</label></td>
   <td><div class="div" id="div2" style="display:none">
   <table>
   <tr><td>criterion:</td><td><input type="text" name="criterion"  value= "gini" onfocus="javascript:if(this.value=='gini')this.value='';" onblur="javascript:if(this.value=='')this.value='gini';"/></td></tr>
   <tr><td>n_estimators:</td><td><input type="text" name="n_estimators1"  value= "100" onfocus="javascript:if(this.value=='100')this.value='';" onblur="javascript:if(this.value=='')this.value='100';"/></td></tr>
   <tr><td>max_depth:</td><td><input type="text" name="max_depth1"  value= "" onfocus="javascript:if(this.value=='')this.value='';" onblur="javascript:if(this.value=='')this.value='';"/></td></tr>
   <tr><td>min_samples_split:</td><td><input type="text" name="min_samples_split1"  value= "2" onfocus="javascript:if(this.value=='2')this.value='';" onblur="javascript:if(this.value=='')this.value='2';"/></td></tr>
   <tr><td>min_samples_leaf:</td><td><input type="text" name="min_samples_leaf1"  value= "1" onfocus="javascript:if(this.value=='1')this.value='1';" onblur="javascript:if(this.value=='')this.value='1';"/></td></tr>
   <tr><td>max_features:</td><td><input type="text" name="max_features1"  value= "" onfocus="javascript:if(this.value=='')this.value='';" onblur="javascript:if(this.value=='')this.value='';"/></td></tr>
   </table>
   </div>
   </td></tr>
   
<tr><td><input type="radio" id="id3" traget="div3" name="Algorithm" value="LR">
   <label for="id3" class="div_label">LR</label></td>
   <td><div class="div" id="div3" style="display:none">
   <table>
   <tr><td>penalty:</td><td><input type="text" name="penalty"  value= "l1" onfocus="javascript:if(this.value=='l1')this.value='';" onblur="javascript:if(this.value=='')this.value='l1';"/></td></tr>
   <tr><td>tol:</td><td><input type="text" name="tol"  value= "1e-4" onfocus="javascript:if(this.value=='1e-4')this.value='';" onblur="javascript:if(this.value=='')this.value='1e-4';"/></td></tr>
   <tr><td>C:</td><td><input type="text" name="C"  value= "1.0" onfocus="javascript:if(this.value=='1.0')this.value='';" onblur="javascript:if(this.value=='')this.value='1.0';"/></td></tr>
   <tr><td>fit_intercept:</td><td><input type="text" name="fit_intercept"  value= "1" onfocus="javascript:if(this.value=='1')this.value='1';" onblur="javascript:if(this.value=='')this.value='1';"/></td></tr>
   <tr><td>intercept_scaling:</td><td><input type="text" name="intercept_scaling"  value= "" onfocus="javascript:if(this.value=='')this.value='';" onblur="javascript:if(this.value=='')this.value='';"/></td></tr>
   <tr><td>solver:</td><td><input type="text" name="solver"  value= "liblinear" onfocus="javascript:if(this.value=='liblinear')this.value='';" onblur="javascript:if(this.value=='')this.value='liblinear';"/></td></tr>
   <tr><td>max_iter:</td><td><input type="text" name="max_iter"  value= "100" onfocus="javascript:if(this.value=='100')this.value='';" onblur="javascript:if(this.value=='')this.value='100';"/></td></tr>
   <tr><td>multi_class:</td><td><input type="text" name="multi_class"  value= "ovr" onfocus="javascript:if(this.value=='ovr')this.value='';" onblur="javascript:if(this.value=='')this.value='ovr';"/></td></tr>
   <tr><td>verbose:</td><td><input type="text" name="verbose"  value= "0" onfocus="javascript:if(this.value=='0')this.value='';" onblur="javascript:if(this.value=='')this.value='0';"/></td></tr>
   <tr><td>warm_start:</td><td><input type="text" name="warm_start"  value= "False" onfocus="javascript:if(this.value=='False')this.value='';" onblur="javascript:if(this.value=='')this.value='False';"/></td></tr>
   <tr><td>n_jobs:</td><td><input type="text" name="n_jobs"  value= "1" onfocus="javascript:if(this.value=='1')this.value='';" onblur="javascript:if(this.value=='')this.value='1';"/></td></tr>
   </table>
   </div>
   </td></tr>
<tr><td><input type="radio" id="id4" traget="div4" name="Algorithm" value="SVM">
   <label for="id4" class="div_label">SVM</label></td>
   <td>
   <div class="div" id="div4" style="display:none">
   <table>
   <tr><td>kernel:</td><td><input type="text" name="kernel"  value= "rbf" onfocus="javascript:if(this.value=='rbf')this.value='';" onblur="javascript:if(this.value=='')this.value='rbf';"/></td></tr>
   <tr><td>gamma:</td><td><input type="text" name="gamma"  value= "auto" onfocus="javascript:if(this.value=='auto')this.value='';" onblur="javascript:if(this.value=='')this.value='auto';"/></td></tr>
   <tr><td>C:</td><td><input type="text" name="C"  value= "1.0" onfocus="javascript:if(this.value=='1.0')this.value='';" onblur="javascript:if(this.value=='')this.value='1.0';"/></td></tr>
   </table>
   </div>
   </td></tr>
   
   
<tr><td><input type="radio" id="id5" traget="div5" name="Algorithm" value="MLPC">
   <label for="id5" class="div_label">MLPC</label></td>
   <td>
   <div class="div" id="div5" style="display:none">
   <table>
   <tr><td>solver:</td><td><input type="text" name="solver"  value= "adam" onfocus="javascript:if(this.value=='adam')this.value='';" onblur="javascript:if(this.value=='')this.value='adam';"/></td></tr>
   <tr><td>alpha:</td><td><input type="text" name="alpha"  value= "1e-4" onfocus="javascript:if(this.value=='1e-4')this.value='';" onblur="javascript:if(this.value=='')this.value='1e-4';"/></td></tr>
   <tr><td>hidden_layer_sizes:</td><td><input type="text" name="hidden_layer_sizes"  value= "(100,)" onfocus="javascript:if(this.value=='(100,)')this.value='';" onblur="javascript:if(this.value=='')this.value='(100,)';"/></td></tr>
   <tr><td>activation:</td><td><input type="text" name="activation"  value= "relu" onfocus="javascript:if(this.value=='relu')this.value='';" onblur="javascript:if(this.value=='')this.value='relu';"/></td></tr>
   <tr><td>learning_rate:</td><td><input type="text" name="random_state"  value= "constant" onfocus="javascript:if(this.value=='constant')this.value='';" onblur="javascript:if(this.value=='')this.value='constant';"/></td></tr>
   <tr><td>batch_size:</td><td><input type="text" name="batch_size"  value= "auto" onfocus="javascript:if(this.value=='auto')this.value='';" onblur="javascript:if(this.value=='')this.value='auto';"/></td></tr>
   <tr><td>learning_rate_init:</td><td><input type="text" name="learning_rate_init"  value= "1e-4" onfocus="javascript:if(this.value=='1e-4')this.value='';" onblur="javascript:if(this.value=='')this.value='1e-4';"/></td></tr>
   <tr><td>max_iter:</td><td><input type="text" name="max_iter"  value= "200" onfocus="javascript:if(this.value=='200')this.value='';" onblur="javascript:if(this.value=='')this.value='200';"/></td></tr>
   <tr><td>shuffle:</td><td><input type="text" name="shuffle"  value= "True" onfocus="javascript:if(this.value=='True')this.value='';" onblur="javascript:if(this.value=='')this.value='True';"/></td></tr>
   </table>
   </div>
   </td></tr>
   
<tr><td><input type="radio" id="id6" traget="div6" name="Algorithm" value="AdaBoost">
   <label for="id6" class="div_label">AdaBoost</label></td>
   <td>
   <div class="div" id="div6" style="display:none">
   <table>
   <tr><td>base_estimator:</td><td><input type="text" name="base_estimator"  value= "DecisionTreeClassifier" onfocus="javascript:if(this.value=='DecisionTreeClassifier')this.value='';" onblur="javascript:if(this.value=='')this.value='DecisionTreeClassifier';"/></td></tr>
   <tr><td>n_estimators:</td><td><input type="text" name="n_estimators"  value= "50" onfocus="javascript:if(this.value=='50')this.value='';" onblur="javascript:if(this.value=='')this.value='50';"/></td></tr>
   <tr><td>learning_rate:</td><td><input type="text" name="learning_rate"  value= "1.0" onfocus="javascript:if(this.value=='1.0')this.value='';" onblur="javascript:if(this.value=='')this.value='1.0';"/></td></tr>
   <tr><td>algorithm:</td><td><input type="text" name="algorithm"  value= "SAMME.R" onfocus="javascript:if(this.value=='SAMME.R')this.value='';" onblur="javascript:if(this.value=='')this.value='SAMME.R';"/></td></tr>
   <tr><td>random_state:</td><td><input type="text" name="intercept_scaling"  value= "None" onfocus="javascript:if(this.value=='None')this.value='';" onblur="javascript:if(this.value=='')this.value='None';"/></td></tr>
   </table>
   </div>
   </td></tr>
   
<tr><td><input type="radio" id="id7" traget="div7" name="Algorithm" value="Bagging">
   <label for="id7" class="div_label">Bagging</label></td>
   <td>
   <div class="div" id="div7" style="display:none">
   <table>
   <tr><td>base_estimator:</td><td><input type="text" name="base_estimator"  value= "None" onfocus="javascript:if(this.value=='None')this.value='';" onblur="javascript:if(this.value=='')this.value='None';"/></td></tr>
   <tr><td>n_estimators:</td><td><input type="text" name="n_estimators"  value= "10" onfocus="javascript:if(this.value=='10')this.value='';" onblur="javascript:if(this.value=='')this.value='10';"/></td></tr>
   <tr><td>max_samples:</td><td><input type="text" name="max_samples"  value= "1.0" onfocus="javascript:if(this.value=='1.0')this.value='';" onblur="javascript:if(this.value=='')this.value='1.0';"/></td></tr>
   <tr><td>max_features :</td><td><input type="text" name="max_features "  value= "1.0" onfocus="javascript:if(this.value=='1.0')this.value='';" onblur="javascript:if(this.value=='')this.value='1.0';"/></td></tr>
   </table>
   </div>
   </td></tr>
   
 <tr><td><input type="radio" id="id8" traget="div8" name="Algorithm" value="KNN">
   <label for="id8" class="div_label">KNN</label></td>
   <td>
   <div class="div" id="div8" style="display:none">
   <table>
   <tr><td>n_neighbors:</td><td><input type="text" name="n_neighbors"  value= "5" onfocus="javascript:if(this.value=='5')this.value='';" onblur="javascript:if(this.value=='')this.value='5';"/></td></tr>
   <tr><td>weights:</td><td><input type="text" name="weights"  value= "uniform" onfocus="javascript:if(this.value=='uniform')this.value='';" onblur="javascript:if(this.value=='')this.value='uniform';"/></td></tr>
   <tr><td>algorithm:</td><td><input type="text" name="algorithm"  value= "auto" onfocus="javascript:if(this.value=='auto')this.value='';" onblur="javascript:if(this.value=='')this.value='auto';"/></td></tr>
   <tr><td>leaf_size:</td><td><input type="text" name="leaf_size"  value= "30" onfocus="javascript:if(this.value=='30')this.value='';" onblur="javascript:if(this.value=='')this.value='30';"/></td></tr>
   </table>
   </div>
   </td></tr>
   
<tr><td><input type="radio" id="id9" traget="div9" name="Algorithm" value="GNB">
   <label for="id9" class="div_label">GNB</label></td>
   <td>
   <div class="div" id="div9" style="display:none">
   <table>
   <tr><td>priors:</td><td><input type="text" name="priors"  value= "" onfocus="javascript:if(this.value=='')this.value='';" onblur="javascript:if(this.value=='')this.value='';"/></td></tr>
   </table>
   </div>
   </td></tr>
   
<tr><td><input type="radio" id="id10" traget="div10" name="Algorithm" value="DT">
   <label for="id10" class="div_label">DT</label></td>
   <td>
   <div class="div" id="div10" style="display:none">
   <table>
   <tr><td>criteria:</td><td><input type="text" name="criteria"  value= "gini" onfocus="javascript:if(this.value=='gini')this.value='';" onblur="javascript:if(this.value=='')this.value='gini';"/></td></tr>
   <tr><td>splitter:</td><td><input type="text" name="splitter"  value= "best" onfocus="javascript:if(this.value=='best')this.value='';" onblur="javascript:if(this.value=='')this.value='best';"/></td></tr>
   <tr><td>max_depth:</td><td><input type="text" name="max_depth"  value= "None" onfocus="javascript:if(this.value=='None')this.value='';" onblur="javascript:if(this.value=='')this.value='None';"/></td></tr>
   <tr><td>min_samples_split:</td><td><input type="text" name="min_samples_split"  value= "2" onfocus="javascript:if(this.value=='2')this.value='';" onblur="javascript:if(this.value=='')this.value='2';"/></td></tr>
   <tr><td>min_samples_leaf:</td><td><input type="text" name="min_samples_leaf"  value= "1" onfocus="javascript:if(this.value=='1')this.value='';" onblur="javascript:if(this.value=='')this.value='1';"/></td></tr>
   <tr><td>min_weight_fraction_leaf:</td><td><input type="text" name="min_weight_fraction_leaf"  value= "0" onfocus="javascript:if(this.value=='0')this.value='';" onblur="javascript:if(this.value=='')this.value='0';"/></td></tr>
   <tr><td>max_features:</td><td><input type="text" name="max_features"  value= "None" onfocus="javascript:if(this.value=='None')this.value='';" onblur="javascript:if(this.value=='')this.value='None';"/></td></tr>
   <tr><td>random_state:</td><td><input type="text" name="random_state"  value= "None" onfocus="javascript:if(this.value=='None')this.value='';" onblur="javascript:if(this.value=='')this.value='None';"/></td></tr>
   <tr><td>max_leaf_nodes:</td><td><input type="text" name="max_leaf_nodes"  value= "None" onfocus="javascript:if(this.value=='None')this.value='';" onblur="javascript:if(this.value=='')this.value='None';"/></td></tr>
   <tr><td>min_impurity_decrease:</td><td><input type="text" name="min_impurity_decrease"  value= "0" onfocus="javascript:if(this.value=='0')this.value='';" onblur="javascript:if(this.value=='')this.value='0';"/></td></tr>
   </table>
   </div>
   </td></tr>
   
<tr><td><input type="radio" id="id12" traget="div12" name="Algorithm" value="MNB">
   <label for="id12" class="div_label">MNB</label></td>
   <td>
   <div class="div" id="div12" style="display:none">
   <table>
   <tr><td>alpha:</td><td><input type="text" name="alpha"  value= "" onfocus="javascript:if(this.value=='')this.value='';" onblur="javascript:if(this.value=='')this.value='';"/></td></tr>
   </table>
   </div>
   </td></tr>
   
<tr><td><input type="radio" id="id13" traget="div13" name="Algorithm" value="BNB">
   <label for="id13" class="div_label">BNB</label></td>
   <td>
   <div class="div" id="div13" style="display:none">
   <table>
   <tr><td>alpha:</td><td><input type="text" name="alpha"  value= "" onfocus="javascript:if(this.value=='')this.value='';" onblur="javascript:if(this.value=='')this.value='';"/></td></tr>
   </table>
   </div>
   </td></tr>
</table>


   
 <input class="div_sumbmit" type="submit" value="提交"  onclick="jh()"/>
</form>
</div>
<div id="div_wait" style="display:none">
<h3>正在计算请稍后.........</h3>
</div>
    </center>
</body>
<script>
function jh(){
document.getElementById("div_Parameters").style.display="none";
document.getElementById("div_wait").style.display="";
}
</script>
<script>
  $(function(){
      $("input").bind("click",function(){
          if(this.checked){
                $("#"+$(this).attr("traget")).show();
          }else{
               $("#"+$(this).attr("traget")).hide();
              }
             
          })
      });
</script>

</html>
