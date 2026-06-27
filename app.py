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
:root {
    --azul: #1d4ed8;
    --azul-claro: #eaf2ff;
    --azul-borde: #93c5fd;
    --verde: #15803d;
    --verde-claro: #ecfdf3;
    --naranja: #c2410c;
    --naranja-claro: #fff3e8;
    --gris: #f8fafc;
    --gris-borde: #cbd5e1;
    --texto: #111827;
}

html, body, [class*="css"] {
    color: var(--texto);
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1150px;
}

.header-lim {
    background: #1d4ed8;
    color: #ffffff;
    padding: 18px 24px;
    border-radius: 16px;
    margin-bottom: 24px;
}

.header-lim h1 {
    margin: 0;
    font-size: 28px;
    color: #ffffff;
}

.header-lim p {
    margin: 4px 0 0 0;
    font-size: 17px;
    color: #ffffff;
}

.paso {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 24px;
    margin-bottom: 12px;
}

.numero-paso {
    background: #1d4ed8;
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
    border: 1px solid var(--gris-borde);
    background: #ffffff;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 16px;
}

.tarjeta-azul {
    border: 1px solid var(--azul-borde);
    background: var(--azul-claro);
    color: #0f172a;
    border-radius: 12px;
    padding: 12px 16px;
    margin: 12px 0;
}

.tarjeta-verde {
    border: 1px solid #86efac;
    background: var(--verde-claro);
    color: #0f172a;
    border-radius: 12px;
    padding: 12px 16px;
    margin: 12px 0;
}

.tarjeta-naranja {
    border: 1px solid #fdba74;
    background: var(--naranja-claro);
    color: #0f172a;
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
    border: 1px solid var(--azul-borde);
    background: #ffffff;
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
    color: #1d4ed8;
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

.division-box {
    display: flex;
    justify-content: center;
    margin: 1rem 0;
}

.division-escolar {
    font-family: 'Courier New', monospace;
    font-size: 42px;
    line-height: 1.25;
    color: #111827;
}

.fila-superior,
.fila-principal,
.fila-resta,
.fila-resto {
    display: grid;
    grid-template-columns: 110px 32px 110px;
    align-items: center;
}

.divisor {
    text-align: center;
    color: #1d4ed8;
    font-weight: 800;
}

.dividendo {
    border-left: 5px solid #111827;
    border-bottom: 5px solid #111827;
    padding-left: 18px;
    text-align: center;
    color: #c2410c;
    font-weight: 800;
}

.cociente {
    border-bottom: 5px solid #111827;
    padding-left: 18px;
    text-align: center;
    color: #15803d;
    font-weight: 800;
}

.resta {
    text-align: center;
    border-bottom: 4px solid #111827;
    color: #15803d;
    font-weight: 800;
}

.resto {
    text-align: center;
    color: #c2410c;
    font-weight: 800;
}

.etiqueta {
    font-size: 15px;
    font-weight: 800;
}

.azul { color: #1d4ed8; font-weight: 800; }
.verde { color: #15803d; font-weight: 800; }
.naranja { color: #c2410c; font-weight: 800; }

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


# -----------------------------
# Encabezado
# -----------------------------
st.markdown("""
<div class="header-lim">
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
    col_a, col_b = st.columns([1, 1.4])

    with col_a:
        st.markdown(
            f"""
            <div class="tarjeta">
                <p>La cuenta muestra cómo se reparten los <b>{total}</b> objetos en <b>{cantidad_grupos}</b> grupos.</p>
                <p><span class="etiqueta naranja">{total}</span> → dividendo: cantidad total de objetos.</p>
                <p><span class="etiqueta azul">{cantidad_grupos}</span> → divisor: cantidad de grupos.</p>
                <p><span class="etiqueta verde">{objetos_por_grupo}</span> → cociente: objetos en cada grupo.</p>
                <p><span class="etiqueta naranja">{sin_repartir}</span> → resto: objetos que no se pudieron repartir.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_b:
        st.markdown(f"""
        <div class="tarjeta">
            <div class="division-box">
              <div class="division-escolar">
                <div class="fila-superior">
                  <div></div>
                  <div></div>
                  <div class="cociente">{objetos_por_grupo}</div>
                </div>
                <div class="fila-principal">
                  <div class="divisor">{cantidad_grupos}</div>
                  <div></div>
                  <div class="dividendo">{total}</div>
                </div>
                <div class="fila-resta">
                  <div></div>
                  <div></div>
                  <div class="resta">−{producto}</div>
                </div>
                <div class="fila-resto">
                  <div></div>
                  <div></div>
                  <div class="resto">{sin_repartir}</div>
                </div>
              </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

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
                <span class="naranja">{total}</span>
                =
                <span class="azul">{cantidad_grupos}</span>
                ×
                <span class="verde">{objetos_por_grupo}</span>
                +
                <span class="naranja">{sin_repartir}</span>
            </div>
            <div style="text-align:center; margin-top:10px; color:#111827;">
                <span class="naranja">dividendo</span> ·
                <span class="azul">divisor</span> ·
                <span class="verde">cociente</span> ·
                <span class="naranja">resto</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
