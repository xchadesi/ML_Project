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
               <div id="main" style="width: 100%;height:900px;">  
                   
               </div>  
             
      <div id='main_1' style="position: relative;height:15px;width: 100%;color:#A52A2A"></div>  
            
 </div>  
    <script type="text/javascript">  
   //data  
    //data=createDatabyHand()  
    var zNodes=[  
    {id:1,pId:0,name:"人工智能",  value: 10, url: "http://localhost:8080/FoolAlgorithm/T.jsp"},  
    
    {id:13,pId:1,name:"技术", value: 10, url: ""},  
    {id:26,pId:13,name:"竞赛服务", value: 10, url: ""}, 
    {id:327,pId:26,name:"Kaggle", value: 10, url: "https://www.kaggle.com/"},
    {id:328,pId:26,name:"阿里天池", value: 10, url: "https://tianchi.aliyun.com"},
    {id:329,pId:26,name:"DataFountain", value: 10, url: "http://dev.wid.org.cn"},
    {id:330,pId:26,name:"datacastle", value: 10, url: "http://www.pkbigdata.com"},
    {id:331,pId:26,name:"Kesci", value: 10, url: "https://www.kesci.com/"},
    {id:332,pId:26,name:"WID", value: 10, url: "http://www.baidu.com"},
    {id:333,pId:26,name:"赛氪", value: 10, url: "http://www.baidu.com"},
    {id:334,pId:26,name:"数睿思", value: 10, url: "http://www.tipdm.org"},
    {id:335,pId:26,name:"数愿", value: 10, url: "http://www.datadreams.org/"},
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
