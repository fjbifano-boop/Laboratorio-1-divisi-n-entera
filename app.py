import streamlit as st

st.set_page_config(page_title="Explorador de divisiones", layout="centered")

st.title("🧩 Explorador de divisiones")

st.write(
    "Primero elegimos una cantidad de objetos. Después decidimos en cuántos grupos repartirlos."
)

# -----------------------------
# Paso 1
# -----------------------------
st.subheader("1. Elegí la cantidad de objetos")

total = st.slider("Cantidad de objetos", 1, 80, 26)

st.write("Objetos disponibles:")
st.markdown("### " + "🟦 " * total)

st.divider()

# -----------------------------
# Paso 2
# -----------------------------
st.subheader("2. Elegí cuántos grupos querés formar")

cantidad_grupos = st.slider("Cantidad de grupos", 1, 12, 3)

objetos_por_grupo = total // cantidad_grupos
sin_repartir = total % cantidad_grupos

st.write("La aplicación reparte los objetos en grupos iguales siempre que sea posible.")

for i in range(cantidad_grupos):
    with st.container(border=True):
        st.write(f"Grupo {i + 1}")
        if objetos_por_grupo > 0:
            st.markdown("### " + "🟦 " * objetos_por_grupo)
        else:
            st.write("Todavía no recibió objetos.")

if sin_repartir > 0:
    with st.container(border=True):
        st.write("Objetos que todavía no se repartieron")
        st.markdown("### " + "🟨 " * sin_repartir)
else:
    st.success("Todos los objetos quedaron repartidos en los grupos.")

st.divider()

# -----------------------------
# Paso 3
# -----------------------------
st.subheader("3. Pensá antes de mirar la cuenta")

st.markdown(f"""
Con esta organización:

- Hay **{cantidad_grupos} grupos**.
- En cada grupo quedaron **{objetos_por_grupo} objetos**.
- Quedaron **{sin_repartir} objetos** sin repartir.

Antes de seguir, respondé con tus palabras:

1. ¿Cómo sabés cuántos objetos quedaron en cada grupo?
2. ¿Por qué los objetos amarillos no se repartieron?
3. ¿Qué tendría que pasar para que todos los grupos reciban un objeto más?
4. Mové la cantidad de objetos. ¿Qué cambia?
5. Mové la cantidad de grupos. ¿Qué cambia?
""")

st.divider()

# -----------------------------
# Paso 4
# -----------------------------
st.subheader("4. Cuenta de dividir")

mostrar_cuenta = st.checkbox("Mostrar la cuenta de dividir")

if mostrar_cuenta:
    producto = cantidad_grupos * objetos_por_grupo

    st.markdown("La cuenta organiza la misma información que vimos con los objetos.")

    # Cuenta en formato escolar aproximado, usando HTML/CSS simple.
    st.markdown(f"""
<style>
.division-box {{
    display: flex;
    justify-content: center;
    margin-top: 1rem;
    margin-bottom: 1rem;
}}
.division-escolar {{
    font-family: 'Courier New', monospace;
    font-size: 34px;
    line-height: 1.25;
    color: inherit;
}}
.fila-superior {{
    display: grid;
    grid-template-columns: 95px 28px 95px;
    align-items: end;
}}
.fila-principal {{
    display: grid;
    grid-template-columns: 95px 28px 95px;
    align-items: center;
}}
.fila-resta {{
    display: grid;
    grid-template-columns: 95px 28px 95px;
    align-items: center;
}}
.fila-resto {{
    display: grid;
    grid-template-columns: 95px 28px 95px;
    align-items: center;
}}
.numero {{
    text-align: center;
}}
.divisor {{
    text-align: center;
}}
.dividendo {{
    border-left: 4px solid currentColor;
    border-bottom: 4px solid currentColor;
    padding-left: 14px;
    text-align: center;
}}
.cociente {{
    border-bottom: 4px solid currentColor;
    padding-left: 14px;
    text-align: center;
}}
.resta {{
    text-align: center;
    border-bottom: 3px solid currentColor;
}}
.resto {{
    text-align: center;
}}
.nombre {{
    font-size: 15px;
    font-family: sans-serif;
    opacity: 0.85;
    text-align: center;
    margin-top: 4px;
}}
</style>

<div class="division-box">
  <div>
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

    st.markdown(f"""
En esta cuenta:

- **{total}** es la cantidad total de objetos. Se llama **dividendo**.
- **{cantidad_grupos}** es la cantidad de grupos entre los que se reparte. Se llama **divisor**.
- **{objetos_por_grupo}** es la cantidad que queda en cada grupo. Se llama **cociente**.
- **{sin_repartir}** es la cantidad que queda sin repartir. Se llama **resto**.
- **{producto}** es la cantidad de objetos que sí pudieron repartirse en partes iguales.
""")

st.divider()

# -----------------------------
# Paso 5
# -----------------------------
st.subheader("5. Escritura matemática")

mostrar_igualdad = st.checkbox("Mostrar la escritura matemática")

if mostrar_igualdad:
    st.markdown(f"### {total} = {cantidad_grupos} × {objetos_por_grupo} + {sin_repartir}")

    st.markdown(f"""
Esta escritura resume lo que se vio antes:

- Se formaron **{cantidad_grupos} grupos**.
- Cada grupo recibió **{objetos_por_grupo} objetos**.
- Quedaron **{sin_repartir} objetos** sin repartir.

Por eso:

**{total} = {cantidad_grupos} × {objetos_por_grupo} + {sin_repartir}**
""")
