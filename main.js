// Create WebSocket connection.
const socket = new WebSocket('ws://localhost:8000/ws');
let data
// Listen for messages
socket.addEventListener('message', (event) => {
    data =  event.data;
    console.log('Aduino Temperatur:' + event.data)
});





var chartColors2 = {
	red: 'rgb(255, 99, 132)',
	orange: 'rgb(255, 159, 64)',
	yellow: 'rgb(255, 205, 86)',
	green: 'rgb(75, 192, 192)',
	blue: 'rgb(54, 162, 235)',
	purple: 'rgb(153, 102, 255)',
	grey: 'rgb(201, 203, 207)'
};


function onRefresh2(chart2) {
	chart2.config.data.datasets.forEach(function(dataset2) {
		dataset2.data.push({
			x: Date.now(),
			y: data
		});
	});
}

var color2 = Chart.helpers.color;
var config2 = {
	type: 'line',
	data: {
		datasets: [{
			label: 'Arbeit',
			backgroundColor: color2(chartColors2.blue).alpha(1.55).rgbString(),
			borderColor: chartColors2.blue,
			fill: true,
			
			data: []
		}]
	},
	options: {
		title: {
			display: true,
			text: 'Line chart (horizontal scroll) sample',
			
			
		},
		scales: {
			xAxes: [{
        scaleLabel: {
					display: true,
					labelString: 'Voltage',
					backgroundColor: "rgba(159,170,174,0.8)",

				},
				ticks: {
					max: 100,
				 	min: -100
				},
				type: 'realtime',
				realtime: {
					duration: 20000,
					refresh: 1000,
					delay: 2000,
					onRefresh: onRefresh2
				}
			}],
			yAxes: [{
				scaleLabel: {
					display: true,
					labelString: 'Electricity'
				},
				ticks: {
					max: 100,
				 	min: -100
				}
			}]
		},
		tooltips: {
			mode: 'nearest',
			intersect: false
		},
		hover: {
			mode: 'nearest',
			intersect: false
		}
	}
};



new Chart("myChart1", config2);