package com.service;


import java.io.IOException;
import java.util.ArrayList;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import com.dao.JobDao;
import com.utils.MD5;

public class JobService extends HttpServlet {
	
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		this.doGet(request, response);
	}
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		String action=request.getParameter("action");
		MD5 MD=new MD5();
		
		String getAll=MD.toMD5("getAll");
		String JobInfo=MD.toMD5("JobInfo");
		String fanye=MD.toMD5("fanye");
		String city_jobtype=MD.toMD5("city_jobtype");
		String choose_fanye=MD.toMD5("choose_fanye");
		if(action.equals(getAll))
			this.getAll(request, response);
		if(action.equals(JobInfo))
			this.getJobInfo(request, response);
		if(action.equals(fanye))
			this.toFanYe(request, response);
		if(action.equals(city_jobtype))
			this.ChooseType(request, response);
		if(action.equals(choose_fanye))
			this.Choose_FanYe(request, response);
		
	}
	
	public void Choose_FanYe(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
	{
		String pagenow=request.getParameter("pagenow");
		request.setAttribute("pagenow",pagenow);
		String city_jobtype=request.getParameter("city_jobtype");
		ArrayList al=new JobDao().getTypeJob(city_jobtype);
		request.setAttribute("ChoseJob",al);
		request.getRequestDispatcher("/ChoseJob.jsp").forward(request, response);
	}
	
	public void ChooseType(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException 
	{
		String city_jobtype=request.getParameter("city_jobtype");
		ArrayList al=new JobDao().getTypeJob(city_jobtype);
		request.setAttribute("ChoseJob",al);
		request.setAttribute("city_job",city_jobtype);
		request.getRequestDispatcher("/ChoseJob.jsp").forward(request, response);
	}
	
	
	public void toFanYe(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
	{
		String pagenow=request.getParameter("pagenow");
		request.setAttribute("pagenow",pagenow);
		ArrayList al=new JobDao().getAllJob();
		request.setAttribute("AllJob",al);
		request.getRequestDispatcher("/Job.jsp").forward(request, response);
	}
	
		public void getJobInfo(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException 
		{
			String jobId=request.getParameter("jobId");
			ArrayList al=new JobDao().getJob(jobId);
			request.setAttribute("JobInfo",al);
			request.getRequestDispatcher("/JobInfo.jsp").forward(request, response);
		}
	
	public void getAll(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException 
	{
		ArrayList al=new JobDao().getAllJob();
		request.setAttribute("AllJob",al);
		request.getRequestDispatcher("/Job.jsp").forward(request, response);
	}

}

