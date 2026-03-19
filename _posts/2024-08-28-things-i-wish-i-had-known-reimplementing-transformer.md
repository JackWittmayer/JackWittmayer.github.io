---
title: Things I wish I had known before reimplementing a Transformer from scratch
date: 2024-08-28
description: If you are like me, you want to gain a deep understanding of what is happening behind the scenes of today’s most impressive AI models like…
---

---

If you are like me, you want to gain a deep understanding of what is happening behind the scenes of today’s most impressive AI models like ChatGPT, Claude, and Gemini. One of the most popular ways of doing that is reimplementing that original transformer model from the [Attention is All You Need paper](https://arxiv.org/pdf/1706.03762).

While the encoder-decoder transformer detailed in the 2017 paper is a fair bit different from the architecture of the models mentioned above, it is still a useful starting point and there are tons of resources on it. One kind of resource I feel is lacking though is documentation of the experience people have had reimplementing the paper, and the lessons they learned along the way. Helping others gain the technical learnings should be the first priority, but why not teach the nontechnical ones too? In this doc I will be attempting to teach those nontechnical learnings that I gained when I [reimplemented the original transformer](https://github.com/JackWittmayer/Transformer-Implementation).

### 1. Use the largest variety of learning resources you can

Understanding the transformer is HARD. You want to give yourself the greatest chance of success by having it explained in the largest variety of mediums, depth, perspective, and focus.

Mediums: blogs, YouTube videos, Jupyter Notebooks, heck — see if you can even find a podcast. This helps keep things fresh and interesting.

Depth: some resources (like [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)) hide away details to try to explain the big picture. Others (like [An Even More Annotated Transformer](https://pi-tau.github.io/posts/transformer/)) show basically everything. You’ll need to use both.

Perspective: There are many lenses to view the transformer model through.

1. Visual: Again, the [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), but also [this cool LLM Visualization tool](https://bbycroft.net/llm).
2. Written: Texts that attempt to explain the transformer in simpler words, like [Attention is All You Need for dummies](https://humanoid.tools/articles/attention-is-all-you-need-by-vaswani-et-al-2017-for-dummies/).
3. Code: [The Annotated](https://nlp.seas.harvard.edu/annotated-transformer/) or [Even More Annotated Transformer](https://pi-tau.github.io/posts/transformer/), or the various reimplementation blogs like [this one](https://towardsdatascience.com/build-your-own-transformer-from-scratch-using-pytorch-84c850470dcb).
4. Math: Do not be intimidated! If you can understand the code, I promise that with some time you can understand the math behind this model. I highly recommend working through [Formal Algorithms for Transformers](https://arxiv.org/abs/2207.09238) as you’ll build a solid idea of *why* each part of the transformer is set up the away it is.

Focus: Once you have a solid grasp of the big picture, I would recommend drilling deeper into the parts you are having trouble understanding. For example, I found [this resource](https://towardsdatascience.com/transformers-explained-visually-part-3-multi-head-attention-deep-dive-1c1ff1024853) super helpful for figuring out what was going on with masking.

### 2. Prefer newer resources

The Attention is All You Need paper is from 2017, so naturally there are resources from every year between then and now. I recommend viewing the resources closer to the current year first, as they teach more towards the common conventions and ways of thinking about transformers that people use today. They focus on teaching the parts of the transformer that are more relevant to today’s models. They’re also just generally higher quality (with some exceptions of course), as they are written by authors who have had more time and resources to build their own knowledge.

### 3. Try to follow today’s machine learning coding standards

While the main priority should just be to learn the material and get a decent model running, a small investment in making your code look nice and standard will pay off in the long run. For example, after reading Formal Algorithms in Transformers, I initially decided that I would implement the transformer following the paper’s column vector notation rather than row vector notation. That is, formatting my data’s shape as [embedding\_size, sequence\_length] rather than the [sequence\_length, embedding\_size] used by basically every resource and library online. This was a terrible idea, as it meant I had to do mental gymnastics to convert my model to the model I was reading every time I tried to view someone else’s code. I ended up switching everything to row vector notation halfway through later.

By making your code look like everyone else’s (but better), you’ll have a much easier time getting yourself unstuck later. Don’t feel bad about using abstractions from ML libraries like Pytorch if you need them. Everyone else is doing the same.

### 4. Feel free to look at other people’s code to unblock yourself

While it’s important to be truly learning the material as best as you can, and you can learn a lot by letting yourself struggle through a problem, agonizing over a small piece of the puzzle for days isn’t efficient. It’s better to use other people’s code to get past a blocking issue so you can move on to experimenting with everything else. Don’t expect to understand everything 100% on your first implementation. You can always come back later.

### 5. Know when to call the implementation DONE

What is your goal? Do you want a model that looks and functions exactly like the one in the original paper, or do you just want something that translates English to German halfway decently? Do you want your code to be nicely formatted in individual files — with tests, documentation, and all — or do you just want a Jupyter Notebook that can run every cell without crashing? Having a clear goal and milestones will make you feel more accomplished and prevent you from spending time on things you don’t really care about.

You could easily spend 60+ hours on this implementation to get something absolutely perfect. I spent around 40 on [mine](https://github.com/JackWittmayer/Transformer-Implementation), but the last 10 or so were mostly just adding tests and making the code look nice. Remember that this paper is quite old, and machine learning is moving extremely fast, so it’s best to not be working on this paper forever. Learn what you need to learn and move on.

### That’s all for now

There are many other things I learned with this implementation that I may go back and add if people are interested and I have the time, but I just wanted to get this out so it is available to others. Let me know if any of this was useful or resonated with you and what you wish you had known before reimplementing the original transformer.

### Other medium articles similar to this one

[*Lessons from implementing transformers from scratch*](https://lbartnik.medium.com/lessons-from-implementing-transformers-from-scratch-90e1b5f57588) by Lukasz A Bartnik.

[*Implementing a Transformer from Scratch*](https://towardsdatascience.com/7-things-you-didnt-know-about-the-transformer-a70d93ced6b2) by Joris Baan.