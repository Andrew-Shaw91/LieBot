$(document).ready(function() {
  $("#toggle_password").on("change", function() {
    const type = $(this).is(":checked") ? "text" : "password";
    $("#login_password").attr("type", type);
  });
});

