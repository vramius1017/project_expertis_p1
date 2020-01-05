/** sur event click du button du formulaire creation d'un json  **/
/**  si OK response afficher sinon affiche erreur **/
$(function() {
    $('button').click(function() { 
            url: '/ajax_data/',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            };
            error: function(error) {
                console.log(error);
            }
        });
    });
