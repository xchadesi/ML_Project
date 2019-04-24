<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ page import="java.awt.Font,java.awt.Rectangle,java.io.File,java.io.IOException,org.jfree.chart.ChartFactory,org.jfree.chart.ChartFrame,org.jfree.chart.ChartUtilities,org.jfree.chart.JFreeChart,org.jfree.chart.axis.CategoryAxis,
    org.jfree.chart.axis.NumberAxis,org.jfree.chart.axis.NumberTickUnit,org.jfree.chart.labels.StandardCategoryItemLabelGenerator,
    org.jfree.chart.plot.CategoryPlot,org.jfree.chart.plot.PlotOrientation,org.jfree.chart.renderer.category.LineAndShapeRenderer,
    org.jfree.data.category.DefaultCategoryDataset,org.jfree.chart.servlet.ServletUtilities
    " %>
<%@ page import="java.awt.Color"%>
<%@ page import="java.awt.Paint"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    <title>My JSP 'SetParameters.jsp' starting page</title>
    <link rel="stylesheet" href="css/style.css">
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
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
    <%
    String[] result =(String[]) request.getAttribute("result");
     ArrayList par_result =new ArrayList();
    DefaultCategoryDataset dataset = new DefaultCategoryDataset();
     int len = result.length;
     for (int j = 0; j <len ; j++) {
        System.out.println(result[j]);
        String[] pars = result[j].split("\\*");
        par_result.add(pars);
        String[] ps = pars[pars.length-1].split(",");
        //System.out.println(pars[pars.length-1]);
        dataset.addValue(Double.valueOf(ps[1]).doubleValue(), " ", ps[0]);
     }
   
    JFreeChart chart = ChartFactory.createLineChart("不同算法搜索到的最优AUC值比较", // 主标题的名称
            "算法",// X轴的标签
            "AUC值",// Y轴的标签
            dataset, // 图标显示的数据集合
            PlotOrientation.VERTICAL, // 图像的显示形式（水平或者垂直）
            true,// 是否显示子标题
            true,// 是否生成提示的标签
            true); // 是否生成URL链接
    // 处理图形上的乱码
    // 处理主标题的乱码
    chart.getTitle().setFont(new Font("宋体", Font.BOLD, 20));
    chart.getTitle().setPaint(Color.WHITE);
    
    // 获取图表区域对象
    CategoryPlot categoryPlot = (CategoryPlot) chart.getPlot();
    // 获取X轴的对象
    CategoryAxis categoryAxis = (CategoryAxis) categoryPlot.getDomainAxis();
    categoryAxis.setMaximumCategoryLabelLines(2);
    categoryAxis.setLabelPaint(Color.white);
    categoryAxis.setTickLabelPaint(Color.white);
    // 获取Y轴的对象
    NumberAxis numberAxis = (NumberAxis) categoryPlot.getRangeAxis();
    numberAxis.setLabelPaint(Color.white);
    numberAxis.setTickLabelPaint(Color.white);
    // 处理X轴上的乱码
    categoryAxis.setTickLabelFont(new Font("Times New Roman", Font.BOLD, 13));
    // 处理X轴外的乱码
    categoryAxis.setLabelFont(new Font("宋体", Font.BOLD, 16));
    // 处理Y轴上的乱码
    numberAxis.setTickLabelFont(new Font("宋体", Font.BOLD, 16));
    // 处理Y轴外的乱码
    numberAxis.setLabelFont(new Font("宋体", Font.BOLD, 16));
    //处理Y轴上显示的刻度，以10作为1格
    numberAxis.setAutoTickUnitSelection(false);
    NumberTickUnit unit = new NumberTickUnit(0.1);
    numberAxis.setTickUnit(unit);
    // 获取绘图区域对象
    LineAndShapeRenderer lineAndShapeRenderer = (LineAndShapeRenderer) categoryPlot
            .getRenderer();
    // 在图形上显示数字
    lineAndShapeRenderer
            .setBaseItemLabelGenerator(new StandardCategoryItemLabelGenerator());
    lineAndShapeRenderer.setBaseItemLabelsVisible(true);
    lineAndShapeRenderer
            .setBaseItemLabelFont(new Font("宋体", Font.BOLD, 12));
    lineAndShapeRenderer.setItemLabelPaint(Color.white);  
    // 在图形上添加转折点（使用小矩形显示）
    Rectangle shape = new Rectangle(5, 5);
    lineAndShapeRenderer.setSeriesShape(0, shape);
    lineAndShapeRenderer.setSeriesShapesVisible(0, true);
    lineAndShapeRenderer.setSeriesPaint(0, Color.green);
    
    CategoryPlot mPlotline = (CategoryPlot)chart.getPlot();  
    //mPlotline.setRangeGridlinePaint(Color.BLUE);//背景底部横虚线  
    mPlotline.setOutlinePaint(Color.RED);//边界线  
    Paint p=Color.decode("#629DE8");
    chart.setBackgroundPaint(p);
    mPlotline.setBackgroundPaint(p); 

    String fileName = "";
    try {
        fileName = ServletUtilities.saveChartAsPNG(chart, 700, 450, null, session);
    } catch (IOException e) {
        e.printStackTrace();
    }
    String URL =  request.getContextPath() + "/DisplayChart?filename=" + fileName;
    %>
      
     <img src="<%= URL %>" width="700px" height="450px" style="margin-top:2em;display:block;margin-left:auto;margin-right:auto">
    
    <%
    for (int i=0; i<par_result.size(); i++)
    {  
    
    %>
    
    <div class='pr_result'>
    <%
          String[] p_re=(String[])par_result.get(i);
        for(int k=0; k<p_re.length; k++){
    %>
    <%=p_re[k] %><br>
        <% 
    }
    %>
    </div>
    <%
    }
     %>
     
  </body>
</html>
