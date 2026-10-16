# AI FUNDAMENTALS
## Tokenization, Embeddings & Transformer Architecture
*A visual, beginner-friendly guide to how modern AI systems work*

`TEXT` | `TOKENS` | `VECTORS` | `ATTENTION` | `OUTPUT`

### THE ONE-LINE IDEA
AI turns information into numerical representations, uses Transformer layers to support relationships, and then generates or retrieves useful information.

---

## Learning Roadmap
*Beginner → Practical → Technical*  
Follow the guide in this order. Each section answers one practical question.

1. **Tokenization** — How text becomes manageable pieces[cite: 2].
2. **Embeddings** — How tokens become numerical representations[cite: 2].
3. **Attention** — How the model connects information[cite: 2].
4. **Transformers** — How the major components work together[cite: 2].
5. **Popular AI Models** — How major model families fit in[cite: 2].
6. **RAG & Vector Search** — How embeddings power document search[cite: 2].
7. **Cheat Sheet** — The concepts to remember[cite: 2].

---

## 01. Tokenization
**Question:** How does an AI model turn human text into something it can process[cite: 2]?

### Simple Explanation
A tokenizer breaks text into smaller pieces called tokens. A token can be a word, part of a word, punctuation, or another learned piece[cite: 2].

> `"I love Python"`  
> `→ I | love | Python`  
> `→ TOKEN IDs`

The exact split depends on the model. Different models can tokenize the same sentence differently[cite: 2].

### Why Tokenization Matters
* The model processes tokens, not raw human text[cite: 2].
* Token count affects context limits and, in many services, cost[cite: 2].
* Subword-style tokenization helps represent uncommon or new words[cite: 2].

> **REMEMBER:** Tokenization = breaking text into pieces[cite: 2].

---

## 02. Embeddings
**Question:** How does the model represent a token numerically[cite: 2]?

### Simple Explanation
An embedding is a vector: a list of learned numbers representing information in a form the neural network can process[cite: 2].

> `TOKEN` → `EMBEDDING` → `VECTOR` → `TRANSFORMER`  
> `"Python"` → `[0.21, -0.43, 0.87, 0.12, …]`

The individual numbers are not simple labels. The complete vector is useful to the neural network[cite: 2].

### Important Distinction
Token embeddings inside an LLM are part of internal processing. A separate text-embedding model is designed for search, similarity, clustering, and RAG[cite: 2].

---

## 03. Attention
**Question:** How does the model decide which other words matter[cite: 2]?

### Simple Explanation
Attention lets a token use information from other tokens in the context. This helps the model understand relationships and meaning[cite: 2].

> `"The dog chased the ball because it was moving."`  
> `dog ↔ it     •     ball ↔ moving`

Attention is a learned mechanism for combining contextual information[cite: 2].

> **REMEMBER:** Attention = deciding which information is relevant to which other information[cite: 2].

---

## 04. Transformer Architecture
**Question:** How do tokenization, embeddings and attention become a modern AI model[cite: 2]?

`INPUT` | `TOKENS` | `EMBEDDINGS` | `ATTENTION` | `LAYERS` | `OUTPUT`

| Technique | Simple Meaning |
| :--- | :--- |
| **Decoder-only** | Generates text one token at a time; common in modern generative models[cite: 2]. |
| **Encoder-only** | Focuses on understanding and representation tasks[cite: 2]. |
| **Encoder–decoder** | Reads an input and generates an output; common in sequence-to-sequence tasks[cite: 2]. |
| **Multi-head attention** | Several attention patterns are learned in parallel[cite: 2]. |
| **Causal attention** | Prevents future tokens from being used when predicting the next token[cite: 2]. |
| **Positional methods** | Provide information about token order[cite: 2]. |
| **KV cache** | Reuses previous attention information to make generation faster[cite: 2]. |

---

## 05. Popular AI Models & Their Approach
*High-level comparison. Exact architecture and tokenizer details can vary by model version, and commercial systems may keep internal details private[cite: 2].*

| Model | Company | Architecture / Technique | Typical Use |
| :--- | :--- | :--- | :--- |
| **GPT** | OpenAI | Transformer-based generative models; modern versions may support multimodal inputs[cite: 2]. | Chat, coding, reasoning[cite: 2] |
| **Gemini** | Google | Transformer-based multimodal model family; details vary by version[cite: 2]. | Text, image, audio/video, coding[cite: 2] |
| **Claude** | Anthropic | Transformer-based language models; many internals are proprietary[cite: 2]. | Writing, analysis, coding, long context[cite: 2] |
| **Mistral** | Mistral AI | Transformer-based; some families use Mixture-of-Experts (MoE)[cite: 2]. | Chat, coding, efficient AI[cite: 2] |
| **Llama** | Meta | Decoder-style Transformer language model family[cite: 2]. | Open/custom AI applications[cite: 2] |
| **Gemma** | Google | Lightweight Transformer-based open model family[cite: 2]. | Local/custom applications[cite: 2] |
| **DeepSeek** | DeepSeek | Transformer-based; some models use MoE and specialized efficiency/reasoning methods[cite: 2]. | Reasoning and coding[cite: 2] |
| **Grok** | xAI | Transformer-based generative model family; exact internals vary[cite: 2]. | Chat, reasoning, coding[cite: 2] |

> **PROFESSIONAL NOTE:** Do not assume that major AI models use the same tokenizer, vocabulary, embedding size, positional method, or attention implementation. These are model-specific[cite: 2].

---

## 06. Embeddings + Vector Search + RAG
**Question:** How can an AI answer questions using your own documents[cite: 2]?

`DOCUMENTS` → `CHUNKS` → `EMBEDDINGS` → `VECTOR DB`  
`QUESTION` → `EMBEDDING` → `SIMILARITY SEARCH` → `RELEVANT CHUNKS` → `LLM`

**Example:** A document says *"Employees receive 20 days of annual leave."* A user asks *"How many vacation days do I get[cite: 2]?"*  
The wording is different, but the meanings can be close in embedding space, so the relevant document chunk can be retrieved[cite: 2].

> **REMEMBER:** RAG = retrieve relevant information first, then ask the LLM to generate an answer using that information[cite: 2].

---

## 07. The Four Concepts You Should Remember

1. **TOKENIZATION:** Break text into pieces[cite: 2].
2. **EMBEDDINGS:** Represent information as vectors[cite: 2].
3. **ATTENTION:** Connect relevant information[cite: 2].
4. **TRANSFORMER:** The neural-network architecture that processes these representations[cite: 2].

`WORDS` | `TOKENS` | `VECTORS` | `ATTENTION` | `CONTEXT` | `ANSWER`

### Final Takeaway
If you understand **tokenization → embeddings → attention → Transformer layers**, you have the core mental model needed to understand modern language AI. RAG, vector databases, multimodal systems, and agents add capabilities around these foundations[cite: 2].

---

## Glossary

| Term | Meaning |
| :--- | :--- |
| **Token** | A piece of text processed by a model[cite: 2]. |
| **Vector** | A list of numbers representing information[cite: 2]. |
| **Embedding** | A learned vector representation[cite: 2]. |
| **Attention** | A mechanism for combining information across tokens[cite: 2]. |
| **Transformer** | A neural-network architecture built around attention and related components[cite: 2]. |
| **LLM** | Large Language Model[cite: 2]. |
| **RAG** | Retrieval-Augmented Generation[cite: 2]. |
| **MoE** | Mixture-of-Experts, where inputs can be routed through different expert subnetworks[cite: 2]. |
| **Context window** | The amount of context a model can work with for a request[cite: 2]. |