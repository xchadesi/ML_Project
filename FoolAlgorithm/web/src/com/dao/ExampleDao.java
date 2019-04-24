package com.dao;

import java.util.ArrayList;
import com.domain.Example;
import com.utils.SqlHelper;

public class ExampleDao {

	SqlHelper sqlHelper=null;
	String  sql=null;
	
	public ExampleDao()
	{
		sqlHelper=new SqlHelper();
	}
	
	public boolean operatExample(String oper, Example single) {		
		
		String sql = null;
		boolean flag =false;
		if (oper.equals("add"))					
			{
			  sql = "insert into example values (?,?,?,?)";
			  String id=(this.queryMaxId()+1)+"";
		      String arg[]={id+"",single.getUname(), single.getTitle(),single.getContent()};
		      flag =sqlHelper.executeUpdate(sql,arg);
			}
		return flag;
	}
	
	public int queryMaxId() {
		int maxId = 0;
		String sql = "select max(id) from example";
		String[]arg={};
		ArrayList al = sqlHelper.query(sql, arg);
		if(((Object[])al.get(0))[0]!=null){
			Object[] objects=(Object[]) al.get(0);
			maxId=(Integer) objects[0];
		}else {
			maxId=1;
		}
		return maxId;
	}	
	
	
	
	public ArrayList getExample(String id)
	{
		sql="select id,uname,title,content from example where id=?";
		String[] arg={id};
		ArrayList aList=sqlHelper.query(sql,arg);
		return aList;
	}
	
	
	public ArrayList getAllExample()
	{
		sql="select id,uname,title,content from example order by id desc";
		String[] arg={};
		ArrayList aList=sqlHelper.query(sql,arg);
		return aList;
	}
}

