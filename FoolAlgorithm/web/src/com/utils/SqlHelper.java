/**
  * @param args
  * date:2015.12.31
  * function:完成一个操作数据库的工具类
  */
package com.utils;

import java.io.IOException;
import java.io.InputStream;
import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Properties;

public class SqlHelper  {

	//定义需要的变量
    private  Connection ct=null;
    private  PreparedStatement ps=null;
    private  ResultSet rs=null;
    private  Properties pp=null;
    private  InputStream is=null;
	private CallableStatement cs=null;
	
	//连接数据库的参数
    private  String driver=null;
    private  String url=null;
    private  String username=null;
    private  String password=null;
    
	/**
	 *  @功能：加载驱动，只需要一次
	 */
	public SqlHelper()
	{
		try {
			//从配置文件中读取driver
			pp=new Properties();
		    is=SqlHelper.class.getClassLoader().getResourceAsStream("com/utils/dbinfo.properties");
			pp.load(is);
			url=pp.getProperty("url");
			driver=pp.getProperty("driver");
			username=pp.getProperty("username");
			password=pp.getProperty("password");
			Class.forName(driver);
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println("加载数据库驱动失败！");
		}finally
		{ 
			//关闭文件流
			try {
				is.close();
			} catch (IOException e) {
				e.printStackTrace();
				System.out.println("关闭文件流失败！");
			}
		}
	}
	
	
	/**
	 *  @功能：得到连接
	 */
	public  Connection getConnection()
	{
		try {
			
			ct=DriverManager.getConnection(url,username,password);
			
		} catch (SQLException e) {
			e.printStackTrace();
			System.out.println("获取连接失败！");
		}
		return ct;
	}
	
	/**
	 *  @功能：为了达到在那里打开资源就在那里关闭资源，把查询到的结果集封装在一个ArrayList中
	 */
	public  ArrayList query(String sql,String[] parameters)
	{
		ArrayList alList=null;
		//静态中不可以使用this
				ct=getConnection();
				try{
					ps=ct.prepareStatement(sql);
					ct.setAutoCommit(false);
					if(parameters!=null)
					{
						for(int i=0;i<parameters.length;i++)
						{
							ps.setString(i+1,parameters[i]);
						}
					}
					rs=ps.executeQuery();
					ct.commit();//提交事务 
					ct.setAutoCommit(true);
					alList=new ArrayList();
					//可以获取ResultSet列的属性和信息的对象
					ResultSetMetaData rSetMetaData=rs.getMetaData();
					//得到列数
					int cloumn=rSetMetaData.getColumnCount();
					while(rs.next())
					{
						//一个对象数组，代表一行数据
						Object ob[]=new Object[cloumn];
						for(int i=1;i<=cloumn;i++)
						{
							ob[i-1]=rs.getObject(i);//一行所有列的数据都取出来放到ob中
						}
						alList.add(ob);
					}
						
				}catch(Exception e)
				{
					 try {
						ct.rollback();//进行事务回滚  
					} catch (SQLException e1) {
						alList=null;
					} 
					 alList=null;
				}finally
				{
					close(rs, ps, ct);
				}
		return alList;
	}
	
	/**
	 *  @功能：写一个insert/delete/update方法
	 */
	public  boolean executeUpdate(String sql,String[] parameters)
	{
		boolean b=true;
		try {
			ct=getConnection();
			ct.setAutoCommit(false);
			ps=ct.prepareStatement(sql);
			if(parameters!=null)
			{
				for(int i=0;i<parameters.length;i++)
				{
					ps.setString(i+1,parameters[i]);
				}
			}
			ps.executeUpdate();
			ct.commit();//提交事务 
			ct.setAutoCommit(true);
		} catch (Exception e) {
			try {
				ct.rollback();//进行事务回滚  
			} catch (SQLException e1) {
				e1.printStackTrace();
			}
			e.printStackTrace();
			b=false;
			//抛出执行不成功的运行异常,给调用该函数的函数一个选择，可以处理，也可以不处理
			throw new RuntimeException(e.getMessage());	
		}finally
		{
			close(rs,ps,ct);
		}
		return b;
	}
	
	/**
	 *  @功能：//关闭资源
	 */
	public void close(ResultSet rs,PreparedStatement ps,Connection ct )
	{
		if(rs!=null)
		{
			try {
				rs.close();
			} catch (SQLException e) {
				e.printStackTrace();
				System.out.println("关闭rs对象失败！");
			}
		}
		
		if(ps!=null)
		{
			try {
				ps.close();
			} catch (SQLException e) {
				e.printStackTrace();
				System.out.println("关闭ps对象失败！");
			}
		}
		
		if(ct!=null)
		{
			try {
				ct.close();
			} catch (SQLException e) {
				e.printStackTrace();
				System.out.println("关闭ct对象失败！");
			}
		}
	}
	
}
