function main_map_init (map, options) {
    let dataurl = "data/";
    // Download GeoJSON via Ajax
    $.getJSON(dataurl, function (data) {
        function onEachFeature(feature, layer) {
            // does this feature have a property named popupContent?
            if (feature.properties && feature.properties.stop_name) {
                layer.bindPopup(feature.properties.stop_name);
                }
            }
        // Add GeoJSON layer
        L.geoJson(data, {onEachFeature: onEachFeature}).addTo(map);
    });
}
