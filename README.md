# :+1: Table Question Answering using TAPAS

[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dineshpiyasamara/table_question_answering_tapas/blob/master/tapas_qa.ipynb)

The TAPAS model was proposed in TAPAS: Weakly Supervised Table Parsing via Pre-training by Jonathan Herzig, Paweł Krzysztof Nowak, Thomas Müller, Francesco Piccinno and Julian Martin Eisenschlos. 
It’s a BERT-based model specifically designed (and pre-trained) for answering questions about tabular data. 

Compared to BERT, TAPAS uses relative position embeddings and has 7 token types that encode tabular structure. TAPAS is pre-trained on the masked language modeling (MLM) objective on a large dataset comprising millions of tables from English Wikipedia and corresponding texts.

### TAPAS has been fine-tuned on several datasets:
- SQA (Sequential Question Answering by Microsoft)
- WTQ (Wiki Table Questions by Stanford University)
- WikiSQL (by Salesforce).

[Read more about `TAPAS` model from `HuggingFace`](https://huggingface.co/docs/transformers/model_doc/tapas)

### Sample image from Demo

<p align="center">
  <img src="https://github.com/dineshpiyasamara/table_question_answering_tapas/blob/master/sample.png" alt="Sample from demo">
</p>