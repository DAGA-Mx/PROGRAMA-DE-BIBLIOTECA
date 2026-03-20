from models import *

print("---CARGANDO CATÁLOGO DE LIBROS---")

libros_fisicos = [
    Libro(101, "Python for Data Analysis", 2022, True, "Wes McKinney", "978-149", "Ciencia de Datos"),
    Libro(102, "Moneyball", 2003, True, "Michael Lewis", "978-039", "Deportes"),
    Libro(103, "Clean Code", 2008, True, "Robert C. Martin", "978-013", "Software"),
    Libro(104, "Data Science from Scratch", 2019, True, "Joel Grus", "978-144", "Tecnología"),
    Libro(105, "The Lean Startup", 2011, True, "Eric Ries", "978-030", "Negocios"),
    Libro(106, "Machine Learning con Scikit-Learn", 2020, True, "Aurelien Geron", "978-149", "Tecnología"),
    Libro(107, "El Juego Perfecto", 2008, True, "W. W. Norton", "978-038", "Deportes"),
    Libro(108, "Deep Learning", 2016, True, "Ian Goodfellow", "978-026", "IA"),
    Libro(109, "Estadística Práctica para Data Scientists", 2021, True, "Peter Bruce", "978-149", "Ciencia de Datos"),
    Libro(110, "Breve Historia del Tiempo", 1988, True, "Stephen Hawking", "978-055", "Ciencia")
]

for ejemplar in libros_fisicos:
    print(ejemplar.mostrar_detalle())

print("---CARGANDO CATÁLOGO DIGITAL---")

recursos_digitales = [
    MaterialDigital(201, "Intro a Pandas (Videotutorial)", 2023, True, "MP4", "/descargas/pandas", 550.5),
    MaterialDigital(202, "Estructuras de Datos Avanzadas", 2024, True, "PDF", "/descargas/eda", 12.5),
    MaterialDigital(203, "Algoritmos de Optimización", 2022, True, "PDF", "/descargas/alg", 15.0),
    MaterialDigital(204, "Gestión de Equipos Remotos", 2021, True, "MP4", "/descargas/mgmt", 850.0),
    MaterialDigital(205, "Dataset Estadísticas MLB 2025", 2025, True, "CSV", "/descargas/mlb", 15.2),
    MaterialDigital(206, "Guía de SQL Básico", 2020, True, "PDF", "/descargas/sql", 5.0),
    MaterialDigital(207, "Curso de Python Avanzado", 2023, True, "MP4", "/descargas/py", 1024.0),
    MaterialDigital(208, "Reglas Oficiales del Béisbol", 2024, True, "PDF", "/descargas/reglas", 3.8),
    MaterialDigital(209, "Manual de Jupyter Notebooks", 2022, True, "PDF", "/descargas/jupyter", 8.4),
    MaterialDigital(210, "Podcast: Hablemos de Data", 2025, True, "MP3", "/descargas/podcast", 45.0)
]

for digital in recursos_digitales:
    print(digital.mostrar_detalle())

print("---DANDO DE ALTA USUARIOS---")

usuarios_registrados = [
    Usuario(301, "Gerardo Gonzalez", 3), Usuario(302, "Carlos Romero", 5),
    Usuario(303, "Maria Fernandez", 2), Usuario(304, "Luis Ramirez", 4),
    Usuario(305, "Ana Martinez", 3), Usuario(306, "Roberto Sanchez", 5),
    Usuario(307, "Sofia Lopez", 2), Usuario(308, "Diego Hernandez", 10),
    Usuario(309, "Valeria Torres", 3), Usuario(310, "Juan Pablo Ruiz", 2)
]

for u in usuarios_registrados:
    print(u.mostrar_detalle())

print("---DANDO DE ALTA BIBLIOTECARIOS---")

personal_biblioteca = [
    Bibliotecario(401, "Patricia Medina"), Bibliotecario(402, "Jorge Vargas"),
    Bibliotecario(403, "Elena Morales"), Bibliotecario(404, "Francisco Rios"),
    Bibliotecario(405, "Daniela Castro"), Bibliotecario(406, "Sergio Mendoza"),
    Bibliotecario(407, "Monica Ortiz"), Bibliotecario(408, "Ricardo Silva"),
    Bibliotecario(409, "Andrea Castillo"), Bibliotecario(410, "Hugo Navarro")
]

for p in personal_biblioteca:
    print(p.mostrar_detalle())

print("---VALIDACIÓN DE DATOS FINALIZADA---")

print("---INICIANDO PROCESO DE PRÉSTAMO---")

sede_principal = Sucursal(1, "Biblioteca Central Puebla")
encargado = personal_biblioteca[0]
solicitante = usuarios_registrados[0]

print(f"Sucursal Activa: {sede_principal.nombre}")
print(f"Bibliotecario en turno: {encargado.nombre}")
print(f"Usuario: {solicitante.nombre} (Límite: {solicitante.limitePrestamos} materiales)")

print("\n[SISTEMA]: Solicitando préstamos...")
print(encargado.gestionarPrestamo(solicitante, libros_fisicos[0], "2026-03-01", "2026-03-15"))
print(encargado.gestionarPrestamo(solicitante, libros_fisicos[2], "2026-03-01", "2026-03-15"))

print("\n[SISTEMA]: Validando disponibilidad de inventario físico...")
print(f"¿El libro '{libros_fisicos[0].titulo}' sigue en el estante?: {libros_fisicos[0].disponible}")

print("---SIMULANDO RETRASO EN DEVOLUCIÓN---")

multa = Penalizacion(0.0, "Retraso de 3 días en entrega", False)
print(multa.calcularMulta(3))
print(f"[ALERTA ESTADO]: {multa.bloquearUsuario()}")

print(f"\nResumen de Cuenta de {solicitante.nombre}:")
print(f"Materiales Activos: {len(solicitante.listaActiva)}")
print(f"Adeudo Pendiente: ${multa.monto}")
print("Estado: BLOQUEADO. Ticket generado en PDF.")