
# Multi-Modal E-commerce Product Classifier Using CLIP

A powerful multi-modal AI system that classifies e-commerce products into categories using [CLIP](https://openai.com/research/clip), combining image and text understanding.

## 🚀 Features

- 🔍 Automatically classifies products into e-commerce categories
- 🧠 Uses OpenAI's CLIP model for multi-modal learning
- 📦 Supports product images and textual descriptions
- ⚡ Built with Python, Torch, and Sentence Transformers
- ✅ Easily extensible to new category sets

## 📂 Use Cases

- E-commerce platforms for auto-tagging and organizing products
- Marketplace search optimization
- Catalog clean-up and product classification

## 🛠️ Tech Stack

- Python 3
- OpenAI CLIP (via `open-clip-torch`)

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- **Python 3.x** (preferably Python 3.7 or higher)
- **pip** (Python package manager)

## Project Setup

Follow these steps to set up and run the project.

### Step 1: Clone the Repository

Clone this repository to your local machine using Git.

```bash
git clone https://github.com/Sam-Begin-tech/multi-modal-Ecom-product-classifier-CLIP.git
```

Navigate to the project directory:

```bash
cd multi-modal-Ecom-product-classifier-CLIP
```

### Step 2: Set Up a Virtual Environment (Recommended)

It is recommended to use a virtual environment to manage dependencies.

#### Create the Virtual Environment

```bash
python -m venv myenv
```

#### Activate the Virtual Environment

- For **Linux/macOS**:

  ```bash
  source myenv/bin/activate
  ```

- For **Windows**:

  ```bash
  myenv\Scripts\activate
  ```

### Step 3: Install Dependencies

After activating the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

This will install all the necessary Python libraries including `torch`, `transformers`, `clip`, etc.

### Step 4: Run the Classifier

Now that the environment is set up, you can run the product classifier.

```bash
streamlit run  ecommerce_classifier.py
```

This script will load the CLIP model and classify the input e-commerce images and product descriptions.

### Step 5: Testing the Classifier with a New Product

The model will classify the image and description and return the predicted category.

## Directory Structure

The directory structure of the project is as follows:

```
multi-modal-Ecom-product-classifier-CLIP/
│
├── ecommerce_classifier.py   # Main Python script for classification
├── requirements.txt          # List of dependencies
├── .gitignore                # Git ignore file
├── images/                   # Folder for sample images
├── README.md                 # This file
└── other_files/              # Any other necessary files
```

## Important Files

- **ecommerce_classifier.py**: This is the main script that loads the CLIP model and performs classification on images and text.
- **requirements.txt**: This file contains a list of all Python packages that are required to run the project.

## Troubleshooting

If you face issues, try the following steps:

- Ensure that your Python version is at least 3.7.
- If you get an error about missing dependencies, try running the following command to fix it:

  ```bash
  pip install -r requirements.txt
  ```

- If you face errors related to CLIP or PyTorch, ensure you have the correct versions installed for your system's architecture (CPU or GPU).

## License

This project is licensed under the MIT License.

---
