from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, validator
import tasks

app = FastAPI()

languages = ["English", "French", "German", "Romanian"]

class Translation(BaseModel):
    text: str
    base_leng: str
    final_lang: str

    @validator('base_lang', 'final_lang')
    def valid_lang(cls, lang): 
        if lang not in languages: 
            raise ValueError("Invalid Language")
        return lang

#Route 1: 
@app.get("/")
def get_root(): 
    return {"message": "Ciao"}

#Route 2: non faremo la traduzione internamente alla web request per motivi di efficienza
#salviamo la traduzione ritornando un id
#eseguiamo la traduzione in background

@app.post("/translate")
def post_translation(t: Translation, background_task: BackgroundTasks):
    t_id = tasks.store_translation(t)
    background_task.add_task(tasks.run_translation, t_id)
    return {"task_id": t_id}