import gradio as gr
from vei_classifier import classify

def process(height, volume_km3, duration_hours):
    if height is None or volume_km3 is None or duration_hours is None:
        return "Please provide all three inputs."
    try:
        vei, eruption_type = classify(height, volume_km3, duration_hours)
        return f"VEI: {vei} — {eruption_type}"
    except ValueError as e:
        return str(e)

reference = """
| Parameter | VEI 0 | VEI 1 | VEI 2 | VEI 3 | VEI 4 | VEI 5 | VEI 6 | VEI 7 | VEI 8 |
|-----------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Column height (km) | <0.1 | 0.1–1 | 1–5 | 3–15 | 10–25 | ≥25 | — | — | — |
| Volume (m³) | <1e4 | 1e4–1e6 | 1e6–1e7 | 1e7–1e8 | 1e8–1e9 | 1e9–1e10 | 1e10–1e11 | 1e11–1e12 | ≥1e12 |
| Duration (h) | <1 | 1–6 | 6–12 | 12–24 | 24–48 | ≥48 | — | — | — |
"""

with gr.Blocks(title="VEI Classifier") as demo:
    gr.Markdown("## VEI Classifier (Newhall & Self, 1982)")
    with gr.Row():
        height_slider = gr.Slider(minimum=0, maximum=50, value=5, step=0.1, label="Column height (km)")
    with gr.Row():
        volume_slider = gr.Slider(minimum=0, maximum=1000, value=0.1, step=0.01, label="Volume of tephra (km³)")
    with gr.Row():
        duration_slider = gr.Slider(minimum=0, maximum=48, value=1, step=0.1, label="Duration of explosive phase (hours)")
    classify_btn = gr.Button("Classify")
    output = gr.Textbox(label="Result")
    gr.Markdown("### Threshold Reference Table")
    gr.Markdown(reference)
    classify_btn.click(fn=process, inputs=[height_slider, volume_slider, duration_slider], outputs=output)

demo.launch(server_name="0.0.0.0", server_port=7860)
