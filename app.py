import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EcoTrack AI 🌱", layout="centered")

st.sidebar.title("EcoTrack AI 🌱")
st.sidebar.write("Track. Improve. Sustain.")

st.header("📥 Enter Your Daily Habits")

name = st.text_input("Enter your name ✍️")
st.title(f"🌱 EcoTrack App - {name}")

transport = st.selectbox(
    "Choose your transport 🚗",
    ["Car", "Bike", "Cycle", "Truck", "Public Transport"]
)

km = st.number_input("Distance travelled (km)", 0, 100, 10)
electricity = st.number_input("⚡ Electricity Usage (units)", 0, 50, 5)
food = st.selectbox("🍔 Food Type", ["Veg", "Non-Veg"])

if st.button("🔍 Calculate My Footprint"):

    # 👉 Transport carbon
    if transport == "Car":
        carbon = km * 0.21
    elif transport == "Bike":
        carbon = km * 0.1
    elif transport == "Cycle":
        carbon = 0
    elif transport == "Truck":
        carbon = km * 0.5
    else:
        carbon = km * 0.05

    # 👉 Add electricity + food
    carbon += electricity * 0.82

    if food == "Non-Veg":
        carbon += 5

    # 👉 Score
    score = max(0, 100 - int(carbon))

    st.header("🌍 Your Results")
    st.metric("Total Carbon Footprint (kg CO₂)", round(carbon, 2))

    st.subheader("🌱 Eco Score")
    st.progress(score)
    st.write(f"⭐ Eco Score: {score}/100")

    # 👉 Tips
    st.subheader("💡 Suggestions")
    tips = []

    if km > 20:
        tips.append("Use public transport 🚍")
    if electricity > 10:
        tips.append("Switch to LED bulbs 💡")
    if food == "Non-Veg":
        tips.append("Try plant-based meals 🥗")

    for tip in tips:
        st.write("👉", tip)

    # 👉 Message
    if carbon < 20:
        st.success("Great job! You're eco-friendly 🌱")
    elif carbon < 50:
        st.warning("Good, but you can improve 👍")
    else:
        st.error("High carbon footprint! Take action ⚠️")

    # 👉 Graph
    st.subheader("📊 Your Activity Breakdown")

    data = {
        "Category": ["Travel", "Electricity", "Food"],
        "CO2": [km * 0.21, electricity * 0.82, 5 if food == "Non-Veg" else 2]
    }

    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.bar(df["Category"], df["CO2"])
    ax.set_ylabel("CO₂ Emission")

    st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Made with ❤️ for Hackathon | EcoTrack AI")
