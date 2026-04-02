import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="EcoTrack AI 🌱", layout="centered")

# Title
st.sidebar.title("EcoTrack AI 🌱")
st.sidebar.write("Track. Improve. Sustain.")

# Input Section
st.header("📥 Enter Your Daily Habits")

transport = st.selectbox(
    "Choose your transport 🚗",
    ["Car", "Bike", "Cycle", "Truck", "Public Transport"]
)

km = st.number_input("Distance travelled (km)", 0, 100, 10)
if transport == "Car":
    carbon = km * 0.21
elif transport == "Bike":
    carbon = km * 0.1
elif transport == "Cycle":
    carbon = km * 0.0
elif transport == "Truck":
    carbon = km * 0.5
else:
    carbon = km * 0.05
    carbon += electricity * 0.82
name = st.text_input("Enter your name ✍️")
st.title(f"🌱 EcoTrack App - {name}")

electricity = st.number_input("⚡ Electricity Usage (units)", min_value=0.0)
food = st.selectbox("🍔 Food Type", ["Veg", "Non-Veg"])
carbon = km * 0.5 + electricity * 1.5 + (5 if food == "Non-Veg" else 2)
if st.button("🔍 Calculate My Footprint"):
    carbon = (km * 0.21) + (electricity * 0.82)

if food == "Non-Veg":
    carbon += 5
    score = max(0, 100 - int(carbon))
                    
    score = 70
    st.progress(score)                

    if score > 80:
        st.success("Excellent 🌱")
    elif score > 50:
     st.warning("Average 👍")
    else:
        st.error("Needs Improvement ⚠️")

    # Results Section
    st.header("🌍 Your Results")

    st.metric("Total Carbon Footprint (kg CO₂)", round(carbon, 2))
    st.progress(score)

    st.write(f"⭐ Eco Score: {score}/100")

# Tips
tips = []

tips.append("Use public transport 🚍")
tips.append("Switch off lights 💡")
tips.append("Plant trees 🌱")

if km > 20:
    tips.append("Use public transport 🚍")
if electricity > 10:
    tips.append("Switch to LED bulbs 💡")
if food == "Non-Veg":
    tips.append("Try plant-based meals 🥗")
    
for tip in tips:
        st.write("👉", tip)
if carbon < 20:
        st.success("Great job! You're eco-friendly 🌱")
elif carbon < 50:
        st.warning("Good, but you can improve 👍")
else:
        st.error("High carbon footprint! Take action ⚠️")

if km > 20:
        st.write("🚶 Try public transport or carpooling")
if electricity > 10:
        st.write("💡 Switch off unused appliances")
if food == "Non-Veg":
        st.write("🥗 Reduce meat consumption for better impact")

    # Graph
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
#theme
st.markdown(
"""
<style>
body {background-color: #f0f2f6;}
</style>
""",
unsafe_allow_html=True
)

# Footer
st.markdown("---")
st.caption("Made with ❤️ for Hackathon | EcoTrack AI")
