import json

SCRUM = {
    "tablero": "EXSF_Medina_Scrum",
    "caso": "Banco Girasol del Peru",
    "columnas": ["Por hacer", "En progreso", "En pruebas", "Hecho"],
    "epica": {
        "id": "EP01",
        "titulo": "Museo RA del Ciclo del Agua y Clasificador Web de Residuos",
        "objetivo_sprint_2_semanas": "Entregar prototipo RA con 4 etapas y pausa/continuar, y clasificador de residuos (paper, plastic, metal) con validacion de formato en 2 semanas.",
    },
    "historias": [
        {
            "id": "HU01",
            "titulo": "Etapas y pausa en RA del ciclo del agua",
            "descripcion": "Como visitante, quiero cambiar entre 4 etapas y pausar/continuar sin recargar, para entender el ciclo del agua.",
            "criterios_aceptacion": [
                "3+ objetos 3D y texto educativo en vista 3D y con marcador Hiro",
                "Cambio entre 4 etapas sin recargar",
                "Botones Pausar/Continuar y eventos markerFound/markerLost",
            ],
            "prioridad": "Alta",
            "estimacion": "5 SP",
            "responsable": "Ryan Medina",
            "estado": "Hecho",
            "subtarea": {
                "id": "SUB-HU01",
                "titulo": "Logica de etapas, pausa y marcador en escena.js y controles.js",
                "estado": "Hecho",
            },
        },
        {
            "id": "HU02",
            "titulo": "Clasificacion de residuos JPG/PNG con puntajes",
            "descripcion": "Como usuario, quiero subir imagen JPG/PNG (o camara/alternativa) y ver clase y puntajes o rechazo invalido, para identificar residuos.",
            "criterios_aceptacion": [
                "Modelo MobileNetV2 evaluado en test con metricas y matriz de confusion",
                "Interfaz muestra clase y puntajes y rechaza archivos invalidos",
                "Camara o carga alternativa verificada",
            ],
            "prioridad": "Alta",
            "estimacion": "8 SP",
            "responsable": "Ryan Medina",
            "estado": "En progreso",
            "subtarea": {
                "id": "SUB-HU02",
                "titulo": "Exportar modelo, conectar interfaz y validar rechazo de archivos",
                "estado": "En progreso",
            },
        },
    ],
}

KANBAN = {
    "tablero": "EXSF_Medina_Kanban",
    "caso": "Banco Girasol del Peru",
    "columnas": ["Pendiente", "En curso", "Terminado"],
    "diferencia_caso_vs_pruebas": "Los tickets son situaciones del caso; los hallazgos reales en pruebas se registran por separado al probar el codigo.",
    "tareas": [
        {
            "id": "TK-01",
            "tipo": "Tarea",
            "label": "incidente",
            "titulo": "Consulta devuelve resultado inesperado reportado por usuario",
            "prioridad": "Alta",
            "responsable": "Ryan Medina",
            "estado": "En curso",
        },
        {
            "id": "TK-02",
            "tipo": "Tarea",
            "label": "deuda-tecnica",
            "titulo": "Revision de posible duplicacion de codigo",
            "prioridad": "Media",
            "responsable": "Ryan Medina",
            "estado": "Pendiente",
        },
        {
            "id": "TK-03",
            "tipo": "Tarea",
            "label": "actividad-operativa",
            "titulo": "Preparacion de datos de demostracion",
            "prioridad": "Media",
            "responsable": "Ryan Medina",
            "estado": "Terminado",
        },
    ],
}

if __name__ == "__main__":
    print(json.dumps({"scrum": SCRUM, "kanban": KANBAN}, indent=2, ensure_ascii=False))
