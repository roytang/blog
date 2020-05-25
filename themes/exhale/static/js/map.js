function createMap(data) {
    let coords = [data["lat"], data["lng"]];
    document.addEventListener("DOMContentLoaded", function(){
        var mymap = L.map('mapid');
        let minlat = 2000, maxlat = -2000, minlong = 2000, maxlong = -2000
        for (let i in data) {
            let item = data[i];
            if (item["lat"] < minlat) {
                minlat = item["lat"];
            }
            if (item["lat"] > maxlat) {
                maxlat = item["lat"];
            }
            if (item["lng"] < minlong) {
                minlong = item["lng"];
            }
            if (item["lng"] > maxlong) {
                maxlong = item["lng"];
            }
            currlat = item["lat"];
            currlng = item["lng"];
            let label = "<b>" + item["title"] + " </b>";
            var marker = L.marker([currlat, currlng]).addTo(mymap);			
            marker.bindPopup(label);
        }

        let delta = Math.min(data.length, 10)/100;
        mymap.fitBounds([
            [minlat-delta, minlong-delta], 
            [maxlat+delta, maxlong+delta], 
        ], 1);

        L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox/streets-v11',
            tileSize: 512,
            zoomOffset: -1,
            accessToken: 'pk.eyJ1IjoiaHVuZ3J5cm95IiwiYSI6ImNrOXpnOTJvaTBhbnQzb252cmpyZzNuZWcifQ.iFkSVmoCUddzDj40_x5T5Q'
        }).addTo(mymap);	
    });
}