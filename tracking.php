<?PHP
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Position tracking</title>
		<script
			type="text/javascript"
			src="https://canvasjs.com/assets/script/jquery-1.11.1.min.js"
		></script>
		<script
			type="text/javascript"
			src="https://canvasjs.com/assets/script/canvasjs.min.js"
		></script>
		<script type="text/javascript">
			window.onload = function () {
				var dataPoints = [];
				t = [];
				ax = [0];
				ay = [0];
				az = [0];
				vx = [0];
				vy = [0];
				vz = [0];
				x = [0];
				y = [0];
				z = [0];
				function getDataPointsFromCSV(csv) {
					var dataPoints = (csvLines = points = []);
					csvLines = csv.split('\n');
					for (var i = 0; i < csvLines.length; i++) {
						if (csvLines[i].length > 0) {
							points = csvLines[i].split(',');
							t.push(parseFloat(points[0]));
						}
					}
					for (var i = 1; i < csvLines.length - 1; i++)
						if (csvLines[i].length > 0) {
							points = csvLines[i].split(',');
							ax.push(parseFloat(points[1]));
							ay.push(parseFloat(points[2]));
							az.push(parseFloat(points[3]));
							vx.push(
								vx[i - 1] + (ax[i] * (t[i + 1] - t[i])) / 1000
							);
							vy.push(
								vy[i - 1] + (ay[i] * (t[i + 1] - t[i])) / 1000
							);
							vz.push(
								vz[i - 1] + (az[i] * (t[i + 1] - t[i])) / 1000
							);
							x.push(
								x[i - 1] + (vx[i] * (t[i + 1] - t[i])) / 1000
							);
							y.push(
								y[i - 1] + (vy[i] * (t[i + 1] - t[i])) / 1000
							);
							z.push(
								z[i - 1] + (vz[i] * (t[i + 1] - t[i])) / 1000
							);
							dataPoints.push({
								x: x[i],
								y: y[i],
							});
						}
					return dataPoints;
				}
				// while (true) {
				setInterval(function () {
					$.get('./output.csv', function (data) {
						var chart = new CanvasJS.Chart('chartContainer', {
							title: {
								text: 'Position tracking system',
							},
							axisX: {
								title: 'X-axis',
								minimum: -5,
								maximum: 5,
							},
							axisY: {
								title: 'Y-axis',
								minimum: -5,
								maximum: 10,
							},
							data: [
								{
									radius: '1',
									color: 'rgb(255, 99, 132)',
									type: 'bubble',
									dataPoints: getDataPointsFromCSV(data),
								},
							],
							options: {
								scales: {
									x: {
										type: 'linear',
										position: 'bottom',
									},
								},
							},
						});

						chart.render();
					});
				}, 1000);

				// }
			};
		</script>
	</head>
	<body>
		<div id="chartContainer" style="width: 100%; height: 90vh"></div>
	</body>
</html>
