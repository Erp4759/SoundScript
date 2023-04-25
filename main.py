import streamlit as st
import openai


# Обращение к GPT
def generate_lyrics(mess):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', 'content': mess}
        ],
        temperature=0
    )
    return response['choices'][0]['message']['content']


# title
st.title("SoundScript")
openai.api_key = st.text_input("Enter your open OpenAI API:")
# inputs
prompt = st.text_input("What will the song be about?")
mood = st.selectbox("Select the mood of the song", ["Happy", "Sad", "Romantic", "Energetic"])
character = st.text_input("Enter additional details of the song")

# generating request
res = f"Write the song about {prompt}, with {mood} mood."
if len(character) > 2:
    res += f"Details of the song: {character}"

# button click event
if st.button("Generate Lyrics"):
    song = generate_lyrics(res)
    st.write("Text:")
    st.write(prompt)
    st.text(song)
    st.write("Chords:")
    chords = generate_lyrics("Generate guitar chords for this text: \n" + prompt)
    st.text(chords)
    print(song)
    print(chords)
