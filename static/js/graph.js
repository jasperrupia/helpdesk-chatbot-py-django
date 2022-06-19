
var ctx = document.getElementById("myChart").getContext("2d");

// var gradient = ctx.crateLinearGradient(0, 0, 0, 400);
// gradient.addColorStop(0, "rgba(58, 123, 213, 1)");
// gradient.addColorStop(1, "rgba(0, 213, 255, 0.3)");

var labels = [1, 2, 3, 4, 5, 6, 7];

var data = {
  labels,
  datasets: [{
    label: 'Visitors',
    data: [0, 5, 6, 8, 25, 9, 24],
    fill: true,
    borderColor: 'rgb(75, 192, 192, 1)',
    backgroundColor: 'rgb(75, 192, 192, 0.1)',
    pointBackgroundColor: 'rgb(0, 0, 0, 0.5)',
    tension: 0.3
  }]
};

var config = {
    type: 'line',
    data,
    options: {
      responsive: true,
      radius: 3,
      hitRadius: 5,
      hoverRadius: 7,
      scales: {
        y: {
          ticks: {
            callback: function(value){
              return value + "k";
            }
          }
        }
      }
    }
};

var theChart = new Chart(ctx, config);