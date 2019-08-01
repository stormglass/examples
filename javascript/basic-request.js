fetch("https://api.stormglass.io/v1/weather/point?lat=58.5&lng=17.8", {
  headers: {
    "Authorization": "YOUR API KEY"  // Get your at https://stormglass.io
  }
}).then(function(response) {
  // Do something with response data.
  var jsonData = response.json();
});