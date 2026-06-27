import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

st.set_page_config(
    page_title="LIM - Laboratorio de división",
    layout="centered"
)

# -----------------------------
# Funciones auxiliares
# -----------------------------

def cargar_fuente(tamano, negrita=False):
    posibles = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if negrita else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if negrita else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for ruta in posibles:
        try:
            return ImageFont.truetype(ruta, tamano)
        except:
            pass
    return ImageFont.load_default()


def dibujar_cuenta(dividendo, divisor, cociente, producto, resto):
    """
    Dibuja la cuenta de dividir en formato escolar argentino:

        dividendo | divisor
       -producto | cociente
        resto
    """
    ancho, alto = 760, 420
    img = Image.new("RGB", (ancho, alto), "white")
    draw = ImageDraw.Draw(img)

    fuente_num = cargar_fuente(62, True)
    fuente_num_med = cargar_fuente(52, True)
    fuente_txt = cargar_fuente(24, True)
    fuente_txt_chica = cargar_fuente(21, False)

    negro = "#111827"
    azul = "#1d4ed8"
    verde = "#15803d"
    naranja = "#b45309"
    rojo = "#dc2626"
    gris = "#d1d5db"

    # Fondo y borde
    draw.rounded_rectangle([15, 15, ancho-15, alto-15], radius=22, fill="white", outline=gris, width=3)

    # Posiciones principales
    x_dividendo = 260
    x_divisor = 500
    y_arriba = 110
    y_abajo = 210
    y_resto = 310

    # Números
    draw.text((x_dividendo, y_arriba), str(dividendo), font=fuente_num, fill=naranja, anchor="mm")
    draw.text((x_divisor, y_arriba), str(divisor), font=fuente_num, fill=azul, anchor="mm")

    # Galera: línea vertical y línea horizontal
    draw.line([(370, 65), (370, 275)], fill=negro, width=6)
    draw.line([(370, 145), (610, 145)], fill=negro, width=6)

    # Cociente
    draw.text((x_divisor, y_abajo), str(cociente), font=fuente_num, fill=verde, anchor="mm")

    # Producto restado y línea de resta
    draw.text((x_dividendo, y_abajo), f"−{producto}", font=fuente_num_med, fill=verde, anchor="mm")
    draw.line([(170, 248), (340, 248)], fill=negro, width=5)

    # Resto
    draw.text((x_dividendo, y_resto), str(resto), font=fuente_num, fill=rojo, anchor="mm")

    # Etiquetas
    draw.text((72, 112), "Dividendo", font=fuente_txt, fill=naranja, anchor="lm")
    draw.line([(182, 112), (218, 112)], fill=naranja, width=4)
    draw.polygon([(218,112), (207,104), (207,120)], fill=naranja)

    draw.text((600, 92), "Divisor", font=fuente_txt, fill=azul, anchor="lm")
    draw.line([(585, 100), (540, 108)], fill=azul, width=4)
    draw.polygon([(540,108), (552,100), (554,116)], fill=azul)

    draw.text((600, 210), "Cociente", font=fuente_txt, fill=verde, anchor="lm")
    draw.line([(585, 210), (540, 210)], fill=verde, width=4)
    draw.polygon([(540,210), (552,202), (552,218)], fill=verde)

    draw.text((335, 325), "Resto", font=fuente_txt, fill=rojo, anchor="lm")
    draw.line([(320, 318), (292, 310)], fill=rojo, width=4)
    draw.polygon([(292,310), (306,306), (302,322)], fill=rojo)

    # Nota inferior
    draw.text(
        (ancho/2, 382),
        f"{dividendo} objetos repartidos en {divisor} grupos: {cociente} en cada grupo y {resto} sin repartir",
        font=fuente_txt_chica,
        fill=negro,
        anchor="mm"
    )

    return img


def mostrar_paso(numero, titulo):
    st.markdown(f"### {numero}. {titulo}")


# -----------------------------
# App
# -----------------------------

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

st.info(f"La aplicación reparte los {total} objetos en {cantidad_grupos} grupos iguales, siempre que sea posible.")

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
    st.write("La cuenta muestra la misma organización que vimos con los objetos.")

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

mostrar_paso(6, "Relacionamos con la escritura matemática")

mostrar_igualdad = st.checkbox("Mostrar la escritura matemática")

if mostrar_igualdad:
    st.markdown(f"## {total} = {cantidad_grupos} × {objetos_por_grupo} + {sin_repartir}")
    st.write("Esta escritura resume lo que se vio con los objetos y con la cuenta.")
