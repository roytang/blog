var hugolunr = require('hugo-lunr');
var h = new hugolunr();
h.setInput('../../content/**');
h.setOutput('lunr.json');
h.index();