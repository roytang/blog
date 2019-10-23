---
date: 2017-08-10 21:19:20
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/45623599/marklogic-flexible-replication
tags:
- marklogic
- questions
- stackoverflow
- software development
title: Marklogic - flexible replication
---

We've been trying to set up flexible replication in our system which uses a MarkLogic database. 
We followed the instructions from https://docs.marklogic.com/8.0/guide/flexrep/quick_start and have been able to set up flexible replication between two MarkLogic servers. We have verified that new documents created in the master are copied over to the replica. However, the master database currently has more than 47 million records that were there before we configured the replication. Once the replication process was triggered, we observed that the documents are being replicated to the replica very slowly. Roughly 20,000 documents were replicated within the first two hours. The rate is very slow, it would take months for the old records to be fully replicated. 

Our questions are:

1. We are looking into increasing the hardware specs of the two servers, but aside from that would anyone have any advice or documentation as to how we could speed up the replication? I couldn't find any existing documentation regarding this?

2. Failing that, would it be possible to set up flexible replication without needing to replicate the initial data set? FYI, we also tried to clone the master database and use the clone as the replica. (We thought this might mean that the older records don't have to be replicated.) However, in this case we encountered XDMP-NEWSTAMP and XDMP-EXTIME errors on the replica server, so we gave up on this approach. A sample of the errors encountered on the replica is below:

> 2017-08-03 18:45:04.376 Notice: exp-rest-content-flexrep:
> XDMP-NEWSTAMP: Timestamp too new for forest exp-rest-content-001-1
> (15017569242290900) 2017-08-03 18:45:04.376 Notice:
> exp-rest-content-flexrep: in /apply.xqy [1.0-ml] 2017-08-03
> 18:45:04.379 Notice: TaskServer: XDMP-EXTIME: try { let
> $raw-module-name := module-path($action-to-execute/p:module) let
> $module-kind := module-kind($raw-module-name) let $module-name := if
> ($module-kind = "xquery" or $module-kind = "javascript") then
> $raw-module-name else $cpfi:xslt-action return if ($module-name = "")
> then fn:error((), "CPF-ACTIONNOTFOUND", "Default success") else if
> ($module-kind = "javascript") then (xdmp:trace("CPF Action Invoke",
> fn:string-join(($caller, xdmp:get-current-user(), $uri,
> $state-or-status, $raw-module-name), " ")), xdmp:invoke($module-name,
> (fn:QName("","uri"), $uri, xs:QName("cpf:document-uri"), $uri,
> fn:QName("","transition"), $chosen-transition,
> options-var-js($action-to-execute)), $invoke-options)) else
> (xdmp:trace("CPF Action Invoke", fn:string-join(($caller,
> xdmp:get-current-user(), $uri, $state-or-status, $raw-module-name), "
> ")), xdmp:invoke($module-name, ($vars, xs:QName("cpf:transition"),
> $chosen-transition, options-var($action-to-execute), if ($module-kind
> = "xslt") then (xs:QName("cpf:stylesheet-uri"), $raw-module-name) else ()), $invoke-options)) } catch ($e) { let $trace := let $context :=
> fn:concat($caller, " ", $uri, " action failed") return
> (cpf:log(fn:string-join(($context, $e/err:format-string), " "),
> "error"), cpf:log(($context, $e), "fine")) let $failure-action :=
> ($pipelines/p:failure-action)[1] let $raw-failure-module :=
> module-path($failure-action/p:module) let $failure-kind :=
> module-kind($raw-failure-module) let $failure-module := if
> ($failure-kind = "xquery" or $failure-kind = "javascript") then
> $raw-failure-module else $cpfi:xslt-action return if ($failure-module
> = "") then fn:error((), "CPF-ACTIONNOTFOUND", "Default failure action") else xdmp:invoke($failure-module, ($vars,
> xs:QName("cpf:transition"), $chosen-transition,
> options-var($failure-action), xs:QName("cpf:exception"), $e, if
> ($failure-kind = "xslt") then (xs:QName("cpf:stylesheet-uri"),
> $raw-failure-module) else ()), $invoke-options) } -- Time limit
> exceeded 2017-08-03 18:45:04.379 Notice: TaskServer: in
> /MarkLogic/cpf/triggers/internal-cpf.xqy, at 213:4, 2017-08-03
> 18:45:04.379 Notice: TaskServer: in execute-action("on-state-enter",
> "http://marklogic.com/states/initial", "/_smslogs/5849823.xml",
> (xs:QName("trgr:uri"), "/_smslogs/5849823.xml",
> xs:QName("trgr:trigger"), ...), <options
> xmlns="xdmp:eval"><isolation>different-transaction</isolation><prevent-deadlocks>t...</options>,
> (fn:doc("http://marklogic.com/cpf/pipelines/12349495875628658916.xml")/p:pipeline,
> fn:doc("http://marklogic.com/cpf/pipelines/3358424510998587926.xml")/p:pipeline,
> fn:doc("http://marklogic.com/cpf/pipelines/13179541037342910978.xml")/p:pipeline,
> ...),
> fn:doc("http://marklogic.com/cpf/pipelines/3358424510998587926.xml")/p:pipeline/p:state-transition[3]/p:default-action, fn:doc("http://marklogic.com/cpf/pipelines/3358424510998587926.xml")/p:pipeline/p:state-transition[3])
> [1.0-ml] 2017-08-03 18:45:04.379 Notice: TaskServer:   $caller =
> "on-state-enter" 2017-08-03 18:45:04.379 Notice: TaskServer:  
> $state-or-status = "http://marklogic.com/states/initial" 2017-08-03
> 18:45:04.379 Notice: TaskServer:   $uri = "/_smslogs/5849823.xml"
> 2017-08-03 18:45:04.379 Notice: TaskServer:   $vars =
> (xs:QName("trgr:uri"), "/_smslogs/5849823.xml",
> xs:QName("trgr:trigger"), ...) 2017-08-03 18:45:04.379 Notice:
> TaskServer:   $invoke-options = <options
> xmlns="xdmp:eval"><isolation>different-transaction</isolation><prevent-deadlocks>t...</options>
> 2017-08-03 18:45:04.379 Notice: TaskServer:   $pipelines =
> (fn:doc("http://marklogic.com/cpf/pipelines/12349495875628658916.xml")/p:pipeline,
> fn:doc("http://marklogic.com/cpf/pipelines/3358424510998587926.xml")/p:pipeline,
> fn:doc("http://marklogic.com/cpf/pipelines/13179541037342910978.xml")/p:pipeline,
> ...) 2017-08-03 18:45:04.379 Notice: TaskServer:   $action-to-execute
> = fn:doc("http://marklogic.com/cpf/pipelines/3358424510998587926.xml")/p:pipeline/p:state-transition[3]/p:default-action 2017-08-03 18:45:04.379 Notice: TaskServer:   $chosen-transition =
> fn:doc("http://marklogic.com/cpf/pipelines/3358424510998587926.xml")/p:pipeline/p:state-transition[3]
> 2017-08-03 18:45:04.379 Notice: TaskServer:   $e = <error:error
> xsi:schemaLocation="http://marklogic.com/xdmp/error error.xsd"
> xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
> xmlns:error="http://marklogic.com/xdmp/error"><error:code>XDMP-NEWSTAMP</error:code><error:name/><error:xquery...</error:error> 2017-08-03 18:45:04.379 Notice: TaskServer: in
> /MarkLogic/cpf/triggers/internal-cpf.xqy, at 342:6, 2017-08-03
> 18:45:04.379 Notice: TaskServer: in
> execute-transition("on-state-enter",
> "http://marklogic.com/states/initial", "/_smslogs/5849823.xml",
> (xs:QName("trgr:uri"), "/_smslogs/5849823.xml",
> xs:QName("trgr:trigger"), ...), <trgr:trigger
> xmlns:trgr="http://marklogic.com/xdmp/triggers"><trgr:trigger-id>6551367241994447650</trgr:trigger-id><trgr:trig...</trgr:trigger>, (fn:doc("http://marklogic.com/cpf/pipelines/12349495875628658916.xml")/p:pipeline,
> fn:doc("http://marklogic.com/cpf/pipelines/3358424510998587926.xml")/p:pipeline,
> fn:doc("http://marklogic.com/cpf/pipelines/13179541037342910978.xml")/p:pipeline,
> ...),
> (fn:doc("http://marklogic.com/cpf/pipelines/12349495875628658916.xml")/p:pipeline/p:state-transition[2],
> fn:doc("http://marklogic.com/cpf/pipelines/3358424510998587926.xml")/p:pipeline/p:state-transition[3],
> fn:doc("http://marklogic.com/cpf/pipelines/13179541037342910978.xml")/p:pipeline/p:state-transition[1],
> ...), <p:null-transition
> xmlns:p="http://marklogic.com/cpf/pipelines"><p:state>http://marklogic.com/states/initial</p:state></p:null-transition>)
> [1.0-ml] 2017-08-03 18:45:04.379 Notice: TaskServer:   $caller =
> cpf:state("http://marklogic.com/states/initial") 2017-08-03
> 18:45:04.379 Notice: TaskServer:   $state-or-status = () 2017-08-03
> 18:45:04.379 Notice: TaskServer:   $uri = (xs:QName("trgr:uri"),
> "/_smslogs/5849823.xml", xs:QName("trgr:trigger"), ...) 2017-08-03
> 18:45:04.379 Notice: TaskServer: in
> /MarkLogic/cpf/triggers/internal-cpf.xqy, at 358:3, 2017-08-03
> 18:45:04.379 Notice: TaskServer: in
> int:execute-state-transition("on-state-enter",
> cpf:state("http://marklogic.com/states/initial"),
> "/_smslogs/5849823.xml", (xs:QName("trgr:uri"),
> "/_smslogs/5849823.xml", xs:QName("trgr:trigger"), ...), <trgr:trigger
> xmlns:trgr="http://marklogic.com/xdmp/triggers"><trgr:trigger-id>6551367241994447650</trgr:trigger-id><trgr:trig...</trgr:trigger>) [1.0-ml] 2017-08-03 18:45:04.379 Notice: TaskServer:   $caller =
> cpf:state("http://marklogic.com/states/initial") 2017-08-03
> 18:45:04.379 Notice: TaskServer:   $state = () 2017-08-03 18:45:04.379
> Notice: TaskServer:   $uri = (xs:QName("trgr:uri"),
> "/_smslogs/5849823.xml", xs:QName("trgr:trigger"), ...) 2017-08-03
> 18:45:04.379 Notice: TaskServer: in
> /MarkLogic/cpf/triggers/on-state-enter.xqy, at 41:6 [1.0-ml]
> 2017-08-03 18:45:04.379 Notice: TaskServer:   $state =
> cpf:state("http://marklogic.com/states/initial") 2017-08-03
> 18:45:04.379 Notice: TaskServer:   $trace = () 2017-08-03 18:45:04.379
> Notice: TaskServer:   $vars = (xs:QName("trgr:uri"),
> "/_smslogs/5849823.xml", xs:QName("trgr:trigger"), ...) 2017-08-03
> 18:45:04.379 Notice: TaskServer: XDMP-NEWSTAMP: Timestamp too new for
> forest exp-rest-content-001-1 (15017569242290900) 2017-08-03
> 18:45:04.379 Notice: exp-rest-content-flexrep: XDMP-NEWSTAMP:
> Timestamp too new for forest exp-rest-content-001-1
> (15017569242290900) 2017-08-03 18:45:04.379 Notice:
> exp-rest-content-flexrep: in /apply.xqy [1.0-ml]