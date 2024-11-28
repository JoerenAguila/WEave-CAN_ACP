# **WEave CAN: Inventory and Order Management System for Filipino Weavers**

<div align="center">
  <img src="/image/WeaveCAN1_Logo.png" alt="WEaveCAN1 Logo" width="800">  
  <br><br>
  <h3 align="center">"Weave got it all for you!"</h3>
  <p align="center">
    <b>By:</b> <br>
    <a href="https://github.com/JoerenAguila">Joeren Aguila IT - 2104</a>
  </p>
</div>

---

## **Table of Contents**

1. [I. Overview](#i-overview)  
2. [II. Sustainable Development Goal 8 (SDG 8) Integration](#ii-sustainable-development-goal-8-sdg-8-integration)  
3. [III. Explanation of Python Concepts and Libraries](#iii-explanation-of-python-concepts-and-libraries)  
4. [IV. Instructions for Running the Program](#iv-instructions-for-running-the-program)  

---

## **I. Overview**

### Why WEave CAN?

**WEave CAN** is a digital solution designed to empower Filipino weavers by streamlining inventory and order management. It addresses the challenges of manual business operations, enabling artisans to focus on their craft while improving efficiency and market access.

### Key Features:
- **Inventory Tracking**:  
  Add, update, and monitor stock levels for products like shawls, bags, and blankets.  
- **Order Management**:  
  Automatically adjust stock and manage customer orders seamlessly.  
- **Reporting**:  
  Generate sales reports to make informed business decisions.  
- **User Roles**:  
  Supports **Weaver** (artisan-focused) and **Admin** (management-focused) roles.  
- **Order History & Cancellation**:  
  View and cancel orders easily.  
- **Discount Management**:  
  Admins can apply promotional discounts to products.  

This project supports market expansion, business sustainability, and cultural preservation for Filipino artisans.

---

## **II. Sustainable Development Goal 8 (SDG 8) Integration**

<div align="center">
  <img src="https://www.un.org/sites/un2.un.org/files/field/image/e_gif_08.gif" alt="SDG 8 GIF" width="600">
</div>

**WEave CAN** aligns with **SDG 8: Decent Work and Economic Growth** by promoting sustainable economic opportunities for Filipino artisans:  

1. **Efficiency and Growth**:  
   Streamlines business operations, helping artisans scale their businesses.  
2. **Economic Empowerment**:  
   Provides artisans access to digital tools for income stability.  
3. **Cultural Heritage**:  
   Highlights traditional weaving materials (e.g., abaca, cotton) to preserve Filipino craftsmanship.  
4. **Community Impact**:  
   Encourages local economic activity, benefiting indigenous and tribal groups in the Philippines.  

---

## **III. Explanation of Python Concepts and Libraries**

**WEave CAN** leverages key Python features to deliver a robust, scalable system:  

### 1. Object-Oriented Programming (OOP)  
- **Classes and Inheritance**:  
  Core entities like `User`, `Weaver`, and `Admin` are implemented using Python classes. Subclasses reuse and extend functionality from parent classes.  
- **Encapsulation**:  
  Encapsulated data within classes ensures modularity.  
- **Polymorphism**:  
  Methods adapt seamlessly to different object types, such as `Product` instances.  

### 2. Modules and Libraries  
- **`random`**:  
  Generates unique order IDs for tracking.  

### 3. Error Handling  
- Functions ensure validation of inputs and handle invalid cases gracefully.  

### 4. Inventory and Order Management  
- The `Product` class manages stock and pricing, while the `Order` class tracks transactions.  

### 5. Admin Functionality  
- Features like generating reports and applying discounts are included for business management.  

### 6. User Interface  
- A user-friendly menu-driven CLI improves usability.

---

## **IV. Instructions for Running the Program**

### Prerequisites
Ensure you have the following installed:  
- Python 3.x  
- Required libraries (`tkinter` for GUI, `random` for unique IDs).  

### Steps to Run the Program  

1. **Set Up the Environment**  
   Install Python and required libraries on your system.  

2. **Prepare the Files**  
   - Backend logic: Save as `weave_can.py`.  
   - GUI logic: Save as `weave_gui.py`.  

3. **Run the Program**  
   Open a terminal and execute:  
   ```bash
   python weave_gui.py

---


## **Acknowledgements**

I would like to express my sincere gratitude to the following individuals:

### **Instructor**
- **Ms. Fatima Marie P. Agdon, MSCS**  
  For your unwavering support, expert guidance, and insightful feedback throughout the development of this project. Your advice has been crucial in shaping the success of this system and in ensuring its overall quality.

### **Filipino Weavers**
- A special dedication goes to the **Filipino weavers**, whose talent and cultural heritage inspired the creation of this system. My goal is to celebrate and preserve Filipino weaving traditions while providing artisans with the tools they need for sustainable growth in today’s economy. This project is a tribute to your skill and creativity, and I hope it helps in enhancing the future of Filipino weaving communities.

<div align="center">
  <img src="/image/WEavers.png" alt="Weavers" width="800"> 
</div>

**Thank you for your priceless contribution to the cultural legacy of the Philippines!**  

**"WEAVE GOT IT ALL FOR YOU!"**

---
