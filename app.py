import streamlit as st

st.set_page_config(
    page_title="LIM - Laboratorio de división",
    layout="wide"
)

# -----------------------------
# Estilos generales
# -----------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    max-width: 1150px;
}

.lim-header {
    background: #1f4ed8;
    color: white;
    padding: 18px 24px;
    border-radius: 14px;
    margin-bottom: 24px;
}

.lim-header h1 {
    margin: 0;
    color: white;
    font-size: 28px;
}

.lim-header p {
    margin: 5px 0 0 0;
    color: white;
    font-size: 17px;
}

.paso {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 26px;
    margin-bottom: 12px;
}

.numero-paso {
    background: #1f4ed8;
    color: white;
    width: 38px;
    height: 38px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 19px;
}

.titulo-paso {
    font-size: 23px;
    font-weight: 800;
    color: #111827;
}

.tarjeta {
    border: 1px solid #cbd5e1;
    background: white;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 16px;
}

.tarjeta-azul {
    border: 1px solid #93c5fd;
    background: #eff6ff;
    color: #111827;
    border-radius: 12px;
    padding: 12px 16px;
    margin: 12px 0;
}

.tarjeta-naranja {
    border: 1px solid #fdba74;
    background: #fff7ed;
    color: #111827;
    border-radius: 12px;
    padding: 12px 16px;
    margin: 12px 0;
}

.tarjeta-verde {
    border: 1px solid #86efac;
    background: #f0fdf4;
    color: #111827;
    border-radius: 12px;
    padding: 12px 16px;
    margin: 12px 0;
}

.objetos {
    font-size: 27px;
    line-height: 1.75;
    word-wrap: break-word;
}

.metric-box {
    border: 1px solid #93c5fd;
    background: white;
    border-radius: 14px;
    padding: 14px;
    text-align: center;
}

.metric-title {
    font-size: 15px;
    color: #111827;
}

.metric-number {
    font-size: 42px;
    font-weight: 800;
    color: #1f4ed8;
    line-height: 1.1;
}

.grupo-titulo {
    font-weight: 800;
    text-align: center;
    margin-bottom: 6px;
    color: #111827;
}

.grupo-objetos {
    font-size: 25px;
    line-height: 1.6;
    text-align: center;
}

.grupo-cantidad {
    text-align: center;
    margin-top: 8px;
    color: #111827;
}

.lista-cuenta p {
    margin: 8px 0;
    color: #111827;
}

