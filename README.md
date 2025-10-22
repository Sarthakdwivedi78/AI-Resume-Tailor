
# AI Resume Tailor



### A web app that uses an AI language model to rewrite and tailor your resume for a specific job description.Built with Gradio and Hugging Face Transformers.






https://github.com/user-attachments/assets/731b8392-c0dc-469f-84a7-586b11e3d5ee








✨ Features

Smart Tailoring: Uses a Large Language Model (LLM) to analyze job descriptions and rewrite your resume.

Keyword Optimization: Automatically infuses your experience with keywords and phrases from the job posting.

Professional Summary: Generates a brand-new summary tailored for the specific role.

Simple Interface: A clean, two-panel UI built with Gradio.

Markdown Format: Outputs a clean Markdown file, easy to copy and paste into any template.

🚀 How to Use (Recommended)

This app is designed to be run for free on a Hugging Face Space.

Visit the App: Go to the live Hugging Face Space URL (click the badge at the top!).

Step 1: Paste your complete base resume into the "Paste Your Base Resume" textbox.

Step 2: Paste the entire job description you are applying for into the "Paste the Job Description" textbox.

Step 3: Click the "Generate Tailored Resume" button and wait for the AI to generate your new resume.

🖥️ Local Setup (For Developers)

You can run this app on your local machine, but it requires a powerful computer (preferably with an NVIDIA GPU) and a complex setup.

1. Prerequisites

```Python 3.10+```

Git

2. Clone the Repository

git clone ```[https://github.com/sarthakdwivedi78/AI-Resume-Tailor.git](https://github.com/sarthakdwivedi78/AI-Resume-Tailor.git)
cd AI-Resume-Tailor```


3. Install Dependencies

Install all the required Python libraries:

```pip install -r requirements.txt```


4. Set Up Gated Model Access

This project uses google/gemma-2b-it, which is a "gated" model. You must have a Hugging Face account and permission to access it.

Get Permission: Go to ``` https://huggingface.co/google/gemma-2b-it, log in, and agree to the terms to get access. ```

Get Token: Go to your Hugging Face Settings > Access Tokens > New token. Create a token with the ```read``` role.

Set Environment Variable: You must set this token as an environment variable before running the app.

Windows (PowerShell):

``` $env:HF_TOKEN = "hf_YOUR_TOKEN_HERE"```


macOS/Linux:

export ``` HF_TOKEN="hf_YOUR_TOKEN_HERE" ```


5. Run the App

Once your token is set, you can run the app:
```bash
python resume_generator_app.py
```


Note: Running this on a CPU (without an ``` NVIDIA GPU ```) will be extremely slow. Generation can take several minutes. This is why running on a Hugging Face Space is the recommended method.

📄 License

This project is licensed under the MIT License.
