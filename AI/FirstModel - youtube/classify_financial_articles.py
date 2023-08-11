from gravityai import gravityai as grav
import pickle
import pandas as pd


model = pickle.load(open(''))

tfidf_vectorized = pickle.load(open(""))
# To skrót od Term Frequency-Inverse Document Frequency (częstotliwość
# występowania słowa - odwrotna częstotliwość w dokumencie). Jest to
# technika używana w przetwarzaniu języka naturalnego, czyli w
# analizowaniu tekstu.
label_encoder = pickle.load(open(""))


def process(inPath, outPath):
    input_Df = pd.read_csv(inPath)
    
    #vectorize the data
    features = tfidf_vectorized.transform(input_Df['body'])
    
    # predict the classes
    predictions = model.predict(features)
    
    #convert output lables to categories
    input_Df['category'] = label_encoder.inverse_transform(predictions)
    
    #save the results to CV
    output_df = input_Df[['id', 'category']]
    output_df.to_csv(outPath, index=False)
    
    
grav.wait_for_requests(process)    
    