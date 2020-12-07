
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Hello world from sAIdalia app!')

data = pd.read_csv('data/char_1.csv')
data.drop_duplicates(inplace = True) 
st.write(data[:5]) # can also st.dataframe(df)
# st.table(data[:1])


st.write('## Distribution for each word len')
from collections import Counter

counter_list, words_len = [], []
for word in data['en_name']:
    words_len.append(len(word))

counter_list = Counter(words_len)

df_counter_list = pd.DataFrame(counter_list.values(), counter_list.keys())

st.bar_chart(df_counter_list)

st.write('-----------')

st.write('### If i search by captureing the box drug, then giving me information about it\n')

image = Image.open('3_En.JPG')
st.image(image, caption='Captured image', use_column_width=True)
df_of_Azathioprine = data[data['en_name'] == 'Azathioprine']
st.table(df_of_Azathioprine.T)
st.write('-----------')

st.write('### If i search for drug by voice, then giving me information about it\n')

audio_file = open('Asprien.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')


df_of_Aspirin = data[data['en_name'] == 'Aspirin']
st.table(df_of_Aspirin.T)
st.write('-----------')
st.write('### If already i have the drug name and want to listen to information about it instate of reading it like:\n')

st.write('الإسبرين بالعربيه عند البحث عنه')
st.write('".اسم الدواء الأسبرين"')
# in Arabic
audio_file = open('Aspirin_Ar.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')


st.write('or like Aspirin in English when searching')
st.write('"The durg neme is Aspirin."')

# in English
audio_file = open('Aspirin.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')



