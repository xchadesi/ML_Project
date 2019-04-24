package com.dao;

import java.util.ArrayList;
import com.domain.User;
import com.utils.SqlHelper;

public class LoginDao {

	
	SqlHelper sqlHelper=null;
	String  sql=null;
	

	public LoginDao()
	{
		sqlHelper=new SqlHelper();
	}
	
	
	
	/**
	 * 
	 */
	
	public Boolean UpdateMaster(String[] s)
	{
		sql="update duser set Passwd=? where UserName=?";
		return sqlHelper.executeUpdate(sql,s);
	}
	
	/**
	 * 
	 */
	public User getPwd(String[] s)
	{
		ArrayList al=null;
		sql="select UserId,UserName,Mail,Passwd from duser where UserName=? and Mail=?";
		al=sqlHelper.query(sql,s);
		User masterBean=new User();
		if(al.size()!=0)            
		{
			Object objects[]=(Object[]) al.get(0);
			masterBean.setUserId((Integer)objects[0]);
		    masterBean.setUserName((String)objects[1]);
		    masterBean.setMail((String)objects[2]);
		    masterBean.setPasswd((String)objects[3]);
		}else                      
		{
			masterBean.setUserName("");
		}
	    
	    return masterBean;
	}
	

			
	/**
	 * 
	 */
	public User getMaster(String[] s)
	{
		ArrayList al=null;
		if(s.length==2)
		{
			sql="select UserId,UserName,Mail,Passwd from duser where UserName=? and Passwd=?";
		    al=sqlHelper.query(sql,s);
		}else if(s.length==1){
			sql="select UserId,UserName,Mail,Passwd from duser";
			String arg[]={};
		    al=sqlHelper.query(sql,arg);
		}
		User masterBean=new User();
		if(al!=null&&al.size()!=0)            
		{
			Object objects[]=(Object[]) al.get(0);
			masterBean.setUserId((Integer)objects[0]);
		    masterBean.setUserName((String)objects[1]);
		    masterBean.setMail((String)objects[2]);
		    masterBean.setPasswd((String)objects[3]);
		}else                      
		{
			masterBean.setUserName("");
		}
	    
	    return masterBean;
	}
	
	
}








