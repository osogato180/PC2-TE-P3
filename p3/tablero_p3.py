from dataclasses import dataclass, asdict
import json

@dataclass
class Subtarea:
    id: str
    titulo: str
    responsable: str
    estado: str

@dataclass
class HistoriaUsuario:
    id: str
    epica: str
    titulo: str
    como: str
    quiero: str
    para: str
    criterios_aceptacion: list[str]
    prioridad: str
    estimacion_sp: int
    responsable: str
    sprint: str
    estado: str
    subtarea: Subtarea

@dataclass
class TareaKanban:
    id: str
    tipo_issue: str
    label: str
    titulo: str
    descripcion: str
    prioridad: str
    responsable: str
    estado: str

# --- 3.1 SCRUM: EXSF_Medina_Scrum ---
tablero_scrum = {
    "tablero": "EXSF_Medina_Scrum",
    "caso": "Banco Girasol del Peru",
    "columnas_sdlc": ["Por hacer", "En progreso", "En pruebas", "Hecho"],
    "epica": {
        "id": "EP01",
        "titulo": "Museo RA del Ciclo del Agua y Clasificador Web de Residuos",
        "objetivo_sprint": "Entregar el prototipo RA con 4 etapas y pausa/continuar, y el clasificador de residuos (paper, plastic, metal) con validacion de formato en un sprint de 2 semanas."
    },
    "sprint": {
        "nombre": "Sprint 1 - 2 Semanas",
        "duracion_semanas": 2,
        "estado": "Activo"
    },
    "historias": [
        asdict(HistoriaUsuario(
            id="HU01",
            epica="EP01",
            titulo="Interaccion con etapas y pausa en RA del ciclo del agua",
            como="estudiante o visitante del museo",
            quiero="cambiar entre las 4 etapas del ciclo del agua y pausar o continuar la animacion sin recargar la pagina",
            para="entender cada etapa de forma visual e interactiva",
            criterios_aceptacion=[
                "Escena con al menos 3 objetos 3D diferenciables y texto educativo en vista 3D y con marcador Hiro",
                "Cambio entre evaporacion, condensacion, precipitacion y acumulacion sin recargar",
                "Botones Pausar/Continuar operativos y mensajes de markerFound / markerLost"
            ],
            prioridad="Alta",
            estimacion_sp=5,
            responsable="Ryan Medina",
            sprint="Sprint 1 - 2 Semanas",
            estado="Hecho",
            subtarea=Subtarea(
                id="SUB-HU01",
                titulo="Programar visibilidad por etapa, pausa y eventos de marcador en escena.js y controles.js",
                responsable="Ryan Medina",
                estado="Hecho"
            )
        )),
        asdict(HistoriaUsuario(
            id="HU02",
            epica="EP01",
            titulo="Clasificacion de residuos JPG/PNG con puntajes y rechazo invalido",
            como="usuario del modulo de clasificacion",
            quiero="cargar una imagen JPG/PNG (o usar camara/alternativa) y ver la clase y puntajes o el rechazo de archivos invalidos",
            para="identificar residuos en paper, plastic o metal de forma confiable",
            criterios_aceptacion=[
                "Modelo entrenado con MobileNetV2 evaluado en test con metricas y matriz de confusion",
                "Interfaz acepta JPG/PNG, muestra clase y puntajes, y rechaza archivos invalidos",
                "Incluye uso de camara o carga alternativa verificada"
            ],
            prioridad="Alta",
            estimacion_sp=8,
            responsable="Ryan Medina",
            sprint="Sprint 1 - 2 Semanas",
            estado="En progreso",
            subtarea=Subtarea(
                id="SUB-HU02",
                titulo="Exportar modelo, conectar interfaz web y validar rechazo de archivos no JPG/PNG",
                responsable="Ryan Medina",
                estado="En progreso"
            )
        ))
    ]
}

# --- 3.2 KANBAN: EXSF_Medina_Kanban ---
tablero_kanban = {
    "tablero": "EXSF_Medina_Kanban",
    "caso": "Banco Girasol del Peru",
    "columnas_sdlc": ["Pendiente", "En curso", "Terminado"],
    "nota_diferencia": "Los tickets siguientes representan situaciones del caso; los hallazgos reales de pruebas se registran por separado al ejecutar y probar el codigo.",
    "tareas": [
        asdict(TareaKanban(
            id="TK-01",
            tipo_issue="Tarea",
            label="incidente",
            titulo="Consulta devuelve resultado inesperado reportado por usuario",
            descripcion="Atender reporte de usuario donde una consulta arroja un resultado distinto al esperado.",
            prioridad="Alta",
            responsable="Ryan Medina",
            estado="En curso"
        )),
        asdict(TareaKanban(
            id="TK-02",
            tipo_issue="Tarea",
            label="deuda-tecnica",
            titulo="Revision de posible duplicacion de codigo",
            descripcion="Revisar y limpiar bloques repetidos en los scripts para mejorar mantenibilidad.",
            prioridad="Media",
            responsable="Ryan Medina",
            estado="Pendiente"
        )),
        asdict(TareaKanban(
            id="TK-03",
            tipo_issue="Tarea",
            label="actividad-operativa",
            titulo="Preparacion de datos de demostracion",
            descripcion="Preparar datos y muestras de prueba limpias para demostrar el funcionamiento.",
            prioridad="Media",
            responsable="Ryan Medina",
            estado="Terminado"
        ))
    ]
}

if __name__ == "__main__":
    print("=== 3.1 SCRUM ===")
    print(json.dumps(tablero_scrum, indent=2, ensure_ascii=False))
    print("\n=== 3.2 KANBAN ===")
    print(json.dumps(tablero_kanban, indent=2, ensure_ascii=False))
