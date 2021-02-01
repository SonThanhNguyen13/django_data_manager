$("#data").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    let formData = new FormData(this);
    // make POST ajax call
    $.ajax({
        type: 'post',
        processData: false,
        contentType: false,
        url: document.getElementById("data").action,
        data: formData,
        success: function (response) {
            let name = response["instance"]
            $("#message").html("Added data " + name)
            $("#message").css("color", "green")
            $('#data').trigger("reset");
        },
        error: function (response) {
            // alert the error if any error occured
            document.getElementById("message").innerHTML = response["responseJSON"]["error"];
            document.getElementById("message").style.color = "red"

        }
    })
})
function openForm(){
    document.getElementById("add-frame").style.display = "block"
    document.getElementById("container-data").style.display ="none"
    $("#buttons").hide()
}
function closeForm(){
    let message = document.getElementById("message").innerHTML;
    if (message !== "No permission" && message !== ""){
        window.location.reload()
    }
    $("#buttons").show()
    document.getElementById("add-frame").style.display = "none"
    document.getElementById("container-data").style.display ="block"

}