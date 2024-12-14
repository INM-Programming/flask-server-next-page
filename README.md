Install Packages

    pip install -r requirements.txt

Services

    Lottery : POST http://127.0.0.1:5000/lottery
              Body JSON {"participants":["1","2","3","4"]}
              Response {"winner":index}

    Gemini : POST http://127.0.0.1:5000/gemini
             Body JSON {"message":"How are you?"}
             Response {"response":response}

.env

    GEMINI_API_KEY = ***********************