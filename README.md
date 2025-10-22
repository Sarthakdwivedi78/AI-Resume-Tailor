<p align="center">
<h1>
🤖



AI Resume Tailor
</h1>
</p>

<p align="center">
A web app that uses an AI language model to rewrite and tailor your resume for a specific job description.





Built with Gradio and Hugging Face Transformers.
</p>

<p align="center">
<a href="https://www.google.com/search?q=https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME">
<img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue" alt="Hugging Face Spaces">
</a>
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Python-3.10%2B-yellow" alt="Python 3.10+">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Gradio-blueviolet" alt="Gradio">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Transformers-orange" alt="Transformers">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/License-MIT-green" alt="License: MIT">
</p>

✨ Features

Smart Tailoring: Uses a Large Language Model (LLM) to analyze job descriptions and rewrite your resume.

Keyword Optimization: Automatically infuses your experience with keywords and phrases from the job posting.

Professional Summary: Generates a brand-new summary tailored for the specific role.

Simple Interface: A clean, two-panel UI built with Gradio.

Markdown Format: Outputs a clean Markdown file, easy to copy and paste into any template.

🚀 How to Use (Recommended)

This app is designed to be run for free on a Hugging Face Space.

Visit the App: Go to the live Hugging Face Space URL (add your link to the badge above!).

Step 1: Paste your complete base resume into the "Paste Your Base Resume" textbox.

Step 2: Paste the entire job description you are applying for into the "Paste the Job Description" textbox.

Step 3: Click the "Generate Tailored Resume" button and wait for the AI to generate your new resume.

🖥️ Local Setup (For Developers)

You can run this app on your local machine, but it requires a powerful computer (preferably with an NVIDIA GPU) and a complex setup.

1. Prerequisites

Python 3.10+

Git

2. Clone the Repository

git clone [https://github.com/YOUR_USERNAME/AI-Resume-Tailor.git](https://github.com/YOUR_USERNAME/AI-Resume-Tailor.git)
cd AI-Resume-Tailor


3. Install Dependencies

Install all the required Python libraries:

pip install -r requirements.txt


4. Set Up Gated Model Access

This project uses google/gemma-2b-it, which is a "gated" model. You must have a Hugging Face account and permission to access it.

Get Permission: Go to https://huggingface.co/google/gemma-2b-it, log in, and agree to the terms to get access.

Get Token: Go to your Hugging Face Settings > Access Tokens > New token. Create a token with the "read" role.

Set Environment Variable: You must set this token as an environment variable before running the app.

Windows (PowerShell):

$env:HF_TOKEN = "hf_YOUR_TOKEN_HERE"


macOS/Linux:

export HF_TOKEN="hf_YOUR_TOKEN_HERE"


5. Run the App

Once your token is set, you can run the app:

python resume_generator_app.py


Note: Running this on a CPU (without an NVIDIA GPU) will be extremely slow. Generation can take several minutes. This is why running on a Hugging Face Space is the recommended method.

📄 License

This project is licensed under the MIT License.
