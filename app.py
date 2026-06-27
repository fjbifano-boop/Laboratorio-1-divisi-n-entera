import streamlit as st

st.set_page_config(page_title="Explorador de divisiones", layout="centered")

st.title("🧩 Explorador de divisiones")

st.write(
    "Primero elegimos una cantidad de objetos. Después decidimos en cuántos grupos repartirlos."
)

# -----------------------------
# Estilos simples
# -----------------------------
st.markdown("""
<style>
.objetos {
    font-size: 28px;
    line-height: 1.8;
    word-wrap: break-word;
}
.grupos {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 10px;
}
.grupo {
    border: 2px solid #999999;
    border-radius: 12px;
    padding: 10px;
    min-width: 110px;
    text-align: center;
    background-color: #f7f7f7;
}
.grupo-titulo {
    font-size: 14px;
    margin-bottom: 6px;
    color: #333333;
}
.grupo-objetos {
    font-size: 24px;
    line-height: 1.5;
}
.sin-repartir {
    border: 2px dashed #999999;
    border-radius: 12px;
    padding: 10px;
    margin-top: 14px;
    background-color: #fff8e5;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Paso 1
# -----------------------------
st.subheader("1. Elegí la cantidad de objetos")

total = st.slider("Cantidad de objetos", 1, 80, 37)

st.markdown(
    f"<div class='objetos'>{'🟦 ' * total}</div>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Paso 2
# -----------------------------
st.subheader("2. Elegí cuántos grupos querés formar")

cantidad_grupos = st.slider("Cantidad de grupos", 1, 12, 5)

objetos_por_grupo = total // cantidad_grupos
sin_repartir = total % cantidad_grupos

st.write("La aplicación organiza los objetos en grupos iguales siempre que sea posible.")

# Arma los grupos visuales
html = "<div class='grupos'>"

for i in range(cantidad_grupos):
    html += f"""
    <div class='grupo'>
        <div class='grupo-titulo'>Grupo {i+1}</div>
        <div class='grupo-objetos'>{'🟦 ' * objetos_por_grupo}</div>
    </div>
    """

html += "</div>"

st.markdown(html, unsafe_allow_html=True)

if sin_repartir > 0:
    st.markdown(
        f"""
        <div class='sin-repartir'>
            <b>Objetos que todavía no se repartieron:</b><br>
            <span style='font-size:24px;'>{'🟨 ' * sin_repartir}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
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
2. ¿Por qué esos objetos amarillos no se repartieron?
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

    cuenta = f"""
             {objetos_por_grupo}
          _______
{cantidad_grupos}   )   {total}
          {producto}
          -------
             {sin_repartir}
"""
    st.code(cuenta, language="text")

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
