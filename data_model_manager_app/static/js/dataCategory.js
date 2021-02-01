$("#data-category").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    let serializedData = $(this).serialize();
    // make POST ajax call
    $.ajax({
        type: 'post',
        url: document.getElementById("data-category").action,
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            // 1. clear the form.
            $("#data-category").trigger('reset');
            // 2. focus
            $("#id_name").focus();
            let key = Object.keys(response)[0];
            if (key === 'Add data'){
                let name = response["Add data"]
                document.getElementById("message").innerHTML = "Added category " + name;
                document.getElementById("message").style.color = "green"
                location.reload()
            }
            else{
                let instance = JSON.parse(response["Edit data"]["instance"]);
                let id = instance[0]["pk"];
                let name = instance[0]["fields"]["name"]
                document.getElementById(id).innerHTML = name
                document.getElementById("message").innerHTML = "Success edit category";
                document.getElementById("message").style.color = "green"
            }
        },

        error: function (response) {
            // alert the error if any error occured
            document.getElementById("message").innerHTML = response["responseJSON"]["error"];
            document.getElementById("message").style.color = "red"
        }
    })
})
function openAddForm(url){
    // change label
    document.getElementById("form-label").innerHTML = "Add category"
    // display form
    document.getElementById("add-frame").style.display = "block";
    document.getElementById("data-category").action = url
    document.getElementById("table-content").style.display = "none";
}

function closeAddForm(){
    document.getElementById("add-frame").style.display = "none";
    document.getElementById("table-content").style.display = "block";
    $("#id_name").focus();
}


function onClick(url){
    document.getElementById("table-content").style.display = "none";
    data_id = url.split("/")[3]
    name = document.getElementById(data_id).innerHTML
    document.getElementById("form-label").innerHTML = "Edit category " + name
    document.getElementById("data-category").action = url;
    document.getElementById("add-frame").style.display = "block";
}