# 🚌 Bus Reservation System

A Bus Reservation System built using **Python, Streamlit, Object-Oriented Programming (OOP), and Data Classes** that enables users to view buses, reserve seats, and monitor seat availability through an interactive web interface.

---

## 📌 Overview

This project simulates a real-world bus reservation platform where users can browse available buses, select seats, and book tickets. The application uses a modular OOP-based architecture to manage buses, passengers, and reservations while providing a clean and intuitive Streamlit interface.

---

## ✨ Features

* 🚌 View available buses and route information
* 🎫 Reserve seats with passenger details
* 🪑 Interactive seat availability visualization
* 📊 Real-time seat status updates
* 💾 Session-based booking management
* 🏗️ Object-Oriented design with separate business logic and UI layers
* 📱 User-friendly Streamlit interface

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Object-Oriented Programming (OOP)
* Data Classes (`@dataclass`)
* Session State Management

---

## 📂 Project Structure

```text
bus-reservation-system/
│
├── app.py                # Streamlit user interface
├── bus_system.py         # Core business logic
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/bus-reservation-system.git
cd bus-reservation-system
```

### Install Dependencies

```bash
pip install streamlit
```

### Run the Application

```bash
streamlit run app.py
```

---

## 🎯 Application Modules

### 1. Available Buses

Displays all available buses along with:

* Bus Number
* Source
* Destination
* Driver Name
* Arrival Time
* Departure Time

---

### 2. Reserve Seat

Users can:

1. Select a bus
2. Enter passenger details
3. Choose an available seat
4. Confirm booking
5. View ticket confirmation

---

### 3. Seat Layout

Provides a visual representation of bus occupancy:

* 🟩 Available Seat
* 🟥 Reserved Seat

Each bus contains **32 seats** arranged in an 8 × 4 layout.

---

## 🏗️ System Design

### Passenger

Stores passenger information:

```python
@dataclass
class Passenger:
    name: str
    gender: str
```

---

### Bus

Responsible for:

* Managing seats
* Reserving tickets
* Tracking seat availability

Key Methods:

```python
reserve_seat()
get_available_seats()
get_seat_layout()
```

---

### BusReservationSystem

Central management layer responsible for:

* Loading buses
* Retrieving bus information
* Managing reservations

Key Methods:

```python
get_all_buses()
get_bus()
preload_buses()
```

---

## 📋 Preloaded Bus Routes

The application includes multiple predefined routes such as:

* Hyderabad → Bangalore
* Chennai → Coimbatore
* Kochi → Trivandrum
* Bangalore → Mysore
* Vijayawada → Tirupati

---

## 💻 Example Workflow

1. Select Bus **5196**
2. Enter passenger details
3. Select seat **12**
4. Click **Book Ticket**
5. Receive booking confirmation

Example Output:

```text
Passenger: Krishna
Seat Number: 12
Bus Number: 5196
Route: Vijayawada → Tirupati
Booking Status: Confirmed
```

---

## 🧠 Concepts Demonstrated

This project showcases:

* Object-Oriented Programming
* Data Classes
* State Management
* Modular Software Design
* Interactive Web Applications
* Basic Reservation System Design

---

## 🔮 Future Enhancements

* User Authentication
* Booking Cancellation
* Search Buses by Route
* Revenue Tracking Dashboard
* Booking History
* Database Integration (SQLite/MySQL)
* Email Ticket Confirmation
* Online Payment Integration
* Route Visualization

---


## ⚠️ Disclaimer

This project is developed for educational and learning purposes. It is a simulation of a reservation system and does not represent an actual bus booking platform.
