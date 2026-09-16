import streamlit as st

# ==========================================
# 1. Page Configuration
# ==========================================
st.set_page_config(
    page_title="Taxonomy Utility Navigator", page_icon="🧬", layout="wide"
)

st.title("Diagnostic Taxonomy Utility Navigator")
st.markdown(
    "*An interactive analytical tool exploring the tension between dual"
    " international diagnostic frameworks and holistic human experience.*"
)

# ==========================================
# 2. Educational Primer & Dual Methodology Explanation
# ==========================================
with st.expander(
    "📚 Methodology & Framework Explanation (DSM-5-TR & ICD-11)", expanded=True
):
  st.markdown("""
    ### Dual-Methodology Integration
    This navigator bridges the two dominant international classification standards to evaluate profiles:
    * **DSM-5-TR (Diagnostic and Statistical Manual of Mental Disorders):** Leveraged for its operationalized **symptom checklists**, structural thresholds, and polythetic criteria.
    * **ICD-11 (International Classification of Diseases):** Leveraged for its narrative **clinical prototypes**, contextual guidelines, and global medical perspective.

    ### The Unified 5-Step Architecture
    When you enter a name or profile below, the engine dynamically maps the subject across a 5-step framework that contrasts **Clinical Utility** (how well the checklist or prototype successfully standardizes and communicates the condition) against **Systemic Limitation** (where the taxonomy oversimplifies, pathologizes normal variation, or strips away vital context).
    """)

