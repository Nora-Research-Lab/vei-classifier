![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# VEI Classifier
 
*For volcanologists and hazard analysts: enter eruption column height, tephra volume, and duration to instantly get the Volcanic Explosivity Index (VEI 0-8) and eruption type.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Volcanology
 
The user provides three numeric inputs: (1) Eruption column height in km (float, range 0–50, default 5), (2) Volume of tephra ejected in km³ (float, range 0–1000, default 0.1), (3) Duration of explosive phase in hours (float, range 0–48, default 1). The core logic follows the Newhall & Self (1982) classification thresholds. Internally, volume in km³ is converted to m³ (×1e9). For each parameter, a VEI value is determined by threshold comparisons:
- Column height (km): VEI 0 <0.1, VEI 1 0.1–1, VEI 2 1–5, VEI 3 3–15, VEI 4 10–25, VEI 5 ≥25; no further discrimination above 25 (use volume).
- Volume (m³): VEI 0 <1e4, VEI 1 1e4–1e6, VEI 2 1e6–1e7, VEI 3 1e7–1e8, VEI 4 1e8–1e9, VEI 5 1e9–1e10, VEI 6 1e10–1e11, VEI 7 1e11–1e12, VEI 8 ≥1e12.
- Duration (hours): VEI 0 <1, VEI 1 1–6, VEI 2 6–12, VEI 3 12–24, VEI 4 24–48, VEI 5 ≥48; duration is not used for VEI ≥6.
The final VEI is the maximum of the three parameter-specific VEIs. The output then maps VEI to eruption type: 0–1 Hawaiian/Strombolian, 2–3 Vulcanian, 4–5 Plinian, 6–7 Ultra-Plinian, 8 Supervolcanic. The Gradio UI has a title, three horizontal sliders with labels and default values, a 'Classify' button, and a results area showing VEI number and eruption type. Below the button, a static table displays the threshold criteria for reference. No AI/ML component; pure lookup and arithmetic.
 
## Run it
 
```bash
docker build -t vei-classifier .
docker run -p 7860:7860 vei-classifier
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-23.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
