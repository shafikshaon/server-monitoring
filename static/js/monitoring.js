function titleCase(str) {
    return str.toLowerCase().split('_').map(function (word) {
        return (word.charAt(0).toUpperCase() + word.slice(1));
    }).join(' ');
}

function populateData(data, element) {
    let elem = $(element);
    var table_body = '<table class="table table-bordered table-small">';
    $.each(data, function (k, v) {
        table_body += '<tr>';
        table_body += '<td class="font-weight-bold">';
        table_body += titleCase(k);
        table_body += '</td>';
        table_body += '<td>';
        table_body += v;
        table_body += '</td>';
        table_body += '</tr>';
    });
    table_body += '</table>';
    elem.html(table_body);
}

function populateNetworkData(data, element) {
    let elem = $(element);
    let table_body = '<table class="table table-bordered table-small">';
    let data_length = Object.keys(data).length;
    $.each(data, function (key, value) {
        table_body += '<td class="font-weight-bold" colspan="' + data_length + '">';
        table_body += key;
        table_body += '</td>';
        $.each(value, function (k, v) {
            table_body += '<tr>';
            table_body += '<td class="font-weight-bold">';
            table_body += titleCase(k);
            table_body += '</td>';
            table_body += '<td>';
            table_body += v;
            table_body += '</td>';
            table_body += '</tr>';
        });
    });
    table_body += '</table>';
    elem.html(table_body);
}

$(function () {
    let memory_url = '/get-monitoring-data/memory/';
    $.get(memory_url, function (data) {
        populateData(data, '#memory');
    }, "json");

    let network_url = '/get-monitoring-data/network/';
    $.get(network_url, function (data) {
        populateNetworkData(data, '#network');
    }, "json");

    let uptime_url = '/get-monitoring-data/uptime/';
    $.get(uptime_url, function (data) {
        populateData(data, '#uptime');
    }, "json");

    let traffic_url = '/get-monitoring-data/traffic/';
    $.get(traffic_url, function (data) {
        populateData(data, '#traffic');
    }, "json");
});

