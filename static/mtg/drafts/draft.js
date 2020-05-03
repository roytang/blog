
var mtgstorm = {
  Draft : function(id) {
    this.picks = [];
    this.currentPack = "";
    this.activePack = 1;
    this.activePick = 1;
    this.id = id || "draft"+ new Date().getTime();
    return this;
  }
}

mtgstorm.Draft.prototype = {
  setActiveLinkClass : function(cls) {
      var el = document.getElementById(this.id + "_pack" + this.activePack);
      if (el) {
        el.className = cls;
      }
      el = document.getElementById(this.id + "_pick" + this.activePick);
      if (el) {
        el.className = cls;
      }  
  },
  
  showActivePick : function(container) {     
    container = container || document.getElementById(this.id + "_wrapper");
    if (container) {
      var idx = (this.activePack-1)*15+this.activePick-1;
      var html = this.generatePick(this.picks[idx]);
      container.innerHTML = html;
      this.setActiveLinkClass('active');
    }
  },
  
  goToPack : function(packNo) {
    if (packNo == this.activePack) return;
    this.setActiveLinkClass('');
    this.activePack = packNo;
    this.showActivePick();
  },
  
  goToPick : function(pickNo) {
    if (pickNo == this.activePick) return;
    this.setActiveLinkClass('');
    this.activePick = pickNo;
    this.showActivePick();
  },
  
  navMenu : function() {
    var i = 0, out = "";
    out += "<div class='draft_navmenu'>";
    out += "Pack ";
    for (i=0; i<3; i++) {
      out += "<a href='#' id='" + this.id + "_pack" + (i+1) + "'"
      + ( i==0 ? " class='active' " : "") 
      + " onclick='mtgstorm.Draft.get(\"" + this.id + "\").goToPack(" + (i+1) + ")'>" 
      + (i+1) + "</a> ";                              
    }
    out += "Pick ";
    for (i=0; i<15; i++) {
      out += "<a href='#' id='" + this.id + "_pick" + (i+1) + "'" 
      + ( i==0 ? " class='active' " : "" ) 
      + " onclick='mtgstorm.Draft.get(\"" + this.id + "\").goToPick(" + (i+1) + ")'>" 
      + (i+1) + "</a> ";                              
    }
    out += '</div>';
    return out;
  },

  generatePick : function(pick) {
    var card, out="", setName = pick.pack;
    // weird special handling for conflux
    if (setName == "CON") {
      setName = "general";
    }
    for (idx in pick.cards) {
      card = pick.cards[idx];  
      if (card.name && card.name !== "") {
          out += "<img src='http://www.wizards.com/global/images/magic/" 
            + setName
            + "/"
            + mtgstorm.Draft.formatName(card.name)
            + ".jpg' class='card"
            + (card.pick ? " pick " : "")
            + "'/>";
      }
    }
    return out;
  },
  
  addPick : function(pick) {
    this.picks.push(pick);
  },
  
  generate : function() {
    var out = "";
    if (this.picks.length > 0) {
      out += this.navMenu();
      out += "<div id='" + this.id + "_wrapper'>";
      out += this.generatePick(this.picks[0]);
      out += "</div>";
      out += "<p>Powered by <a href='http://mtgstorm.com/drafts/'>MtgStorm Draft Converter</p>";
    }
    return out;
  },
  
  generateScript : function() {
    var out = "";
    out += "<link rel='stylesheet' href='http://mtgstorm.com/drafts/draft.css' />"
    out += "<script src='http://mtgstorm.com/drafts/draft.js'></"+"script>";
    out += "<script>var d = new mtgstorm.Draft('" + this.id + "');"  
    for (idx in this.picks) {
      out += "\nd.addPick(" + JSON.stringify(this.picks[idx]) + ");";
    }
    out += "\nmtgstorm.Draft.put(d);";
    out += "\n</"+"script>";
    return out;
  },
  
  startPack : function(setName) {
    this.currentPack = setName;
  }
}

mtgstorm.Draft.convert = function(dataIn, fieldOut, previewElement) {
  if (!dataIn) {
    if (document.getElementById("draft_in")) {
      dataIn = document.getElementById("draft_in").value;
    }
  }
  fieldOut = fieldOut || document.getElementById("draft_out");
  previewElement = previewElement || document.getElementById("draft_preview");
  var lines = dataIn.split("\n"), 
      line = "", 
      set = ""
      d = new mtgstorm.Draft(),
      pick = null,
      card = null,
      out = "";
  
  for (idx in lines) {
    line = lines[idx];
    if (line.match(/------/) != null) {
      // extract set name
      set = line.replace(/-/g, "").replace(/ /g, "");
      d.startPack(set);
    } else if (line.match(/Pack [0-9] pick 1?[0-9]:/) != null) {
      // store the old pick, if it exists
      if (pick) {
        d.addPick(pick);
      }
      // this line starts a new pick
      pick = new Object();
      pick.pack = d.currentPack;
      pick.cards = [];
    } else if (pick && line.trim().length > 0) {
      card = new Object();
      card.name = line.substring(4, line.length)
      if (line.substring(0, 4) == "--> ") {
        card.pick = true;
      }
      pick.cards.push(card);
    }    
  }
  // store the last  pick, if it exists
  if (pick) {
    d.addPick(pick);
  }

  var script = d.generateScript();  
  var html = d.generate();
  if (fieldOut) {
    fieldOut.value = script + "\n" + html;
  }
  if (previewElement) {
    previewElement.innerHTML = html;
  }
  return html;
}

mtgstorm.Draft._registry = {};
mtgstorm.Draft.put = function(d) {
  mtgstorm.Draft._registry[d.id] = d;
}
mtgstorm.Draft.get = function(id) {
  return mtgstorm.Draft._registry[id];
}
mtgstorm.Draft.formatName = function(name) {
    return name.toLowerCase().replace(/[:',\/]/g, '').replace(/[ -]/g, "_")
      .replace(new RegExp(String.fromCharCode(230), "g"), "ae")
      .replace(/_\(foil\)/g, "");
}
   


function test() {
var d = new mtgstorm.Draft();
d.addPick({ pack: "ALA", cards : [
  { name : "Resounding Thunder"}, 
  { name : "Jhessian Lookout"}, 
  { name : "Resounding Silence"}, 
  { name : "Dregscape Zombie"}, 
  { name : "Obelisk of Jund"}, 
  { name : "Cathartic Adept"}, 
  { name : "Lightning Talons"}, 
  { name : "Naya Panorama"}, 
  { name : "Onyx Goblet"}, 
  { name : "Obelisk of Esper"}, 
  { name : "Grixis Charm"}, 
  { name : "Bant Battlemage"}, 
  { name : "Etherium Astrolabe"}, 
  { name : "Sigil of Distinction", pick: true}, 
  { name : "Island"} 
]});
return d.generate();
}
