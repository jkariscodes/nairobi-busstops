function main_map_init (map, options) {
    let dataurl = '{% url "data" %}';
    // Download GeoJSON via Ajax
    $.getJSON(dataurl, function (data) {
        // Add GeoJSON layer
        L.geoJson(data).addTo(map);
    });
}