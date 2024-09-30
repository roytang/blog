---
date: 2017-10-30 06:15:37
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/47009063/marklogic-9-mlcp-fails-when-importing-records-with-a-transform
tags:
- marklogic
- mlcp
- marklogic-9
- questions
- stackoverflow
- software development
title: 'Marklogic 9: MLCP fails when importing records with a transform'
---

I'm trying to migrate one of my dev envts from ML8 to ML9. I have an import script that successfully works on the ML8 version, but there's an error when I try running it against the ML9 database. The ML9 version is 9.0.3.1. The MLCP version is 9.0.3

My MLCP options file is as follows:

    import
    -host 
    192.168.33.10
    -port 
    8041
    -username 
    admin
    -password
    admin
    -input_file_path 
    d:\maroon\data\mbastest.csv 
    -mode 
    local 
    -input_file_type 
    delimited_text 
    -uri_id 
    ClientId 
    -output_uri_prefix
    /test/records/
    -output_uri_suffix 
    .json 
    -document_type 
    json 
    -transform_module 
    /ingestion/transform.js
    -transform_function 
    testTransform
    -transform_param
    test
    -content_encoding 
    windows-1252 
    -thread_count
    1

Here's the output of a test run with only 2 records in the test CSV file:

    17/10/30 14:07:33 INFO contentpump.LocalJobRunner: Content type: JSON
    17/10/30 14:07:33 INFO contentpump.ContentPump: Job name: local_455168344_1
    17/10/30 14:07:33 INFO contentpump.FileAndDirectoryInputFormat: Total input paths to process : 1
    17/10/30 14:07:38 WARN contentpump.TransformWriter: Failed document /test/records/31.json
    17/10/30 14:07:38 WARN contentpump.TransformWriter: <error:format-string xmlns:error="http://marklogic.com/xdmp/error" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">XDMP-UNEXPECTED: (err:XPST0003) Unexpected token syntax error, unexpected QName_, expecting $end or SemiColon_</error:format-string>
    17/10/30 14:07:38 WARN contentpump.TransformWriter: Failed document /test/records/32.json
    17/10/30 14:07:38 WARN contentpump.TransformWriter: <error:format-string xmlns:error="http://marklogic.com/xdmp/error" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">XDMP-UNEXPECTED: (err:XPST0003) Unexpected token syntax error, unexpected QName_, expecting $end or SemiColon_</error:format-string>
    17/10/30 14:07:38 INFO contentpump.LocalJobRunner:  completed 100%
    17/10/30 14:07:38 INFO contentpump.LocalJobRunner: com.marklogic.mapreduce.MarkLogicCounter:
    17/10/30 14:07:38 INFO contentpump.LocalJobRunner: INPUT_RECORDS: 2
    17/10/30 14:07:38 INFO contentpump.LocalJobRunner: OUTPUT_RECORDS: 2
    17/10/30 14:07:38 INFO contentpump.LocalJobRunner: OUTPUT_RECORDS_COMMITTED: 0
    17/10/30 14:07:38 INFO contentpump.LocalJobRunner: OUTPUT_RECORDS_FAILED: 2
    17/10/30 14:07:38 INFO contentpump.LocalJobRunner: Total execution time: 5 sec

If I remove the transform params, the import works fine.

I thought it might be a parsing issue with my transform module itself, so I tried replacing it with the following example from the documentation:

    // Add a property named "NEWPROP" to any JSON input document.
    // Otherwise, input passes through unchanged.
    
    function addProp(content, context)
    {
      const propVal = (context.transform_param == undefined)
                     ? "UNDEFINED" : context.transform_param;
    
      if (xdmp.nodeKind(content.value) == 'document' &&
          content.value.documentFormat == 'JSON') {
        // Convert input to mutable object and add new property
        const newDoc = content.value.toObject();
        newDoc.NEWPROP = propVal;
    
        // Convert result back into a document
        content.value = xdmp.unquote(xdmp.quote(newDoc));
      }
      return content;
    };
    
    exports.addProp = addProp;

(Of course I changed the params in the MLCP options file accordingly)

The issue still persists even with just this test function.

Any advice?