package com.dao;

import java.util.ArrayList;
import com.utils.SqlHelper;

public class JobDao {

	SqlHelper sqlHelper=null;
	String  sql=null;
	
	public JobDao()
	{
		sqlHelper=new SqlHelper();
	}
	
	public ArrayList getTypeJob(String city)
	{
		sql="select *from job where jobname like '%"+city+"%' or req like '%"+city+"%' order by id desc";
		String[] arg={};
		ArrayList aList=sqlHelper.query(sql,arg);
		return aList;
	}
	
	public ArrayList getJob(String id)
	{
		sql="select id,jobname,req,time from job where id=?";
		String[] arg={id};
		ArrayList aList=sqlHelper.query(sql,arg);
		return aList;
	}
	
	
	public ArrayList getAllJob()
	{
		sql="select id,jobname,req,time from job order by id desc";
		String[] arg={};
		ArrayList aList=sqlHelper.query(sql,arg);
		return aList;
	}
}
