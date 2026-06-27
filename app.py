import streamlit as st

st.set_page_config(page_title="Explorador de divisiones", layout="centered")

st.title("🧩 Explorador de divisiones")

st.write(
    "Mové los controles o usá los botones para explorar cómo se forman grupos."
)

# Conserva el valor elegido aunque se actualice la pantalla
if "total" not in st.session_state:
    st.session_state.total = 37

grupo = st.slider("¿Cuántos objetos tiene cada grupo?", 1, 20, 5)

st.write("Cantidad de objetos")

col_b1, col_b2, col_b3 = st.columns([1, 2, 1])

with col_b1:
    if st.button("➖ Quitar 1"):
        if st.session_state.total > 1:
            st.session_state.total -= 1

with col_b2:
    st.session_state.total = st.slider(
        "Cantidad de objetos",
        1,
        100,
        st.session_state.total,
        label_visibility="collapsed"
    )

with col_b3:
    if st.button("➕ Agregar 1"):
        if st.session_state.total < 100:
            st.session_state.total += 1

total = st.session_state.total
grupos_completos = total // grupo
sin_agrupar = total % grupo
faltan = 0 if sin_agrupar == 0 else grupo - sin_agrupar

st.divider()

st.subheader("Lo que se ve")

for _ in range(grupos_completos):
    st.write("🟦 " * grupo)

if sin_agrupar > 0:
    st.write("🟨 " * sin_agrupar + "⬜ " * faltan)
else:
    st.success("Todos los objetos quedaron en grupos completos.")

st.caption(
    "🟦 objetos en grupos completos · 🟨 objetos que todavía no forman un grupo completo · ⬜ lugares que faltan para completar otro grupo"
)

st.divider()

st.subheader("Observá")

if sin_agrupar == 0:
    st.info("Se completaron todos los grupos. ¿Qué pasa si agregás 1 objeto?")
elif sin_agrupar == grupo - 1:
    st.info("Falta sólo 1 objeto para completar otro grupo. ¿Qué pensás que pasará si lo agregás?")
else:
    st.info(f"Faltan {faltan} objetos para completar otro grupo.")

st.subheader("Desafíos para pensar antes de mostrar otras escrituras")

st.markdown("""
1. Dejá fijo el tamaño de los grupos y agregá objetos de a uno.
2. Observá cuándo se completa un nuevo grupo.
3. Explicá con tus palabras qué pasa con los objetos que todavía no forman un grupo completo.
4. ¿Puede quedar sin completar una fila con tantos objetos como tiene un grupo completo?
5. ¿Qué cambia justo cuando se completa un nuevo grupo?
""")

st.divider()

st.subheader("Otras formas de representar lo que viste")

mostrar_igualdad = st.checkbox("Mostrar la escritura matemática")

if mostrar_igualdad:
    st.markdown(f"### {total} = {grupo} × {grupos_completos} + {sin_agrupar}")

    st.markdown(f"""
En esta escritura:

- **{total}** es la cantidad total de objetos. En la división se llama **dividendo**.
- **{grupo}** es la cantidad de objetos que tiene cada grupo. En la división se llama **divisor**.
- **{grupos_completos}** es la cantidad de grupos completos. En la división se llama **cociente**.
- **{sin_agrupar}** es la cantidad de objetos que no alcanzan para formar otro grupo completo. En la división se llama **resto**.
""")

mostrar_cuenta = st.checkbox("Mostrar la cuenta de dividir")

if mostrar_cuenta:
    producto = grupo * grupos_completos

    cuenta = f"""
          {grupos_completos}
       ______
{grupo}  )  {total}
       {producto}
       ------
          {sin_agrupar}
"""

    st.code(cuenta, language="text")

    st.markdown(f"""
En la cuenta:

- **{producto}** representa los objetos que sí pudieron organizarse en grupos completos.
- **{total} - {producto} = {sin_agrupar}** muestra los objetos que no alcanzan para formar otro grupo completo.
""")
