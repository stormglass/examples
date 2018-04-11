fetch('https://api.stormglass.io/forecast?lat=58.5&lng=17.8', {
  headers: {
    'Authentication-Token': 'YOUR API KEY'  // Get your at https://stormglass.io
  }
}).then(function(response) {
  // Do something with response data.
  var jsonData = response.json();
});