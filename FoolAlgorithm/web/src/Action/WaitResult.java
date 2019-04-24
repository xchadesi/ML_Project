package Action;

import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.LineNumberReader;
import java.io.PrintWriter;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.HashMap;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class WaitResult
 */
@WebServlet("/WaitResult")
public class WaitResult extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private static final String UPLOAD_DIRECTORY = "PredictUpload";
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        // 设置刷新自动加载的事件间隔为 5 秒
        response.setIntHeader("Refresh", 5);
     
        // 设置响应内容类型
        response.setContentType("text/html;charset=UTF-8");
     
        // 获取当前的时间
        Calendar calendar = new GregorianCalendar();
        String am_pm;
        int hour = calendar.get(Calendar.HOUR);
        int minute = calendar.get(Calendar.MINUTE);
        int second = calendar.get(Calendar.SECOND);
        if(calendar.get(Calendar.AM_PM) == 0)
            am_pm = "AM";
        else
            am_pm = "PM";
     
        String CT = hour+":"+ minute +":"+ second +" "+ am_pm;
        
        PrintWriter out = response.getWriter();
        String title = "正在计算中..........";
        String docType = "<!DOCTYPE html> \n";
        
        
      //获取上传文件的文件名
      		String trainPath = request.getParameter("trainPath");
      		String testPath = request.getParameter("testPath");
      		String testPathName = testPath.substring(17, testPath.length());
      		
      		//System.out.println("****************"+testPathName);
      		
      		String column = request.getParameter("column");
      		//System.out.println(column);
      		String ratio = request.getParameter("ratio");
      		//System.out.println(ratio);
      		String dim_reduce = request.getParameter("dim_reduce");
      		//System.out.println(dim_reduce);
      		String dims = request.getParameter("dims");
      		//System.out.println(dims);
      		
      		Map<String, String[]> par = new HashMap<String, String[]>();
      		
      		
      		
      		String Algorithm = request.getParameter("Algorithm");
      		//System.out.println(Algorithm);
      		if (Algorithm.equals("GBDT"))
      		{
      			String GBDT_par[] = new String[7];
      			String learning_rate = request.getParameter("learning_rate");
      			GBDT_par[0]="Model__learning_rate,"+learning_rate;
      			String n_estimators = request.getParameter("n_estimators");
      			GBDT_par[1]="Model__n_estimators,"+n_estimators;
      			String max_depth = request.getParameter("max_depth");
      			GBDT_par[2]="Model__max_depth,"+max_depth;
      			String min_samples_split = request.getParameter("min_samples_split");
      			GBDT_par[3]="Model__min_samples_split,"+min_samples_split;
      			String min_samples_leaf = request.getParameter("min_samples_leaf");
      			GBDT_par[4]="Model__min_samples_leaf,"+min_samples_leaf;
      			String max_features = request.getParameter("max_features");
      			GBDT_par[5]="Model__max_features,"+max_features;
      			String subsample = request.getParameter("subsample");
      			GBDT_par[6]="Model__subsample,"+subsample;
      			par.put(Algorithm, GBDT_par);
      		}
      		
      		if (Algorithm.equals("RF"))
      		{
      			String RF_par[] = new String[6];
      			String criterion = request.getParameter("criterion");
      			RF_par[0]="Model__criterion,"+ criterion;
      			String n_estimators = request.getParameter("n_estimators1");
      			RF_par[1]="Model__n_estimators,"+n_estimators;
      			String max_depth = request.getParameter("max_depth1");
      			RF_par[2]="Model__max_depth,"+max_depth;
      			String min_samples_split = request.getParameter("min_samples_split1");
      			RF_par[3]="Model__min_samples_split,"+min_samples_split;
      			String min_samples_leaf = request.getParameter("min_samples_leaf1");
      			RF_par[4]="Model__min_samples_leaf,"+min_samples_leaf;
      			String max_features = request.getParameter("max_features1");
      			RF_par[5]="Model__max_features,"+max_features;
      			par.put(Algorithm, RF_par);
      		}
      		
      		if (Algorithm.equals("LR"))
      		{
      			String LR_par[] = new String[11];
      			String 	penalty = request.getParameter("penalty");
      			LR_par[0]="Model__penalty,"+ penalty;
      			String tol = request.getParameter("tol");
      			LR_par[1]="Model__tol,"+tol;
      			String C = request.getParameter("C");
      			LR_par[2]="Model__C,"+C;
      			String fit_intercept = request.getParameter("fit_intercept");
      			LR_par[3]="Model__fit_intercept,"+fit_intercept;
      			String intercept_scaling = request.getParameter("intercept_scaling");
      			LR_par[4]="Model__intercept_scaling,"+intercept_scaling;
      			String solver = request.getParameter("solver");
      			LR_par[5]="Model__solver,"+solver;
      			String max_iter = request.getParameter("max_iter");
      			LR_par[6]="Model__max_iter,"+max_iter;
      			String multi_class = request.getParameter("multi_class");
      			LR_par[7]="Model__multi_class,"+multi_class;
      			String verbose = request.getParameter("verbose");
      			LR_par[8]="Model__verbose,"+verbose;
      			String warm_start = request.getParameter("warm_start");
      			LR_par[9]="Model__warm_start,"+warm_start;
      			String n_jobs = request.getParameter("n_jobs");
      			LR_par[10]="Model__n_jobs,"+n_jobs;
      			par.put(Algorithm, LR_par);
      		}
      		
      		
      		//通过文件的方式把参数传递给python
      		trainPath =  getServletContext().getRealPath("./") + File.separator + UPLOAD_DIRECTORY + File.separator + trainPath;
      		testPath =  getServletContext().getRealPath("./") + File.separator + UPLOAD_DIRECTORY + File.separator + testPath;
      		String line = trainPath +","+ column + "," + ratio + "," + dim_reduce + "," + dims;
      		for (Map.Entry<String, String[]> entry : par.entrySet()) {  
      			  
      			line = line+"*"+entry.getKey()+"#";
      			String[] pars = entry.getValue();
      			for (int j = 0; j < pars.length; j++) {
                      line = line+pars[j]+"#";
                  } 
      			//line = line;
      		}  
      		
      		//System.out.println(line);
      		
      		String pattern = "yyyyMMddHHmmss";  
              SimpleDateFormat df = new SimpleDateFormat(pattern);  
              Date today = new Date();  
              String tString = df.format(today);
      		String parametersPath1 = getServletContext().getRealPath("./") + File.separator + UPLOAD_DIRECTORY + File.separator + "Par_" + tString;
      		String parametersPath2 = "";
      		if (testPathName.indexOf('.') != -1)
      		{
      			parametersPath2 = testPathName.substring(0, testPathName.length()-4);
      		}else
      		{
      			parametersPath2 = testPathName;
      		}
              ParsingFile PF= new ParsingFile();
      		//System.out.println("**************");
      		PF.TextWrite(line, parametersPath1+parametersPath2+".txt");
      		
      		//调用python
      		//System.out.println("开始调用python！"+testPath);
      		Process pr = Runtime.getRuntime().exec("E:\\Python2.7\\python E:\\pycharm_project\\FA_test\\Predict.py "+parametersPath1+" "+parametersPath2 + " " +testPath ); 
      		InputStreamReader ir = new InputStreamReader(pr.getInputStream());
              LineNumberReader input = new LineNumberReader(ir);
              String result = input.readLine();
              //System.out.println("**************"+result);
              input.close();
              ir.close();
      		
      		
      		//System.out.println("调用结束！");
              
      		 boolean tag = false;
      		 String resultName = "Re_"+ tString+ parametersPath2+".csv";
      		 //System.out.println(resultName);
      	        while(!tag)
      	        {
      	        	tag = PF.getFileName("E:\\workplace\\.metadata\\.me_tcat85\\webapps\\FoolAlgorithm\\PredictUpload\\", resultName);
      	        }
      	        
      	       if (tag == true)
      	       {
      	    	  //获取python的运行结果
      	   		  String result_path = resultName;
      	   		  //System.out.println("开始读文件！");
      	           //String[] result = PF.TextRead2(readPath);
      	           //request.setAttribute("result_path", result_path);
      	           //request.setAttribute("Algorithm", Algorithm);
      	    	// 跳转到 message.jsp
      	          // getServletContext().getRequestDispatcher("/PredictResult.jsp").forward(request, response);
      	       }
        
        
      	     out.println(docType +
      	            "<html>\n" +
      	            "<head><title>" + title + "</title></head>\n"+
      	            "<body bgcolor=\"#f0f0f0\">\n" +
      	            "<h1 align=\"center\">" + title + "</h1>\n" +
      	            "<p>当前时间是：" + CT + "</p>\n");
        
    }

}
