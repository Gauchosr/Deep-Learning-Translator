from models import TranslationModel
from transformers import T5Tokenizer, T5ForConditionalGeneration

#Inizializziamo i modelli
#si possono usare anche t5-base e t5-large, ma richiedono più tempo
tokenizer = T5Tokenizer.from_pretrained("t5-small", model_max_length=512)
translator = T5ForConditionalGeneration.from_pretrained("t5-small")


#store translation, salva la traduzione nel db per poterla accedere tramite id successivamente
def store_translation(t): 
    model = TranslationModel(text=t.text, base_lang=t.base_lang, final_leng=t.final_leng)
    model.save()
    return model.id 

#run translation
def run_translation(t_id: int): 
    #recupero la traduzione tramide id dal database
    model = TranslationModel.get_by_id(t_id)
    #formato della traduzione
    prefix = f"translate {model.base_lang} to {model.final_leng}: {model.text}"
    #tokenizziamola per darla all'algoritmo di traduzione
    input_ids = tokenizer(prefix, return_tensor="pt").input_ids
    #generiamo la traduzione, lunghezza massima 512
    outputs = translator.generate(input_ids, max_new_tokens=512)
    #decodifichiamo i token
    translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    #salviamo traduzione e modello 
    model.translation = translation
    model.save()
