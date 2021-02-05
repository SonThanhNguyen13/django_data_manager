$(document).ready(function() {
      document.title = "Change password"
});
function validate_change_password(){
	let password = $("#password")[0].value
	let new_password = $('#new')[0].value
	let cnf_password = $('#conf_new')[0].value
	if (password != "" && new_password != "" && cnf_password != "" && cnf_password === new_password){
			$("#icon").attr('class', 'fa fa-check')
			$("#icon").attr('style', 'color:green;');
			$('#submit').removeAttr('disabled')
	}
	else{
			$("#icon").attr('class', 'fa fa-exclamation-triangle')
      $("#icon").attr('style', 'color:red;');
      $('#submit').attr('class','btn btn-success');
      $('#submit').attr('disabled','disable');
      
	}
}
function dataFadeIn(){
	$("#container").fadeIn("slow");
}
$(window).on("load",function(){
    $("#loader-wrapper").fadeOut("fast");
});
