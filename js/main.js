$(document).ready(function () {
    reloadTable();
    
    $("#btnCrearAlumno").click(function (){
        let numControl = $("#numCtrlNuevo").val()
        let nombre = $("#nomAlmnNuevo").val()
        var fechaNacimiento = $("#fechNacNuevo").val()
        fechaNacimiento = fechaNacimiento.split("/").reverse().join("-");
        let telefono = $("#telNuevo").val()
        $.ajax({
            method: "POST",
            url: "http://localhost/p/veranos/alumno.py",
            data: { accion: 'INSERT', numControl: numControl, nombre: nombre, fechaNacimiento: fechaNacimiento, telefono: telefono }
        })
        .done(function (msg) {
            if(parseInt(msg) > 0){
                alert("insercion completa")
                $("#nuevoAlumnoModal").modal('hide')
                reloadTable()
            }else{
                alert("ocurrio un error")
                $("#nuevoAlumnoModal").modal('hide')
                reloadTable()
            }
        });
    });

});

function reloadTable(){
    $("#tablaAlumnos tbody").html("")
    $.ajax({
        method: "POST",
        url: "http://localhost/p/veranos/alumno.py",
        data: { accion: 'SELECTALL'}
    })
    .done(function (msg) {
        msg = msg.replaceAll("'","\"")
        console.log(msg)
        let json = JSON.parse(msg)
        for(item in json){
            var row = "<tr>"
            row = row + "<td>" + json[item].Num_Control + "</td>"
            row = row + "<td>" + json[item].Nombre + "</td>"
            row = row + "<td>" + json[item].Fecha_Nacimiento + "</td>"
            row = row + "<td>" + json[item].Telefono + "</td>"
            row = row + "<td style='text-align: center'><input class='btn btn-outline-primary btn-sm' type='button' data-toggle='modal'data-target='#editarAlumnoModal' value='Editar'> <input class='btn btn-outline-danger btn-sm' type='button' value='Eliminar'></td>"
            row = row + "</tr>"
            $("#tablaAlumnos").append(row)
        }
    });
}