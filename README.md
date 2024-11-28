<div align="center">
  <img src="/image/WeaveCAN1_Logo.png" alt="WEaveCAN1 Logo" width="800">  
  <br><br>
    <a href="https://github.com/JoerenAguila">Joeren Aguila IT - 2104</a>
  </p>
</div>

---

## **Table of Contents**

I. [Overview](#i-overview)  
II. [Python Principles](#ii-python-principles)  
III. [Sustainable Development Goal (SDG) Integration](#iii-sustainable-development-goal-sdg-integration)  
IV. [Instructions for Running the Program](#iv-instructions-for-running-the-program)  

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

## **III. Python Concepts and Libraries**

**WEave CAN** utilizes essential Python principles and libraries to ensure a structured and efficient system. Below is a breakdown of the concepts applied in the program:

### 1. **Object-Oriented Programming (OOP)**
The system is built using OOP to model real-world entities effectively:
- **Classes and Subclasses**:  
  - `User` serves as a base class for `Weaver` and `Admin`, which inherit and extend its functionality.
  - `Product` and `Order` classes represent inventory items and customer transactions, respectively.
- **Encapsulation**:  
  Data and methods are encapsulated within classes, maintaining modularity and data security. For example, `order_history` in the `Weaver` class is private to the user.
- **Inheritance**:  
  The `Admin` class inherits from the `User` class and adds admin-specific functionalities like generating sales reports.
- **Polymorphism**:  
  Methods like `get_user_type` return outputs based on the user type (e.g., Weaver or Admin), demonstrating dynamic behavior.

### 2. **Error Handling**
- The `Product` class validates the material and pattern inputs against predefined sets (`VALID_MATERIALS` and `VALID_PATTERNS`), raising a `ValueError` for invalid entries.
- Try-except blocks are used to handle invalid inputs during order creation.

### 3. **Core Libraries**
- **`random`**:  
  Generates unique order IDs for tracking orders, ensuring no duplicate identifiers.
  
### 4. **Dynamic Features**
- **Inventory Management**:  
  The `Product` class tracks stock levels and sales. Methods like `apply_sale` allow dynamic price adjustments.
- **Order Creation and Tracking**:  
  The `Order` class manages transaction details, including product quantity, customer details, and total amount.
- **User Roles**:  
  - `Weaver` users can view their order history and cancel pending orders.
  - `Admin` users have additional privileges, like generating sales reports and applying discounts.

### 5. **Reusable Functions**
The system includes reusable functions to streamline operations:
- **`view_inventory`**: Displays the current stock with details like price, stock quantity, material, and pattern.
- **`create_order`**: Facilitates order placement, updating inventory and customer order history.

### 6. **Validation and Reporting**
- **Admin Reporting**:  
  Admin users can generate reports to identify the best and least-selling products using the `generate_best_seller_report` and `generate_least_seller_report` methods.
- **Input Validation**:  
  Functions validate user inputs to ensure consistency and prevent errors (e.g., invalid product selections or insufficient stock).

This system demonstrates Python's versatility in building scalable, modular applications that can handle diverse user roles and operations.

---

## **III. Sustainable Development Goal (SDG) Integration**

<div align="center">
  <img src="https://www.un.org/sites/un2.un.org/files/field/image/e_gif_08.gif" alt="SDG 8 GIF" width="200">
</div>

**WEave CAN** aligns with the **United Nations Sustainable Development Goals**, particularly **SDG 8: Decent Work and Economic Growth**. Here’s how it contributes:

1. **Efficient Business Practices**  
   Streamlines operations for Filipino weavers, enabling them to scale their businesses efficiently.

2. **Economic Empowerment**  
   Provides digital tools for weavers to stabilize their income and expand their reach.

3. **Cultural Preservation**  
   Highlights and supports traditional weaving materials (e.g., abaca, piña, cotton), preserving Filipino artistry.

4. **Community Upliftment**  
   Enhances opportunities for indigenous and rural communities by creating sustainable economic activities.

5. **Inclusive Growth**  
   Promotes gender equality and inclusivity by empowering female artisans, who are often the primary weavers.

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
<br><br>
  <h3 align="center"><strong>Thank you for your priceless contribution to the cultural legacy of the Philippines!</strong></h3>
  <h2 align="center">"WEAVE GOT IT ALL FOR YOU!"</h2>
</div>
---
