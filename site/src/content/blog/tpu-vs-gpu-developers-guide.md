---
title: "TPUs vs GPUs Explained: What Every AI Developer Should Actually Know"
description: "You use AI models every day but probably cannot explain why Google built its own chips. Here is the hardware difference that shapes which models are fast, cheap, or neither."
date: "2026-04-11"
slug: "tpu-vs-gpu-developers-guide"
keywords: "TPU vs GPU explained, TPU vs GPU AI, Google TPU developer guide, AI hardware for developers"
episodes: ["4"]
---

TPUs (tensor processing units) are Google's custom-designed AI chips built exclusively for matrix multiplication, the core operation in neural network training and inference. GPUs (graphics processing units) are general-purpose parallel processors, originally designed for rendering graphics, that became the default AI hardware because their architecture happened to overlap with machine learning workloads. The key architectural difference: TPUs use systolic arrays that pass data directly between operations, while GPUs require memory round-trips between each step. This makes TPUs faster and more power-efficient for AI workloads, but less flexible and only available through Google Cloud.

When we covered this on [ADI Pod Episode 4](/episodes/4-open-ai-code-red-tpu-vs-gpu-and-more-autonomous-coding-agents/), my co-host Dan Lasky (who studied hardware engineering) walked through the physical architecture in a level of detail that changed how I think about inference costs. This post distills that conversation into the parts that matter if you are a developer who consumes AI rather than trains it: what is actually different, why it matters for the models you use, and what it means for the choices you make about which APIs to call.

## How GPUs Became the Default AI Hardware

GPUs were never designed for machine learning. They were designed to rotate thousands of 3D points in a point cloud so your character could turn left in Quake. The math underneath (massively parallel floating-point multiplication) turned out to overlap heavily with the math underneath neural network training. Around 2012, researchers working on the ImageNet challenge discovered that GPUs could accelerate image recognition training by orders of magnitude compared to CPUs. The hardware was cheap, available, and already sitting in data centers.

That discovery became a path dependency. Labs built on GPUs. Nvidia invested in CUDA, a programming framework that made it easier to run non-graphics workloads on GPU hardware. Libraries like cuDNN and later PyTorch built their entire stack on top of CUDA. By the time transformer models arrived, the entire ML ecosystem was GPU-native, not because GPUs were optimal for the task, but because they were there first and the tooling had accumulated around them.

This is a pattern anyone who has worked in software recognizes: the technically adequate early solution becomes the industry default because switching costs compound faster than the performance gap widens. CUDA's moat is the ten years of libraries, tutorials, debugging tools, and muscle memory that sit on top of it, not raw compute.

## What a TPU Actually Is

A TPU (tensor processing unit) is Google's answer to a specific question: what would you build if you were designing a chip from scratch for matrix multiplication and nothing else?

The name comes from tensors, which are just matrices with more than two dimensions. Every forward pass through a neural network is, at the hardware level, a chain of tensor multiplications. GPUs can do this. TPUs were built to do only this.

The first difference is what is absent. A GPU carries dedicated silicon for texture mapping, rasterization, and other graphics-specific operations. As Dan put it on the show, "when you think about it for machine learning, most of that silicon is essentially wasting space." A TPU strips all of that out. No texture rendering pipeline. No graphics hardware. The die area that would have been allocated to making Call of Duty look realistic is instead allocated to more multiply-accumulate units.

The second difference, and the more consequential one, is how the chip handles memory access during chained multiplications.

## Why Memory Bandwidth Matters More Than Raw Compute

This is where the architecture diverges in a way that has direct implications for inference speed.

On a GPU, every multiplication involves a round trip to memory. Dan walked through this at a level that made me feel like I was back in school: the chip asks memory for operand A, fetches it, asks memory for operand B, fetches it, performs the multiplication, writes the result back to memory, then fetches it again for the next operation. Each fetch has latency. In many cases, the memory access is actually slower than the multiplication itself.

This is why memory bandwidth (the rate at which data can move between memory and compute units) shows up as a bottleneck in every GPU inference benchmark. When you hear people debating whether an M4 Max is "good enough" for local inference, they are mostly arguing about memory bandwidth, not raw compute. The multiplications are fast. The fetching is slow.

TPUs address this with a structure called a systolic array. Instead of the back-and-forth between compute and memory, the output of one multiplication flows directly into the input of the next. A times B produces C, and C goes straight into the next multiplication without a memory round trip. For the kind of chained multiplications that dominate neural network inference (layer after layer of matrix operations feeding into each other), this eliminates the primary bottleneck.

The analogy I keep coming back to is a factory assembly line versus a warehouse-based workflow. The GPU approach is: do one step, put the part back on the shelf, walk to the shelf, pick up the part, bring it to the next station. The TPU approach is: do one step, hand the part directly to the next station. Same operations, radically different throughput when you have hundreds of sequential steps.

## TPU vs GPU Comparison Table

| | **Google TPU** | **Nvidia GPU** |
|---|---|---|
| **Designed for** | Matrix multiplication only | General-purpose parallel compute |
| **Key architecture** | Systolic arrays (no memory round-trips) | CUDA cores + tensor cores |
| **Latest chip** | TPU V7 (4,614 TFLOPS) | H100 (990 TFLOPS dense FP16) |
| **Memory** | 192 GB (V7) | 80 GB HBM3 (H100) |
| **Software ecosystem** | JAX, TensorFlow | CUDA, PyTorch (dominant) |
| **Availability** | Google Cloud only | Any cloud provider, on-premise |
| **Flexibility** | AI workloads only | AI + graphics + general compute |
| **Vendor lock-in** | High (Google Cloud required) | Low (multi-vendor) |
| **Who uses it** | Google (Gemini), Google Cloud customers | OpenAI, Meta, Microsoft, most labs |

