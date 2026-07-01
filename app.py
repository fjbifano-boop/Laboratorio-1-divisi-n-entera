import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO
import math

# Reemplazar cuando estén disponibles
FORMULARIO_COMENTARIOS_URL = ""
DOCUMENTO_LIM_URL = ""

st.set_page_config(page_title="LIM - Explorando la división entera", layout="centered")

def buscar_organizacion_rectangular(n):
    if n <= 0:
        return (0, 0)
    mejor_filas, mejor_columnas = 1, n
    for filas in range(1, int(math.sqrt(n)) + 1):
        if n % filas == 0:
            mejor_filas, mejor_columnas = filas, n // filas
    return mejor_filas, mejor_columnas

def dibujar_objetos_rectangulares(n, color="#2F80ED"):
    """
    Dibuja n objetos como cuadrados del mismo tamaño.
    Si n admite una organización rectangular, la prioriza.
    """
    filas, columnas = buscar_organizacion_rectangular(n)

    if n == 0:
        fig, ax = plt.subplots(figsize=(2, 0.8), dpi=150)
        ax.axis("off")
        ax.text(0.5, 0.5, "Sin objetos", ha="center", va="center", fontsize=12)
    else:
        lado = 1
        margen = 0.35
        separacion = 0.25

        ancho = columnas * lado + (columnas - 1) * separacion + 2 * margen
        alto = filas * lado + (filas - 1) * separacion + 2 * margen

        fig, ax = plt.subplots(figsize=(max(2.0, ancho * 0.55), max(1.3, alto * 0.55)), dpi=150)
        ax.set_xlim(0, ancho)
        ax.set_ylim(0, alto)
        ax.axis("off")
        ax.set_aspect("equal")

        for f in range(filas):
            for c in range(columnas):
                x = margen + c * (lado + separacion)
                y = alto - margen - lado - f * (lado + separacion)
                cuadrado = plt.Rectangle(
                    (x, y),
                    lado,
                    lado,
                    facecolor=color,
                    edgecolor="#1E40AF" if color == "#2F80ED" else "#C2410C",
                    linewidth=1.5
                )
                ax.add_patch(cuadrado)

    buffer = BytesIO()
    fig.savefig(buffer, format="png", bbox_inches="tight", pad_inches=0.08, transparent=True)
    plt.close(fig)
    buffer.seek(0)
    return buffer

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
        fontsize=12, ha="center", va="center", color=negro
    )

    buffer = BytesIO()
    fig.savefig(buffer, format="png", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    buffer.seek(0)
    return buffer

def mostrar_paso(numero, titulo):
    st.markdown(f"### {numero}. {titulo}")

st.title("Explorando la división entera")
st.subheader("Repartir en grupos iguales")
st.write("Exploramos cómo repartir objetos completos en grupos iguales.")

st.info(
    "Este laboratorio trabaja con división entera: buscamos repartir objetos completos en grupos iguales. "
    "Cuando no alcanza para dar otro objeto a cada grupo, algunos objetos quedan sin repartir."
)

st.divider()

mostrar_paso(1, "Elegí la cantidad de objetos")
total = st.slider("Cantidad de objetos", 1, 80, 37, step=1)
st.write(f"Total de objetos: **{total}**")
st.markdown("### " + "🟦 " * total)

st.divider()

mostrar_paso(2, "Elegí en cuántos grupos iguales querés repartir")

cantidad_grupos = st.slider("Cantidad de grupos", 1, 12, 5, step=1)

st.write(f"Se formarán **{cantidad_grupos} grupos iguales**.")

objetos_por_grupo = total // cantidad_grupos
sin_repartir = total % cantidad_grupos
producto = cantidad_grupos * objetos_por_grupo

st.info(f"Con esta elección, los {total} objetos se repartirán en {cantidad_grupos} grupos iguales, siempre que sea posible.")

if total < cantidad_grupos:
    st.warning(
        f"Como hay menos objetos ({total}) que grupos ({cantidad_grupos}), en división entera no alcanza para dar 1 objeto a cada grupo. "
        f"Por eso cada grupo recibe 0 objetos y quedan {sin_repartir} objetos sin repartir. "
        "En otro tipo de problema se podrían partir los objetos y usar fracciones, pero este laboratorio se concentra en la división entera."
    )

st.divider()

mostrar_paso(3, "Así quedaron los objetos")

filas, columnas = buscar_organizacion_rectangular(objetos_por_grupo)

if objetos_por_grupo > 1 and filas > 1:
    st.caption(f"En cada grupo, los {objetos_por_grupo} objetos se organizan como un rectángulo de {filas} × {columnas}.")
elif objetos_por_grupo > 0:
    st.caption(f"En cada grupo, los {objetos_por_grupo} objetos quedan organizados en una sola fila.")

for i in range(cantidad_grupos):
    with st.container(border=True):
        st.write(f"Grupo {i + 1}")
        if objetos_por_grupo > 0:
            imagen_grupo = dibujar_objetos_rectangulares(objetos_por_grupo, color="#2F80ED")
            st.image(imagen_grupo, width=220)
            st.write(f"{objetos_por_grupo} objetos")
        else:
            st.write("Todavía no recibió objetos.")

if sin_repartir > 0:
    st.warning("Objetos que todavía no se repartieron:")
    imagen_sin_repartir = dibujar_objetos_rectangulares(sin_repartir, color="#F97316")
    st.image(imagen_sin_repartir, width=220)
else:
    st.success("Todos los objetos quedaron repartidos en los grupos.")

st.divider()

mostrar_paso(4, "Respondé estas preguntas antes de mirar la cuenta")

st.markdown("""
1. ¿Cuántos objetos hay en cada grupo?
2. ¿Cuántos grupos se formaron?
3. ¿Quedaron objetos sin repartir? ¿Qué número representa esa cantidad?
4. ¿Qué tendría que pasar para que cada grupo recibiera un objeto más?
5. Mové la cantidad de objetos o la cantidad de grupos de a uno. ¿Qué cambia?
""")

st.subheader("Para pensar: lo que queda sin repartir y la cantidad de grupos")

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

st.divider()

mostrar_paso(5, "Miramos la cuenta de dividir")

if st.checkbox("Mostrar la cuenta de dividir"):
    st.write("La cuenta representa el mismo reparto que observamos con los objetos.")
    imagen_cuenta = dibujar_cuenta(total, cantidad_grupos, objetos_por_grupo, producto, sin_repartir)
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
st.markdown("**Versión:** 1.0 (prototipo de circulación)")
st.markdown("Este laboratorio continúa en desarrollo. Tus comentarios nos ayudan a mejorarlo.")

if FORMULARIO_COMENTARIOS_URL:
    st.link_button("💬 Enviar un comentario o sugerencia", FORMULARIO_COMENTARIOS_URL)
else:
    st.caption("Próximamente: formulario para enviar comentarios o sugerencias.")

if DOCUMENTO_LIM_URL:
    st.link_button("📄 ¿Qué es LIM?", DOCUMENTO_LIM_URL)
else:
    st.caption("Próximamente: documento breve de presentación del proyecto LIM.")
