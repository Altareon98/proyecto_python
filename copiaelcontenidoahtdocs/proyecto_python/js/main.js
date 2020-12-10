$(document).ready(function () {
    reloadTable();

    $("#btnCrearAlumno").click(function () {
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
                if (parseInt(msg) > 0) {
                    alert("insercion completa")
                    $("#nuevoAlumnoModal").modal('hide')
                    reloadTable()
                } else {
                    alert("ocurrio un error")
                    $("#nuevoAlumnoModal").modal('hide')
                    reloadTable()
                }
            });
    });

    $('#btnCargar').click(function(){
        $.ajax({
            method: "GET",
            async: false,
            url: "http://localhost/p/veranos/cargarArchivo.py",
            success:function(msg){
                msg = msg.replaceAll("'", "\"")
                let json = JSON.parse(msg)
                for(item in json){
                    $.ajax({
                        method: "POST",
                        url: "http://localhost/p/veranos/alumno.py",
                        data: { accion: 'INSERT', numControl: json[item].Num_Control, nombre: json[item].Nombre, fechaNacimiento: json[item].Fecha_Nacimiento, telefono: json[item].Telefono },
                        success:function(msg){
                            
                        }
                    })
                }
                alert("hecho");
            }
        })
        reloadTable()
    });


    $('#btnGuardar').click(function(){
        let numControl = $("#numCtrlEditar").val()
        let nombre = $("#nomAlmnEditar").val()
        var fechaNacimiento = $("#fechNacEditar").val()
        fechaNacimiento = fechaNacimiento.split("/").reverse().join("-");
        let telefono = $("#telEditar").val()
        $.ajax({
            method: "POST",
            url: "http://localhost/p/veranos/alumno.py",
            data: { accion: 'UPDATE', numControl: numControl, nombre: nombre, fechaNacimiento: fechaNacimiento, telefono: telefono },
            success:function(msg){
                if (parseInt(msg) > 0) {
                    alert("actualizacion completa")
                } else {
                    alert("ocurrio un error")
                }
                $("#editarAlumnoModal").modal('hide')
                reloadTable()
            }
        })
    });

    $('#btnDescargar').click(function(){
        $.ajax({
            method: "GET",
            url: "http://localhost/p/veranos/generarArchivo.py",
            success:function(msg){
                alert(msg)
            }
        })
    });
});

function reloadTable() {
    $("#tablaAlumnos tbody").html("")
    $.ajax({
        method: "POST",
        url: "http://localhost/p/veranos/alumno.py",
        data: { accion: 'SELECTALL' }
    })
        .done(function (msg) {
            msg = msg.replaceAll("'", "\"")
            let json = JSON.parse(msg)
            for (item in json) {
                var row = "<tr>"
                row = row + "<td>" + json[item].Num_Control + "</td>"
                row = row + "<td>" + json[item].Nombre + "</td>"
                row = row + "<td>" + json[item].Fecha_Nacimiento + "</td>"
                row = row + "<td>" + json[item].Telefono + "</td>"
                row = row + "<td style='text-align: center'><input class='btn btn-outline-primary btn-sm editar' type='button' value='Editar'> <input class='btn btn-outline-danger btn-sm eliminar' type='button' value='Eliminar'></td>"
                row = row + "</tr>"
                $("#tablaAlumnos").append(row)
            }

            $("#tablaAlumnos tbody tr td").find('.editar').click(function () {
                let numControl = ($(this).closest('tr').find('td').html())
                $.ajax({
                    method: "POST",
                    url: "http://localhost/p/veranos/alumno.py",
                    data: { accion: 'SELECTWHERE', numControl: numControl },
                    success:function(msg){
                        msg = msg.replaceAll("'", "\"")
                        let json = JSON.parse(msg)
                        let fechaNacimiento = json.Fecha_Nacimiento.split("-").reverse().join("/");

                        $('#numCtrlEditar').val(json.Num_Control)
                        $('#nomAlmnEditar').val(json.Nombre)
                        $('#fechNacEditar').val(fechaNacimiento)
                        $('#telEditar').val(json.Telefono)
                        $('#editarAlumnoModal').modal()
                    }
                })
            });

            $("#tablaAlumnos tbody tr td").find('.eliminar').click(function () {
                let numControl = ($(this).closest('tr').find('td').html())
                if (confirm("Realmente desea eliminar el usuario: " + numControl)) {
                    $.ajax({
                        method: "POST",
                        url: "http://localhost/p/veranos/alumno.py",
                        data: { accion: 'DELETE', numControl: numControl },
                        success: function (msg) {
                            if (parseInt(msg) > 0) {
                                alert("Se elimino el usuario")
                                reloadTable()
                            } else {
                                alert("ocurrio un error")
                                reloadTable()
                            }
                        }
                    })
                }
            });
        });
}