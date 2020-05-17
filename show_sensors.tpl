<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="2">
    <title>Sensor Readout</title>
    <style>
    table, th, td {
      border: 1px solid black;
    }
    th, td {    
      padding: 20px;
    }
    </style>

</head>
<body>

    <table>

        <tr>
            <th>Temp</th>
            <th>Pres</th>
            <th>Alti</th>
            <th>Moti</th>
        </tr>
        <tr>
            <td>{{conversion}}</td>
            <td>{{adjpressure}}</td>
            <td>{{altitude}}</td>
            <td>{{pirstatus}}</td>
        </tr>

    </table>

</body>
</html>
