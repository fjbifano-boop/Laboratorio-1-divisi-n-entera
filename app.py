import streamlit as st

st.set_page_config(page_title="Explorador de divisiones", layout="centered")

st.title("🧩 Explorador de divisiones")

st.write(
    "Mové los controles y observá qué ocurre con los grupos, el cociente y el resto."
)

total = st.slider("¿Cuántos objetos hay?", 1, 100, 37)
grupo = st.slider("¿Cuántos objetos forman cada grupo?", 1, 20, 5)

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
    st.info("✔ El resto es 0. ¿Qué significa esto respecto de los grupos?")
elif resto == grupo - 1:
    st.info("🤔 Sólo falta un objeto para formar otro grupo completo.")
else:
    st.info(f"🤔 Faltan {grupo-resto} objetos para completar otro grupo.")

st.markdown("""
### Desafíos

1. Dejá fijo el tamaño del grupo y cambiá la cantidad de objetos.
2. ¿Cuándo vuelve a aparecer resto 0?
3. ¿Cuáles son todos los restos posibles para este divisor?
4. ¿Puede el resto ser igual al tamaño del grupo?
5. ¿Qué ocurre con el cociente cuando el resto vuelve a 0?
""")
