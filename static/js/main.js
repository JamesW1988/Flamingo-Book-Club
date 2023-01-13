
$(document).ready(function () {
    $('#book-table').DataTable({
        scrollY:1000,
        ajax: {
            url: '/database/',
            type: 'GET',
            datatype: 'json'
        },
        columns: [
            { data: 'title' },
            { data: 'author' },
            { data: 'description' },
            { data: 'grade_level' },
            { data: 'inventory' },
        ],
    });
});



