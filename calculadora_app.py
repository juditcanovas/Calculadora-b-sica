import streamlit as st

st.title("Calculadora Básica de Python")

# Entrada de números
num1 = st.number_input("Introduce el primer número", value=0.0)
num2 = st.number_input("Introduce el segundo número", value=0.0)

# Selección de operación
operacion = st.selectbox(
    "Selecciona una operación",
    ("Suma", "Resta", "Multiplicación", "División")
)

# Realizar cálculo cuando el usuario presiona un botón
if st.button("Calcular"):
    resultado = 0
    if operacion == "Suma":
        resultado = num1 + num2
    elif operacion == "Resta":
        resultado = num1 - num2
    elif operacion == "Multiplicación":
        resultado = num1 * num2
    elif operacion == "División":
        if num2 != 0:
            resultado = num1 / num2
        else:
            st.error("Error: No se puede dividir por cero.")
            resultado = "Indefinido" # O puedes poner None para manejarlo mejor

    # Mostrar el resultado
    st.success(f"El resultado es: {resultado}")

st.markdown("---")
st.write("¡Una calculadora simple hecha con Streamlit!")