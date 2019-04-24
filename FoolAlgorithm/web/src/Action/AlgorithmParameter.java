package Action;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.LineNumberReader;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.File; 
 

/**
 * Servlet implementation class AlgorithmParameter
 */
@WebServlet("/AlgorithmParameter")
public class AlgorithmParameter extends HttpServlet {
	
	// 文件存储目录
    private static final String UPLOAD_DIRECTORY = "AlgorithmUpload";
    
	protected void doPost(HttpServletRequest request,
	        HttpServletResponse response) throws ServletException, IOException {
		
		//获取上传文件的文件名
		String dataPath = request.getParameter("filePath");
		String fileName = dataPath.substring(17, dataPath.length());
		//System.out.println("****************"+fileName);
		
		String column = request.getParameter("column");
		//System.out.println(column);
		String ratio = request.getParameter("ratio");
		//System.out.println(ratio);
		String dim_reduce = request.getParameter("dim_reduce");
		//System.out.println(dim_reduce);
		String dims = request.getParameter("dims");
		//System.out.println(dims);
		
		Map<String, String[]> par = new HashMap<String, String[]>();
		
		
		
		String GBDT = request.getParameter("GBDT");
		//System.out.println(GBDT);
		if (GBDT!=null)
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
			par.put(GBDT, GBDT_par);
		}
		
