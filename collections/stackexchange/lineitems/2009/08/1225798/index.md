---
date: 2009-08-04 05:27:59
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1225798/javascript-programmatically-invoking-events
tags:
- javascript
- javascript-events
- questions
- stackoverflow
- software development
title: Javascript - programmatically invoking events
---

Say I add events to an object using either addEventListener or attachEvent (depending on the browser); is it possible to later invoke those events programmatically? 

The events handlers are added/removed using an object like this:

    var Event = {
    	add: function(obj,type,fn) {
    		if (obj.attachEvent) {
    			obj.attachEvent('on'+type,fn);
    		} else {
    			obj.addEventListener(type,fn,false);
        	}
    	},
    	remove: function(obj,type,fn) {
    		if (obj.detachEvent) {
    			obj.detachEvent('on'+type,fn);
    		} else {
    			obj.removeEventListener(type,fn,false);
        	}
    	}
    }

Or do I need to store copies of each handler and just add an Event.invoke(...) function?

Edit: Also, jQuery is not an option :D