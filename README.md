# Llama3 Email Writer: (About the project)
This is a small project that write email based on user's description using LLama3 Instruct (Opensource model).

# More info about LLama3 Access
To access LLama3 access it is requried to get Huggingface access token since the model "meta-llama/Meta-Llama-3-8B-Instruct" is made gated for access. 
For this anyone one get the access to this model by filling the form at "meta-llama/Meta-Llama-3-8B-Instruct" and upon receiving the approval from the author in your mail associated to hugging face, one can use it using hugging face acess token.

Note: In the "access_token = hf_access_token" code in "llama3_mail_writer.py" please make sure to keep your actual hugging face access token value. 

# Running the Project:
## 1. Dependency installation:
Please install the requirements listed in requirements.txt using 

```pip install -r requirements.txt```

## 2. Running the email writer (Llama3)
For this just run the llama3_mail_writer.py using

```python llama3_mail_writer.py```
