---
date: 2010-10-14 07:49:44
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/3931119/configuring-container-managed-security-in-weblogic
tags:
- security
- weblogic
- questions
- stackoverflow
- software development
title: Configuring container-managed security in Weblogic
---

Anyone know of any guides for this? I'm a complete newbie to weblogic and to container-managed security. What I've done already is:

1. setup an LDAP authenticator in Weblogic
2. created a simple webapp in Eclipse 
3. Configure web.xml: Added security-constraint, security-role and login-config elements. The realm name used is "myrealm" which already exists in Weblogic. The role name I used is "Admin" which is a global role in Weblogic
4. Create a simple jsp page "login.jsp". It doesn't actually do any logging in but just a Hello World type of thing. I set this page as form-login-page and form-error-page in login-config in web.xml
5. Export this webapp to a war file and deploy it in Weblogic
6. I test it by accessing http://weblogic-server/test/login.jsp, and I expect that I'll be asked to login using an LDAP user first. This doesn't happen, it just shows the Hello World jsp.

I've also tried adding a weblogic.xml to map the "Admin" role to a specific LDAP user (didn't work).

Any advice? It seems there's a lack of online references for this sort of thing (or I don't really know what I should be searching for)

Edit: I've also tried using BASIC auth instead of FORM (no luck)

My web.xml settings are below:


    <security-constraint>
  	<display-name>Test SC</display-name>
  	<web-resource-collection>
  		<web-resource-name>Test WR</web-resource-name>
  		<url-pattern>/hello.jsp</url-pattern>
  		<http-method>*</http-method>
  	</web-resource-collection>
  	<auth-constraint>
  		<role-name>Admin</role-name>
  	</auth-constraint>
    </security-constraint>
  
    <security-role>
  	<role-name>Admin</role-name>
    </security-role>
  
      <login-config>
    	<auth-method>BASIC</auth-method>
    	<realm-name>myrealm</realm-name>
    </login-config>