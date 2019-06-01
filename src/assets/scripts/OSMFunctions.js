import $ from 'jquery'


export default {
  updateOSMTimes(centros, currentLocation, callback) {
    const request_max_size = 300;
    var  ajax_calls = [],
          localizaciones = "";

    for (var i = 0; i < centros.length; i += request_max_size) {
      //Get center locations string
      localizaciones = centros.slice(i, i + request_max_size - 1).map(function(centro) {
        return centro.coordenadas.lon.toString()  + "," +  centro.coordenadas.lat.toString();
      });

      //Create AJAX call
      ajax_calls.push(
        $.ajax({
          method: "GET",
          url: "https://osrm.aquelando.info/table/v1/driving/" +
                currentLocation.lon.toString() +
                "," +
                currentLocation.lat.toString() +
                ";" +
                localizaciones.join(";"),
          data: {
            sources: 0
          }
        })
      );
    }

    $.when.apply($, ajax_calls).then(
      function() {
        for (var i = 0; i < arguments.length; i++) {
          for(var j = 0; j < arguments[i][0].durations[0].length; j++) {
            if(! centros [i*request_max_size + j]) continue;
            if (! centros[i*request_max_size + j].osm) centros[i*request_max_size + j].osm = {};
            centros[i*request_max_size + j].osm.tiempo = arguments[i][0].durations[0][j+1];
          }
        }
        callback();
      },
      function(e) {
           console.log("My ajax failed");
      });
  },
  updateOSMDistances(centros, currentLocation, callback) {
    const R = 6371; // Radius of the earth in km
    var dLat,dLon,a;

    for (var i = 0; i < centros.length; i++) {
      dLat = (centros[i].coordenadas.lat - currentLocation.lat) * Math.PI / 180;  // deg2rad below
      dLon = (centros[i].coordenadas.lon - currentLocation.lon) * Math.PI / 180;
      a =
       0.5 - Math.cos(dLat)/2 +
       Math.cos(currentLocation.lat * Math.PI / 180) * Math.cos(centros[i].coordenadas.lat * Math.PI / 180) *
       (1 - Math.cos(dLon))/2;

      if (! centros[i].osm) centros[i].osm = {};
      centros[i].osm.distancia = R * 2 * Math.asin(Math.sqrt(a));
    }
    callback();
  },
  getOSMDetailedRouteInfo(centro, currentLocation, callback) {
    $.ajax({
      method: "GET",
      url: "https://osrm.aquelando.info/route/v1/driving/" +
            currentLocation.lon.toString() +
            "," +
            currentLocation.lat.toString() +
            ";" +
            centro.coordenadas.lon.toString()  +
            "," +
            centro.coordenadas.lat.toString(),
      data: {
        steps: true,
        overview: false
      }
    }).done (function(data) {
      centro.osm.details = data.routes[0];
      callback();
    })
  }
}
