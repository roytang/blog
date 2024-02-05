---
date: 2016-05-05 00:00:00
slug: when-is-a-destroy-method-calle
source: quora
syndicated:
- type: quora
  url: https://www.quora.com/When-is-a-destroy-method-called-for-a-servlet/answer/Roy-Tang
tags:
- answers
---

Someone on [quora](https://quora.com) asked:

> [When is a destroy method called for a servlet?](https://www.quora.com/When-is-a-destroy-method-called-for-a-servlet/answer/Roy-Tang)


This will largely depend on the implementation of the servlet container. It will be called whenever the servlet container deallocates the servlet instance. The servlet spec does not specify when this should happen. The servlet instance may be active for the entire duration that the servlet container is up, or it may deallocate instances earlier for performance purposes