## The Performance Numbers

The performance trajectory makes the architectural advantage concrete. Google's TPU V5 delivered 459 teraflops, roughly 459 trillion floating-point operations per second. The TPU V7, announced more recently, delivers 4,614 teraflops. That is a 10x improvement in raw compute across two generations, while memory capacity doubled from 96 GB to 192 GB.

For context, Nvidia's H100 (the GPU that defined the 2023-2024 AI infrastructure buildout) delivers around 990 teraflops of dense FP16 compute. The TPU V7 outperforms it by a factor of roughly 4.7x on raw throughput. These numbers are not directly comparable because workload characteristics matter, and Nvidia's tensor cores have their own optimizations for matrix math. But the directional gap is not subtle.

What makes this more than a spec-sheet comparison is the timeline. Google started designing TPUs in 2013. The first version was released in 2016, before OpenAI was even founded, and seven years before ChatGPT made LLMs a mainstream product. Google was being proactive, not reactive. Internal projections showed that if every Android user used voice search for just three minutes a day, the company would need to double its global data center capacity. Building the chip was a capacity planning decision rather than an AI strategy decision. The AI advantage was a consequence.

## Why This Matters for Gemini (and for You)

Google's hardware advantage explains something that puzzled a lot of people in late 2025: why Gemini 3 was so fast. When we discussed it on the show, I pointed out that Google has their own chip, their own model, and some of the best engineers in the world, so how could they possibly lose this fight? The speed advantage is primarily a hardware story, not a model architecture story. Gemini runs on TPU infrastructure that was purpose-built for exactly this workload, and the systolic array architecture means inference involves fewer memory round trips per token generated.

For developers, this surfaces in three practical ways.

**Inference cost and speed.** When you call the Gemini API and it responds noticeably faster than a competitor at a similar capability level, that is partly hardware. Google can serve inference at lower cost per token because the chips doing the work are more efficient at the specific task. This does not mean Gemini is always the best model for every task; model architecture, training data, and [RLHF tuning all matter](/topics/ai-coding-agents-compared/). But the cost floor for serving a Gemini-class model is structurally lower when the hardware is purpose-designed.

**Availability and capacity.** TPU manufacturing is controlled by Google. They do not sell TPUs on the open market the way Nvidia sells H100s. This means Google Cloud is effectively the only place to access TPU compute, which constrains the ecosystem but gives Google certainty of supply. When Nvidia GPUs were backordered for months in 2023-2024, Google's TPU pipeline was unaffected. If you are building on Google Cloud and need to scale training or inference workloads, TPU availability can be a genuine advantage over competing for GPU allocation.

**Model-hardware co-optimization.** Google trains and serves Gemini on the same TPU architecture. This allows tight co-optimization between model design and hardware capabilities, something that is difficult when model developers and hardware vendors are separate companies. OpenAI trains on Nvidia hardware, but Nvidia's design priorities serve the entire GPU market, not just OpenAI's specific needs. Google's vertical integration means the model can be designed around the chip's strengths, and vice versa.

## The Counterargument: Why GPUs Still Dominate

It would be misleading to frame this as "TPUs are better, end of story." GPUs dominate the AI ecosystem for reasons that are not purely inertial.

CUDA's software ecosystem is genuinely massive. PyTorch, the most popular ML framework, is CUDA-native. JAX supports TPUs well, and Google has invested heavily in TPU-compatible tooling, but the median ML engineer has CUDA experience and does not have TPU experience. Switching costs are real, and they compound at the organizational level: rewriting training pipelines, retraining staff, and re-validating results is expensive even when the destination hardware is faster.

GPUs are also more flexible. Nvidia's latest architectures include tensor cores that implement many of the same optimizations TPUs use for matrix math, while retaining the general-purpose programmability that makes GPUs useful for a wider range of workloads. If you need to run inference, train a model, and also run some non-ML compute on the same hardware, GPUs handle that. TPUs do one thing, but they do it exceptionally well.

And the market structure matters. Anyone can buy Nvidia GPUs. Amazon, Microsoft, Meta, and every major cloud provider offer GPU instances. TPU access requires Google Cloud. For organizations with multi-cloud strategies or existing infrastructure commitments, TPU adoption involves a level of vendor lock-in that many are not willing to accept.

## What to Actually Do With This Information

Most application developers will never optimize the hardware layer directly. You are calling APIs, not provisioning silicon. But understanding the architecture underneath those APIs changes how you evaluate tradeoffs.

When a model is fast and cheap, ask whether that reflects model efficiency or hardware advantage. The answer affects how durable the pricing is. When Google undercuts competitors on inference pricing, part of that margin comes from TPU efficiency that others cannot replicate without building their own chips. Amazon (with Trainium), Microsoft (with Maia), and Meta (with their custom accelerator) are all attempting exactly this, which tells you the industry agrees the advantage is real.

When you are choosing between providers for latency-sensitive workloads, the hardware stack matters more than the model benchmark. A slightly less capable model on purpose-built hardware can outperform a stronger model on general-purpose hardware in production, where latency and cost per token compound over millions of requests.

And when you hear that Google "fell behind" in AI and then suddenly "caught up," understand that the hardware investment that makes Gemini competitive was started thirteen years ago. It is a silicon race as much as a model architecture race or a data race, and the lead times are measured in years, not quarters.

The chip is the moat. The model is what you build on top of it.
