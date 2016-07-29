$("[class='adm-cb']").bootstrapSwitch();
var active_user = function(_id){
    if(!_id){
        return;
    }

    console.log("Ativando/Desativando "+_id);

    $.getjson("/admin/users/active/"+_id, function(data){
        console.data(data.data)
    });
}

$("[class='adm-cb']").bootstrapSwitch().on('switchChange.bootstrapSwitch',function(event, state){
    var id = $(this).attr('id');
    active_user(id);
});
