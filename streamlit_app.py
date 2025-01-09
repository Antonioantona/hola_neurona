import streamlit as st

# Mostrar la imagen
st.image("./img/neurona.jpg")

# Título de la aplicación
st.header("¡Hola neurona!")

# Variable de estado para controlar qué botón ha sido pulsado
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = "Una entrada"  # Valor predeterminado

# Crear las pestañas
tabs = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y un sesgo"])

# --- Pestaña: Una entrada ---
with tabs[0]:
    st.subheader("Una neurona con una entrada y un peso")
    
    # Configuración de sliders y entradas
    w = st.slider("Peso", min_value=0.0, max_value=5.0, value=0.0, key="peso_una_entrada")
    x = st.number_input("Introduzca el valor de la entrada", value=0.0, key="entrada_una_entrada")
    
    # Calcular salida
    if st.button("Calcular la salida", key="calc_one"):
        st.write(f"La salida de la neurona es {w * x}")

# --- Pestaña: Dos entradas ---
with tabs[1]:
    # Configuración de sliders y entradas
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Peso w<sub>0</sub>", unsafe_allow_html=True)
        w0 = st.slider("Peso w<sub>0</sub>", min_value=0.0, max_value=5.0, value=0.0, key="peso_w0_dos_entradas", label_visibility="collapsed")
        st.markdown("Entrada x<sub>0</sub>", unsafe_allow_html=True)
        x0 = st.number_input("Entrada x<sub>0</sub>", value=0.0, key="entrada_x0_dos_entradas", label_visibility="collapsed")
    with col2:
        st.markdown("Peso w<sub>1</sub>", unsafe_allow_html=True)
        w1 = st.slider("Peso w<sub>1</sub>", min_value=0.0, max_value=5.0, value=0.0, key="peso_w1_dos_entradas", label_visibility="collapsed")
        st.markdown("Entrada x<sub>1</sub>", unsafe_allow_html=True)
        x1 = st.number_input("Entrada x<sub>1</sub>", value=0.0, key="entrada_x1_dos_entradas", label_visibility="collapsed")
        
    # Calcular salida
    if st.button("Calcular la salida", key="calc_two"):
        salida = w0 * x0 + w1 * x1
        st.write(f"La salida de la neurona es {salida}")

# --- Pestaña: Tres entradas y un sesgo ---
with tabs[2]:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("Peso w<sub>0</sub>", unsafe_allow_html=True)
        w0 = st.slider("Peso w<sub>0</sub>", min_value=0.0, max_value=5.0, value=0.0, key="peso_w0_tres_entradas", label_visibility="collapsed")
        st.markdown("Entrada  x<sub>0</sub>", unsafe_allow_html=True)
        x0 = st.number_input("Entrada x<sub>0</sub>", value=0.0, key="entrada_x0_tres_entradas", label_visibility="collapsed")
    with col2:
        st.markdown("Peso w<sub>1</sub>", unsafe_allow_html=True)
        w1 = st.slider("Peso w<sub>1</sub>", min_value=0.0, max_value=5.0, value=0.0, key="peso_w1_tres_entradas", label_visibility="collapsed")
        st.markdown("Entrada  x<sub>1</sub>", unsafe_allow_html=True)
        x1 = st.number_input("Entrada x<sub>1</sub>", value=0.0, key="entrada_x1_tres_entradas", label_visibility="collapsed")
    with col3:
        st.markdown("Peso w<sub>2</sub>", unsafe_allow_html=True)
        w2 = st.slider("Peso w<sub>2</sub>", min_value=0.0, max_value=5.0, value=0.0, key="peso_w2_tres_entradas", label_visibility="collapsed")
        st.markdown("Entrada  x<sub>2</sub>", unsafe_allow_html=True)
        x2 = st.number_input("Entrada x<sub>2</sub>", value=0.0, key="entrada_x2_tres_entradas", label_visibility="collapsed")
    
    # Configuración para el sesgo
    bias = st.number_input("Introduzca el valor del sesgo", value=0.0, key="bias_tres_entradas")
     
    # Calcular salida
    if st.button("Calcular la salida", key="calc_three"):
        salida = w0 * x0 + w1 * x1 + w2 * x2 + bias
        st.write(f"La salida de la neurona es {salida}")
