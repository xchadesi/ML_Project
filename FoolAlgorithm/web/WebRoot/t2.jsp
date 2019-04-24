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
               <div id="main" style="width: 100%;height:1100px;">  
                   
               </div>  
             
      <div id='main_1' style="position: relative;height:15px;width: 100%;color:#A52A2A"></div>  
            
 </div>  
    <script type="text/javascript">  
   //data  
    //data=createDatabyHand()  
    var zNodes=[  
    
    {id:1,pId:0,name:"人工智能",  value: 10, url: "http://localhost:8080/FoolAlgorithm/T.jsp"},
    {id:13,pId:1,name:"技术", value: 10, url: ""},  
    {id:23,pId:13,name:"机器学习", value: 10, url: "http://localhost:8080/FoolAlgorithm/t2.jsp"},
    {id:312,pId:23,name:"机器学习分类", value: 10, url: ""},
    {id:313,pId:23,name:"机器学习算法", value: 10, url: ""},
    {id:41,pId:313,name:"机器学习基础", value: 10, url: ""},
    {id:42,pId:313,name:"线性模型", value: 10, url: ""},
    {id:43,pId:313,name:"逻辑回归", value: 10, url: ""},
    {id:44,pId:313,name:"决策树模型", value: 10, url: ""},
    {id:45,pId:313,name:"支持向量机", value: 10, url: ""},
    {id:46,pId:313,name:"贝叶斯分类器", value: 10, url: ""},
    {id:47,pId:313,name:"神经网络", value: 10, url: ""},
    {id:48,pId:313,name:"聚类算法", value: 10, url: ""},
    {id:49,pId:312,name:"监督学习", value: 10, url: ""},
    {id:410,pId:312,name:"无监督学习", value: 10, url: ""},
    {id:411,pId:312,name:"强化学习", value: 10, url: ""},
    {id:412,pId:312,name:"迁移学习", value: 10, url: ""},
    
    {id:51,pId:41,name:"特征工程", value: 10, url: ""},
    {id:52,pId:41,name:"模型评估", value: 10, url: ""},
    {id:53,pId:42,name:"线性回归", value: 10, url: ""},
    {id:54,pId:44,name:"DT", value: 10, url: ""},
    {id:55,pId:44,name:"RF", value: 10, url: ""},
    {id:56,pId:44,name:"GBDT", value: 10, url: ""},
    {id:57,pId:44,name:"XGBoost", value: 10, url: ""},
    {id:58,pId:44,name:"AdaBoost", value: 10, url: ""},
    {id:59,pId:44,name:"bagging", value: 10, url: ""},
    {id:510,pId:47,name:"深度学习", value: 10, url: ""},
    {id:511,pId:48,name:"K均值", value: 10, url: ""},
    
    {id:61,pId:510,name:"MLP", value: 10, url: ""},
    {id:62,pId:510,name:"CNN", value: 10, url: ""},
    {id:63,pId:510,name:"RNN", value: 10, url: ""},
    {id:64,pId:510,name:"GAN", value: 10, url: ""},
    
    {id:71,pId:63,name:"LSTM", value: 10, url: "http://www.baidu.com"},
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
