import json
from openai import OpenAI
import streamlit as st

# ==========================================
# 1. Page Configuration
# ==========================================
st.set_page_config(
    page_title="Taxonomy Utility Navigator", page_icon="🧬", layout="wide"
)

st.title("Diagnostic Taxonomy Utility Navigator")
st.markdown("""
Enter a historical figure, theoretical case, or specific psychological construct. 
The AI logic engine will map the subject across a 5-step Unified Diagnostic Architecture, 
exposing the tension between algorithmic clinical utility and systemic limitations.
""")

# ==========================================
# 2. Sidebar Configuration & Key Handling
# ==========================================
with st.sidebar:
  st.header("Configuration")

  # Safely check Streamlit Secrets first; fallback to empty string for manual input
  secret_key = st.secrets.get("OPENAI_API_KEY", "")

  api_key = st.text_input(
      "API Key",
      value=secret_key,
      type="password",
      help=(
          "Automatically loaded from Streamlit Secrets. Alternatively, paste"
          " your key here."
      ),
  )

  model_name = st.text_input(
      "Model Name",
      value="gemini-1.5-flash",
      help="e.g., gemini-1.5-flash or gemini-1.5-pro",
  )

  base_url = st.text_input(
      "Base URL",
      value="https://generativelanguage.googleapis.com/v1beta/openai/",
      help="Google Gemini OpenAI-compatible endpoint.",
  )

# ==========================================
# 3. System Prompt Architecture
# ==========================================
SYSTEM_INSTRUCTION = """
You are the logic engine for the "Taxonomy Utility Navigator." Your role is to analyze user-submitted cases using a 5-step Unified Diagnostic Architecture derived from the DSM-5-TR and ICD-11. 

Map the case across 5 sequential nodes:
1. Core Presentation (Symptoms & Clinical Prototypes)
2. Clinical Threshold (Distress/Impairment vs. Normative Experience)
3. Exclusionary Boundaries (Medical/Substance Exclusions & Differential Diagnosis)
4. Temporal Progression (Duration & Longitudinal Course)
5. Dimensional Modifiers (Severity & Extension Codes)

For EACH node, generate:
- "caseMapping": How the case fits this node.
- "clinicalUtility": How the algorithm successfully captures this case.
- "systemicLimitation": The friction point—how the taxonomy oversimplifies or misses the holistic reality.

Output ONLY valid JSON using this exact schema:
{
  "subjectName": "String",
  "nodes": [
    {
      "nodeId": 1,
      "nodeName": "String",
      "caseMapping": "String",
      "clinicalUtility": "String",
      "systemicLimitation": "String"
    }
  ],
  "synthesis": "String (Summary of tension between algorithmic diagnosis and holistic understanding)"
}
"""

# ==========================================
# 4. Main Application Logic
# ==========================================
subject_input = st.text_input(
    "Subject to Analyze:",
    placeholder="e.g., Vincent van Gogh, ADHD, or a theoretical case of grief...",
)

if st.button("Run Analysis", type="primary"):
  if not api_key:
    st.error(
        "No API Key found. Please add OPENAI_API_KEY to your Streamlit Secrets"
        " or enter it in the sidebar."
    )
  elif not subject_input:
    st.warning("Please enter a subject to analyze.")
  else:
    try:
      with st.spinner(
          f"Analyzing {subject_input} through the diagnostic taxonomy..."
      ):
        client_kwargs = {"api_key": api_key}
        if base_url.strip():
          client_kwargs["base_url"] = base_url.strip()

        client = OpenAI(**client_kwargs)

        response = client.chat.completions.create(
            model=model_name,
            response_format={"type": "json_object"},
            temperature=0.3,
            messages=[
                {"role": "system", "content": SYSTEM_INSTRUCTION},
                {
                    "role": "user",
                    "content": f"Analyze this subject: {subject_input}",
                },
            ],
        )

        raw_content = response.choices[0].message.content
        data = json.loads(raw_content)

      # ==========================================
      # 5. UI Rendering
      # ==========================================
      st.success("Analysis Complete")
      st.header(f"Subject: {data.get('subjectName', subject_input)}")

      for node in data.get("nodes", []):
        with st.expander(
            f"Node {node['nodeId']}: {node['nodeName']}", expanded=True
        ):
          st.write("**Case Mapping:**")
          st.write(node.get("caseMapping", ""))

          tab1, tab2 = st.tabs(
              ["✅ Clinical Utility", "⚠️ Systemic Limitation"]
          )

          with tab1:
            st.info(node.get("clinicalUtility", ""))
          with tab2:
            st.warning(node.get("systemicLimitation", ""))

      st.divider()
      st.subheader("System Synthesis")
      st.write(data.get("synthesis", ""))

    except json.JSONDecodeError:
      st.error(
          "The model failed to return structured JSON. Try running the request"
          " again."
      )
    except Exception as e:
      st.error(f"API Error: {e}")
