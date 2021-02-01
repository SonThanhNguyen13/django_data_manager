function validate(){
    let username = $('#username')[0].value
    let password = $('#password')[0].value
    if (username === "" || password === ""){
        $('#submit').attr('disabled','disable')
    }
    else{
        $('#submit').removeAttr('disabled')
    }
}