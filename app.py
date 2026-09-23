import math
from io import BytesIO

import matplotlib.pyplot as plt
import streamlit as st

# -----------------------------
# Configuración general
# -----------------------------
st.set_page_config(
    page_title="LIM - Explorando la división entera",
    layout="wide"
)

# Reemplazar cuando estén disponibles
FORMULARIO_COMENTARIOS_URL = ""
DOCUMENTO_LIM_URL = ""

MAX_GRUPOS = 12


# -----------------------------
# Estado de la aplicación
# -----------------------------
if "cantidad_grupos" not in st.session_state:
    st.session_state.cantidad_grupos = 5


def disminuir_grupos():
    st.session_state.cantidad_grupos = max(1, st.session_state.cantidad_grupos - 1)


def aumentar_grupos():
    st.session_state.cantidad_grupos = min(MAX_GRUPOS, st.session_state.cantidad_grupos + 1)


# -----------------------------
# Estilo visual
# -----------------------------
st.markdown(
    """
<style>
.block-container {
    max-width: 1220px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top left, #152238 0%, #0b111c 42%, #070b12 100%);
    color: #f8fafc;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

h1, h2, h3, p, li, span, div {
    color: #f8fafc;
}

.lim-topbar {
    display: flex;
    align-items: center;
    border-bottom: 1px solid rgba(148, 163, 184, 0.45);
    padding-bottom: 14px;
    margin-bottom: 24px;
}

.lim-code {
    color: #2f80ed;
    font-weight: 800;
    font-size: 22px;
}

.lim-title {
    color: #ffffff;
    font-size: 22px;
    font-weight: 500;
    margin-left: 12px;
}

.step-title {
    font-size: 32px;
    font-weight: 850;
    color: #ffffff;
    margin-top: 24px;
    margin-bottom: 18px;
}

.group-value {
    text-align: center;
    font-size: 30px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.25;
}

.group-number {
    color: #2f80ed;
    font-size: 58px;
    font-weight: 950;
    padding: 0 12px;
}

.info-card {
    border: 1px solid rgba(47, 128, 237, 0.55);
    background: rgba(14, 71, 125, 0.38);
    border-radius: 10px;
    padding: 18px 22px;
    color: #dbeafe;
    font-size: 19px;
    margin: 18px 0;
}

.info-card .num {
    color: #2f80ed;
    font-weight: 900;
}

.summary-card {
    display: grid;
    grid-template-columns: 1.25fr 0.15fr 1.25fr 0.15fr 1.35fr 0.15fr 1fr;
    gap: 14px;
    align-items: center;
    border: 1px solid rgba(148, 163, 184, 0.35);
    background: rgba(15, 23, 42, 0.58);
    border-radius: 12px;
    padding: 18px;
    margin: 18px 0;
}

.summary-box {
    border-radius: 10px;
    padding: 12px;
    text-align: center;
    background: rgba(2, 6, 23, 0.36);
}

.box-blue { border: 1px solid #2f80ed; }
.box-green { border: 1px solid #47d147; }
.box-yellow { border: 1px solid #f2b705; }
.box-red { border: 1px solid #ef4444; }

.summary-label {
    color: #ffffff;
    font-size: 18px;
}

.summary-num {
    font-size: 32px;
    font-weight: 900;
}

.blue { color: #2f80ed; }
.green { color: #47d147; }
.yellow { color: #f2b705; }
.red { color: #ef4444; }

.op {
    color: #ffffff;
    font-size: 28px;
    font-weight: 800;
    text-align: center;
}

.board {
    border: 1px solid rgba(148, 163, 184, 0.35);
    background: rgba(15, 23, 42, 0.50);
    border-radius: 12px;
    padding: 20px;
    margin-top: 18px;
}

.board-title {
    color: #ffffff;
    font-size: 24px;
    font-weight: 850;
    margin-bottom: 14px;
}

.group-card {
    border: 1px solid rgba(148, 163, 184, 0.38);
    background: rgba(2, 6, 23, 0.38);
    border-radius: 10px;
    padding: 12px;
    text-align: center;
    overflow-x: auto;
    min-height: 92px;
    margin-bottom: 14px;
}

.group-title {
    color: #ffffff;
    font-size: 17px;
    font-weight: 750;
    margin-bottom: 10px;
}

.objects {
    display: inline-flex;
    flex-direction: column;
    gap: 5px;
    align-items: flex-start;
}

.object-row {
    display: flex;
    gap: 5px;
}

.square {
    display: inline-block;
    width: 22px;
    height: 22px;
    border-radius: 3px;
    flex: 0 0 auto;
}

.square-blue {
    background: #2f80ed;
    border: 2px solid #1e40af;
}

.square-red {
    background: #ef4444;
    border: 2px solid #b91c1c;
}

.explain-card {
    border: 1px solid rgba(47, 128, 237, 0.50);
    background: rgba(14, 71, 125, 0.34);
    border-radius: 10px;
    padding: 18px 22px;
    margin-top: 18px;
    color: #ffffff;
    font-size: 20px;
}

.explain-title {
    color: #facc15;
    font-size: 24px;
    font-weight: 900;
    margin-bottom: 8px;
}

.small-note {
    color: #cbd5e1;
    font-size: 16px;
    font-style: italic;
    margin-top: 12px;
}

.section-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(148, 163, 184, 0.28);
    border-radius: 12px;
    padding: 20px;
    margin-top: 22px;
}

button[kind="secondary"] {
    border: 1px solid rgba(148, 163, 184, 0.55);
    background-color: rgba(15, 23, 42, 0.88);
    color: #ffffff;
}
</style>
""",
    unsafe_allow_html=True
)


