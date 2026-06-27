import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO

st.set_page_config(
    page_title="LIM - Laboratorio de división",
    layout="centered"
)

def dibujar_cuenta(dividendo, divisor, cociente, producto, resto):
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

    rect = plt.Rectangle(
        (0.2, 0.2), 9.6, 6.6,
        linewidth=2,
        edgecolor=gris,
        facecolor="white"
    )
    ax.add_patch(rect)

    x_izq = 3.4
    x_der = 6.3

    ax.text(x_izq, 5.2, str(dividendo), fontsize=40, fontweight="bold",
            ha="center", va="center", color=naranja)

    ax.text(x_der, 5.2, str(divisor), fontsize=40, fontweight="bold",
            ha="center", va="center", color=azul)

    ax.plot([4.8, 4.8], [2.0, 6.1], color=negro, linewidth=4)
    ax.plot([4.8, 7.55], [4.4, 4.4], color=negro, linewidth=4)

    ax.text(x_der, 3.4, str(cociente), fontsize=40, fontweight="bold",
            ha="center", va="center", color=verde)

    ax.text(x_izq, 3.4, f"−{producto}", fontsize=34, fontweight="bold",
            ha="center", va="center", color=verde)

    ax.plot([2.35, 4.35], [2.65, 2.65], color=negro, linewidth=3)

    ax.text(x_izq, 1.7, str(resto), fontsize=40, fontweight="bold",
            ha="center", va="center", color=rojo)

    ax.annotate(
        "Dividendo",
        xy=(x_izq - 0.45, 5.2), xytext=(0.85, 5.2),
        fontsize=16, fontweight="bold", color=naranja,
        arrowprops=dict(arrowstyle="->", lw=2.5, color=naranja),
        ha="left", va="center"
    )

    ax.annotate(
        "Divisor",
        xy=(x_der + 0.25, 5.2), xytext=(7.85, 5.2),
        fontsize=16, fontweight="bold", color=azul,
        arrowprops=dict(arrowstyle="->", lw=2.5, color=azul),
        ha="left", va="center"
    )

    ax.annotate(
        "Cociente",
        xy=(x_der + 0.25, 3.4), xytext=(7.85, 3.4),
        fontsize=16, fontweight="bold", color=verde,
        arrowprops=dict(arrowstyle="->", lw=2.5, color=verde),
        ha="left", va="center"
    )

    ax.annotate(
        "Resto",
        xy=(x_izq + 0.20, 1.7), xytext=(4.75, 1.15),
        fontsize=16, fontweight="bold", color=rojo,
        arrowprops=dict(arrowstyle="->", lw=2.5, color=rojo),
        ha="left", va="center"
    )

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


def mostrar_paso(numero, titulo):
    st.markdown(f"### {numero}. {titulo}")


st.title("LIM · Laboratorio de división")
st.write("Exploramos cómo repartir objetos en grupos iguales.")

st.divider()

mostrar_paso(1, "Elegí la cantidad de objetos")
total = st.slider("Cantidad de objetos", 1, 80, 37)
st.write(f"Total de objetos: **{total}**")
st.markdown("### " + "🟦 " * total)

st.divider()

mostrar_paso(2, "Elegí cuántos grupos iguales querés formar")
cantidad_grupos = st.slider("Cantidad de grupos", 1, 12, 5)
st.write(f"Cantidad de grupos: **{cantidad_grupos}**")

objetos_por_grupo = total // cantidad_grupos
sin_repartir = total % cantidad_grupos
producto = cantidad_grupos * objetos_por_grupo

st.info(
    f"La aplicación reparte los {total} objetos en {cantidad_grupos} grupos iguales, siempre que sea posible."
)

st.divider()

mostrar_paso(3, "Así quedaron los objetos")

for i in range(cantidad_grupos):
    with st.container(border=True):
        st.write(f"Grupo {i + 1}")
        if objetos_por_grupo > 0:
            st.markdown("### " + "🟦 " * objetos_por_grupo)
            st.write(f"{objetos_por_grupo} objetos")
        else:
            st.write("Todavía no recibió objetos.")

if sin_repartir > 0:
    st.warning(f"Objetos que todavía no se repartieron: {'🟨 ' * sin_repartir}")
else:
    st.success("Todos los objetos quedaron repartidos en los grupos.")

st.divider()

mostrar_paso(4, "Respondé estas preguntas antes de mirar la cuenta")

st.markdown("""
1. ¿Cuántos objetos hay en cada grupo?
2. ¿Cuántos grupos se formaron?
3. ¿Cuántos objetos no se pudieron repartir?
4. ¿Qué tendría que pasar para que cada grupo recibiera un objeto más?
5. Mové la cantidad de objetos o la cantidad de grupos. ¿Qué cambia?
""")

st.divider()

mostrar_paso(5, "Miramos la cuenta de dividir")

mostrar_cuenta = st.checkbox("Mostrar la cuenta de dividir")

if mostrar_cuenta:
    st.write("La cuenta representa el mismo reparto que observamos con los objetos.")

    imagen_cuenta = dibujar_cuenta(
        dividendo=total,
        divisor=cantidad_grupos,
        cociente=objetos_por_grupo,
        producto=producto,
        resto=sin_repartir
    )

    st.image(imagen_cuenta, use_container_width=True)

    st.markdown(f"""
- **{total}** es la cantidad total de objetos. Se llama **dividendo**.
- **{cantidad_grupos}** es la cantidad de grupos. Se llama **divisor**.
- **{objetos_por_grupo}** es la cantidad de objetos en cada grupo. Se llama **cociente**.
- **{sin_repartir}** es la cantidad de objetos que no se pudieron repartir. Se llama **resto**.
- **{producto}** es la cantidad de objetos que sí pudieron repartirse en partes iguales.
""")

st.divider()

mostrar_paso(6, "Relacionamos con la expresión matemática")

mostrar_expresion = st.checkbox("Mostrar la expresión matemática")

if mostrar_expresion:
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
