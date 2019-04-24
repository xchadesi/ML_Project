package com.service;


import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Properties;
import javax.mail.Message;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.dao.JobDao;
import com.dao.LoginDao;
import com.domain.User;
import com.utils.MD5;
import com.utils.MyTools;

public class LoginService extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		this.doGet(request, response);
	}
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		String action=request.getParameter("action");
		MD5 MD=new MD5();
		String tologin=MD.toMD5("toLogin");
		String login=MD.toMD5("login");
		String forget=MD.toMD5("forget");
		String getpwd=MD.toMD5("getpwd");
		String Jihuologin=MD.toMD5("Jihuologin");
		String quit=MD.toMD5("quit");
		if(action.equals(tologin))
			this.toLogin(request, response);
		if(action.equals(login))
			this.loginCheck(request, response);                            
		if(action.equals("islogin"))
			this.isLogin(request, response);                              
		if(action.equals(forget))                                       
			this.forget(request, response);
		if(action.equals(getpwd))                                       
			this.getPwd(request, response);
		if(action.equals(Jihuologin))                                       
				this.Jihuologin(request, response);
		if(action.equals(quit))                                       
			this.logout(request, response);
  
	}
		
	/**
	 * @用户退出
	 */
	public void logout(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
		HttpSession session=request.getSession();
		session.removeAttribute("masterBean");
		RequestDispatcher rd=request.getRequestDispatcher("/index.jsp");
		rd.forward(request,response);
	}
	
	/**
	 * @激活账号
	 */
	public void Jihuologin(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
		 String name=request.getParameter("name");
		 String pwd=request.getParameter("pwd");
		 System.out.println(name+pwd);
		 if(name==null||name.equals(""))                                     
		 {   
			 request.setAttribute("messages","<span>注册名称<b>不能为空！</b></span>");
			 request.getRequestDispatcher("/Jihuo.jsp").forward(request, response);
		 }else if(pwd==null||pwd.equals(""))                                  
		 {   
			 request.setAttribute("messages","<span>注册密码 <b>不能为空！</b></span>");
			 request.getRequestDispatcher("/Jihuo.jsp").forward(request, response);
		 }else	 
		 {
			 MD5 md5=new MD5();
			 String[]s={md5.toMD5(MyTools.toChinese(pwd)),MyTools.toChinese(name)};
			 String[]ss={MyTools.toChinese(name),md5.toMD5(MyTools.toChinese(pwd))};
			 if(new LoginDao().UpdateMaster(s))
			 {
				 User masterBean=new LoginDao().getMaster(ss);                                                      
			     HttpSession session=request.getSession();
			     session.setAttribute("masterBean", masterBean);  
				 response.sendRedirect("/FoolAlgorithm/index.jsp");                         
			 }else {
				 request.setAttribute("messages","<span> <b>账号已激活！</b></span>");
				 request.getRequestDispatcher("/Jihuo.jsp").forward(request, response);
			}
		 }
	}

	/**
	 * @前往激活页面
	 */
	public void Jihuo(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
		
		RequestDispatcher rd=request.getRequestDispatcher("/Jihuo.jsp");
		rd.forward(request,response);
	}
	
	/**
	 * @找回密码
	 */
	public void getPwd(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
		String name=request.getParameter("name");
		String mail=request.getParameter("mail");
		if(name==null||name.equals(""))                                     
		 {   
			 request.setAttribute("messages","<span>注册名称不能为空！</b></span>");
			 request.getRequestDispatcher("/Forget.jsp").forward(request, response);
		 }else if(mail==null||mail.equals(""))                                  
		 {   
			 request.setAttribute("messages","<span>注册邮箱 <b>不能为空！</b></span>");
			 request.getRequestDispatcher("/Forget.jsp").forward(request, response);
		 }
		 else{
			 String[]s={MyTools.toChinese(name),MyTools.toChinese(mail)};
			 User masterBean=new LoginDao().getPwd(s);
			 if(masterBean.getUserName().equals(""))                       
			 {
				 request.setAttribute("messages","<span>这个用户名还没有注册！</span>"); 
				 request.getRequestDispatcher("/Forget.jsp").forward(request,response);
			 }else {                                                         
				   if(MyTools.validateEmail(masterBean.getMail()))
				   {
					   this.toMail(masterBean, request, response);
				   }else {
					   request.setAttribute("messages","<span>输入的邮箱无效！</span>"); 
					   request.getRequestDispatcher("/Forget.jsp").forward(request,response);
				}
				 
			}
		 }
		
	}
	
	/**
	 * @邮箱找回密码
	 */
	
	public void toMail(User user,HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
	{
		try {
			String smtphost = "smtp.163.com"; 
			String mailuser = "dataanswer"; // 
			String password = "xuchao123456"; // 
			
			String from = "dataanswer@163.com";  
			String to = user.getMail(); 
			String subject ="DataAnswer用户名密码找回"; 
		
			String body =user.getUserName()+"感谢使用DataAnswer傻瓜式预测算法工具，点击下面链接进行密码找回：<br>" +
					"<h3><a href='http://www.dataanswer.cn/ToJihuo.jsp'>DataAnswer找回密码</a></h3><br>"; 
			   
			Properties props = new Properties();
			props.put("mail.smtp.host", smtphost);
			props.put("mail.smtp.auth", "true");
		    response.setContentType("text/html;charset=utf-8");
		    PrintWriter out = response.getWriter();
			Session ssn = Session.getInstance(props, null);
			MimeMessage message = new MimeMessage(ssn);
			InternetAddress fromAddress = new InternetAddress(from);
			message.setFrom(fromAddress);
			InternetAddress toAddress = new InternetAddress(to);
			message.addRecipient(Message.RecipientType.TO,toAddress);
			message.setSubject(subject);
		    message.setContent(body,
                    "text/html;charset=utf-8" );
		    message.saveChanges();     
			Transport transport = ssn.getTransport("smtp");
			transport.connect(smtphost,mailuser,password);
			transport.sendMessage(message, message.getAllRecipients());
			transport.close();
		    } catch (Exception e) {
			e.printStackTrace();
			}
		request.setAttribute("messages","<span><b>请前往注册邮箱进行激活！</b></span>");
		RequestDispatcher rd=request.getRequestDispatcher("/Jihuo.jsp");
		rd.forward(request,response);
	}
	
	
	/**
	 * @忘记密码
	 */
	public void forget(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
		RequestDispatcher rd=request.getRequestDispatcher("/Forget.jsp");
		rd.forward(request,response);
	}
	
	/**
	 * @前去登录
	 */
	public void toLogin(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
		RequestDispatcher rd=request.getRequestDispatcher("/Login.jsp");
		rd.forward(request,response);
	}	
	
	/**
	 * @判断用户是否登录
	 */
	public void isLogin(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException 
			{
		        User mBean=(User)request.getSession().getAttribute("masterBean");
		        if(mBean==null)
		        {
		        	request.getRequestDispatcher("/Login.jsp").forward(request, response);
		        }else {
		        	request.getRequestDispatcher("/Ques.jsp").forward(request, response);
				}
			}
	
	
	/**
	 * @登录验证
	 */
	public void loginCheck(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException 
	{
		 String name=request.getParameter("name");
		 String pwd=request.getParameter("pwd");
		 if(name==null||name.equals(""))                                     
		 {   
			 request.setAttribute("messages","<span>登录用户名 <b>不能为空！</b></span>");
			 request.getRequestDispatcher("/Login.jsp").forward(request, response);
		 }else if(pwd==null||pwd.equals(""))                                  
		 {   
			 request.setAttribute("messages","<span>登录密码<b>不能为空！</b></span>");
			 request.getRequestDispatcher("/Login.jsp").forward(request, response);
		 }else	 
		 {
			 MD5 md5=new MD5();
			 String[]s={MyTools.toChinese(name),md5.toMD5(pwd)};
			 User masterBean=new LoginDao().getMaster(s);
			 if(masterBean.getUserName().equals(""))                        
			 {
				 request.setAttribute("messages","<span>您输入的用户名称或密码有误！</span>"); 
				 request.getRequestDispatcher("/Login.jsp").forward(request,response);
			 }else {                                                         
				     HttpSession session=request.getSession();
				     session.setAttribute("masterBean", masterBean);  
				     response.sendRedirect("/FoolAlgorithm/index.jsp");
			}
		 }
		 
		 
	}
}
