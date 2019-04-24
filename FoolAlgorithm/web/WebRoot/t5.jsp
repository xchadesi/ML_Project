<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>  
<head>  
  <meta charset="UTF-8">  
<title>数联未来</title>   
   <script src="js/echarts-2.x.js"></script>  
    <script src="js/TreeGraph.js"></script>  
    
   </head>  
  <body>  
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->  
   <div style="width:100%;height:100%;">   
  
        <!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->  
               <div id="main" style="width: 100%;height:700px;">  
                   
               </div>  
             
      <div id='main_1' style="position: relative;height:15px;width: 100%;color:#A52A2A"></div>  
            
 </div>  
    <script type="text/javascript">  
   //data  
    //data=createDatabyHand()  
    var zNodes=[  
    {id:1,pId:0,name:"人工智能",  value: 10, url: "http://localhost:8080/FoolAlgorithm/T.jsp"},  
    
    {id:13,pId:1,name:"技术", value: 10, url: ""},  
 
    {id:25,pId:13,name:"研究领域", value: 10, url: ""},  
   
    {id:320,pId:25,name:"语义识别", value: 10, url: ""},
    {id:321,pId:25,name:"语音识别", value: 10, url: ""},
    {id:322,pId:25,name:"字符识别", value: 10, url: ""},
    {id:323,pId:25,name:"计算机视觉", value: 10, url: ""},
    {id:324,pId:25,name:"自动控制", value: 10, url: ""},
    {id:325,pId:25,name:"人机对弈", value: 10, url: ""},
    {id:326,pId:25,name:"数据挖掘", value: 10, url: ""},
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
</html>
