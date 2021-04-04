function submitform() {
    var url = '/login/register';
    $('#loginform').attr('action', url);
    var data = JSON.stringify({
        "username": $('#username').val(),
        "password": $('#password').val()
    })
    //$('<input type="hidden" name="json"/>').val(data).appendTo('#loginform');
    $("#loginform").submit();
}