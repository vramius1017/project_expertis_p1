$(function () {

   $('form').on('submit', function () {
     $.ajax({
         data : $('form').val(),
         type : 'POST',
         url : '/result_polish/',
         success : function(response){
             console.log(response);
         },
         error: function (error) {
             console.log(error);
         }
       });
    });
});   