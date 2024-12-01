<div align="center">
  <img src="/image/WEaveCAN1_Logo.png" alt="WEaveCAN1 Logo" width="800">  
  <br><br>
    <a href="https://github.com/JoerenAguila">Joeren Aguila IT - 2104</a>
  </p>
</div>

---

## **Table of Contents**

I. [Overview](#i-overview)  
II. [Python Concepts in WEave CAN](#ii-python-concepts-in-weave-can)  
III. [Sustainable Development Goal (SDG) Integration](#iii-sustainable-development-goal-sdg-integration)  
IV. [Instructions for Running the Program](#iv-instructions-for-running-the-program)  

---

## **I. Overview**

### Why WEave CAN?

**WEave CAN** is a digital solution designed to empower Filipino weavers by streamlining inventory and order management. It addresses the challenges of manual business operations, enabling artisans to focus on their craft while improving efficiency and market access.

### Key Features:
- **Inventory Tracking** - add, update, and monitor stock levels for products like shawls, bags, and blankets.  
- **Order Management** - automatically adjust stock and manage customer orders seamlessly.  
- **Reporting** - generate sales reports to make informed business decisions.  
- **User Roles** - supports **Weaver** (artisan-focused) and **Admin** (management-focused) roles.  
- **Order History & Cancellation** - view and cancel orders easily.  
- **Discount Management** - admins can apply promotional discounts to products.  

This project supports market expansion, business sustainability, and cultural preservation for Filipino artisans.

---

## **II. Python Concepts in WEave CAN**

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
In the concept of the name **WEave CAN,**

**WE** means Woman Empowerment which highlights the woman lead business of the weaving community here in our country.

**CAN** means they CAN also elevate the opportunities of their business transactions or the capability to work through a digitalized console based application.

Thus, **WEave CAN** aligns with multiple Sustainable Development Goals, particularly **SDG 8: Decent Work and Economic Growth** and **SDG 5: Gender Equality**. 

---

### **1. SDG 8: Decent Work and Economic Growth**

<div align="center">
  <img src="https://www.un.org/sites/un2.un.org/files/field/image/e_gif_08.gif" width="200">
</div>

**WEave CAN** contributes to **SDG 8** by fostering sustainable business practices and supporting economic growth in artisan communities:

- **Efficiency and Growth** - streamlines inventory and order management, enabling artisans to scale their businesses efficiently.
- **Economic Empowerment** - provides access to digital tools that help weavers achieve income stability and financial independence.
- **Cultural Heritage** - highlights traditional weaving techniques and materials (e.g., abaca, cotton) to preserve Filipino craftsmanship.
- **Community Impact** - strengthens local economies and benefits indigenous and tribal groups reliant on weaving as a primary source of livelihood.

---

### **2. SDG 5: Gender Equality**

<div align="center">
  <img src="https://www.un.org/sites/un2.un.org/files/field/image/e_gif_05.gif" alt="SDG 5 GIF" width="200">
</div>

**WEave CAN** actively supports **SDG 5** by promoting gender equality and empowering women, who constitute a significant portion of Filipino weavers:

- **Women’s Empowerment** - focuses on providing digital tools and resources to women artisans, enabling them to manage their businesses more effectively and access larger markets.
- **Economic Inclusion** - addresses barriers that limit women’s participation in the workforce by offering solutions tailored to their roles in traditional crafts.
- **Skill Development** - encourages the preservation and growth of weaving skills, often passed down through generations of women, ensuring their cultural and economic relevance.
- **Leadership Opportunities** - recognizes women artisans as leaders in preserving cultural heritage and driving economic change within their communities.

By integrating these SDGs into its design and goals, **WEave CAN** serves as a platform for inclusive growth, gender equality, and cultural preservation, contributing to a better future for Filipino weaving communities.


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
