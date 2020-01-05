$(function () {

   $('form').on('submit', function () {
     $.ajax({
         data : $('form').val(),
         type : 'POST',
         url : '/',
         success : function(response){
             console.log(response);
         },
         error: function (error) {
             console.log(error);
         }
       });
    });
});   