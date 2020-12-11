#!C:\Users\DELL\AppData\Local\Programs\Python\Python39\python.exe

print('Content-type: text/html\n')

print("""<!DOCTYPE html>
<html lang="es">

<head>
    <title>Catálogo de alumnos</title>
    <meta name="title" content="Catálogo de alumnos">
    <meta name="description" content="Un listado de los alumnos de una institución">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link href="../assets/css/style.css" rel="stylesheet" type="text/css">
</head>

<body>
    <div class="titulo-pagina">
        <h1>Catálogo de alumnos</h1>
    </div>

    <div class="container">
        <!-- Botones de acción: Crear, Cargar, Descargar -->
        <div class="nav justify-content-end">
            <button class="btn btn-primary" type="button" data-toggle="modal"
                data-target="#nuevoAlumnoModal">Nuevo</button>
            <!-- <button class="btn btn-warning" type="file" data-toggle="modal" data-target="#cargarArchivoModal">Cargar</button> -->
            <button class="btn btn-warning" id="btnCargar">Cargar</button>
            <button id="btnDescargar" class="btn btn-info" type="button">Descargar</button>
        </div>

        <!-- Tabla de alumnos -->
        <div class="table-responsive">
            <table class="table table-bordered table-striped" id="tablaAlumnos">
                <thead class="thead-dark">
                    <tr style="text-align: center;">
                        <th>Num. control</th>
                        <th>Nombre del alumno</th>
                        <th>Fecha Nac.</th>
                        <th>Teléfono</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>

                </tbody>
            </table>
        </div>

        <!-- Formulario: Crear nuevo alumno -->
        <div class="modal fade" id="nuevoAlumnoModal" tabindex="-1" role="dialog" aria-labelledby="nuevoAlumnoModal"
            aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="nuevoAlumnoModalLabel">Crear nuevo alumno</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <div class="container-fluid">
                            <form>
                                <div class="form-group row">
                                    <label for="numCtrlNuevo" class="col-sm-4 col-form-label">Num. Control</label>
                                    <div class="col-sm-8">
                                        <input type="text" class="form-control" id="numCtrlNuevo"
                                            aria-describedby="numCtrlHelp" placeholder="8 dígitos">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label for="nomAlmnNuevo" class="col-sm-4 col-form-label">Nombre alumno</label>
                                    <div class="col-sm-8">
                                        <input type="text" class="form-control" id="nomAlmnNuevo"
                                            aria-describedby="nomAlmnHelp" placeholder="Nombre y apellidos">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label for="fechNacNuevo" class="col-sm-4 col-form-label">Fech. Nacimiento</label>
                                    <div class="col-sm-8">
                                        <input type="date" class="form-control" id="fechNacNuevo"
                                            aria-describedby="fechNacHelp" placeholder="dd/mm/aaaa">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label for="telNuevo" class="col-sm-4 col-form-label">Teléfono</label>
                                    <div class="col-sm-8">
                                        <input type="text" class="form-control" id="telNuevo" aria-describedby="telHelp"
                                            placeholder="10 dígitos">
                                    </div>
                                </div>
                                <div class="form-group text-right">
                                    <button id="btnCrearAlumno" type="button" class="btn btn-success">Crear</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Formulario: Editar alumno -->
        <div class="modal fade" id="editarAlumnoModal" tabindex="-1" role="dialog" aria-labelledby="nuevoAlumnoModal"
            aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="editarAlumnoModalLabel">Editar alumno</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <div class="container-fluid">
                            <form>
                                <div class="form-group row">
                                    <label for="numCtrlEditar" class="col-sm-4 col-form-label">Num. Control</label>
                                    <div class="col-sm-8">
                                        <input type="text" class="form-control" id="numCtrlEditar"
                                            aria-describedby="numCtrlHelp" placeholder="8 dígitos" readonly>
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label for="nomAlmnEditar" class="col-sm-4 col-form-label">Nombre alumno</label>
                                    <div class="col-sm-8">
                                        <input type="text" class="form-control" id="nomAlmnEditar"
                                            aria-describedby="nomAlmnHelp" placeholder="Nombre y apellidos">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label for="fechNacEditar" class="col-sm-4 col-form-label">Fech. Nacimiento</label>
                                    <div class="col-sm-8">
                                        <input type="date" class="form-control" id="fechNacEditar"
                                            aria-describedby="fechNacHelp" placeholder="dd/mm/aaaa">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label for="telEditar" class="col-sm-4 col-form-label">Teléfono</label>
                                    <div class="col-sm-8">
                                        <input type="text" class="form-control" id="telEditar"
                                            aria-describedby="telHelp" placeholder="10 dígitos">
                                    </div>
                                </div>
                                <div class="form-group text-right">
                                    <button id="btnGuardar" type="button" class="btn btn-success">Guardar</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Formulario: Cargar archivo -->
        <div class="modal fade" id="cargarArchivoModal" tabindex="-1" role="dialog" aria-labelledby="cargarArchivoModal"
            aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="editarAlumnoModalLabel">Cargar archivo</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <div class="container-fluid">
                            <form>
                                <div class="form-group row">
                                    <div class="col-sm-8">
                                        <input type="file" id="archivoCargar" aria-describedby="archivoCargarHelp" name="Datos_Alumnos">
                                    </div>
                                </div>
                                <div class="form-group text-right">
                                    <button id="btnGuardar" type="button" class="btn btn-success">Guardar</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.min.js"
        integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
    <script src="../js/main.js"></script>
</body>

</html>""")
