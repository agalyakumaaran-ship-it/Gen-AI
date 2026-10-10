import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Beautiful Calculator",
    page_icon="🧮",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

    .main {
        background-color: #f5f7fb;
    }

    .calculator-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .calculator-subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .result-box {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    .result-label {
        color: #777;
        font-size: 16px;
    }

    .result-value {
        font-size: 40px;
        font-weight: bold;
        margin-top: 8px;
    }

</style>
""", unsafe_allow_html=True)


# Title
st.markdown(
    '<div class="calculator-title">🧮 Smart Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="calculator-subtitle">Simple • Beautiful • Powerful</div>',
    unsafe_allow_html=True
)


# Input section
col1, col2 = st.columns(2)

with col1:
    number1 = st.number_input(
        "🔢 First Number",
        value=0.0
    )

with col2:
    number2 = st.number_input(
        "🔢 Second Number",
        value=0.0
    )


# Operation
operation = st.selectbox(
    "⚙️ Choose Operation",
    [
        "➕ Addition",
        "➖ Subtraction",
        "✖️ Multiplication",
        "➗ Division"
    ]
)


# Calculate button
if st.button("✨ Calculate", use_container_width=True):

    if operation == "➕ Addition":
        result = number1 + number2
        symbol = "+"

    elif operation == "➖ Subtraction":
        result = number1 - number2
        symbol = "-"

    elif operation == "✖️ Multiplication":
        result = number1 * number2
        symbol = "×"

    elif operation == "➗ Division":

        if number2 == 0:
            st.error("⚠️ Cannot divide by zero!")
            st.stop()

        result = number1 / number2
        symbol = "÷"


    # Display calculation
    st.markdown(
        f"""
        <div class="result-box">
            <div class="result-label">Your Result</div>
            <div class="result-value">
                {number1:g} {symbol} {number2:g} = {result:g}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("✅ Calculation completed successfully!")


# Information section
st.divider()

st.markdown("### 💡 How to use")

st.write("""
1. Enter your first number.
2. Enter your second number.
3. Select an operation.
4. Click **✨ Calculate**.
5. Your result will appear above.
""")

st.caption("Built with ❤️ using Python and Streamlit")