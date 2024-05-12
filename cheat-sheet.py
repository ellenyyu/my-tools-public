import streamlit as st
import re

st.set_page_config(layout='wide')

CON_HEIGHT = 150

my_list = []

def apply_to_use_case(value):
    label = ' '.join(re.findall(r'\b[A-Z]{4,}\b', value))
    agree = st.checkbox("Applicable to use case?", key = label)
    if agree: 
        return label

col1, col2, col3 = st.columns(3)

with col1: 
    zsp = st.text_area(label ='Zero-shot Prompting', 
                value = 'Large language models (LLMs) today, such as gpt-3.5 Turbo, gpt-4, and Claude 3, are tuned to follow instructions and are trained on large amounts of data.\
                So, give it instructions and zero examples is ZERO SHOT PROMPTING ', 
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(zsp))


    fsp = st.text_area(label ='Few-shot Prompting', 
                value = 'When zero-shot prompting falls short on more complex tasks, try FEW SHOT PROMPTING, which is inserting 1-10 input-output pairs in the prompt.\
                When few-shot prompting is not sufficient, consider more advanced prompting techniques like CoT.', 
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(fsp))


    cot = st.text_area(label ='Chain-of-Thought Prompting (CoT)', 
                value = 'COT PROMPTING enables complex reasonging capabilties through Intermediate reasing steps. CoT prompting can be few-shot or zero-shot. \
                Zero-shot is accomplished by the instruction \'Let\'s think step by step\' or \'Let\'s work this out in a step by step way to be sure we have the right answer\'', 
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(cot))

    
    acot = st.text_area(label ='Auto-CoT Prompting', 
                value = 'AUTO-COT PROMPTING is the idea of first clustering questions and developing heuristics for the clusters such as the length of questions (ex 60 tokens) \
                and the number of steps in rationale. Less straightforward to implement- see if Zhang et al (2022) paper addresses implementation.', 
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(acot))


    scot = st.text_area(label ='Self-Consistency Prompting', 
                value = 'SELF-CONSISTENCY PROMPTING is the idea of introducing diverse reasoning paths in few-shot COT and use that which is the most consistent response as the answer.\
                Effective for arithmetic problems. Less straightforward to implement- check out Wang et al (2022) paper for implementation advice.', 
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(scot))


    gkp = st.text_area(label ='Generate Knowledge Prompting', 
                value = 'GENERATE KNOWLEDGE PROMPTING is the idea of using few shot examples to generate knowledge for the model to use before asking it to \'explain and answer\'\
                This seems to require two llm calls as well as there are more details to consider so, check out paper by Liu et al (2022)', 
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(gkp))

with col2: 
    pc = st.text_area(label ='Prompt Chaining', 
                value = 'PROMPT CHAINING is accomplished by breaking tasks into subtasks and chaining the response of one llm call into the next llm call. Prompt chaining is a great \
                    alternative to a very detailed prompt, and increases controlability and transparency of your llm application.',
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(pc))

    tot = st.text_area(label ='Tree of Thought (ToT)', 
                value = 'TREE OF THOUGHT PROMPTING is for tasks that require exploration and strategic lookahead. ToT maintains a tree of thought, where thoughts represent coherent \
                language sequences that serve as intermediate steps toward solving a problem. The idea in prompt form is: ',
                height = CON_HEIGHT)
    st.code(body = """Imagine three different experts are answering this question.
    All experts will write down 1 step of their thinking,
    then share it with the group.
    Then all experts will go on to the next step, etc.
    If any expert realises they're wrong at any point then they leave.
    The question is...""")
    
    my_list.append(apply_to_use_case(tot))

    rag = st.text_area(label ='Retrieval Augmented Generation (RAG)', 
                value = 'RETRIEVAL AUGMENTED GENERATION is the idea of from input to retrieval of documents and concatenating the documents as context with the prompt and fed to the generator.\
                RAG can be very nuanced e.g. Lweis et al (2021). An interesting idea is, if your database is ever evolving, RAG allows for your system to evolve.',
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(rag))

    art = st.text_area(label ='Automatic Reasoning and Tool-use (ART)', 
                value = 'AUTOMATIC REASONING and TOOL-USE is the idea of generalizing from demonstrations to decompose a new task and use tools in appropriate places, in a zero-shot fashion.\
                To be honest, I\'m not sure how it does it. See Paranjape et al (2023) for the information',
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(art))

    ape = st.text_area(label ='Automatic Prompt Engineer (APE)', 
                value = 'AUTOMATIC PROMPT ENGINEER is idea of generating prompts which are evaluated to surface an optimized prompt. In more details, the first step involves a large language model\
                     that is given output demonstrations to generate instruction canddates for a task. The instructions are executed using a target model and the most appropriate instruction is\
                    selected based on computed evaluation scores.',
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(ape))

with col3: 
    ap = st.text_area(label ='Active-Prompt', 
                value = 'ACTIVE-PROMPT adapts LLMs to different task-specfic example prompts. The first step is query the LLM with or without a few CoT exampls. k possible answers are generated for a set of training questions. \
                     An uncertainty metric is calculated based on the k answers (disagreement used). The most uncertain quetions are selected for annotation by humans. See Diao et al (2023).',
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(ap))

    dsp = st.text_area(label ='Directional Stimulus Prompting', 
                value = 'DIRECTIONAL STIMULUS PROMPTING is the use of RL to optimzied LLM- specifically, a tunable policy LM is trained to generate the stimulus/hint. The stimulus/hint is fed to the LLM. See Li et al. (2023) for more information',
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(dsp))

    pal = st.text_area(label ='Program-Aided Language Models (PAL)', 
                value = 'PROGRAM-AIDED LANGUAGE MODELS is the idea of offloading the intermediary reasoning steps to a Python interpreter. As far as I can tell, this is good only for arithmetic prompts. See Gao et al (2022) for more information',
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(pal))

    rp = st.text_area(label ='ReAct Prompting', 
                value = 'REACT PROMPTING is question-thought-act-answer-thought-act-answer etc. framework. ReACT is operationalized in Langchain.',
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(rp))

    r = st.text_area(label ='Reflexion', 
                value = 'REFLEXION, based on my current understanding, is a multi agent apporach where there is a responder that generates initial response, a reviser that revises the response, and cycles through that N times to arrive at the final generated response',
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(r))

    r = st.text_area(label ='Multimodel CoT Prompting', 
                value = 'MULTIMODEL COT PROMPTING is the framework of rationale generation based on multimodal information followed by answer inference, which leverages the informative generated rationales. For example, given an images of cracker and fries, the framework\
                cracker is salty, fries is salty, cracker is not soft, fries are soft and so, the property that the two objects have in common is salty.',
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(r))

    g = st.text_area(label ='Graph Prompting', 
                value = 'GRAPH PROMPTING tbd - see Liu et al (2023)',
                height = CON_HEIGHT)
    
    my_list.append(apply_to_use_case(g))

st.markdown("#")
st.markdown("#")

st.text(f'Apply these to use case: {[x for x in my_list if x]}')

my_string = ', '.join(['https://www.promptingguide.ai/techniques/prompt_chaining', 
                       'https://en.wikipedia.org/wiki/Prompt_engineering#Text-to-text'])
st.text(f'Sources: {my_string}')


my_questions = ', '.join(['Go through the papers to see what foundation models are these methodologies tested on? Are all foundational models created equal? We might have to use the foundational model the paper used'])
st.text(f'Sources: {my_questions}')