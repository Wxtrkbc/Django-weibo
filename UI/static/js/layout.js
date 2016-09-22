/**
 * Created by Administrator on 2016/9/22.
 */

// 登录Tab
$(function () {
    $('.tab_bar a').click(function () {
        $(this).addClass('cur').siblings().removeClass('cur');
        $("[node_type="+$(this).attr('node-type')+"]").removeClass('hide').siblings().addClass("hide");

    })

    //点击登录弹出模态对话框
    $('.S_txt1').click(function () {
        $("#accountDialog").removeClass('hide');
    })
    
    // 关闭对话框
    
    $("[node-type='close']").click(function () {
        $("#accountDialog").addClass('hide');
    })
    

    // 提交数据

    $("[node-type='submitBtn']").click(function () {
        var user = $("#username").val();
        var pwd = $("#password").val();
        $.ajax({
            url: '/login/',
            type:'POST',
            data: {username:user ,
                   password: pwd
                    },

            success:function (data) {
                console.log(data)
            }
        })
    })
    
});


