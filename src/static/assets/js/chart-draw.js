var data = {
  // A labels array that can contain any sort of values
  labels: ['1', '2', '3', '4', '5'],
  // Our series array that contains series objects or in this case series data arrays
  series: [
    [5, 2, 4, 2, 0, 5]
  ],
  
};


var data2 = {
  // A labels array that can contain any sort of values
  labels: ['1', '2', '3', '4', '5'],
  // Our series array that contains series objects or in this case series data arrays
  series: [
    [5, 2, 4, 2, 1, 0]
  ],
  
};


var data3 = {
  // A labels array that can contain any sort of values
  labels: ['1', '2', '3', '4', '5'],
  // Our series array that contains series objects or in this case series data arrays
  series: [
    [3, 2, 4, 2, 0, 7]
  ],
  
};

var option = {
  width: 90,
  height: 32,
    showPoint: false,
    showLine: true,
    showArea: true,
    fullWidth: true,
    showLabel: false,
    axisX: {
      showGrid: false,
      showLabel: false,
      offset: 0
    },
    axisY: {
      showGrid: false,
      showLabel: false,
      offset: 0
    },
    chartPadding: 0,
    low: 0
  
};

// Create a new line chart object where as first parameter we pass in a selector
// that is resolving to our chart container element. The Second parameter
// is the actual data object.
if (document.querySelector('#first-chart') !== null){
  new Chartist.Line('#first-chart', data, option);
}

if (document.querySelector('#second-chart') !== null){
  new Chartist.Line('#second-chart', data2, option);
}
if (document.querySelector('#third-chart') !== null){
  new Chartist.Line('#third-chart', data3, option);
}


let chart_1_width;

if (document.querySelector('#chart-1') !== null){
  let computedStyle = getComputedStyle(document.querySelector('#chart-1'), null);
  let chart_1_width = parseInt(computedStyle.getPropertyValue('width'));
  console.log(chart_1_width);
}


var option2 = {
  width: chart_1_width,
  height: 124,
    showPoint: false,
    showLine: true,
    showArea: true,
    fullWidth: true,
    showLabel: false,
    axisX: {
      showGrid: true,
      showLabel: false,
      offset: 0
    },
    axisY: {
      showGrid: false,
      showLabel: false,
      offset: 0
    },
    chartPadding: 0,
    low: 0
  
};


var data4 = {
  // A labels array that can contain any sort of values
  labels: ['1', '2', '3', '4', '5'],
  // Our series array that contains series objects or in this case series data arrays
  series: [
    [50, 80, 120, 140, 140, 120, 60, 60, 60, 20]
  ],
  
};

if (document.querySelector('#chart-1') !== null){
  new Chartist.Line('#chart-1', data4, option2);
}

if (document.querySelector('#chart-2') !== null){
  new Chartist.Line('#chart-2', data4, option2);
}

if (document.querySelector('#chart-3') !== null){
  new Chartist.Line('#chart-3', data4, option2);
}