---
title: Multimodal AI: The Story of LLaVA, Mixture of Experts, and MoE-LLaVA
date: 2024-11-19
description: Multimodal AI models have a bright future in the era of large-scale compute. Many of the most well-known LLMs, such as GPT-4, Gemini, and…
---

---

Multimodal AI models have a bright future in the era of large-scale compute. Many of the most well-known LLMs, such as GPT-4, Gemini, and Claude, have multimodal versions that were only developed in the last year. Despite this infancy, these models are surprisingly capable at what many consider to be [AI-complete or AI hard](https://en.wikipedia.org/wiki/AI-complete) problems in the vision space.

But how do they work? How can image and text be combined and understood by a model to be used for a wide variety of tasks like image captioning, visual question answering (VQA), virtual assistants, and more? In this post I will attempt to answer this question through a medium-depth analysis of LLaVA as well as one of its alternative versions, MoE-LLaVA.

### LLaVA: An Open-Weight Multimodal AI

LLaVA (large language and vision assistant), is an open-weight multimodal model developed by a collaboration between University of Wisconsin-Madison, Microsoft Research, and Columbia University that was introduced in the paper [“Visual Instruction Tuning”](https://arxiv.org/abs/2304.08485) in April 2023. Other than generously providing the open-source model, the paper mainly contributes to the space by detailing a clever way of using GPT-4 to generate enhanced training-data and describing how a pretrained visual and language decoder can be combined. Let’s look at each of these individually.

#### GPT’s Synthetic Data

Synthetic data has proven to be an effective input for training many models and LLaVA is no exception. The authors use GPT-4 to generate instruction-following data using the following process:

1. Extract the captions and numerically described object bounding boxes from examples in the COCO image dataset.

2. Combine this data and supply it to the language-only GPT-4 and ask it to create three types of instruction-following data, starting with a few manually designed examples to help get it going.

a. Conversation. A back-and-forth question and answering session about factual, visual components of the image.

b. Detailed description. A rich and comprehensive description of the image.

c. Complex reasoning. An in-depth reasoning question that requires an understanding of the image beyond what is immediately visible.

3. Turn these responses into a supervised learning dataset, where the questions and prompts from the above are the input and the answers are the target output.

Here is a full example of this process given in the paper.

![](/images/2024-11-19-multimodal-ai-llava-mixture-of-experts-1.png)

A LLaVA data generation example

Important note: the image of the van is provided for the reader’s benefit only. It is not supplied to GPT-4. The language model is provided the captions and bounding boxes only but is asked to respond as if it can see the image anyway.

#### Stitching Vision and Language Together

­­LLaVA is a couple pretrained models stitched together with an image to text translator in between. The authors provide the following diagram of the LLaVA network architecture in their paper.

![](/images/2024-11-19-multimodal-ai-llava-mixture-of-experts-2.png)

LLaVA architecture

I personally found this difficult to piece together at first, so let’s break it down.

First, an input image Xv is sent through a visual encoder called CLIP, which turns it into a visual feature embedding Zv. Think of this as an encoded representation of the image that only the vision model can understand. At the same time, Xq, a language instruction such as “What challenges do these people face” in the example above is sent through a language model encoder, like the first part of an LLM, to create a text feature embedding Hq. We now have an encoded representation of the image and input text. How do we combine them? First, we need to convert Zv into something more similar to Hq and align their distributions. This is done by sending Zv through a simple linear layer, which is the same as multiplying it by a trainable projection matrix W, to ultimately produce Hv. Finally, the two representations are simply concatenated and supplied to a pretrained LLM, (represented by fϕ) to produce the language response Xa. LLaVA uses Vicuna for this LLM, but other LLMs can be used as well (more on that later).

I just described the full flow of the input data through the model. But how is LLaVA trained? Thankfully, it’s simple. It involves two main stages.

Stage I: Keep the visual encoder and LLM weights frozen and train W only. This process uses simple image-caption pairs as training data and is done to teach W to align the visual embeddings with the word embeddings, to sort of get them within the same ballpark.

Stage II: Keep the visual encoder weights frozen, train W and the LLM. Here is where the synthetic dataset created earlier is used, where the image and generated instructions are passed as input and the model output is compared to the answer generated by GPT. By the end of stage I, the model was pretty good at associating text with visual input. Stage II finetunes the model to be effective at question answering.

By the end, the model can analyze images and respond accurately to diverse prompts.. Here is a funny example provided by the paper:

![](/images/2024-11-19-multimodal-ai-llava-mixture-of-experts-3.png)

A LLaVA visual input example

LLaVA excels by aligning visual and text features, combining pretrained models, and fine-tuning on a GPT-generated dataset. From here, LLaVA can be further fine-tuned for a variety of tasks using domain-specific datasets, or deployed directly for tasks like VQA shown above.

Now, let’s move on to an innovation made adjacent to multimodal models, Mixture of Experts (MoE).

### Mixture of Experts: an Old Approach Made New

Mixture of experts is an ensemble machine learning technique where only a subset of a model’s learned parameters is used during training and inference. You can think of it as multiple specialized models or “experts” working together to solve a problem, with a router deciding which expert gets which work.

The paper [“Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity”](https://arxiv.org/abs/2101.03961) provides the following diagram on MoE that illustrates it well.

![](/images/2024-11-19-multimodal-ai-llava-mixture-of-experts-4.png)

MoE diagram

The main difference of MoE transformers is that the single feed-forward neural network of the transformer block is divided into multiple experts. In this case four are pictured. A router learns to choose which of these experts to use for each provided token of the input and directs the flow of the model there.

How exactly does this routing work? I will explain the process used for [Mixtral](https://arxiv.org/abs/2401.04088), Mistral’s MoE language model. For each MoE module, each input token is sent through a linear layer that creates a logit for each expert. The router picks the top K of these logits and then softmaxes them, which creates a vector of values between 0 and 1, with only K of them being greater than 0. Each of these K experts computes their output for the token, and then the weighted sum of the outputs is computed using the original weight vector. Crucially, the experts that had a 0 in the weight vector are not activated at all.

K is a fixed hyperparameter that decides the number of experts that will be active for each token. For Mixtral, K=2, with eight experts in total.

#### Why use MoE?

Mixture of experts dates back to the 1991 paper “[Adaptive Mixtures of Local Experts](https://ieeexplore.ieee.org/document/6797059)”, but has become especially relevant in recent years due to the great advantage it offers for training time and inference speed. Because only the best fraction of the model is used for each token, the total training and inference time is cut down by the number of experts. For example, if the model consists of eight experts, and only uses one at inference time, it will take only one-eighth the time to generate a response as compared to a model with one expert (ignoring fixed overhead from other layers).

This allows for “sparse” models with an outrageous number of total parameters to be trained, as the final computational cost remains mostly fixed as more parameters are added. All these parameters must be stored in memory though, so there is still a limit of course.

One downside of MoE is the significant training complexity it adds vs training “dense” models. One needs to avoid allowing the model to converge on only activating just a few experts, as this will result in creating a weaker model with many dead parameters hanging around. In fact, this is what will happen by default if there are no interventions, as the experts that succeed early on are more likely to be chosen by the router, which makes them perform better, which makes them more likely to be chosen.

One strategy for avoiding this problem is adding noise to the decision of which expert to choose, forcing all experts to be occasionally chosen randomly. Another is training two regularization terms to penalize over relying on one expert and rewarding relying on equal expert utilization.

With all that said, is it possible to combine MoE with LLaVA?

### MoE-LLaVA: Bringing it all Together

Of course it is! One can simply replace the language model used in LLaVA with an MoE version, like Mixtral or otherwise. The paper [“MoE-LLaVA: Mixture of Experts for Large Vision-Language Models”](https://arxiv.org/abs/2401.15947), published in January 2024, details exactly this approach, as well as the training procedure they call MoE-Tuning to get it all working in practice.

#### MoE-Tuning

The authors provide the following diagram which divides MoE-Tuning into three stages.

![](/images/2024-11-19-multimodal-ai-llava-mixture-of-experts-5.png)

MoE-LLaVA diagram

If you can remember from earlier, Stage I and Stage II are the same as with generic LLaVA. First, solely train the projection matrix to adapt the visual input to the text input, then train the projection matrix and the LLM to respond to prompts about images. What’s new is stage III.

In stage III, the feed-forward networks of the original LLM are saved and copied to initialize a group of experts. A new router is also added which decides the top-K experts to use for each token and then takes the weighted sum of the outputs of only those experts. The model uses an instruction-following data mixture that was used to train LLaVA-1.5 to finally train the model to properly utilize and diversify the experts.

The main thing to note here is that the authors chose to not merge stage II and stage III together, as they encountered challenges simultaneously transforming the LLM into an LVLM (large language-vision model) and sparsifying the LVLM. Instead, they break it into two parts and reuse the weights of stage II to initialize stage III.

#### End Results

So, is it worth going through this extra stage of training just to have the MoE architecture? The answer seems to be **yes**, as the MoE-LLaVA performed similarly or better than dense models on a variety of benchmarks, with only a fraction of the active parameters. This is important because vision models perform significantly better as they are scaled up, and any efficiency improvement that allows further scaling is very desirable. However, the authors do note that their model can be taken as just a baseline to be improved upon.

### Conclusion and Moving Forward

In this post, we learned all about how LLaVA works, as well as saw a brief overview of MoE and how it can be combined to create a new version of LLaVA. There are several innovations that this post does not cover though, most notably the improvements within LLaVA itself to [LLaVA-NeXT](https://arxiv.org/abs/2407.07895), which learns to analyze both single-image input and multi-image, video, and multi-view input. Multimodal models are developing at a breakneck speed and MoE-LLaVA is just one small, but impressive step in the journey.