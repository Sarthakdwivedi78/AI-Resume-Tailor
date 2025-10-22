import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

# --- Model Setup ---
# We are using the "smart" model that is powerful enough for this task.
# This model WILL NOT work on your local laptop (it causes a crash).
# This code is intended for deployment on Hugging Face Spaces.
model_id = "microsoft/Phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

print(f"Loading model: {model_id} (this will run on the remote server)...")

try:
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype="auto", # Let the server handle the data type
        device_map="auto",  # Let the server auto-assign to its CPU/GPU
        trust_remote_code=True
    )
    
    print("Model loaded successfully on remote server.")

    # Create a "pipeline" for text generation
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )
    # We must set this special token for Phi-3 to stop generating text correctly
    pipe.tokenizer.pad_token_id = pipe.model.config.eos_token_id
    
    print("Pipeline created successfully.")

except Exception as e:
    print(f"Failed to load the model: {e}")
    raise e

# --- Core Logic Function ---
def generate_tailored_resume(base_resume, job_description):
    """
    This function takes the user's inputs, builds the prompt,
    and asks the model to generate the new resume.
    """
    if not base_resume or not job_description:
        return "Please fill out both your Base Resume and the Job Description."

    # This is the correct chat-style prompt for the Phi-3 model
    prompt = f"""
<|system|>
You are an expert, AI-powered resume writer. Your task is to rewrite a user's base resume to perfectly tailor it for a new job description.
You must:
1.  Write a new "Professional Summary" that mirrors the job description.
2.  Rewrite work experience bullet points to include keywords from the job description.
3.  Emphasize achievements that match what the job is looking for.
4.  Do NOT invent any new facts, jobs, or skills.
5.  Format the output as a clean, professional resume in Markdown.
<|end|>
<|user|>
HERE IS MY BASE RESUME:
---
{base_resume}
---

HERE IS THE TARGET JOB DESCRIPTION:
---
{job_description}
---

Please generate the new, tailored resume in Markdown format now.
<|end|>
<|assistant|>
"""

    print("--- GENERATING RESUME (using Phi-3-mini) ---")
    
    # Settings for the model's response
    generation_args = {
        "max_new_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.9,
        "do_sample": True,
    }

    try:
        # Ask the model to generate a response
        output = pipe(prompt, **generation_args)
        
        # We only want the text *after* the final <|assistant|> tag
        generated_text = output[0]['generated_text'].split("<|assistant|>")[-1].strip()
        
        print("--- GENERATION COMPLETE ---")
        return generated_text

    except Exception as e:
        print(f"Error during generation: {e}")
        return f"An error occurred: {e}."

# --- UI Setup (Gradio) ---
with gr.Blocks(theme=gr.themes.Default(primary_color="#0066cc")) as demo:
    gr.Markdown(
        """
        # 🤖 AI Resume Tailor
        Stop applying with the same resume! Paste your **Base Resume** and the **Job Description**, 
        and the AI will generate a new resume perfectly tailored for the role.
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            base_resume_input = gr.Textbox(
                lines=20,
                label="Step 1: Paste Your Base Resume",
                placeholder="Paste your entire current resume here..."
            )
            job_description_input = gr.Textbox(
                lines=20,
                label="Step 2: Paste the Job Description",
                placeholder="Paste the target job description here..."
            )
        with gr.Column(scale=1):
            generate_button = gr.Button("✨ Generate Tailored Resume", variant="primary")
            resume_output = gr.Markdown(
                label="Step 3: Your New AI-Tailored Resume"
            )

    # Connect the button to the function
    generate_button.click(
        fn=generate_tailored_resume,
        inputs=[base_resume_input, job_description_input],
        outputs=[resume_output]
    )
    
    gr.Examples(
        [
            [
                """
                **John Doe**
                Software Engineer | john.doe@email.com | (123) 456-7890

                **Summary**
                Versatile software engineer with 3 years of experience in full-stack development. Proficient in Python and JavaScript. Looking for a new role.

                **Experience**
                *Software Engineer*, TechCorp (2022-Present)
                - Wrote code for web applications.
                - Fixed bugs reported by QA.
                - Attended daily stand-up meetings.

                **Skills**
                - Python, JavaScript, React, Node.js, SQL
                """, 
                """
                **Senior Python Backend Engineer**
                We are seeking a Senior Python Backend Engineer with 3+ years of experience to build and scale our high-performance data pipelines. The ideal candidate will have deep expertise in Python, cloud platforms (AWS), and database management (PostgreSQL). You will be responsible for designing REST APIs, optimizing database queries, and mentoring junior developers.
                """
            ]
        ],
        inputs=[base_resume_input, job_description_input]
    )

# --- Run the App ---
if __name__ == "__main__":
    # This will create a local web server
    demo.launch()

