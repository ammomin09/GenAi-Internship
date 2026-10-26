import chromadb

client=chromadb.Client()

coll=client.create_collection(name="docs")
documents=[
        "This is docs about amcost",
        "**AMCOST Anand** (Anand Mercantile College of Science, Management & Computer Technology) is an educational institution in Anand, Gujarat, established in 1999. The college offers undergraduate programs such as **BCA, BBA, and B.Com** and focuses on academic knowledge, practical skills, and career development.AMCOST is affiliated with **Sardar Patel University, Vallabh Vidyanagar**. Its basic information can be used as a knowledge base in a **RAG system**, allowing an AI chatbot to retrieve information about courses, admissions, facilities, and other college-related details and provide relevant answers to students."
    ]

coll.add(
    ids=["1","2"],
    documents=documents
)

final=coll.query(
    query_texts=["What is college name and its policy"],
    n_results=2
)
print(final)