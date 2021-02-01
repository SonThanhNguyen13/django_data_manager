$("#data").submit(function(e){
        // submit using ajax
        e.preventDefault();
        let formData = new FormData(document.getElementById("data"));
        // ajax call
        $.ajax({
            type:"POST",
            url: document.getElementById("data").action,
            processData: false,
            contentType: false,
            data: formData,
            success: function(response){
                // get data
                let fields = JSON.parse(response["instance"])[0]["fields"]
                // update html =))) 2 tired and 2 long
                console.log(fields[["data_category"].name])
                $("#name").html(fields["name"])
                $("#category").html(fields["data_category"])
                $("#size_on_disk").html(fields["size_on_disk"] + " GB")
                $("#directory_of_data").html(fields["directory_of_data"])
                $("#number_of_images").html(fields["number_of_images"])
                $("#number_of_classes").html(fields["number_of_classes"])
                $("#iqa").html(fields["iqa_0"] + ", " + fields["iqa_1"] + ", " + fields["iqa_2"] + ", " + fields["iqa_3"] + ", " + fields["iqa_4"])
                $("#shape").html(fields["shape_0"] + ", " + fields["shape_1"] + ", " + fields["shape_2"] + ", " + fields["shape_3"] + ", " + fields["shape_4"])
                $("#analyzed").html(fields["analyzed"])
                $("#best_result").html(fields["best_result"])
                $("#best_analyzed_model").html(fields["best_analyzed_model"])
                if(fields["data_avatar"]){
                    $("#image").attr("src", "/media/" + fields["data_avatar"])
                }
                else {
                    $("#image").attr("src", "/static/images/db.png")
                }
                // show message
                $("#message").css('color', 'green')
                $("#message").html("Success")

            },
            error: function (response) {
                // alert the error if any error occured
                document.getElementById("message").innerHTML = response["responseJSON"]["error"];
                document.getElementById("message").style.color = "red"
            }
        })
    }
);
function openForm(){
    document.getElementById("edit-frame").style.display = "block"
    document.getElementById("data-detail-content").style.display ="none"
    $('.my-button').css('display', 'none')
}
function closeForm(){
    document.getElementById("edit-frame").style.display = "none"
    $('.my-button').css('display', 'block')
    document.getElementById("data-detail-content").style.display ="flex"
    $("#message").html("");
}

function openDeleteConfirm(){
    $("#delete-confirm").css("display","block")
    $("#data-detail-content").css("display", "none")
    $('.my-button').css('display', 'none')
}
function closeDeleteConfirm(){
    $("#delete-confirm").css("display","none")
    $("#data-detail-content").css("display", "flex")
    $('.my-button').css('display', 'block')
    $("#message").html("");
}

$('#confirm-delete').submit(function(event){
        event.preventDefault();
        $.ajax({
                headers: {"X-CSRFToken":$('input[name="csrfmiddlewaretoken"]').val()},
                url: document.getElementById("data").action,
                method: 'DELETE',

                success: function(response){
                    $("#message").css('color', 'green')
                    $("#message").html("Success. Redirect to data page after 2 seconds")
                    $("#delete-confirm").css("display","none")
                    $("#data-detail-content").css("display", "none")
                    $('.my-button').css('display', 'none')
                    setTimeout(function(){ window.location = "/data/"; },2000);
                },
                error: function(response){
                    document.getElementById("message").innerHTML = response["responseJSON"]["error"];
                    document.getElementById("message").style.color = "red"
                }
            }
        )
    }
)