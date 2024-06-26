class Persona{
    constructor(rut, nombre, apellido, edad, peso, estatura){
        this.rut = rut;
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
        this.peso = peso;
        this.estatura = estatura;
        this.imc = 0;
        this.estado = " "
    }

    /**
     * ! Metodos get
     */

    get getRut(){
        return this.rut;
    }

    get getNombre(){
        return this.nombre;
    }

    get getApellido(){
        return this.apellido;
    }
     get getEdad(){
        return this.edad;
    }

    get getPeso(){
        return this.peso;
    }

    get getEstatura(){
        return this.estatura;
    }

    get getImc(){
        return this.imc;
    }
    
    get getEstado(){
        return this.estado;
    }

    /**
     * ! Funciones de la clase
     */

    calcImc(){
        this.imc = (this.peso/Math.pow(this.estatura,2)).toFixed(3);
    }
}

let personas = [];

/**
 * ! Funciones del programa
 * ? addPersona: agregar una persona con sus atributos a la lista personas[]
 * ? findPersona: identifica si el rut escrito está asociado a una persona agregada a la lista personas[]
 */

let addPersona = function(){
    let rt = document.getElementById("p-rut").value;
    let nom = document.getElementById("p-nom").value;
    let ape = document.getElementById("p-ape").value;
    let edad = parseInt(document.getElementById("p-edad").value);
    let peso = parseInt(document.getElementById("p-peso").value);
    let est = parseFloat(document.getElementById("p-est").value);

    let p = new Persona(rt, nom, ape, edad, peso, est);
    p.calcImc();
    personas.push(p);
    alert("Persona Agregada");
    console.log(personas);
}

let findPersona = function(){
    let buscar = document.getElementById("b-rut").value;
    let color = "yellow";
    let p = personas.find(item => item.getRut === buscar);

    if (p != undefined){
        alert("Encontrada")
        document.getElementById("r-rut").innerHTML = "Rut: "+p.getRut;
        document.getElementById("r-nom").innerHTML = "Nombre:"+p.getNombre+" "+p.getApellido;
        document.getElementById("r-edad").innerHTML = "Edad: "+p.getEdad;
        document.getElementById("r-peso").innerHTML = "Peso: "+p.getPeso;
        document.getElementById("r-est").innerHTML = "Estatura: "+p.getEstatura;
        document.getElementById("r-imc").innerHTML = "IMC: "+p.getImc;
        document.getElementById("r-estado").innerHTML = "Estado: "+p.getEstado;
    }else{
        alert("No encontrada")
        document.getElementById("r-rut").innerHTML="";
        document.getElementById("r-nom").innerHTML="";
        document.getElementById("r-edad").innerHTML="";
    }
}