		String RF = request.getParameter("RF");
		//System.out.println(RF);
		if (RF!=null)
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
			par.put(RF, RF_par);
		}
		
		String SVM = request.getParameter("SVM");
		//System.out.println(LR);
		if (SVM!=null)
		{
			String SVM_par[] = new String[3];
			String 	kernel = request.getParameter("kernel");
			SVM_par[0]="Model__kernel,"+ kernel;
			String gamma = request.getParameter("gamma");
			SVM_par[1]="Model__gamma,"+gamma;
			String C = request.getParameter("C");
			SVM_par[2]="Model__C,"+C;
			par.put(SVM, SVM_par);
		}
		
		String MLPC = request.getParameter("MLPC");
		//System.out.println(LR);
		if (MLPC!=null)
		{
			String LR_par[] = new String[9];
			String 	solver = request.getParameter("solver");
			LR_par[0]="Model__solver,"+ solver;
			String alpha = request.getParameter("alpha");
			LR_par[1]="Model__alpha,"+alpha;
			String hidden_layer_sizes = request.getParameter("hidden_layer_sizes");
			LR_par[2]="Model__hidden_layer_sizes,"+hidden_layer_sizes;
			String activation = request.getParameter("activation");
			LR_par[3]="Model__activation,"+activation;
			String learning_rate = request.getParameter("learning_rate");
			LR_par[4]="Model__learning_rate,"+learning_rate;
			String batch_size = request.getParameter("batch_size");
			LR_par[5]="Model__batch_sizer,"+batch_size;
			String learning_rate_init = request.getParameter("learning_rate_init");
			LR_par[6]="Model__learning_rate_init,"+learning_rate_init;
			String max_iter = request.getParameter("max_iter");
			LR_par[7]="Model__max_iter,"+max_iter;
			String shuffle = request.getParameter("shuffle");
			LR_par[8]="Model__shuffle,"+shuffle;
			par.put(MLPC, LR_par);
		}
		
		String AdaBoost = request.getParameter("AdaBoost");
		//System.out.println(LR);
		if (AdaBoost!=null)
		{
			String LR_par[] = new String[5];
			String 	base_estimator = request.getParameter("base_estimator");
			LR_par[0]="Model__base_estimator,"+ base_estimator;
			String n_estimators = request.getParameter("n_estimators");
			LR_par[1]="Model__n_estimators,"+n_estimators;
			String learning_rate = request.getParameter("learning_rate");
			LR_par[2]="Model__learning_rate,"+learning_rate;
			String algorithm = request.getParameter("algorithm");
			LR_par[3]="Model__algorithm,"+algorithm;
			String random_state = request.getParameter("random_state");
			LR_par[4]="Model__random_state,"+random_state;
			par.put(AdaBoost, LR_par);
		}
		
		String Bagging = request.getParameter("Bagging");
		//System.out.println(LR);
		if (Bagging!=null)
		{
			String LR_par[] = new String[4];
			String 	base_estimator = request.getParameter("base_estimator");
			LR_par[0]="Model__base_estimator,"+ base_estimator;
			String n_estimators = request.getParameter("n_estimators");
			LR_par[1]="Model__n_estimators,"+n_estimators;
			String max_samples = request.getParameter("max_samples");
			LR_par[2]="Model__max_samples,"+max_samples;
			String max_features = request.getParameter("max_features");
			LR_par[3]="Model__max_features,"+max_features;
			par.put(Bagging, LR_par);
		}
		
		String KNN = request.getParameter("KNN");
		//System.out.println(LR);
		if (KNN!=null)
		{
			String LR_par[] = new String[4];
			String 	n_neighbors = request.getParameter("n_neighbors");
			LR_par[0]="Model__n_neighbors,"+ n_neighbors;
			String weights = request.getParameter("weights");
			LR_par[1]="Model__weights,"+weights;
			String algorithm = request.getParameter("algorithm");
			LR_par[2]="Model__algorithm,"+algorithm;
			String leaf_size = request.getParameter("leaf_size");
			LR_par[3]="Model__leaf_size,"+leaf_size;
			par.put(KNN, LR_par);
		}
		
		String GNB = request.getParameter("GNB");
		//System.out.println(LR);
		if (GNB!=null)
		{
			String LR_par[] = new String[1];
			String 	priors = request.getParameter("priors");
			LR_par[0]="Model__priors,"+ priors;
			par.put(GNB, LR_par);
		}
		
		String DT = request.getParameter("DT");
		//System.out.println(LR);
		if (DT!=null)
		{
			String LR_par[] = new String[10];
			String 	criteria = request.getParameter("criteria");
			LR_par[0]="Model__criteria,"+ criteria;
			String splitter = request.getParameter("splitter");
			LR_par[1]="Model__splitter,"+splitter;
			String max_depth = request.getParameter("max_depth");
			LR_par[2]="Model__max_depth,"+max_depth;
			String min_samples_split = request.getParameter("min_samples_split");
			LR_par[3]="Model__min_samples_split,"+min_samples_split;
			String min_samples_leaf = request.getParameter("min_samples_leaf");
			LR_par[4]="Model__min_samples_leaf,"+min_samples_leaf;
			String min_weight_fraction_leaf = request.getParameter("min_weight_fraction_leaf");
			LR_par[5]="Model__min_weight_fraction_leaf,"+min_weight_fraction_leaf;
			String max_features = request.getParameter("max_features");
			LR_par[6]="Model__max_features,"+max_features;
			String random_state = request.getParameter("random_state");
			LR_par[7]="Model__random_state,"+random_state;
			String max_leaf_nodes = request.getParameter("max_leaf_nodes");
			LR_par[8]="Model__max_leaf_nodes,"+max_leaf_nodes;
			String min_impurity_decrease = request.getParameter("min_impurity_decrease");
			LR_par[9]="Model__min_impurity_decrease,"+min_impurity_decrease;
			par.put(DT, LR_par);
		}
		
		String MNB = request.getParameter("MNB");
		//System.out.println(LR);
		if (MNB!=null)
		{
			String LR_par[] = new String[1];
			String 	alpha= request.getParameter("alpha");
			LR_par[0]="Model__alpha,"+ alpha;
			par.put(MNB, LR_par);
		}
		
		String BNB = request.getParameter("BNB");
		//System.out.println(LR);
		if (BNB!=null)
		{
			String LR_par[] = new String[1];
			String 	alpha= request.getParameter("alpha");
			LR_par[0]="Model__alpha,"+ alpha;
			par.put(BNB, LR_par);
		}
		
		
		//通过文件的方式把参数传递给python
		dataPath =  getServletContext().getRealPath("./") + File.separator + UPLOAD_DIRECTORY + File.separator + dataPath;
		String line = dataPath + "," + column + "," + ratio + "," + dim_reduce + "," + dims;
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
		if (fileName.indexOf(".") > 0)
		{
			parametersPath2 = fileName.substring(0, fileName.length()-4);
		}else
		{
			parametersPath2 = fileName;
		}
		
		ParsingFile PF= new ParsingFile();
		//System.out.println("**************");
		PF.TextWrite(line, parametersPath1+parametersPath2+".txt");
		
		//调用python
		System.out.println("开始调用python！");
		
		//System.out.println(parametersPath1+parametersPath2+".txt");
		Process pr = Runtime.getRuntime().exec("E:\\Python2.7\\python E:\\pycharm_project\\FA_test\\ChangeAlgorithm.py "+parametersPath1+" "+parametersPath2); 
		InputStreamReader ir = new InputStreamReader(pr.getInputStream());
        LineNumberReader input = new LineNumberReader(ir);
        String p_result = input.readLine();
        System.out.println("**************###########"+p_result);
        input.close();
        ir.close();
        
		System.out.println("调用结束！");
		
		 boolean tag = false;
		 String resultName = "Re_"+ tString+ parametersPath2+".txt";
		 //System.out.println(resultName);
		 while(!tag)
	        {
	        	tag = PF.getFileName("E:\\workplace\\.metadata\\.me_tcat85\\webapps\\FoolAlgorithm\\AlgorithmUpload", resultName);
	        }
	        
	       if (tag == true)
	       {
	    	  //获取python的运行结果
	   		  String readPath = "E:\\workplace\\.metadata\\.me_tcat85\\webapps\\FoolAlgorithm\\AlgorithmUpload\\" + resultName;
	   		  System.out.println("开始读文件！");
	           String[] result = PF.TextRead2(readPath);
	           //System.out.println(result);
	           request.setAttribute("result", result);
	           //request.setAttribute("par_result", par_result);
	    	// 跳转到 message.jsp
	           getServletContext().getRequestDispatcher("/AlgorithmResult.jsp").forward(
	                   request, response);
	       }
	}
    
}
