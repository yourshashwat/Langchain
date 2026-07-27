# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from dotenv import load_dotenv
# load_dotenv()

# embeddings= GoogleGenerativeAIEmbeddings(
#     model="models/text-embedding-004",
#     dimension=64
# )

# result= embeddings.embed_query("Bihar se bani ho")

# print(str(result))


from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
vector = embeddings.embed_query("hello, world!")
print(vector)