# ==========================================
# 3. Dynamic Profile Generation Engine
# ==========================================
def generate_dynamic_profile(subject):
  subject_clean = subject.strip().title()
  subject_lower = subject.lower()

  if "nietzsche" in subject_lower:
    name = "Friedrich Nietzsche (Philosophical/Affective Profile)"
    presentation = (
        "Profound intellectual intensity, grandiose philosophical mission,"
        " progressive cognitive fragmentation, and late-stage psychological"
        " collapse evaluated via DSM operational criteria and ICD clinical"
        " prototypes."
    )
    threshold = (
        "Weighs DSM symptom duration thresholds against ICD clinical prototype"
        " boundaries to distinguish visionary critique from functional"
        " deterioration."
    )
    exclusion = (
        "Addresses differential boundaries between tertiary neurosyphilis,"
        " frontotemporal dementia, or primary affective illness."
    )
    temporal = (
        "Maps progressive longitudinal decline from acute onset to permanent"
        " cognitive withdrawal."
    )
    modifiers = (
        "Applies severe cognitive and executive functional specifiers based"
        " on historical biographical markers."
    )
    synthesis = (
        "Exposes how DSM checklists and ICD prototypes capture late-stage"
        " cognitive decay while struggling to map the structural interplay"
        " between profound intellectual genius and psychological vulnerability."
    )
  elif "ahab" in subject_lower or "captain" in subject_lower:
    name = "Captain Ahab (Literary Monomaniacal Profile)"
    presentation = (
        "Fixed, unshakeable delusional belief system centered on a persecutory"
        " object, evaluated using both ICD narrative prototypes and DSM"
        " criteria for fixed beliefs."
    )
    threshold = (
        "Contrasts rigid DSM impairment metrics against ICD contextual"
        " guidelines regarding obsessive human drives."
    )
    exclusion = (
        "Differentiates primary psychotic processes from cultural,"
        " obsessive-compulsive, or grief-driven fixations under multi-axial"
        " differential rules."
    )
    temporal = (
        "Tracks the chronic, unyielding escalation of mono-ideational"
        " obsession over a multi-year narrative trajectory."
    )
    modifiers = (
        "Applies severe functional impairment and social isolation specifiers."
    )
    synthesis = (
        "Demonstrates how combining DSM structural thresholds with ICD narrative"
        " prototypes effectively flags extreme behavioral fixation while"
        " missing the symbolic and literary dimensions of human motivation."
    )
  else:
    name = f"{subject_clean} (Behavioral Profile Analysis)"
    presentation = (
        f"Observable patterns and cognitive-affective characteristics"
        f" associated with {subject_clean}, mapped through synthesized DSM"
        " checklist metrics and ICD clinical prototypes."
    )
    threshold = (
        "Evaluates whether traits cross operational DSM severity cutoffs or"
        " violate ICD normative boundaries of everyday functioning."
    )
    exclusion = (
        "Applies dual-system rules requiring the exclusion of acute medical,"
        " neurological, or external situational stressors."
    )
    temporal = (
        "Traces longitudinal trait stability and developmental onset across a"
        " standardized temporal axis."
    )
    modifiers = (
        "Quantifies functional impact and severity specifiers drawing from both"
        " international standards."
    )
    synthesis = (
        f"Analyzing {subject_clean} through the dual DSM-5-TR and ICD-11"
        " framework highlights the persistent friction between standardizing"
        " human traits into rigid algorithmic categories and appreciating"
        " individual holistic context."
    )

  return {
      "subjectName": name,
      "nodes": [
          {
              "nodeId": 1,
              "nodeName": (
                  "Core Presentation (DSM Checklists & ICD Prototypes)"
              ),
              "caseMapping": presentation,
              "clinicalUtility": (
                  "Combines DSM operationalized symptom criteria with ICD"
                  " narrative prototypes to structure observable features."
              ),
              "systemicLimitation": (
                  "Reduces complex lived patterns into static symptom summaries,"
                  " ignoring unique environmental drivers."
              ),
          },
          {
              "nodeId": 2,
              "nodeName": (
                  "Clinical Threshold (Distress vs. Normative Experience)"
              ),
              "caseMapping": threshold,
              "clinicalUtility": (
                  "Establishes a dual-system baseline rule to separate typical"
                  " human variation from actual pathological impairment."
              ),
              "systemicLimitation": (
                  "Arbitrary cutoffs across both manuals often mislabel"
                  " unconventional lifestyles, intense focus, or stress"
                  " adaptations as mental illness."
              ),
          },
          {
              "nodeId": 3,
              "nodeName": (
                  "Exclusionary Boundaries (Differential & Medical Rules)"
              ),
              "caseMapping": exclusion,
              "clinicalUtility": (
                  "Mandates a broad differential review complying with both"
                  " North American and global medical standards."
              ),
              "systemicLimitation": (
                  "Limited or retrospective profile data makes definitive"
                  " physiological and differential exclusion nearly impossible"
                  " in non-clinical settings."
              ),
          },
          {
              "nodeId": 4,
              "nodeName": (
                  "Temporal Progression (Duration & Longitudinal Course)"
              ),
              "caseMapping": temporal,
              "clinicalUtility": (
                  "Aids in mapping whether a condition is acute, episodic, or"
                  " chronic across a lifespan timeline using standardized"
                  " specifiers."
              ),
              "systemicLimitation": (
                  "Flattens rich life trajectories into linear clinical courses"
                  " that ignore environmental and cultural triggers."
              ),
          },
          {
              "nodeId": 5,
              "nodeName": (
                  "Dimensional Modifiers (Severity & Extension Codes)"
              ),
              "caseMapping": modifiers,
              "clinicalUtility": (
                  "Utilizes dimensional grading from both frameworks to score"
                  " severity and functional impact rather than treating"
                  " diagnoses as rigid binaries."
              ),
              "systemicLimitation": (
                  "Standardized severity scales often fail to capture internal"
                  " resilience or qualitative nuances of human experience."
              ),
          },
      ],
      "synthesis": synthesis,
  }

# ==========================================
# 4. User Input Interface
# ==========================================
st.markdown("### Profile Input")
subject_input = st.text_input(
    "Type any name, character, or psychological profile:",
    placeholder=(
        "e.g., Friedrich Nietzsche, Captain Ahab, Burnout Syndrome, etc."
    ),
)

if st.button("Run Diagnostic Analysis", type="primary"):
  if not subject_input.strip():
    st.warning("Please enter a name or profile to analyze.")
  else:
    # Fixed assignment syntax here
    data = generate_dynamic_profile(subject_input)

    st.success("Analysis Complete")
    st.header(f"Profile: {data['subjectName']}")

    for node in data["nodes"]:
      with st.expander(
          f"Node {node['nodeId']}: {node['nodeName']}", expanded=True
      ):
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
