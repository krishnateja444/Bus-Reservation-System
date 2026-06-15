import streamlit as st
from bus_system import BusReservationSystem

st.set_page_config(
    page_title="Bus Reservation System",
    page_icon="🚌",
    layout="wide"
)

if "system" not in st.session_state:
    st.session_state.system = BusReservationSystem()

system = st.session_state.system

st.title("🚌 Bus Reservation System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Available Buses",
        "Reserve Seat",
        "Seat Layout"
    ]
)

# -----------------------------
# AVAILABLE BUSES
# -----------------------------
if menu == "Available Buses":

    st.header("Available Buses")

    for bus in system.get_all_buses():

        with st.container(border=True):

            st.subheader(f"Bus No: {bus.bus_no}")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**From:** {bus.source}")
                st.write(f"**To:** {bus.destination}")
                st.write(f"**Driver:** {bus.driver}")

            with col2:
                st.write(f"**Arrival:** {bus.arrival}")
                st.write(f"**Departure:** {bus.departure}")

# -----------------------------
# RESERVE SEAT
# -----------------------------
elif menu == "Reserve Seat":

    st.header("Reserve a Seat")

    bus_numbers = [
        bus.bus_no
        for bus in system.get_all_buses()
    ]

    selected_bus = st.selectbox(
        "Select Bus",
        bus_numbers
    )

    bus = system.get_bus(selected_bus)

    name = st.text_input("Passenger Name")

    gender = st.selectbox(
        "Gender",
        ["M", "F"]
    )

    available_seats = bus.get_available_seats()

    seat_no = st.selectbox(
        "Select Seat",
        available_seats
    )

    if st.button("Book Ticket"):

        success, message = bus.reserve_seat(
            seat_no,
            name,
            gender
        )

        if success:

            st.success(message)

            st.markdown("## 🎫 Ticket Confirmation")

            st.write(f"**Passenger:** {name}")
            st.write(f"**Gender:** {gender}")
            st.write(f"**Seat Number:** {seat_no}")
            st.write(f"**Bus Number:** {bus.bus_no}")
            st.write(
                f"**Route:** {bus.source} ➜ {bus.destination}"
            )
            st.write(f"**Arrival:** {bus.arrival}")
            st.write(f"**Departure:** {bus.departure}")

        else:
            st.error(message)

# -----------------------------
# SEAT LAYOUT
# -----------------------------
elif menu == "Seat Layout":

    st.header("Seat Layout")

    bus_numbers = [
        bus.bus_no
        for bus in system.get_all_buses()
    ]

    selected_bus = st.selectbox(
        "Select Bus",
        bus_numbers
    )

    bus = system.get_bus(selected_bus)

    seats = bus.get_seat_layout()

    for row in range(8):

        cols = st.columns(4)

        for col in range(4):

            idx = row * 4 + col

            if seats[idx] is None:
                label = f"🟩 {idx+1}"
            else:
                label = (
                    f"🟥 {idx+1}\n"
                    f"({seats[idx].gender})"
                )

            cols[col].button(
                label,
                key=f"seat_{idx}",
                disabled=True
            )