import Alpine from "alpinejs";
import htmx from "htmx.org";
import zxcvbn from "zxcvbn";
window.zxcvbn = zxcvbn;


Alpine.start();

window.initMap = function() {
    const address = document.getElementById('address').value;
    const geocoder = new google.maps.Geocoder();
    
    geocoder.geocode({ 'address': address }, function(results, status) {
        if (status === 'OK') {
            const map = new google.maps.Map(document.getElementById('map'), {
                zoom: 15,
                center: results[0].geometry.location
            });
            new google.maps.Marker({
                position: results[0].geometry.location,
                map: map
            });
        } else {
            console.error('Geocode was not successful for the following reason: ' + status);
        }
    });
};
