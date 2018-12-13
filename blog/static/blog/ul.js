$(function(){
    $(".cominput").on("keyup", function(){
        var fullnum = 300;
        var num = $(".cominput").val()
        var nums = num.length;
        $(".nums").text(nums+"/"+fullnum)
    });

    $(".btn_gnb").on('click', function(){
        $("html").toggleClass('gnb_open')
    });

    $(".cominput").on("keydown", function(key){
        if (key.keyCode == 13 && !key.shiftKey) {
                key.preventDefault();
                $(".post-form").submit();
                $(".login_submit").get(0).click();
        }
    });
    })
