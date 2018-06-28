fetch('https://api.stormglass.io/point?lat=38.678876&lng=-9.340417&params=seaLevel', {
  headers: {
    "Authorization": "YOUR API KEY"  // Get your at https://stormglass.io
  }
})
.then(response => response.json())
.then(function(response) {
  const hours = response.hours;
  const minmax = [];
      
  hours.forEach((hour, index) => {

    // Skip if first or last element in list.
    if (index === 0 || index === hours.length - 1) {
      return;
    }

    // Get previous, current and next hour.
    const [previous, current, next] = hours.slice(index - 1, index + 2);

    // Get sea level from first source in response.
    const { seaLevel: [ { value: currentValue } ] } = current;
    const { seaLevel: [ { value: previousValue } ] } = previous;
    const { seaLevel: [ { value: nextValue } ] } = next;
    
    // Check if current valut is a local minimum.
    if (previousValue > currentValue < nextValue) {
      minmax.push([current.time, index, 'low']);
    }

    // Check if current valut is a local maximum.
    if (previousValue < currentValue > previousValue) {
      minmax.push([current.time, index, 'high']);
    }
  });

  // Do something with results.
  console.log(minmax);
});