# -----------------------------
# Funciones matemáticas y visuales
# -----------------------------
def buscar_organizacion_rectangular(n: int) -> tuple[int, int]:
    if n <= 0:
        return (0, 0)

    mejor_filas = 1
    mejor_columnas = n

    for filas in range(1, int(math.sqrt(n)) + 1):
        if n % filas == 0:
            mejor_filas = filas
            mejor_columnas = n // filas

    return (mejor_filas, mejor_columnas)


def objetos_html(n: int, color: str = "blue") -> str:
    filas, columnas = buscar_organizacion_rectangular(n)

    if n == 0:
        return "<span style='color:#cbd5e1;'>Sin objetos</span>"

    square_class = "square-blue" if color == "blue" else "square-red"

    html = "<div class='objects'>"
    for _ in range(filas):
        html += "<div class='object-row'>"
        for _ in range(columnas):
            html += f"<span class='square {square_class}'></span>"
        html += "</div>"
    html += "</div>"
    return html


def dibujar_cuenta(dividendo: int, divisor: int, cociente: int, producto: int, resto: int) -> BytesIO:
    fig, ax = plt.subplots(figsize=(8, 4.6), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    negro = "#111111"
    azul = "#0057D9"
    verde = "#137A2A"
    naranja = "#C45100"
    rojo = "#C00000"
    gris = "#DDDDDD"

    ax.add_patch(plt.Rectangle((0.2, 0.2), 9.6, 6.6, linewidth=2, edgecolor=gris, facecolor="white"))

    x_izq, x_der = 3.4, 6.3

    ax.text(x_izq, 5.2, str(dividendo), fontsize=40, fontweight="bold", ha="center", va="center", color=naranja)
    ax.text(x_der, 5.2, str(divisor), fontsize=40, fontweight="bold", ha="center", va="center", color=azul)

    ax.plot([4.8, 4.8], [2.0, 6.1], color=negro, linewidth=4)
    ax.plot([4.8, 7.55], [4.4, 4.4], color=negro, linewidth=4)

    ax.text(x_der, 3.4, str(cociente), fontsize=40, fontweight="bold", ha="center", va="center", color=verde)
    ax.text(x_izq, 3.4, f"−{producto}", fontsize=34, fontweight="bold", ha="center", va="center", color=verde)

    ax.plot([2.35, 4.35], [2.65, 2.65], color=negro, linewidth=3)
    ax.text(x_izq, 1.7, str(resto), fontsize=40, fontweight="bold", ha="center", va="center", color=rojo)

    ax.annotate("Dividendo", xy=(x_izq - 0.45, 5.2), xytext=(0.85, 5.2),
                fontsize=16, fontweight="bold", color=naranja,
                arrowprops=dict(arrowstyle="->", lw=2.5, color=naranja), ha="left", va="center")
    ax.annotate("Divisor", xy=(x_der + 0.25, 5.2), xytext=(7.85, 5.2),
                fontsize=16, fontweight="bold", color=azul,
                arrowprops=dict(arrowstyle="->", lw=2.5, color=azul), ha="left", va="center")
    ax.annotate("Cociente", xy=(x_der + 0.25, 3.4), xytext=(7.85, 3.4),
                fontsize=16, fontweight="bold", color=verde,
                arrowprops=dict(arrowstyle="->", lw=2.5, color=verde), ha="left", va="center")
    ax.annotate("Resto", xy=(x_izq + 0.20, 1.7), xytext=(4.75, 1.15),
                fontsize=16, fontweight="bold", color=rojo,
                arrowprops=dict(arrowstyle="->", lw=2.5, color=rojo), ha="left", va="center")

    ax.text(
        5, 0.55,
        f"Al repartir {dividendo} objetos en {divisor} grupos iguales, quedan {cociente} objetos en cada grupo y quedan {resto} objetos sin repartir.",
        fontsize=12,
        ha="center",
        va="center",
        color=negro
    )

    buffer = BytesIO()
    fig.savefig(buffer, format="png", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    buffer.seek(0)
    return buffer


def render_topbar():
    st.markdown(
        """
        <div class="lim-topbar">
            <span class="lim-code">DE-01</span>
            <span style="color:#94a3b8; margin-left:12px;">|</span>
            <span class="lim-title">Explorar la división entera: repartir en grupos iguales</span>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_step_title(number: int, text: str):
    st.markdown(f"<div class='step-title'>{number}. {text}</div>", unsafe_allow_html=True)


def render_summary(total: int, grupos: int, por_grupo: int, resto: int):
    st.markdown(
        f"""
        <div class="summary-card">
            <div class="summary-box box-blue">
                <div class="summary-label">Objetos totales</div>
                <div class="summary-num blue">{total}</div>
            </div>
            <div class="op">=</div>
            <div class="summary-box box-green">
                <div class="summary-label">En cada grupo</div>
                <div class="summary-num green">{por_grupo}</div>
            </div>
            <div class="op">×</div>
            <div class="summary-box box-yellow">
                <div class="summary-label">Cantidad de grupos</div>
                <div class="summary-num yellow">{grupos}</div>
            </div>
            <div class="op">+</div>
            <div class="summary-box box-red">
                <div class="summary-label">Resto</div>
                <div class="summary-num red">{resto}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_groups(grupos: int, por_grupo: int):
    st.markdown(f"<div class='board-title'>Grupos formados ({grupos} grupos de {por_grupo})</div>", unsafe_allow_html=True)

    cols_por_fila = 4
    for inicio in range(0, grupos, cols_por_fila):
        columnas = st.columns(cols_por_fila)
        for j, col in enumerate(columnas):
            idx = inicio + j
            if idx < grupos:
                with col:
                    st.markdown(
                        f"""
                        <div class="group-card">
                            <div class="group-title">Grupo {idx + 1}</div>
                            {objetos_html(por_grupo, color="blue")}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


def render_remainder(resto: int):
    st.markdown("<div class='board-title'>Quedan sin repartir</div>", unsafe_allow_html=True)
    if resto > 0:
        st.markdown(
            f"""
            <div class="group-card" style="max-width:420px;">
                {objetos_html(resto, color="red")}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.success("No quedaron objetos sin repartir.")


# -----------------------------
# Interfaz
# -----------------------------
render_topbar()

st.title("Explorando la división entera")
st.subheader("Repartir en grupos iguales")
st.write("Exploramos cómo repartir objetos completos en grupos iguales.")

st.info(
    "Este laboratorio trabaja con división entera: buscamos repartir objetos completos en grupos iguales. "
    "Cuando no alcanza para dar otro objeto a cada grupo, algunos objetos quedan sin repartir."
)

st.divider()

# 1. Cantidad de objetos
render_step_title(1, "Elegí la cantidad de objetos")
total = st.slider("Cantidad de objetos", 1, 80, 37, step=1)

# 2. Cantidad de grupos
render_step_title(2, "Elegí en cuántos grupos iguales querés repartir")

col_menos, col_valor, col_mas = st.columns([1, 2.6, 1])

with col_menos:
    st.button("←  − 1 grupo", on_click=disminuir_grupos, use_container_width=True)

with col_mas:
    st.button("+ 1 grupo  →", on_click=aumentar_grupos, use_container_width=True)

cantidad_grupos = st.session_state.cantidad_grupos
objetos_por_grupo = total // cantidad_grupos
sin_repartir = total % cantidad_grupos
producto = cantidad_grupos * objetos_por_grupo

with col_valor:
    st.markdown(
        f"<div class='group-value'>Se formarán <span class='group-number'>{cantidad_grupos}</span> grupos iguales</div>",
        unsafe_allow_html=True
    )

st.markdown(
    f"""
    <div class="info-card">
        Con esta elección, los <span class="num">{total}</span> objetos se repartirán en
        <span class="num">{cantidad_grupos}</span> grupos iguales, siempre que sea posible.
    </div>
    """,
    unsafe_allow_html=True
)

if total < cantidad_grupos:
    st.warning(
        f"Como hay menos objetos ({total}) que grupos ({cantidad_grupos}), en división entera no alcanza para dar 1 objeto a cada grupo. "
        f"Por eso cada grupo recibe 0 objetos y quedan {sin_repartir} objetos sin repartir. "
        "En otro tipo de problema se podrían partir los objetos y usar fracciones, pero este laboratorio se concentra en la división entera."
    )

# 3. Observamos el reparto
render_step_title(3, "Observamos el reparto")

st.markdown("<div class='board'>", unsafe_allow_html=True)
col_grupos, col_resto = st.columns([2.2, 1])
with col_grupos:
    render_groups(cantidad_grupos, objetos_por_grupo)
with col_resto:
    render_remainder(sin_repartir)
st.markdown("</div>", unsafe_allow_html=True)

# 4. ¿Qué está pasando?
render_step_title(4, "¿Qué está pasando?")

st.markdown(
    f"""
    <div class="explain-card">
        <div class="explain-title">Miramos el reparto</div>
        <div>
            Se formaron <span class="blue"><b>{cantidad_grupos}</b></span> grupos de
            <span class="green"><b>{objetos_por_grupo}</b></span> objetos cada uno.
            En total se pudieron repartir <span class="green"><b>{producto}</b></span> objetos.
            Quedaron <span class="red"><b>{sin_repartir}</b></span> objetos sin repartir.
        </div>
        <div class="small-note">Antes de seguir, comprobá que esta descripción coincide con lo que observás.</div>
    </div>
    """,
    unsafe_allow_html=True
)

# 5. Representación matemática
render_step_title(5, "Lo representamos matemáticamente")
st.write("Esta es una forma de escribir el reparto que acabamos de observar:")
render_summary(total, cantidad_grupos, objetos_por_grupo, sin_repartir)

# 6. Preguntas
render_step_title(6, "Respondé estas preguntas antes de mirar la cuenta")

with st.container(border=True):
    st.markdown("""
1. ¿Cuántos objetos hay en cada grupo?
2. ¿Cuántos grupos se formaron?
3. ¿Quedaron objetos sin repartir? ¿Qué número representa esa cantidad?
4. ¿Qué tendría que pasar para que cada grupo recibiera un objeto más?
5. Cambiá la cantidad de objetos o la cantidad de grupos de a uno. ¿Qué cambia?
""")

    st.markdown("#### Para pensar: lo que queda sin repartir y la cantidad de grupos")
    st.markdown(f"""
Ahora quedaron **{sin_repartir} objetos sin repartir** y hay **{cantidad_grupos} grupos**.

Probá mover los controles y pensá:

- ¿Puede quedar sin repartir una cantidad igual a la cantidad de grupos?
- ¿Puede quedar sin repartir una cantidad mayor que la cantidad de grupos?
- ¿Qué pasaría si quedaran sin repartir tantos objetos como grupos hay?
""")

    if st.checkbox("Mostrar una ayuda sobre esta relación"):
        st.info(
            "Si quedaran sin repartir tantos objetos como grupos hay, podríamos darle 1 objeto más a cada grupo. "
            "Por eso, en la división entera, la cantidad que queda sin repartir siempre es menor que la cantidad de grupos."
        )

# 7. Cuenta
render_step_title(7, "Miramos la cuenta de dividir")

with st.container(border=True):
    if st.checkbox("Mostrar la cuenta de dividir"):
        st.write("La cuenta representa el mismo reparto que observamos con los objetos.")
        st.image(
            dibujar_cuenta(total, cantidad_grupos, objetos_por_grupo, producto, sin_repartir),
            use_container_width=True
        )

        st.markdown(f"""
- **{total}** es la cantidad total de objetos. Se llama **dividendo**.
- **{cantidad_grupos}** es la cantidad de grupos. Se llama **divisor**.
- **{objetos_por_grupo}** es la cantidad de objetos en cada grupo. Se llama **cociente**.
- **{sin_repartir}** es la cantidad de objetos que no se pudieron repartir. Se llama **resto**.
- **{producto}** es la cantidad de objetos que sí pudieron repartirse en partes iguales.
""")

# 8. Expresión matemática
render_step_title(8, "Relacionamos la cuenta con la expresión matemática")

with st.container(border=True):
    if st.checkbox("Mostrar la expresión matemática"):
        st.markdown(f"## {total} = {cantidad_grupos} × {objetos_por_grupo} + {sin_repartir}")

        st.markdown(f"""
La expresión matemática también representa el mismo reparto:

- **{total}** es el **dividendo**: la cantidad total de objetos.
- **{cantidad_grupos}** es el **divisor**: la cantidad de grupos.
- **{objetos_por_grupo}** es el **cociente**: la cantidad de objetos en cada grupo.
- **{sin_repartir}** es el **resto**: la cantidad de objetos que quedaron sin repartir.

En palabras:

**Al repartir {total} objetos en {cantidad_grupos} grupos iguales, quedan {objetos_por_grupo} objetos en cada grupo y quedan {sin_repartir} objetos sin repartir.**
""")

st.divider()

st.markdown("### Sobre este laboratorio")
st.markdown(
    "**Explorando la división entera: repartir en grupos iguales** forma parte de **LIM (Laboratorio de Ideas Matemáticas)**, "
    "un proyecto de investigación y desarrollo dedicado al diseño de laboratorios para explorar ideas matemáticas."
)
st.markdown("**Versión:** 1.7 (prototipo de circulación)")
st.markdown("Este laboratorio continúa en desarrollo. Tus comentarios nos ayudan a mejorarlo.")

if FORMULARIO_COMENTARIOS_URL:
    st.link_button("💬 Enviar un comentario o sugerencia", FORMULARIO_COMENTARIOS_URL)
else:
    st.caption("Próximamente: formulario para enviar comentarios o sugerencias.")

if DOCUMENTO_LIM_URL:
    st.link_button("📄 ¿Qué es LIM?", DOCUMENTO_LIM_URL)
else:
    st.caption("Próximamente: documento breve de presentación del proyecto LIM.")
# ---------------------------------------------------------
# CONTACTO
# ---------------------------------------------------------

st.markdown("---")

st.markdown(
    """
    ### ¿Usaste este laboratorio?

    Si sos docente y estás pensando utilizar este laboratorio, o ya lo probaste
    con estudiantes, nos interesa conocer tu experiencia.

    📩 **Contacto:**  
    [fjbifano@ccpems.exactas.uba.ar](mailto:fjbifano@ccpems.exactas.uba.ar)
    """
)
