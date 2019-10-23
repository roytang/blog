---
date: 2012-07-03 07:00:24
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/11305956/capturing-and-replacing-the-jsp-response-in-a-filter
tags:
- jsp
- servlet-filters
- questions
- stackoverflow
- software development
title: Capturing and replacing the JSP response in a Filter
---

I'm trying to write a servlet Filter that under certain conditions will read the HTML response returned by the JSP file and process it (using an XHTML parser) and make some modifications to it before finally returning it to the browser (basically I'm trying to implement a global change to avoid having to modify hundreds of JSPs individually)

I'm using Tomcat. I started out by providing a wrapper for the HttpServletResponse and the ServletOutputStream before passing them back to the filter chain. However, I'm getting an "IllegalStateException: getOutputStream() has already been called for this response." It seems to happen whenever one of our taglibs tries to write using the writer returned by "this.pageContext.getOut()", so I guess the response/writer/outputstream being used by Tomcat isn't using the wrapper classes I passed via the filter.

Any suggestions? Or is there a better way to accomplish what I'm trying to do?