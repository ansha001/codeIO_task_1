$(".message a").click(function () {

  if($(".register").css("display")=="none"){
    $(".login").slideToggle();
    $(".register").slideToggle();
  }
  else{
    $(".register").slideToggle();
    $(".login").slideToggle();
  }
});

// $(".message a").click(function () {
//     $("form").animate({ height: "toggle"}, "slow");
//   });

var name = $(".name");
var password = $(".password");
var password2 = $(".password2");
var email = $(".email");

function setError(className,error){
  $(className).html()
}
