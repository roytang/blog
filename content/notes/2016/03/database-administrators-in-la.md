---
date: 2016-03-15 00:00:00
slug: database-administrators-in-la
source: quora
syndicated:
- type: quora
  url: https://www.quora.com/Database-Administrators-In-laymans-terms-what-do-you-do-and-what-tools-programming-skills-do-you-use/answer/Roy-Tang
tags:
- answers
---

Someone on [quora]() asked:
> [Database Administrators: In layman's terms, what do you do and what tools/programming skills do you use?](https://www.quora.com/Database-Administrators-In-laymans-terms-what-do-you-do-and-what-tools-programming-skills-do-you-use/answer/Roy-Tang)
<span class="ui_qtext_rendered_qtext"><p class="ui_qtext_para u-ltr u-text-align--start">Typically, a database administrator will have the following tasks:</p><ol><li>Database installation and configuration</li><li>Maintenance - version upgrades and applying patches</li><li>Migration - transferring data from one database to another, or an older database version to another</li><li>Setting up regular backups and planning for recovery procedures</li><li>Configure security models</li><li>Storage and capacity planning - this means monitoring the disk storage used by the database</li><li>Performance monitoring and tuning - users will complain if the database slows to a crawl! Tuning here can mean modifying SQL statements or stored procedures to improve performance</li><li>General database troubleshooting</li><li>Maintaining data integrity - this means making sure the data in the tables and the relationships between them are "correct". Typically a database will have internal mechanisms to ensure this, such as foreign keys (which may be configured by the database administrator also), and applications using the database will have their own set of rules that they impose upon the data. However, the applications aren't always correct, so that may from time to time require running SQL scripts to correct any data errors that arise from misconfiguration or application errors</li></ol><p class="ui_qtext_para u-ltr u-text-align--start">Hope that helps!</p></span>