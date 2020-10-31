
/*Validación de Rut*/
function validarRut() {
    var rut = document.getElementById("txtRut").value;
    if (rut.length != 10) {
        alert("El largo de rut es incorrecto, debe tener 10 carácteres");
        return flase;
    }
    var suma = 0;
    var num = 3;
    for (let index = 0; index < 8; index++) {
        var car = rut.slice(index, index + 1);
        suma = suma + (num * car);
        num = num - 1;
        if (num == 1){
            num = 7;
        }
    }
    var resto = suma % 11;
    var dv= 11 - resto;
    if (dv>9){
        if (dv==10) {
            dv='K'
            
        } else {
            dv=0;
            
        }
    }
    var dv_usuario= rut.slice(-1).toUpperCase();
    if (dv!=dv_usuario){
        alert("Rut inválido, ingrese nuevamente");
        return false;
    }  else{
        alert("Rut correcto");
        return true;
    }                          
}


function validarFecha() {
    var fechaNac = document.getElementById("txtFecha").value;
    var fechaSistema = new Date();

    var anio = fechaNac.slice(0,4);
    var mes = fechaNac.slice(5,7);
    var dia = fechaNac.slice(8,10);
           
    var fechaDeNac = new Date(anio,mes-1,dia);   

    if (fechaDeNac > fechaSistema) {
        alert("Fecha de nacimiento inválida");
        return false;
        
    }else{
        alert("Fecha válida");
        return true;
    }
}






function validarNombre(){
    var n =document.getElementById("txtNombre").value;
    if(n.trim().length >2 && n.trim().length <81) {
        return true;
    }

    alert("Error. El nombre debe tener entre 3 y 80 caracteres")
    return false;
}

function validarApellido(){
    var a = document.getElementById("txtApellido").value;
    if(a.trim().length >2 && a.trim().length <81){
        return true;
    }
    alert("Error. El apellido debe tener entre 3 y 80 caracteres ")
    return false;
}

function validarUsuario(){
    var u = document.getElementById("txtUsuario").value;
    if(u.trim().length > 8){
        return true;

    }
    alert("Error. El usuario debe tener un largo que sea mayor a 8 caracteres")
    return false;
}

function validarContraseña(){
    var p = document.getElementById("txtContraseña").value;
    if (p.trim().length >8){
        return true;
    }
    alert("Error. La contraseña debe tener un largo que sea mayor a 8 caracteres")
}




function validarTodo(){
    var resp = validarRut();
    if (resp==false) {
        return false;
        
    }

    resp = validarFecha();
        if (resp==false) {
            return false;
            
        }

    var resp = validarNombre();
    if (resp==false) {
        return false;
    }

    var resp = validarApellido();
    if (resp==false){
        return false;
    }

    var resp = validarUsuario();
    if (resp==false){
        return false;
    }

    var resp = validarContraseña();
    if (resp==false){
        return false;
    }
    



}



function validarInsumo(){
    var i = document.getElementById("txtInsumo").value;
    if (i.trim().length >2 && n.trim().length <121){
        return true;
    }
    alert("El nombre del insumo debe tener entre 3 y 120 caracteres")
}

function validarPrecio(){
    var p = document.getElementById("precio").value;
    if (p > 0){
        return true;
    }
    alert("El precio debe ser mayor a 0")
}

function validarDesc(){
    var d = document.getElementById("txtDescrip").value;
        if (d.trim().length > 2 && d.length < 121){
            return true;

        }
        alert("La descripción debe tener entre 3 y 200 caracteres")
    
}
function validarStock(){
    var s = document.getElementById("txtStock").value;
    if (s >= 0){
        return true;
    }
    alert("El stock debe ser mayor o igual a 0")

}




function validarTodoInsumo(){
    var resp = validarInsumo();
    if (resp == false) {
        return false;
    }
    var resp = validarPrecio();
    if (resp == false) {
        return false;
    }
    var resp = validarDesc();
        if (resp == false){
            return false;
    }
    var resp = validarStock();
    if (resp = false){
        return false;
    }


}






