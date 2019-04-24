package Action;

import java.io.BufferedReader; 
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader; 
import java.io.FileWriter;
import java.io.IOException;

public class ParsingFile { 
	
	
	public boolean  searchFileName(String path, String FileName) {
        File f = new File(path);
        File fa[] = f.listFiles();
        for (int i = 0; i < fa.length; i++) {
            File fs = fa[i];
			 if (fs.getName().equals(FileName)) {
			        return true;
			    }
        }
        return false;
    }
	
	public boolean  getFileName(String path, String FileName) {
        File f = new File(path);
        File fa[] = f.listFiles();
        for (int i = 0; i < fa.length; i++) {
            try {
            	 File fs = fa[i];
                 FileInputStream fis = new FileInputStream(fs);
				 long s= fis.available();
				 if (fs.getName().equals(FileName) && s>0 ) {
		                return true;
		            } 
			} catch (IOException e) {
				e.printStackTrace();
			}
        }
        return false;
    }
	

	public String[] TextRead2(String FileName) { 
    	String item[] = null;
        try { 
            BufferedReader reader = new BufferedReader(new FileReader(FileName));//换成你的文件名
            String line = reader.readLine();//第一行信息，为标题信息，不用，如果需要，注释掉
           // System.out.println(line);
            item = line.split("#");//CSV格式文件为逗号分隔符文件，这里根据逗号切分
        } catch (Exception e) { 
        	item = null;
            e.printStackTrace(); 
        } 
        
        return item;
    } 
	
    public String[] TextRead(String FileName) { 
    	String item[] = null;
        try { 
            BufferedReader reader = new BufferedReader(new FileReader(FileName));//换成你的文件名
            String line = reader.readLine();//第一行信息，为标题信息，不用，如果需要，注释掉
           // System.out.println(line);
            item = line.split(",");//CSV格式文件为逗号分隔符文件，这里根据逗号切分
        } catch (Exception e) { 
        	item = null;
            e.printStackTrace(); 
        } 
        
        return item;
    } 
    
    public void TextWrite(String line, String FileName) { 
    	try { 
			  
			  //System.out.println(FileName);
			  File parameter = new File(FileName); 
	          BufferedWriter bw = new BufferedWriter(new FileWriter(parameter, false)); // 附加
	          // 添加新的数据行
	          bw.write(line); 
	          bw.newLine(); 
	          bw.close(); 
	    
	        } catch (FileNotFoundException e) { 
	          // File对象的创建过程中的异常捕获
	          e.printStackTrace(); 
	        } catch (IOException e) { 
	          // BufferedWriter在关闭对象捕捉异常
	          e.printStackTrace(); 
	        } 
    } 

}

