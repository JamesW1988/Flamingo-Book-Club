
const rows = document.getElementById("row-data")


$.ajax({
    type: 'GET',
    url: '/database/',
    success: function (response) {
        const data = response.data
        data.forEach(element => {
            var row = `<tr>
                        <td>${element.title}</td>
                        <td>${element.author}</td> 
                        <td>${element.description}</td> 
                        <td>${element.grade_level}</td> 
                        <td>${element.inventory}</td>  
                        </tr>`;
            $('.table-data tbody').append(row);
        });
    },
    error: function (error) {
        console.log(error)
    }
})



/* $('#database-form').submit(function(event){
    event.preventDefault();
    var formData = $(this).serialize();
    $.ajax({
        type: 'POST',
        url: 'database-form/',
        data: formData,
        success: function(response) {
           console.log(response.message);
        }
    });
});

$.ajax({
    type: 'GET',
    url: 'database-form/',
    data: {
      q: searchTerm
    },
    success: function(response) {
      var data = response.data;
      $('#table-body').html('');
      for(var i = 0; i < data.length; i++) {
          var row = data[i];
          $('#table-body').append(
              '<tr>' + 
                  '<td>' + row.title + '</td>' + 
                  '<td>' + row.author + '</td>' + 
                  '<td>' + row.grade_level + '</td>' + 
                  '<td>' + row.inventory + '</td>' + 
                  '<td>' + row.condition + '</td>' + 
              '</tr>'
          );
      }
    }
  }); */