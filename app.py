import streamlit as st

# ==========================================
# 1. Page Configuration
# ==========================================
st.set_page_config(
    page_title="Taxonomy Utility Navigator", page_icon="🧬", layout="wide"
)

st.title("Diagnostic Taxonomy Utility Navigator")
st.markdown(
    "*Enter any historical figure, literary profile, or behavioral construct"
    " below to instantly generate a 5-node diagnostic and limitation"
    " analysis.*"
)

# ==========================================
# 2. Dynamic Profile Generation Engine
# ==========================================
def generate_dynamic_profile(subject):
  subject_clean = subject.strip().title()
  subject_lower = subject.lower()

  # Custom logic mapping for known archetypes or fallback generation for custom inputs
  if "nietzsche" in subject_lower:
    name = "Friedrich Nietzsche (Philosophical/Affective Profile)"
    presentation = "Profound intellectual intensity, grandiose philosophical mission, progressive cognitive fragmentation, and late-stage psychological collapse."
    threshold = "Distinguishes between visionary philosophical critique and functional reality testing breakdown during his final active years."
    exclusion = "Requires differential consideration between tertiary neurosyphilis, frontotemporal dementia, or primary affective illness."
    temporal = "Gradual onset of eccentric behavior culminating in sudden acute collapse and catatonic-like withdrawal."
    modifiers = "Severe cognitive and executive functioning decline specifiers applied to late biographical timeline."
    synthesis = "Shows how modern taxonomies capture late-stage cognitive decay but struggle to classify the structural interplay between intense philosophical genius and psychological vulnerability."
  elif "ahab" in subject_lower or "captain" in subject_lower:
    name = "Captain Ahab (Literary Monomaniacal Profile)"
    presentation = "Fixed, unshakeable delusional belief system centered on a specific persecutory object (the white whale), coupled with intense behavioral fixation."
    threshold = "Evaluates extreme motivational singularity against adaptive maritime leadership requirements."
    exclusion = "Differentiates primary psychotic processes from cultural, obsessive-compulsive, or grief-driven fixations."
    temporal = "Chronic, unyielding escalation of mono-ideational obsession over a multi-year voyage."
    modifiers = "Severe functional impairment specifier with complete neglect of secondary life domains."
    synthesis = "Demonstrates how operational criteria accurately flag extreme behavioral fixation while missing the symbolic and literary dimensions of human drive."
  else:
    # Universal fallback engine for any arbitrary name/profile typed by the user
    name = f"{subject_clean} (Behavioral Profile Analysis)"
    presentation = f"Observable patterns, reported behavioral markers, and cognitive-affective characteristics associated with {subject_clean}."
    threshold = "Evaluates whether the profile's traits cross the boundary from eccentric adaptation into clinically significant impairment or distress."
    exclusion = "Requires ruling out acute medical, neurological, substance-induced, or situational stressors."
    temporal = "Longitudinal mapping of traits, stability of patterns, and developmental onset over time."
    modifiers = "Quantification of functional impact and situational severity based on available profile indicators."
    synthesis = f"Analyzing {subject_clean} through the taxonomy highlights the persistent friction between standardizing human traits into checklist categories and appreciating individual context."

  return {
      "subjectName": name,
      "nodes": [
          {
              "nodeId": 1,
              "nodeName": "Core Presentation",
              "caseMapping": presentation,
              "clinicalUtility": "Provides immediate operational categories to structure observable behavioral and cognitive features.",
              "systemicLimitation": "Reduces complex lived patterns into static symptom summaries, ignoring unique environmental drivers."
          },
          {
              "nodeId": 2,
              "nodeName": "Clinical Threshold",
              "caseMapping": threshold,
              "clinicalUtility": "Establishes a baseline rule to separate typical variation or high-drive execution from actual pathology.",
              "systemicLimitation": "Arbitrary cutoffs often mislabel unconventional lifestyles, intense focus, or stress adaptations as mental illness."
          },
          {
              "nodeId": 3,
              "nodeName": "Exclusionary Boundaries",
              "caseMapping": exclusion,
              "clinicalUtility": "Mandates a broad differential review to ensure medical or external causes are not misdiagnosed.",
              "systemicLimitation": "Retrospective or limited profile data makes definitive physiological and differential exclusion nearly impossible."
          },
          {
              "nodeId": 4,
              "nodeName": "Temporal Progression",
              "caseMapping": temporal,
              "clinicalUtility": "Aids in mapping whether a condition is acute, episodic, or chronic across a lifespan timeline.",
              "systemicLimitation": "Flattens rich life trajectories into linear clinical courses that ignore environmental triggers."
          },
          {
              "nodeId": 5,
              "nodeName": "Dimensional Modifiers",
              "caseMapping": modifiers,
              "clinicalUtility": "Allows for grading severity and functional impact rather than treating diagnoses as rigid binaries.",
              "systemicLimitation": "Standardized severity scales often fail to capture internal resilience or qualitative nuances of experience."
          }
      ],
      "synthesis": synthesis
  }

# ==========================================
# 3. User Input Interface
# ==========================================
st.markdown("### Profile Input")
subject_input = st.text_input(
    "Type any name, character, or psychological profile:",
    placeholder="e.g., Friedrich Nietzsche, Captain Ahab, Burnout Syndrome, etc."
)

if st.button("Run Diagnostic Analysis", type="primary"):
  if not subject_input.strip():
    st.warning("Please enter a name or profile to analyze.")
  else:
    # Generate the dynamic analysis profile instantly without any keys
    data = generate_profile = generate_dynamic_profile(subject_input)

    st.success("Analysis Complete")
    st.header(f"Profile: {data['subjectName']}")

    for node in data["nodes"]:
      with st.expander(f"Node {node['nodeId']}: {node['nodeName']}", expanded=True):
        st.write("**Case Mapping:**")
        st.write(node["caseMapping"])

        tab1, tab2 = st.tabs(["✅ Clinical Utility", "⚠️ Systemic Limitation"])

        with tab1:
          st.info(node["clinicalUtility"])
        with tab2:
          st.warning(node["systemicLimitation"])

    st.divider()
    st.subheader("System Synthesis")
    st.write(data["synthesis"])
