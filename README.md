# Dynamic Graph Influence Maximization - AAAI 2025  

This repository contains the **code, datasets, and paper** associated with our research on **Dynamic Influence Maximization in Evolving Networks**, accepted at **AAAI-25**.  

## 🔍 Overview  
- Influence Maximization (**InfMax**) is a fundamental problem in **network science**, focusing on identifying the most influential nodes in a network.  
- Traditional approaches assume **static networks**, which is unrealistic for evolving systems (e.g., **social media, traffic, biological networks**).  
- We propose a **GNN-BiLSTM-based adaptive framework** that efficiently tracks **influential nodes** while reducing computational overhead.  

## 📜 Paper  
📄 **[Download Full Paper](https://github.com/Priyankagautam08/DynamicGraphInfluenceMaximization-AAAI2025/blob/main/AAAI25_Dynamic_Infmax.pdf)**  

## 🚀 Key Features  
- **Dynamic Network Adaptability:** Handles evolving structures over time.  
- **Efficient Candidate Node Selection:** Uses **Graph Neural Networks (GNNs)** to predict influential nodes.  
- **Faster Computation:** Achieves **2× speedup** over traditional **Greedy algorithms** while maintaining influence spread.  
- **Scalability:** Works on both **small and large-scale networks** (320 – 11,492 nodes).
  
## 📊 Experimental Setup  
- **Datasets:** Real-world (SNAP, Email-Eu-core, College-Msg) and synthetic (Barabasi-Albert, Erdős-Rényi).  
- **Hardware:** Experiments conducted on **Intel i9-12900K & NVIDIA RTX 3090 GPU**.  
- **Evaluation Metrics:** Accuracy, computational efficiency, and influence spread.  


## 🤝 Contributors  
This research is a collaboration between **Kansas State University** and **Pacific Northwest National Laboratory (PNNL)**.  

| Contributor                  | Affiliation                                | Google Scholar |
|------------------------------|--------------------------------------------|----------------|
| **Priyanka Gautam**          | Kansas State University                   | [Google Scholar]([https://scholar.google.com/](https://scholar.google.com/citations?user=7uzapiUAAAAJ&hl=en)) |
| **Balasubramaniam Natarajan**| Kansas State University                   | [Google Scholar]([https://scholar.google.com/](https://scholar.google.com/citations?user=ePCK5e8AAAAJ&hl=en)) |
| **Sai Munikoti**             | Pacific Northwest National Laboratory     | [Google Scholar]([https://scholar.google.com/](https://scholar.google.com/citations?user=2qzs41QAAAAJ&hl=en)) |
| **S M Ferdous**              | Pacific Northwest National Laboratory     | [Google Scholar]([https://scholar.google.com/](https://scholar.google.com/citations?user=pqbWrO0AAAAJ&hl=en)) |
| **Mahantesh Halappanavar**   | Pacific Northwest National Laboratory     | [Google Scholar]([https://scholar.google.com/](https://scholar.google.com/citations?user=E4Wqxq8AAAAJ&hl=en)) |

## 🏛 Research Lab
This research is conducted as part of the Cyber-Physical Systems and Wireless Networking (CPSWIN) Lab at Kansas State University.
🔗 Learn more about our lab

## 🙏 Acknowledgments
This work is supported by the National Science Foundation (NSF) under Award No. OIA-2148878, with matching support from the State of Kansas through the Kansas Board of Regents.

Additionally, this research is supported by the U.S. Department of Energy (DOE) through the Exascale Computing Project (17-SC-20-SC) (ExaGraph) at Pacific Northwest National Laboratory (PNNL).

We appreciate the support from Kansas State University and PNNL, as well as our collaborators who contributed valuable insights to this work.


## 🛠 Installation & Setup
Clone the repository and install dependencies:  
```bash
- git clone https://github.com/YourRepoHere/DynamicGraphInfluenceMaximization-AAAI2025.git
- cd DynamicGraphInfluenceMaximization-AAAI2025
- pip install -r requirements.txt
