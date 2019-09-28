function titleCase(str) {
    return str.toLowerCase().split('_').map(function (word) {
        return (word.charAt(0).toUpperCase() + word.slice(1));
    }).join(' ');
}

function populateMemoryData(data, element) {
    let elem = $(element);
    var table_body = '<table class="table table-bordered table-small">';
    $.each(data, function (k, v) {
        table_body += '<tr>';
        table_body += '<td>';
        table_body += titleCase(k);
        table_body += '</td>';
        table_body += '<td>';
        table_body += v + ' MB';
        table_body += '</td>';
        table_body += '</tr>';
    });
    table_body += '</table>';
    elem.html(table_body);
}

$(function () {
    let url = '/monitoring/get-monitoring-data/memory/';
    $.get(url, function (data) {
        populateMemoryData(data, '#memory');
    }, "json");
});

