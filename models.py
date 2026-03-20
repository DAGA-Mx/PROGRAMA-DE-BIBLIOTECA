class Persona:
    def __init__(self, idPersona, nombre):
        self.idPersona = idPersona
        self.nombre = nombre

class Usuario(Persona):
    def __init__(self, idPersona, nombre, limitePrestamos):
        super().__init__(idPersona, nombre)
        self.limitePrestamos = limitePrestamos
        self.listaActiva = []

    def mostrar_detalle(self):
        return f"ID: {self.idPersona} | Usuario: {self.nombre} | Límite Préstamos: {self.limitePrestamos}"

class Bibliotecario(Persona):
    def __init__(self, idPersona, nombre):
        super().__init__(idPersona, nombre)

    def gestionarPrestamo(self, usuario, material, fechaInicio, fechaDevolucion):
        if material.disponible and len(usuario.listaActiva) < usuario.limitePrestamos:
            nuevo_prestamo = Prestamo(len(usuario.listaActiva) + 1, fechaInicio, fechaDevolucion, material)
            usuario.listaActiva.append(nuevo_prestamo)
            material.disponible = False
            return f"[ÉXITO] Préstamo autorizado por {self.nombre}. '{material.titulo}' asignado a {usuario.nombre}."
        elif not material.disponible:
            return f"[ERROR] El material '{material.titulo}' no está disponible."
        else:
            return f"[ERROR] {usuario.nombre} ha alcanzado su límite de préstamos."

    def transferirMaterial(self, material, sucursalDestino):
        return f"El bibliotecario {self.nombre} transfirió '{material.titulo}' a la sucursal {sucursalDestino.nombre}."

    def mostrar_detalle(self):
        return f"ID: {self.idPersona} | Bibliotecario: {self.nombre} | Sucursal Asignada"

class Material:
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible):
        self.idMaterial = idMaterial
        self.titulo = titulo
        self.añoPublicacion = añoPublicacion
        self.disponible = disponible

class Libro(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, autor, isbn, genero):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

    def mostrar_detalle(self):
        estado = "DISPONIBLE" if self.disponible else "PRESTADO"
        return f"ID: {self.idMaterial} | {self.titulo} ({self.añoPublicacion}) | Cat: Libro - {estado}"

class MaterialDigital(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, tipoArchivo, urlDescarga, tamañoMB):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamañoMB = tamañoMB

    def mostrar_detalle(self):
        return f"ID: {self.idMaterial} | {self.titulo} ({self.tipoArchivo}) | Cat: Digital - {self.tamañoMB}MB"

class Revista(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, edicion, periodicidad):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.edicion = edicion
        self.periodicidad = periodicidad

class Prestamo:
    def __init__(self, idPrestamo, fechaInicio, fechaDevolucion, material):
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.material = material

class Penalizacion:
    def __init__(self, monto, motivo, pagada):
        self.monto = monto
        self.motivo = motivo
        self.pagada = pagada

    def calcularMulta(self, dias_retraso):
        self.monto = dias_retraso * 15.0
        return f"Multa calculada: ${self.monto} por {dias_retraso} días de retraso."

    def bloquearUsuario(self):
        if not self.pagada:
            return "Usuario BLOQUEADO en el sistema por adeudo de penalización."
        return "Usuario activo."

class Sucursal:
    def __init__(self, idSucursal, nombre):
        self.idSucursal = idSucursal
        self.nombre = nombre
        self.catalogoLocal = []

class Catalogo:
    def buscarPorAutor(self, autor, lista_materiales):
        resultados = [m.titulo for m in lista_materiales if isinstance(m, Libro) and m.autor == autor]
        return resultados