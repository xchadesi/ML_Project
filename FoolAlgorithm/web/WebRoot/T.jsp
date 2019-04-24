<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>  
<head>  
  
<title>数联未来</title>   
   <script src="js/echarts-2.x.js"></script>  
    <script src="js/TreeGraph.js"></script>  
    
   </head>  
  <body>  
   <div style="width:100%;height:100%;">   
  
        <!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->  
               <div id="main" style="width: 100%;height:1600px;">  
                   
               </div>  
             
      <div id='main_1' style="position: relative;height:15px;width: 100%;color:#A52A2A"></div>  
            
 </div>  
    <script type="text/javascript">  
   //data  
    //data=createDatabyHand()  
    var zNodes=[  
    {id:1,pId:0,name:"人工智能",  value: 10, url: "http://localhost:8080/FoolAlgorithm/T.jsp"},  
    
    {id:11,pId:1,name:"概述", value: 10, url: ""},  
    {id:12,pId:1,name:"历史", value: 10, url: ""},  
    {id:13,pId:1,name:"技术", value: 10, url: "http://localhost:8080/FoolAlgorithm/T.jsp"},  
    {id:14,pId:1,name:"应用", value: 10, url: ""},  
    
    {id:21,pId:13,name:"数学基础", value: 10, url: "http://localhost:8080/FoolAlgorithm/t3.jsp"},  
    {id:22,pId:13,name:"计算机基础", value: 10, url: ""},  
    {id:23,pId:13,name:"机器学习", value: 10, url: "http://localhost:8080/FoolAlgorithm/t2.jsp"},  
    {id:24,pId:13,name:"基础服务", value: 10, url: "http://localhost:8080/FoolAlgorithm/t4.jsp"},  
    {id:25,pId:13,name:"研究领域", value: 10, url: "http://localhost:8080/FoolAlgorithm/t5.jsp"},  
    {id:26,pId:13,name:"竞赛服务", value: 10, url: "http://localhost:8080/FoolAlgorithm/t6.jsp"}, 
    {id:27,pId:13,name:"相关技术", value: 10, url: "http://localhost:8080/FoolAlgorithm/t7.jsp"}, 
    {id:28,pId:14,name:"金融", value: 10, url: ""}, 
    {id:29,pId:14,name:"医疗", value: 10, url: ""}, 
    {id:210,pId:14,name:"制造", value: 10, url: ""}, 
    {id:211,pId:14,name:"教育", value: 10, url: ""}, 
    {id:212,pId:14,name:"机器人", value: 10, url: ""},
    {id:213,pId:14,name:"翻译", value: 10, url: ""},
    {id:214,pId:14,name:"仿生", value: 10, url: ""},
    {id:215,pId:14,name:"娱乐", value: 10, url: ""},
    {id:216,pId:14,name:"艺术", value: 10, url: ""},
    {id:217,pId:14,name:"客服", value: 10, url: ""},
    {id:218,pId:12,name:"人工智能诞生", value: 10, url: ""}, 
    {id:219,pId:12,name:"第一波浪潮", value: 10, url: ""}, 
    {id:220,pId:12,name:"第二波浪潮", value: 10, url: ""}, 
    {id:221,pId:12,name:"第三波浪潮", value: 10, url: ""}, 
    ]  
    data=getData(zNodes)  
    var myChart = echarts.init(document.getElementById('main'), 'macarons');  
    createTreeV(myChart,"人工智能图谱",zNodes); 
    
       // 路径配置  
/*require.config({  
    paths : {  
        echarts : 'js/build/dist'  
    }  
}); */  
 var ecConfig = echarts.config;
//var ecConfig = require('echarts/config');  
myChart.on(ecConfig.EVENT.CLICK, focus) ;    




    //实现节点点击事件
            function focus(param) {
            //alert(1111);
            console.log(param);
            var url = "";
            for(var i=0;i<zNodes.length;i++){
                  if(zNodes[i].name==param.data.name){
                           url= zNodes[i].url
                  }
            }
            window.open(url);
                /* var option = myChart.getOption();
                var data = param.data;
                //判断节点的相关数据是否正确
                if (data != null && data != undefined) {
                    if (data.url != null && data.url != undefined) {
                        //根据节点的扩展属性url打开新页面
                        window.open(data.url);
                    }
                } */ 
            }   
  </script>        
  </body>
