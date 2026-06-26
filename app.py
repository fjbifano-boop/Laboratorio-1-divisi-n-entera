import streamlit as st

st.set_page_config(page_title="Explorador de divisiones", layout="centered")

st.title("🧩 Explorador de divisiones")

st.write(
    "Mové los controles o usá los botones para observar qué ocurre con los grupos, "
    "el cociente y el resto."
)

# Valor inicial guardado
if "total" not in st.session_state:
    st.session_state.total = 37

grupo = st.slider("¿Cuántos objetos forman cada grupo?", 1, 20, 5)

st.write("Cantidad de objetos")

col_b1, col_b2, col_b3 = st.columns([1, 2, 1])

with col_b1:
    if st.button("➖ Quitar 1"):
        if st.session_state.total > 1:
            st.session_state.total -= 1

with col_b2:
    st.session_state.total = st.slider(
        "¿Cuántos objetos hay?",
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

cociente = total // grupo
resto = total % grupo

st.divider()

st.subheader("Representación")

for _ in range(cociente):
    st.write("🟦 " * grupo)

if resto > 0:
    st.write("**Sobran:**")
    st.write("🟨 " * resto)
else:
    st.success("No sobra ningún objeto.")

st.divider()

mostrar_igualdad = st.checkbox("Mostrar la igualdad de la división")

if mostrar_igualdad:
    st.subheader("Escritura matemática")

    st.markdown(f"### {total} = {grupo} × {cociente} + {resto}")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Grupos completos", cociente)

    with col2:
        st.metric("Objetos que sobran", resto)

st.divider()

st.subheader("¿Qué podés investigar?")

if resto == 0:
    st.info("✔ El resto es 0. Se completó un grupo. ¿Qué ocurrió con el cociente?")
elif resto == grupo - 1:
    st.info("🤔 Sólo falta un objeto para formar otro grupo completo. ¿Qué pensás que pasará si agregás 1?")
else:
    st.info(f"🤔 Faltan {grupo-resto} objetos para completar otro grupo.")

st.markdown("""
### Desafíos

1. Dejá fijo el tamaño del grupo y usá varias veces el botón **Agregar 1**.
2. Observá qué pasa con el resto.
3. ¿Cuándo vuelve a aparecer resto 0?
4. ¿Qué ocurre con el cociente justo en ese momento?
5. ¿Puede el resto ser igual al tamaño del grupo?
""")
