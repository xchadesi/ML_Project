package com.dao;

import java.util.ArrayList;

import com.utils.SqlHelper;

public class RegisterDao {

		SqlHelper sqlHelper=null;
		String  sql=null;
		
		public RegisterDao()
		{
			sqlHelper=new SqlHelper();
		}
				

		public boolean toRegister(String[]s)
		{
			boolean b=false;
			String num="";
			String sql="insert into duser values(?,?,?,?)";
			num=(this.queryMaxId()+1)+"";
			if(s.length==3)
			{
				String[]arg={num,s[0],s[1],s[2]};
				b=sqlHelper.executeUpdate(sql, arg);
			}
			return b;
		}
		
		
		public int queryMaxId() {
			int maxId = 0;
			String sql = "select max(UserId) from duser";
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
}
