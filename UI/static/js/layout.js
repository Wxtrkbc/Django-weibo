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
    $('.login_mt').click(function () {
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
            dataType: 'json',
            data: {username:user ,
                   password: pwd
                    },

            success:function (data) {
                if(data.status){
                    $("#accountDialog").addClass('hide');
                }else{
                    alert(1)
                }
            }
        })
    })
    
});


