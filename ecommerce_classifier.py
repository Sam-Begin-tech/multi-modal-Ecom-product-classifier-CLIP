

import torch
import clip
from PIL import Image
import streamlit as st

# Load CLIP model
device = "cpu"  # or "cuda" if you have GPU
model, preprocess = clip.load("ViT-B/32", device=device)

# Define eCommerce categories
categories = [
    "Smartphone",
    "Laptop",
    "Shirt",
    "Shoes",
    "Book",
    "Watch",
    "Headphones",
    "Camera",
    "Tablet",
    "Bag",
    "Jewelry",
    "Furniture",
    "Cosmetics",
    "Food",
    "Toys"
]

# Tokenize category labels
text = clip.tokenize(categories).to(device)

# Streamlit setup
st.title("eCommerce Product Categorizer")
st.write("Upload a product image to classify it into one of the eCommerce categories.")

# Upload image through Streamlit
uploaded_image = st.file_uploader("Choose a product image...", type=["jpg", "jpeg", "png",'webp'])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    
    # Preprocess and encode the image
    image_input = preprocess(image).unsqueeze(0).to(device)
    
    # Get image features from CLIP model
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text)
        
        # Calculate similarity between image and categories
        similarity = (image_features @ text_features.T).squeeze(0)
        
        # Get the index of the most similar category
        category_idx = similarity.argmax().item()
        predicted_category = categories[category_idx]
        confidence = similarity[category_idx].item() * 100
        
        # Display result
        st.image(image, caption="Uploaded Image", width=200)
        st.write(f"Predicted Category: **{predicted_category}** with {confidence:.2f}% confidence.")