.color-dividendo { color: #b45309; font-weight: 800; }
.color-divisor { color: #1d4ed8; font-weight: 800; }
.color-cociente { color: #15803d; font-weight: 800; }
.color-resto { color: #dc2626; font-weight: 800; }

</style>
""", unsafe_allow_html=True)


def paso(numero, titulo):
    st.markdown(
        f"""
        <div class="paso">
            <div class="numero-paso">{numero}</div>
            <div class="titulo-paso">{titulo}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def cuenta_dividir_svg(dividendo, divisor, cociente, producto, resto):
    """
    Dibuja la cuenta escolar en formato de galera:
    dividendo a la izquierda, divisor arriba a la derecha,
    cociente debajo del divisor, producto restado y resto abajo.
    """
    return f"""
    <svg width="720" height="370" viewBox="0 0 720 370" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="700" height="350" rx="18" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>

        <!-- Cuenta escolar -->
        <text x="245" y="115" text-anchor="middle" font-family="Courier New, monospace" font-size="56" font-weight="700" fill="#b45309">{dividendo}</text>
        <text x="455" y="115" text-anchor="middle" font-family="Courier New, monospace" font-size="56" font-weight="700" fill="#1d4ed8">{divisor}</text>
        <line x1="350" y1="70" x2="350" y2="260" stroke="#111827" stroke-width="5"/>
        <line x1="350" y1="135" x2="535" y2="135" stroke="#111827" stroke-width="5"/>
        <text x="455" y="210" text-anchor="middle" font-family="Courier New, monospace" font-size="56" font-weight="700" fill="#15803d">{cociente}</text>

        <text x="245" y="185" text-anchor="middle" font-family="Courier New, monospace" font-size="50" font-weight="700" fill="#15803d">−{producto}</text>
        <line x1="170" y1="205" x2="320" y2="205" stroke="#111827" stroke-width="4"/>
        <text x="245" y="270" text-anchor="middle" font-family="Courier New, monospace" font-size="56" font-weight="700" fill="#dc2626">{resto}</text>

        <!-- Etiquetas -->
        <text x="105" y="115" font-family="Arial, sans-serif" font-size="18" fill="#b45309" font-weight="700">Dividendo</text>
        <path d="M165 110 C185 105, 205 105, 225 110" fill="none" stroke="#b45309" stroke-width="3" marker-end="url(#arrowOrange)"/>

        <text x="535" y="85" font-family="Arial, sans-serif" font-size="18" fill="#1d4ed8" font-weight="700">Divisor</text>
        <path d="M520 90 C500 92, 485 98, 470 105" fill="none" stroke="#1d4ed8" stroke-width="3" marker-end="url(#arrowBlue)"/>

        <text x="535" y="200" font-family="Arial, sans-serif" font-size="18" fill="#15803d" font-weight="700">Cociente</text>
        <path d="M520 198 C500 200, 485 205, 470 208" fill="none" stroke="#15803d" stroke-width="3" marker-end="url(#arrowGreen)"/>

        <text x="330" y="294" font-family="Arial, sans-serif" font-size="18" fill="#dc2626" font-weight="700">Resto</text>
        <path d="M320 288 C300 282, 282 275, 260 268" fill="none" stroke="#dc2626" stroke-width="3" marker-end="url(#arrowRed)"/>

        <defs>
            <marker id="arrowOrange" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
                <path d="M0,0 L0,6 L6,3 z" fill="#b45309"/>
            </marker>
            <marker id="arrowBlue" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
                <path d="M0,0 L0,6 L6,3 z" fill="#1d4ed8"/>
            </marker>
            <marker id="arrowGreen" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
                <path d="M0,0 L0,6 L6,3 z" fill="#15803d"/>
            </marker>
            <marker id="arrowRed" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
                <path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/>
            </marker>
        </defs>
    </svg>
    """


# -----------------------------
# Encabezado
# -----------------------------
st.markdown("""
<div class="lim-header">
    <h1>LIM · Laboratorio de división</h1>
    <p>Exploramos cómo repartir objetos en grupos iguales</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Paso 1
# -----------------------------
paso(1, "Elegí la cantidad de objetos")

col1, col2 = st.columns([4, 1])

with col1:
    total = st.slider("Cantidad de objetos", 1, 80, 37)

with col2:
    st.markdown(
        f"""
        <div class="metric-box">
            <div class="metric-title">Total de objetos</div>
            <div class="metric-number">{total}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    f"""
    <div class="tarjeta">
        <div class="objetos">{'🟦 ' * total}</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<div class='tarjeta-azul'>Usá el deslizador para cambiar la cantidad de objetos.</div>",
    unsafe_allow_html=True
)

# -----------------------------
# Paso 2
# -----------------------------
paso(2, "Elegí cuántos grupos iguales querés formar")

col1, col2 = st.columns([4, 1])

with col1:
    cantidad_grupos = st.slider("Cantidad de grupos", 1, 12, 5)

with col2:
    st.markdown(
        f"""
        <div class="metric-box">
            <div class="metric-title">Total de grupos</div>
            <div class="metric-number">{cantidad_grupos}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

objetos_por_grupo = total // cantidad_grupos
sin_repartir = total % cantidad_grupos
producto = cantidad_grupos * objetos_por_grupo

st.markdown(
    f"<div class='tarjeta-azul'>La aplicación reparte los objetos en {cantidad_grupos} grupos iguales, siempre que sea posible.</div>",
    unsafe_allow_html=True
)

# -----------------------------
# Paso 3
# -----------------------------
paso(3, "Así quedaron los objetos")

cols_por_fila = 4
for inicio in range(0, cantidad_grupos, cols_por_fila):
    cols = st.columns(cols_por_fila)
    for j in range(cols_por_fila):
        idx = inicio + j
        if idx < cantidad_grupos:
            with cols[j]:
                with st.container(border=True):
                    st.markdown(f"<div class='grupo-titulo'>Grupo {idx + 1}</div>", unsafe_allow_html=True)
                    if objetos_por_grupo > 0:
                        st.markdown(
                            f"<div class='grupo-objetos'>{'🟦 ' * objetos_por_grupo}</div>",
                            unsafe_allow_html=True
                        )
                        st.markdown(
                            f"<div class='grupo-cantidad'>{objetos_por_grupo} objetos</div>",
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown("<div class='grupo-cantidad'>Todavía no recibió objetos.</div>", unsafe_allow_html=True)

if sin_repartir > 0:
    st.markdown(
        f"""
        <div class="tarjeta-naranja">
            <b>Objetos que todavía no se repartieron:</b>
            <span style="font-size:26px; margin-left:14px;">{'🟨 ' * sin_repartir}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown("<div class='tarjeta-verde'>Todos los objetos quedaron repartidos en los grupos.</div>", unsafe_allow_html=True)

# -----------------------------
# Paso 4
# -----------------------------
paso(4, "Respondé estas preguntas antes de mirar la cuenta")

st.markdown(
    """
    <div class="tarjeta">
    <ol>
        <li>¿Cuántos objetos hay en cada grupo?</li>
        <li>¿Cuántos grupos se formaron?</li>
        <li>¿Cuántos objetos no se pudieron repartir?</li>
        <li>¿Qué tendría que pasar para que cada grupo recibiera un objeto más?</li>
        <li>Mové la cantidad de objetos o la cantidad de grupos. ¿Qué cambia?</li>
    </ol>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Paso 5
# -----------------------------
paso(5, "Miramos la cuenta de dividir")

mostrar_cuenta = st.checkbox("Mostrar la cuenta de dividir")

if mostrar_cuenta:
    col_a, col_b = st.columns([1, 1.5])

    with col_a:
        st.markdown(
            f"""
            <div class="tarjeta lista-cuenta">
                <p>La cuenta muestra cómo se reparten los <b>{total}</b> objetos en <b>{cantidad_grupos}</b> grupos.</p>
                <p><span class="color-dividendo">{total}</span> → dividendo: cantidad total de objetos.</p>
                <p><span class="color-divisor">{cantidad_grupos}</span> → divisor: cantidad de grupos.</p>
                <p><span class="color-cociente">{objetos_por_grupo}</span> → cociente: objetos en cada grupo.</p>
                <p><span class="color-resto">{sin_repartir}</span> → resto: objetos que no se pudieron repartir.</p>
                <p><b>{producto}</b> es la cantidad de objetos que sí se pudieron repartir en partes iguales.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_b:
        st.markdown(cuenta_dividir_svg(total, cantidad_grupos, objetos_por_grupo, producto, sin_repartir), unsafe_allow_html=True)

# -----------------------------
# Paso 6
# -----------------------------
paso(6, "Relacionamos con la escritura matemática")

mostrar_igualdad = st.checkbox("Mostrar la escritura matemática")

if mostrar_igualdad:
    st.markdown(
        f"""
        <div class="tarjeta">
            <div style="font-size:42px; text-align:center; font-weight:800; color:#111827;">
                <span class="color-dividendo">{total}</span>
                =
                <span class="color-divisor">{cantidad_grupos}</span>
                ×
                <span class="color-cociente">{objetos_por_grupo}</span>
                +
                <span class="color-resto">{sin_repartir}</span>
            </div>
            <div style="text-align:center; margin-top:10px; color:#111827;">
                <span class="color-dividendo">dividendo</span> ·
                <span class="color-divisor">divisor</span> ·
                <span class="color-cociente">cociente</span> ·
                <span class="color-resto">resto</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
