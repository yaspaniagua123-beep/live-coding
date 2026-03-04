
function registrar() {
    const usuario = document.getElementById("usuario").value;
    const email = document.getElementById("cor").value;
    const cont = document.getElementById("cont").value;

    if (!usuario || !email || !cont) { alert("Completa todos los campos"); return; }

    let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];
    if (usuarios.find(u => u.usuario === usuario || u.email === email)) {
        alert("Usuario o email ya existe");
        return;
    }

    usuarios.push({usuario, email, password: cont});
    localStorage.setItem("usuarios", JSON.stringify(usuarios));
    alert("Usuario registrado correctamente");
    window.location.href = "login.html";
}

function login() {
    const usuario = document.getElementById("usuario").value;
    const cont = document.getElementById("cont").value;

    let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];
    let user = usuarios.find(u => u.usuario === usuario && u.password === cont);

    if (user) {
        localStorage.setItem("usuarioActual", usuario);
        alert("Login exitoso");
        window.location.href = "foro.html";
    } else {
        alert("Usuario o contraseña incorrectos");
    }
}

function publicar() {
    const texto = document.getElementById("mensaje").value.trim();
    const usuario = localStorage.getItem("usuarioActual");

    if (!usuario) { alert("Debes iniciar sesión"); return; }
    if (!texto) { alert("Escribe un mensaje"); return; }

    let mensajes = JSON.parse(localStorage.getItem("mensajes")) || [];
    mensajes.push({autor: usuario, texto: texto, fecha: new Date().toLocaleString()});
    localStorage.setItem("mensajes", JSON.stringify(mensajes));

    document.getElementById("mensaje").value = "";
    cargarMensajes();
}

function cargarMensajes() {
    const muro = document.getElementById("muro");
    if (!muro) return;

    const mensajes = JSON.parse(localStorage.getItem("mensajes")) || [];
    muro.innerHTML = "";

    mensajes.forEach(m => {
        const div = document.createElement("div");
        div.className = "mensaje";
        div.innerText = `${m.autor}: ${m.texto} (${m.fecha})`;
        muro.appendChild(div);
    });
}

function cerrarSesion() {
    localStorage.removeItem("usuarioActual");
    window.location.href = "login.html";
}

window.addEventListener("load", () => {
    const usuario = localStorage.getItem("usuarioActual");
    if (!usuario) window.location.href = "login.html";

    document.getElementById("bienvenida").innerText = `Bienvenido, ${usuario}!`;
    cargarMensajes();
});