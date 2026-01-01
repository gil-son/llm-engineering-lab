from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
load_dotenv()

long_text = """
Dawn threads a pale gold through the alley of glass.
The city yawns in a chorus of brakes and distant sirens.
Windows blink awake, one by one, like sleepy eyes.
Streetcloth of steam curls from manholes, a quiet river.
Coffee steam spirals above a newspaper's pale print.
Pedestrians sketch light on sidewalks, hurried, loud with umbrellas.
Buses swallow the morning with their loud yawns.
A sparrow perches on a steel beam, surveying the grid.
The subway sighs somewhere underground, a heartbeat rising.
Neon still glows in the corners where night refused to retire.
A cyclist cuts through the chorus, bright with chrome and momentum.
The city clears its throat, the air turning a little less electric.
Shoes hiss on concrete, a thousand small verbs of arriving.
Dawn keeps its promises in the quiet rhythm of a waking metropolis.
The morning light cascades through towering windows of steel and glass,
casting geometric shadows on busy streets below.
Traffic flows like rivers of metal and light,
while pedestrians weave through crosswalks with purpose.
Coffee shops exhale warmth and the aroma of fresh bread,
as commuters clutch their cups like talismans against the cold.
Street vendors call out in a symphony of languages,
their voices mixing with the distant hum of construction.
Pigeons dance between the feet of hurried workers,
finding crumbs of breakfast pastries on concrete sidewalks.
The city breathes in rhythm with a million heartbeats,
each person carrying dreams and deadlines in equal measure.
Skyscrapers reach toward clouds that drift like cotton,
while far below, subway trains rumble through tunnels.
This urban orchestra plays from dawn until dusk,
a endless song of ambition, struggle, and hope.
"""

# Split long text into smaller parts
# Optimal chunk size and overlap for summarization
splitter = RecursiveCharacterTextSplitter(
    chunk_size=250, chunk_overlap=50, 
)

# Create documents from the long text
parts = splitter.create_documents([long_text])

# Print the parts (optional - for verification)
print("\nDOCUMENTS PARTS WITH CHUNK(250) AND OVERLAP(50):\n")
for i, part in enumerate(parts[:10], start=1):
    print(f"DOCUMENT PART {i}:\n{part.page_content}\n{'-'*30}")

print(f"\nNow, starting 'pipeline' to summarize {len(parts)} parts...\n")

# Initialize the language model
llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0)

# LCEL map stage: summarize each chunk
map_prompt = ChatPromptTemplate.from_template("Write a concise summary of the following text:\n{context}")
map_chain = map_prompt | llm | StrOutputParser()

# Prepare inputs for map stage | Internal function to prepare inputs | Each document part is converted to a dict with "context" key
prepare_map_inputs = RunnableLambda(lambda docs: [{"context": d.page_content} for d in docs])

# Execute map stage it means: prepare inputs | map_chain over each part
map_stage = prepare_map_inputs | map_chain.map()

# LCEL reduce stage: combine summaries into one final summary
# Then create reduce chain | Prompt to combine summaries
reduce_prompt = ChatPromptTemplate.from_template("Combine the following summaries into a single concise summary:\n{context}")

reduce_chain = reduce_prompt | llm | StrOutputParser()

# Prepare inputs for reduce stage | Join all summaries into a single string separated by new lines
prepare_reduce_input = RunnableLambda(lambda summaries: {"context": "\n".join(summaries)})
pipeline = map_stage | prepare_reduce_input | reduce_chain

result = pipeline.invoke(parts) # parts is a list of Document objects. It will be processed in the map stage.

print("\n RESUMED ALL SUMMARIES:\n", result["output_text"])