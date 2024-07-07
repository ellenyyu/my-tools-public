'''
I want all the blogs I want to follow 
on one page 
'''

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide')

HEIGHT=350

col1, col2, col3, col4, col5= st.columns(5)

blog_list = ['https://arxiv.org/',
           'https://blog.langchain.dev/graph-based-metadata-filtering-for-improving-vector-search-in-rag-applications/', 
           'https://aman.ai/',
           'https://www.andrewng.org/about/', 
           'https://karpathy.ai/', 
           'https://ai.meta.com/blog/?page=1',
           'https://openai.com/news/research/',
           'https://www.midjourney.com/showcase',
           'https://blogs.microsoft.com/ai/page/2/',
           'https://research.google/blog/',
           'https://blogs.nvidia.com/',
           'https://www.tesla.com/AI',
           'https://aws.amazon.com/blogs/aws/category/artificial-intelligence/',
           'https://www.youtube.com/@ByteByteGo', 
           'https://www.youtube.com/@Fireship', 
           'https://www.youtube.com/@AI-Makerspace',
           'https://www.youtube.com/@codebasics',
           'https://streamlit.io/gallery?category=nlp-language',
           'https://www.llamaindex.ai/blog',
           'https://talkpython.fm/episodes/show/436/an-unbiased-evaluation-of-environment-and-packaging-tools', 
           'https://www.latent.space/podcast',
            ]

def create_iframe(list_index):
    components.iframe(blog_list[list_index], height=HEIGHT)
    st.markdown(f"""<p align="center">
                <a href={blog_list[list_index]}>link</a>
                </p>""",
                unsafe_allow_html=True)
    st.markdown("#")

with col1:
    for idx in range(0, len(blog_list), 5):
        create_iframe(idx)

with col2:
    for idx in range(1, len(blog_list), 5):
        create_iframe(idx)

with col3:
    for idx in range(2, len(blog_list), 5):
        create_iframe(idx)

with col4:
    for idx in range(3, len(blog_list), 5):
        create_iframe(idx)

with col5:
    for idx in range(4, len(blog_list), 5):
        create_iframe(idx)

