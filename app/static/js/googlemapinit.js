function init() {
  var lat = document.getElementById("latitude").dataset.latitude;
  var long = document.getElementById("longitude").dataset.longitude;

console.log(lat);
console.log(long);
  
  var myCenter=new google.maps.LatLng(Number(lat), Number(long));

  var mapProp = {
    center:myCenter,
    zoom:15,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

  var marker=new google.maps.Marker({
  position:myCenter,
  });

  marker.setMap(map);
}
google.maps.event.addDomListener(window, 'load', init);

