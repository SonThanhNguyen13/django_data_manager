$(document).ready(function() {
      document.title = "Models & Data"
});
$("#model-train-data").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    let serializedData = $(this).serialize();
    // make POST ajax call
    $.ajax({
        type: 'post',
        url: document.getElementById("model-train-data").action,
        data: serializedData,
        success: function (response) {
            // on successful creating object
            // 1. clear the form.
            $("#model-train-data").trigger('reset');
            // 2. focus
            $("#id_name").focus();
            let key = Object.keys(response)[0];
            if (key === 'Added data'){
                document.getElementById("form-label").innerHTML = "Success add data "
                document.getElementById("form-label").style.color = "green"
            }
            else{
                document.getElementById("form-label").innerHTML = "Success edit data "
                document.getElementById("form-label").style.color = "green"
            }
        },

        error: function (response) {
            // alert the error if any error occured
            document.getElementById("form-label").innerHTML = response["responseJSON"]["error"];
            document.getElementById("form-label").style.color = "red"
        }
    })
})

function openAddForm(url){
    // change label
    document.getElementById("form-label").innerHTML = "Add Model"
    // display form
    document.getElementById("add-frame").style.display = "block";
    document.getElementById("table-content").style.display = "none";
    // hide buttons
    $("#buttons").css('display', 'none')
}

function closeAddForm(){
    let message = $("#form-label").html();
    if (message.startsWith("Success")){
        location.reload()
    }
    else{
        document.getElementById("add-frame").style.display = "none";
        document.getElementById("table-content").style.display = "block";
        $("#id_model_name").focus();
        $("#buttons").css('display', 'block')
    }

}

function onClick(url){
    document.getElementById("table-content").style.display = "none";
    model_id = url.split("/")[2]
    document.getElementById("form-label").innerHTML = "Edit Data"
    document.getElementById("model-train-data").action = url;
    document.getElementById("add-frame").style.display = "block";
    $("#buttons").css('display', 'none')
}

function openDeleteConfirm(url){
    $("#buttons").css('display', 'none')
    document.getElementById("confirm-delete").action = url;
    $("#delete-item").html("Are you sure you want to delete this record?")
    $("#delete-confirm").css("display","block")
    $("#table-content").css("display", "none")
}

function closeDeleteConfirm(){
    $("#message").html("")
    $("#delete-confirm").css("display","none")
    $("#table-content").css("display", "block")
    $("#buttons").css('display', 'block')
}


$('#confirm-delete').submit(function(event){
        event.preventDefault();
        $.ajax({
                headers: {"X-CSRFToken":$('input[name="csrfmiddlewaretoken"]').val()},
                url: document.getElementById("confirm-delete").action,
                method: 'DELETE',

                success: function(response){
                    $('#delete-confirm').css("display", "none")
                    $("#message").css('color', 'green')
                    $("#message").html("Success. Redirect to previous page after 0.5 seconds")
                    setTimeout(function(){ window.location = "/model_data/"; },500);
                },
                error: function(response){
                    document.getElementById("message").innerHTML = response["responseJSON"]["error"];
                    document.getElementById("message").style.color = "red"
                }
            }
        )
    }
)
$(window).on("load",function(){
    $("#loader-wrapper").fadeOut("fast");
});
