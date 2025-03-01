import streamlit as st

# Inline CSS to add background color, styling, and hover effect on images
st.markdown("""
    <style>
    body {
        background-color: #FFEB3B; /* Fresh yellow color */
        background-size: cover;
        background-position: center;
        font-family: Arial, sans-serif;
        color: #4CAF50; /* Green color for text, complementing fruit theme */
    }

    .stApp {
        background: rgba(255, 255, 255, 0.8); /* Semi-transparent white background for readability */
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Light shadow effect */
    }

    .stButton>button {
        background-color: #FF6F61; /* Button color */
        color: white;
    }

    .stButton>button:hover {
        background-color: #FF3B30; /* Button hover color */
    }

    .stTitle, .stHeader, .stSubheader {
        color: #D32F2F; /* Red color for headers to make it vibrant */
    }

    /* Sidebar Styling */
    .css-1d391kg {
        background-color: #2C3E50; /* Dark blue-gray background for sidebar */
        color: #BDC3C7; /* Light gray color for text */
    }

    .css-1d391kg a {
        color: #BDC3C7; /* Links inside sidebar */
    }

    .css-1d391kg a:hover {
        color: #FF6F61; /* On hover, change link color to warm red */
    }

    /* Sidebar header */
    .css-1v3fvcr {
        color: #FFFFFF; /* White color for the sidebar header */
    }

    /* Hover Effect on Product Images */
    .product-image {
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease; /* Smooth transition */
    }

    .product-image:hover {
        transform: scale(1.1); /* Zoom effect on hover */
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2); /* Add shadow when hovered */
    }
    </style>
""", unsafe_allow_html=True)

# Sample fruit data (name, price, description, image)
fruits = [
    {"name": "Apple", "price": 3, "description": "Fresh red apples", "image": "apple.png"},
    {"name": "Banana", "price": 1, "description": "Sweet yellow bananas", "image": "banana.png"},
    {"name": "Orange", "price": 2, "description": "Juicy orange fruits", "image": "orange.png"},  # Image name updated to orange.png
    {"name": "Grapes", "price": 4, "description": "Fresh green grapes", "image": "grapes.png"},
    {"name": "Mango", "price": 5, "description": "Delicious ripe mangoes", "image": "mango.png"},
    {"name": "Pineapple", "price": 6, "description": "Tropical sweet pineapples", "image": "pineapple.png"},
]

# Shopping Cart and Wishlist
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'wishlist' not in st.session_state:
    st.session_state.wishlist = []

# Display fruits in the market
def show_fruits():
    # Custom header with inline CSS
    st.markdown("""
        <h1 style="text-align: center; color: #D32F2F; font-family: 'Arial', sans-serif;">
            Welcome to the Fresh Fruit Market!
        </h1>
    """, unsafe_allow_html=True)
    
    st.write("Browse our selection of fresh fruits below:")

    # Create columns to display products
    cols = st.columns(3)  # Create 3 columns

    for i, fruit in enumerate(fruits):
        with cols[i % 3]:  # Distribute fruits in columns
            # Use st.image with the image file name (assuming the images are in the same directory)
            st.image(fruit["image"], width=150)  # Ensure the image paths are correct
            
            # Display description and price
            st.write(fruit["description"])
            st.write(f"Price: ${fruit['price']} per item")
            
            # Add buttons to add to cart and wishlist
            if st.button(f"Add {fruit['name']} to Cart", key=f"cart_{fruit['name']}"):
                st.session_state.cart.append(fruit)
                st.success(f"{fruit['name']} added to your cart!")
            if st.button(f"Add {fruit['name']} to Wishlist", key=f"wishlist_{fruit['name']}"):
                st.session_state.wishlist.append(fruit)
                st.success(f"{fruit['name']} added to your wishlist!")

# Cart Page
def show_cart():
    st.subheader("Your Cart")
    if not st.session_state.cart:
        st.write("Your cart is empty.")
    else:
        total_price = 0
        for item in st.session_state.cart:
            st.write(f"{item['name']} - ${item['price']}")
            total_price += item['price']

        st.write(f"Total: ${total_price}")
        
        if st.button("Proceed to Checkout"):
            st.session_state.total_price = total_price
            st.session_state.cart_items = st.session_state.cart
            st.session_state.cart = []  # Clear cart after proceeding to checkout
            show_checkout()

# Wishlist Page
def show_wishlist():
    st.subheader("Your Wishlist")
    if not st.session_state.wishlist:
        st.write("Your wishlist is empty.")
    else:
        for item in st.session_state.wishlist:
            st.write(f"{item['name']} - ${item['price']}")
        
        if st.button("Move to Cart"):
            # Add all wishlist items to cart
            st.session_state.cart.extend(st.session_state.wishlist)
            st.session_state.wishlist = []  # Clear wishlist
            st.success("All items have been moved to the cart.")

# Checkout Page
def show_checkout():
    st.title("Checkout")
    st.subheader("Enter your details to complete the order")

    # User details form
    name = st.text_input("Full Name")
    address = st.text_area("Shipping Address")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")

    # Order summary
    st.subheader("Order Summary")
    for item in st.session_state.cart_items:
        st.write(f"{item['name']} - ${item['price']}")
    st.write(f"Total Price: ${st.session_state.total_price}")

    # Confirm order button
    if st.button("Confirm Order"):
        if name and address and email and phone:
            st.success("Order confirmed! Thank you for shopping with us.")
            st.write(f"Name: {name}")
            st.write(f"Address: {address}")
            st.write(f"Email: {email}")
            st.write(f"Phone: {phone}")
            st.write(f"Total: ${st.session_state.total_price}")
        else:
            st.error("Please fill in all the details to confirm your order.")

# Display the fruit market, cart, or wishlist page
page = st.sidebar.selectbox("Choose a page", ("Market", "Cart", "Wishlist"))

if page == "Market":
    show_fruits()
elif page == "Cart":
    show_cart()
elif page == "Wishlist":
    show_wishlist()
