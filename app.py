import streamlit as st

st.set_page_config(page_title="P3 - Scrum & Kanban | Banco Girasol", layout="wide")
st.title("Gestión del Trabajo — Banco Girasol del Perú (P3)")

tab_scrum, tab_kanban = st.tabs(["3.1 Scrum (EXSF_Medina_Scrum)", "3.2 Kanban (EXSF_Medina_Kanban)"])

with tab_scrum:
    st.subheader("Tablero Scrum: EXSF_Medina_Scrum")
    st.info(
        "**Épica (EP01):** Museo RA del Ciclo del Agua y Clasificador Web de Residuos  \n"
        "**Sprint (2 semanas):** Sprint 1 — *Objetivo verificable:* Entregar el prototipo RA con 4 etapas y pausa/continuar, "
        "y el clasificador de residuos (paper, plastic, metal) con validación de formato."
    )

    historias = [
        {
            "id": "HU01",
            "titulo": "Visualizar etapas y control de animación en RA del ciclo del agua",
            "descripcion": "Como visitante del museo, quiero cambiar entre las 4 etapas y pausar/continuar sin recargar, para entender el ciclo del agua.",
            "criterios": [
                "3+ objetos 3D diferenciables y texto educativo en vista 3D y con marcador Hiro.",
                "Cambio entre evaporación, condensación, precipitación y acumulación sin recargar.",
                "Botones Pausar/Continuar operativos y mensajes de markerFound / markerLost."
            ],
            "prioridad": "Alta",
            "estimacion": "5 SP",
            "responsable": "Ryan Medina",
            "estado": "Hecho",
            "subtarea": "SUB-HU01: Lógica de etapas, pausa y marcador en escena.js y controles.js (Hecho)"
        },
        {
            "id": "HU02",
            "titulo": "Clasificación de residuos JPG/PNG con puntajes y rechazo inválido",
            "descripcion": "Como usuario, quiero subir una imagen JPG/PNG (o usar cámara/alternativa) y ver la clase y puntajes o el rechazo inválido, para identificar residuos.",
            "criterios": [
                "Modelo MobileNetV2 evaluado en test con métricas y matriz de confusión.",
                "Interfaz acepta JPG/PNG, muestra clase y puntajes, y rechaza archivos inválidos.",
                "Incluye cámara o carga alternativa verificada."
            ],
            "prioridad": "Alta",
            "estimacion": "8 SP",
            "responsable": "Ryan Medina",
            "estado": "En progreso",
            "subtarea": "SUB-HU02: Exportar modelo, conectar interfaz web y validar archivos no JPG/PNG (En progreso)"
        }
    ]

    with st.expander("Ver detalle completo de Backlog, Historias y Subtareas", expanded=True):
        for h in historias:
            st.markdown(f"**{h['id']} — {h['titulo']}** | Prioridad: `{h['prioridad']}` | Estimación: `{h['estimacion']}` | Responsable: `{h['responsable']}` | Estado: **`{h['estado']}`**")
            st.write(h["descripcion"])
            st.write("**Criterios de aceptación:** " + " / ".join(h["criterios"]))
            st.caption(h["subtarea"])
            st.divider()

    st.markdown("#### Vista de Tablero SDLC (Sprint Activo)")
    columnas_scrum = ["Por hacer", "En progreso", "En pruebas", "Hecho"]
    cols_s = st.columns(4)
    for idx, col_name in enumerate(columnas_scrum):
        with cols_s[idx]:
            st.markdown(f"### {col_name}")
            for h in historias:
                if h["estado"] == col_name:
                    st.success(f"**{h['id']}**: {h['titulo']}\n\nResp: {h['responsable']} | {h['estimacion']}\n\n*{h['subtarea']}*")

with tab_kanban:
    st.subheader("Tablero Kanban: EXSF_Medina_Kanban")
    st.warning(
        "**Nota metodológica:** Los tickets mostrados corresponden a situaciones del caso Banco Girasol del Perú; "
        "los hallazgos reales detectados durante la ejecución y pruebas del código se documentan por separado."
    )

    tareas_kanban = [
        {
            "id": "TK-01",
            "tipo": "Tarea",
            "label": "incidente",
            "titulo": "Consulta devuelve resultado inesperado reportado por usuario",
            "prioridad": "Alta",
            "responsable": "Ryan Medina",
            "estado": "En curso"
        },
        {
            "id": "TK-02",
            "tipo": "Tarea",
            "label": "deuda-tecnica",
            "titulo": "Revisión de posible duplicación de código",
            "prioridad": "Media",
            "responsable": "Ryan Medina",
            "estado": "Pendiente"
        },
        {
            "id": "TK-03",
            "tipo": "Tarea",
            "label": "actividad-operativa",
            "titulo": "Preparación de datos de demostración",
            "prioridad": "Media",
            "responsable": "Ryan Medina",
            "estado": "Terminado"
        }
    ]

    with st.expander("Ver detalle de Tareas registradas", expanded=True):
        for t in tareas_kanban:
            st.markdown(f"**{t['id']} ({t['tipo']})** — {t['titulo']} | Label: `{t['label']}` | Prioridad: `{t['prioridad']}` | Resp: `{t['responsable']}` | Estado: **`{t['estado']}`**")

    st.markdown("#### Vista de Tablero Kanban")
    columnas_kanban = ["Pendiente", "En curso", "Terminado"]
    cols_k = st.columns(3)
    for idx, col_name in enumerate(columnas_kanban):
        with cols_k[idx]:
            st.markdown(f"### {col_name}")
            for t in tareas_kanban:
                if t["estado"] == col_name:
                    st.info(f"**{t['id']}** [`{t['label']}`]\n\n{t['titulo']}\n\nPrioridad: {t['prioridad']} | Resp: {t['responsable']}")
