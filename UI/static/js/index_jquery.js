/**
 * Created by Administrator on 2016/9/23.
 */
$(function(){
	$('.emotion').qqFace({
		id : 'facebox',
		assign:'saytext',
		path:'/static/plugins/emoji/arclist/'	//表情存放的路径
	});
	$(".sub_btn").click(function(){
		var str = $("#saytext").val();
		$("#show").html(replace_em(str));
	});
});