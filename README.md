# Medical ChatBot API 
* This repo contains the code required to deploy the medical chat bot which I have created using custom datasets collected and wrangled from multiple sources
* The dataset is available on hugging face here -> [link](Mohammed-Altaf/medical-instruction-100k)
* There are basically three different variants of the orginal model
* * First one is a quantized 8bit model which this script usese
  * Second is adapters created using the above dataset on GPT-NEOX 20B MODEL,
  * Third are also adapters much finer one, trained on GCP TPU's, which I got for free 😅, for few days.

  ## To Use this repo
  `git clone https://github.com/Mohammed-Altaf-01/medical-chatbot-api.git
  `
  * create a virtual environment
    `python -m venv venv 
    `
    * install dependencies - **after activating the environment**
      `pip install -r requirements.txt
      `
      * Then run the main file
        `uvicorn main:app --reload
        `
 **But make sure to run this locally only if you have high Ram or some GPU, else your workstation might Crash... or behave inappropriately**
👆🏼This happent to me

* You will get the api running on the local host and below code hits the api endpoint to get the response from the LLM.
`localhost:8000/query/I want to improve my memory can you suggest me anything?
          `
