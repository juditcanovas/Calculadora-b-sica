import streamlit as st

#Configuració den la página
st.set_page_config(
    page_title= 'Calculadora Básica',
    page_icon= '🧮',
    layout= 'wide',
    initial_sidebar_state= 'expanded'
)


st.title('🧮 Mi calculadora mejorada en Python')
st.markdown('Una calcuadora interactiva simple con **Steamlit**.')
st.write('---')

# --- DÓNDE COLOCAR st.columns() ---
# Aquí es donde creamos las tres columnas para las entradas y la operación.
# Estas columnas serán de igual ancho.
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('Primer Número')
    num1 = st.number_input("Introduce el primer número", value=0.0, key= 'num1')

with col2:
    st.subheader('Sgundo Número')
    num2 = st.number_input("Introduce el segundo número", value=0.0, key= 'num2')

# Selección de operación
with col3:
    st.subheader('Operación')
    operacion = st.selectbox(
    "Selecciona una operación",
    ("Suma", "Resta", "Multiplicación", "División"), key='operation_selector'
)

st.write('---') # Otra línea divisoria

# --- Centrando el Botón de Cálculo con Columnas ---
# Aquí creamos columnas con anchos relativos: una pequeña a la izquierda (1),
# una más grande en el medio para el botón (1), y otra pequeña a la derecha (1).
# Esto empuja el botón hacia el centro visualmente.
col_button_left, col_button_center, col_button_right = st.columns([1, 1, 1])

with col_button_center: # Colocamos el botón en la columna central
    if st.button('Calcular Resultado🪄'): # Faltaba el colon (:)
        resultado = None # Necesita más indentación
        # Todo este bloque necesita un nivel más de indentación para estar dentro del if del botón
        if operacion == "Suma":
            resultado = num1 + num2
            st.success(f'✅ La suma es: {resultado}')
        elif operacion == "Resta":
            resultado = num1 - num2
            st.success(f'✅ La resta es: {resultado}')
        elif operacion == "Multiplicación":
            resultado = num1 * num2
            st.success(f'✅ La multiplicación es: {resultado}')
        elif operacion == "División":
            if num2 != 0:
                resultado = num1 / num2
                st.success(f'✅ La división es: {resultado}')
            else:
                st.error("❌ Error: No se puede dividir por cero.")
                resultado = "Indefinido" # O puedes poner None para manejarlo mejor
        elif operacion == 'Módulo': # Corregido 'operación' a 'operacion'
            if num2 != 0:
                resultado = num1 % num2
                st.success(f'✅ El módulo es: {resultado}')
            else:
                # Esta línea necesita indentación adicional para estar dentro del 'else'
                st.error('❌ Error: No se puede calcular el módulo por cero.')

st.markdown("---")
st.write("¡Una calculadora simple hecha con Streamlit!")