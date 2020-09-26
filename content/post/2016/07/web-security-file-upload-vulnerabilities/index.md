---
author: roy
categories: []
date: 2016-07-07 01:30:00
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/750868946899857409/
tags:
- Software Development
title: 'Web Security: File Upload Vulnerabilities'
type: post
url: /2016/07/web-security-file-upload-vulnerabilities/
---

A friend of mine had an informal consultation with me the other day (read: asked me questions over FB messenger) about what their IT staff was telling them about a file upload vulnerability that had been recently exploited in one of their applications. Obviously it was difficult for me to judge given that I didn't know all the details, but for me it was most likely a vulnerability introduced in the application code itself.

If you're not familiar with file upload vulnerability, the simplest type of attack goes something like this: the user (or attacker in this case) uploads a file using a file upload function on the system (a common functionality), and the system allows the user to execute that file as if it were code. This can happen if the application saves the uploaded file directly into the web application path, such that it can be executed directly from the client. This is a common vulnerability listed on the OWASP page.

For example, your application provides a function to upload an image to use as the user's profile picture, then the applications stores the uploaded image in the file system directly in the application path such that it is served to the user as something like /images/uploadedfile.png. However, if the user uploads instead a file that can be executed directly by the web server, such as a .PHP file for PHP webservers or a .JSP file for Java containers, the user can now execute any code that was in his uploaded file simply by invoking /images/uploadedfile.php! And this access would be absolute, everything your system has access to will be fair game: file system, network, database, etc., and provides the attacker with more information for succeeding attacks.

The key to protecting yourself from file upload vulnerabilities is one of the basic tenets of web application security: **Never trust user submitted data**. This means that you should validate uploaded files -- maybe you only allow image files for example -- and your validation should be thorough. You shouldn't validate only be checking the file extension or the content type in the HTTP header, as these can be faked. Use a server-side API call to verify the file type.

In addition, **do not store or serve the uploaded files in a way that they will be executed by the web application**. For Java webapps I've worked on, often we will store uploaded files in the Oracle database, and when they need to be served they are dumped directly into the response OutputStream. If you _must_ store the uploads in the file system, do it in a location that is not accessible from the web server directly. For J2EE containers that can be inside /WEB-INF/ or outside the application path itself. For PHP, it should be outside the HTTP doc folder of the Apache server.

For the PHP example above, you should also avoid serving the image files using a PHP include. If the URL to access the image is something like uploadedimage?image\_id=1 and your code maps that image\_id to a file on the file system and serves it using a PHP include, it will still be executed by the system as code. Instead the file should be dumped directly into the response. One way to do it is as follows:

> <pre>&lt;?php
header('Content-Type: [whatever your content type is]');
header("Content-Disposition: inline; filename=\"$file_name\"");
echo $file;
?&gt;</pre>

This is only the most basic attack. File upload functions can be exploited in a number of other ways. For example, the attacker could upload a number of large files to attempt to take down your server due to insufficient disk space (prevention: restrict file upload size, prevent user uploading too many files). So developers need to be carefully in how they allow file uploads in their system and be aware of possible vulnerabilities and exploits, the OWASP page linked above lists some more prevention measures.