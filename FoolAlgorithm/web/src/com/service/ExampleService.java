package com.service;

import java.io.IOException;
import java.util.ArrayList;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import com.dao.ExampleDao;
import com.domain.Example;
import com.domain.User;
import com.utils.MD5;
import com.utils.MyTools;

public class ExampleService extends HttpServlet {
	
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		this.doPost(request, response);
	}
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		String action=request.getParameter("action");
		MD5 MD=new MD5();
		String getAll=MD.toMD5("getAll");
		String ExampleInfo=MD.toMD5("ExampleInfo");
		String fanye=MD.toMD5("fanye");
		String Add=MD.toMD5("Add");
		if(action.equals(getAll))
			this.getAll(request, response);
		if(action.equals(ExampleInfo))
			this.getExampleInfo(request, response);
		if(action.equals(fanye))
			this.toFanYe(request, response);
		if(action.equals(Add))
			this.AddExample(request, response);
	}
	
	public void AddExample(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException 
	{
		String title=request.getParameter("example_title");
		String content=request.getParameter("example_content");
		User mBean=(User)request.getSession().getAttribute("masterBean");
		Example al=new Example();
			al.setTitle(MyTools.toChinese(title));
			al.setContent(MyTools.toChinese(content));
			al.setUname(mBean.getUserName());
			if(new ExampleDao().operatExample("add",al))
			{
				String message = "发布成功！";
				request.setAttribute("message",message);
				response.sendRedirect("/FoolAlgorithm/AddExample.jsp");
			}
	}
	
	public void toFanYe(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
	{
		String pagenow=request.getParameter("pagenow");
		request.setAttribute("pagenow",pagenow);
		ArrayList al=new ExampleDao().getAllExample();
		request.setAttribute("AllExample",al);
		request.getRequestDispatcher("/Example.jsp").forward(request, response);
	}
	
		public void getExampleInfo(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException 
		{
			String ExampleId=request.getParameter("ExampleId");
			ArrayList al=new ExampleDao().getExample(ExampleId);
			request.setAttribute("ExampleInfo",al);
			request.getRequestDispatcher("/ExampleInfo.jsp").forward(request, response);
		}
	
	public void getAll(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException 
	{
		ArrayList al=new ExampleDao().getAllExample();
		request.setAttribute("AllExample",al);
		System.out.print("**********************"+al.size());
		request.getRequestDispatcher("/Example.jsp").forward(request, response);
	}

}

