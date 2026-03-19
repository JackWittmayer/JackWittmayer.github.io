---
title: Does weak-to-strong generalization generalize?
date: 2025-02-02
description: This post is a summary of a small project I completed for the AI Safety Fundamentals online course hosted by BlueDot Impact in October…
---

---

This post is a summary of a small project I completed for the [AI Safety Fundamentals online course](https://aisafetyfundamentals.com/) hosted by BlueDot Impact in October 2024.

TL;DR: the datasets I chose for the experiment were mostly ill-suited, which means I don’t have enough results yet to know whether it generalizes.

### What is weak-to-strong generalization?

[Weak-to-strong generalization](https://openai.com/index/weak-to-strong-generalization/) is a research direction for AI superalignment that OpenAI investigated in late 2023. Its main draw is that it may be a tractable method to teach AI that is much smarter than humans to align with human intent. As AI models continue to grow in capabilities, it will become increasingly difficult for humans to judge the models’ output and teach them to behave in certain ways. For example, how will humans efficiently judge the outputs of a model that rapidly writes textbooks in difficult subjects like quantum mechanics? The theory of weak-to-strong generalization is that perhaps humans don’t need to be perfect judges, and that extremely intelligent models can still learn from imperfect training signals without compromising on performance too much.

There were not models intelligent enough to fit this problem scenario in late 2023, so OpenAI cleverly set up a analogical experiment: making a weak (low parameter count) model train a strong (high parameter count) model.

![](/images/2025-02-02-does-weak-to-strong-generalization-generalize-1.jpeg)

OpenAI’s figure explaining what weak-to-strong generalization is at a high level.

Practically, this involves the following steps:

1. Fine-tune a weak model on a dataset and extract its flawed outputs and evaluate its performance.
2. Fine-tune a strong model on a dataset and evaluate its performance.
3. Fine-tune a strong model on the flawed outputs from 1 and evaluate its performance.
4. Compare the performance of 1, 2, and 3 to see how well the strong model could learn from the weak model.

The key metric in 4 is the performance gap recovered (PGR), which is essentially how much the weak-to-strong model triumphed over the weak-model is comparison to the strong model. If the weak-to-strong model did just as well as the strong model, the PGR is 1.0. If it performed no better than the weak model after learning from its outputs, the PGR is 0.0.

#### Results

OpenAI found that the method was overall fairly successful, with the main promise being that they were able to find simple ways to build on it and improve its efficacy.

![](/images/2025-02-02-does-weak-to-strong-generalization-generalize-2.png)

Summary of OpenAI’s results using weak-to-strong generalization.

One finding that I found particularly interesting was that how successful weak-to-strong generalization was varied based on the dataset.

### Eleuther AI’s experiment

In June 2024, [Eleuther AI](https://www.eleuther.ai/about/), a non-profit AI research lab released [a blog post continuation](https://blog.eleuther.ai/weak-to-strong/) of OpenAI’s research. They reimplemented the paper with weak-to-strong generalization applied to the open-source models Qwen1.5 0.5B (weak) and Llama 3 8B (strong). They ran a number of experiments with attempted augmentations to the original method to see if it would improve. Unfortunately, the vanilla method used by OpenAI was generally the most effective.

I found it interesting that weak-to-strong generalization performed very well on some datasets (ethics utilitarianism, cola, and mc\_taco) while failing on others (hellaswag, piqa, quartz). This realization inspired me to run the method on more datasets to try to discover any patterns of which kinds of tasks work best.

![](/images/2025-02-02-does-weak-to-strong-generalization-generalize-3.png)

Eleuther AI’s weak-to-strong generalization results on 25 NLP datasets. The method performs much better on some datasets than others.

A major contribution of this blog post was their [code](https://github.com/EleutherAI/w2s) that contains a simple experiment workflow that new datasets can easily be plugged into and ran. I chose to use this code for my project.

### Applying weak-to-strong generalization to Google BIG-Bench tasks

The [Beyond the Imitation Game Benchmark (BIG-bench)](https://github.com/google/BIG-bench) is a collaborative benchmark intended to probe large language models and extrapolate their future capabilities. Over 200 NLP tasks have been added to the repository for anyone to download and evaluate their models with. To try to further investigate the abilities of weak-to-strong generalization, I ran Eleuther AI’s code on a sample of these tasks. Below are the results

![](/images/2025-02-02-does-weak-to-strong-generalization-generalize-4.png)

Results from my experiments. Blue = weak model performance, red = strong model performance, yellow = weak-to-strong model performance.

#### Analysis

While I intended to run the experiment for as many datasets as possible, unfortunately, most of the ones in Google BIG-Bench were not suited for the task either because they were too small (<100 examples), they were not multiple choice questions, they were too hard (all models could not improve from fine-tuning), or they were too easy (all models reached 1.0 AUC from fine-tuning). This combined with time constraints meant I only obtained final results for the five datasets shown above. This sadly leaves too little data to analyze for interesting patterns.

### Conclusion

In this post I summarized what the research area of weak-to-strong generalization is and results from recent experiments. I hope that what I have published can serve as a jumping off point for others interested in the area to follow up on, or at least a warning to choose your experiment setup wisely. I recommend applying the method to large and modern NLP datasets and tasks in the future as they will be more likely to yield usable results. I may continue this work when I have time, but am just publishing what I have for now.