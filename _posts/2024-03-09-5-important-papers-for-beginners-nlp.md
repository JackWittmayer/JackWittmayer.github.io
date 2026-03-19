---
title: 5 Important Papers for a Beginner to Understand Today’s NLP
date: 2024-03-09
description: Natural language processing (NLP) is progressing extremely quickly nowadays and it can be difficult to know which research papers to start…
---

---

![](/images/2024-03-09-5-important-papers-for-beginners-nlp-1.png)

Photo by [Emiliano Vittoriosi](https://unsplash.com/@emilianovittoriosi?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

Natural language processing (NLP) is progressing extremely quickly nowadays and it can be difficult to know which research papers to start with if you’re interested in getting into the field. In this post I will detail five of the papers I read as a machine learning novice that greatly expanded my knowledge of NLP, and why they’re so important.

### 1. Attention is All You Need

[Attention is All You Need](https://arxiv.org/abs/1706.03762), published June 2017, is widely regarded as one of the most important papers in NLP because it was the debut of the transformer, a neural network architecture that most NLP models are using parts or versions of today.

As stated by the paper’s name, the transformer model relies on the attention mechanism, which is unique because many prior NLP models were using recurrent neural networks (RNNs).

This paper is a big challenge to understand as a beginner, but thankfully there are tons of resources online that break it down into simpler concepts. Here are two of my favorites.

1. [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/): This beautiful page uses drawings and animations to explain the transformer. It starts with a high level overview and then slowly drills down into fine details.
2. [The Annotated Transformer](https://nlp.seas.harvard.edu/2018/04/03/attention.html): If you are hoping to reimplement this paper or just want a deeper understanding, this page provides working code for the transformer, explaining each important block one at a time.

It will probably take a couple of weeks to understand this paper fully, but once you do, the remaining papers on this list (and most of today’s NLP) will be much clearer. It’s well worth the investment.

#### Big Takeaways

* Self-attention is an attention mechanism in which tokens at different positions of one sequence are related to one another.
* The transformer consists of a series of encoder and decoder layers which each utilize self-attention.
* The transformer improved upon previous models like LSTMs because they allowed for parallel computation and could handle long dependencies better due to being able to process long passages of text all at once.

### 2. GPT-1: Improving Language Understanding by Generative Pre-training

OpenAI wasted no time and created [their first GPT model](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf), which uses a stripped-down transformer, in June 2018. It demonstrated the effectiveness of the unsupervised pre-training → supervised fine-tuning process that is seen in many NLP models today.

Most state-of-the-art (SOTA) models before GPT were specialized for one particular task, like question answering, but were unable to do others. This approach was hitting road blocks because there simply wasn’t enough labeled data for these specific tasks. The authors at OpenAI instead decided to tap into the vast amount of unlabeled data available online.

The results of the paper are modest compared to today’s GPT models, but they showed that it is possible to create a model that has a general understanding of language and then use it for a variety of tasks afterwards.

#### Big Takeaways

* Unlabeled text data is abundant but labeled data for specific NLP tasks is scarce.
* GPT is a decoder-only transformer model.
* In contrast to previous approaches, GPT does task-aware input transformations during fine-tuning which requires minimal changes to model architecture.
* The fine-tuned versions outperformed models that used architectures specifically crafted to a given task, achieving SOTA in 9 of 12 tasks studied.

### 3. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

Now that you are familiar with the inner workings of GPT, it’s time to look at a different architecture, [BERT](https://arxiv.org/pdf/1810.04805.pdf). Released by Google in October 2018, Bidirectional Encoder Representations from Transformers was another incredible jack of all trades. BERT utilizes a bidirectional representation of the input text to learn from and predict the tokens both before and after the current token. It also reemphasized the strength and wide applicability of pretraining a general language model before fine-tuning it to a particular task.

#### **Big Takeaways**

* BERT is an encoder-only transformer model.
* One way it learns is by masking some percentage of the input tokens at random, and then predicting those masked tokens.
* This training approach was especially influential — it’s what gave the embeddings bi-directionality.
* The paper’s main lasting influences were demonstrating the importance of bi-directional embeddings and the utility of pre-trained models (instead of building task-specific model architectures).

### 4. GPT-2: Language Models are Unsupervised Multitask Learners

OpenAI released [GPT-2](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) in February 2019, not even a year after GPT-1. GPT-2 takes the quirks of GPT-1 to the next level by training exclusively unsupervised and having no task-specific input transformations. It generalizes well and had state-of-the-art performance on several tasks in a zero-shot setting.

GPT-2, with its eerily-human generated text, made it clear that training on unsupervised data was the way forward for large language models.

#### Big Takeaways

* GPT-2 supports the hypothesis that large language models can learn to do any task naturally if given enough data. This is because the model will have an understanding of the most commonly tested tasks just by going over the dataset.
* GPT-2 is about ten times larger than GPT-1, and has large performance improvements because of this.
* Its architecture looks very similar to GPT-1.
* The task for the model is prompted within the input. This wasn’t done before. For example, if we want GPT-2 to summarize an input text, we just add TL;DR (too long, didn’t read) to the end of the input and it outputs a summary.

### 5. Scaling Laws for Neural Language Models

OpenAI released an [interesting paper](https://arxiv.org/abs/2001.08361) in January 2020 that provided more evidence that simply increasing the scale of models, whether from compute, data, or parameters, was a reliable way to increase their performance. In fact, these factors were much more important than model shape, like whether the transformer had many small layers or a few large ones.

Through a series of experiments, they showed that for optimal performance, the three meaningful factors (params, dataset, compute) should be scaled in tandem, and that performance has a power-law relationship with each of those three factors *when not bottlenecked by the other two.*

#### Big Takeaways

* Large models are more sample-efficient than small models, reaching the same level of performance with fewer optimization steps and fewer data points.
* The optimal strategy for limited compute/budget is to train large models on a modest amount of data and stop significantly before convergence.

### Conclusion

After reading, taking notes, and reviewing these 5 papers, you should have a strong foundational knowledge of some of NLP’s most important models and techniques. However, there are still many more important and new topics (reinforcement learning from human feedback is a big one that comes to mind) that this post does not cover. The field is changing more rapidly than ever, so never stop learning!