var server = "http://127.0.0.1:5000";
var op_num = { 'sum': [3, 4] };

function update_var() {
    var n1 = parseFloat($("#n1").val());
    var n2 = parseFloat($("#n2").val());
    op_num['sum'] = [n1, n2];
}
$(function() {
    $("#sum").click(function() {
        var appdir = '/';
        var send_msg = "<p>Sending numbers</p>";
        var received_msg = "<p>Result returned</p>";
        update_var();
        console.log(send_msg);
        $('#message').html(send_msg);
        $.ajax({
                type: "POST",
                url: server + appdir,
                data: JSON.stringify(op_num),
                dataType: 'json',
            })
            .done(function(data) {
                console.log(data);
                $('#n3').val(data['sum']);
                $('#message').html(received_msg + data['msg']);
            });
    });
});