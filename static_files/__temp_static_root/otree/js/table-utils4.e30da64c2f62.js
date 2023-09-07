/*
Lame trick...I increment the filename when I release a new version of this file,
because on runserver, Chrome caches it, so all oTree users developing on Chrome
would need to Ctrl+F5.
 */

function populateTableBody($tbody, rows) {
    tbody = $tbody[0];
    for (let row of rows) {
        tbody.appendChild(createTableRow(row));
    }
}

function truncateStringEllipsis(str, num) {
  if (str.length > num) {
    return str.slice(0, num) + "…";
  } else {
    return str;
  }
}


function makeCellDatasetValue(value) {
    if (value === null) return '';
    return value.toString();
}

function makeCellDisplayValue(value, fieldName) {
    if (value === null) {
        return '';
    }
    if (fieldName === '_last_page_timestamp') {
        let date = new Date(parseFloat(value) * 1000);
        let dateString = date.toISOString();
        return `<time class="timeago" datetime="${dateString}"></time>`;
    }
    return value.toString();
}

function createTableRow(row) {
    let tr = document.createElement('tr');
    for (let [field, value] of Object.entries(row)) {
        let td = document.createElement('td');
        td.dataset.field = field;
        td.dataset.value = makeCellDatasetValue(value);
        td.innerHTML = makeCellDisplayValue(value, field);
        tr.appendChild(td)
    }
    return tr;
}

function updateDraggable($table) {
    $table.toggleClass(
        'draggable',
        ($table.get(0).scrollWidth > $table.parent().width())
        || ($table.find('tbody').height() >= 450));
}

function flashGreen($ele) {
    $ele.css('background-color', 'green');
    $ele.animate({
            backgroundColor: "white"
        },
        10000
    );
}


let diffpatcher = jsondiffpatch.create({
    objectHash: (obj) => obj.numeric_label
});

function updateTable($table, new_json) {
    let changeDescriptions = [];
    let old_json = $table.data("raw");
    let $tbody = $table.find('tbody');
    // build table for the first time
    if (old_json === undefined) {
        populateTableBody($tbody, new_json);
    } else {
        let deltas = diffpatcher.diff(old_json, new_json);
        if (deltas) {
            for (let [key, delta] of Object.entries(deltas)) {
                if (key === '_t') continue;
                // 2017-08-13: when i have time, i should update this
                // to the refactor I did in SessionMonitor.html
                let rowNum = parseInt(key);
                let $row = $tbody.find(`tr:eq(${rowNum})`);
                let rowChanges = [];
                for (let header_name of Object.keys(delta)) {
                    let cell_to_update = $row.find(`td[data-field='${header_name}']`);
                    let rawValue = delta[header_name][1];
                    let new_value = makeCellDisplayValue(rawValue);
                    cell_to_update.text(new_value);
                    flashGreen(cell_to_update);

                    let fieldName = header_name.split('.').pop();
                    let newValueTrunc = truncateStringEllipsis(new_value, 7);
                    rowChanges.push(`${fieldName}=${newValueTrunc}`);
                }
                // @ makes it easier to scan visually
                changeDescriptions.push(`@P${rowNum+1}: ${rowChanges.join(', ')}`)
            }
        }
    }
    $table.data("raw", new_json);
    updateDraggable($table);
    return changeDescriptions;
}


function makeTableDraggable($table) {
    var mouseX, mouseY;
    $table.mousedown(function (e) {
        e.preventDefault();
        $table.addClass('grabbing');
        mouseX = e.pageX;
        mouseY = e.pageY;
    }).on('scroll', function () {
        $table.find('> thead, > tbody').width($table.width() + $table.scrollLeft());
    });
    $(document)
        .mousemove(function (e) {
            if (!$table.hasClass('grabbing')) {
                return;
            }
            e.preventDefault();
            $table.scrollLeft($table.scrollLeft() - (e.pageX - mouseX));
            var $tableBody = $table.find('tbody');
            $tableBody.scrollTop($tableBody.scrollTop() - (e.pageY - mouseY));
            mouseX = e.pageX;
            mouseY = e.pageY;
        }).mouseup(function (e) {
        if (!$table.hasClass('grabbing')) {
            return;
        }
        e.preventDefault();
        $table.removeClass('grabbing');
    });
}
