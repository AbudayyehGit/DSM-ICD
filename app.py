import streamlit as st

# ==========================================
# 1. Page Configuration
# ==========================================
st.set_page_config(
    page_title="Taxonomy Utility Navigator", page_icon="🧬", layout="wide"
)

st.title("Diagnostic Taxonomy Utility Navigator")
st.markdown(
    "*An interactive analytical tool exploring the tension between algorithmic"
    " psychological taxonomies (DSM-5-TR / ICD-11) and holistic human experience.*"
)

# ==========================================
# 2. Pre-Loaded Case Database
# ==========================================
CASES = {
    "Jesus of Nazareth (Historical/Textual Analysis)": {
        "subjectName": "Jesus of Nazareth (Historical/Textual Analysis)",
        "nodes": [
            {
                "nodeId": 1,
                "nodeName": "Core Presentation",
                "caseMapping": (
                    "Subject exhibits intense prophetic messaging, apocalyptic"
                    " declarations, radical social non-conformity, and claims of"
                    " a unique divine filiation, as recorded in ancient"
                    " scriptural narratives."
                ),
                "clinicalUtility": (
                    "The taxonomy provides structured categories (e.g.,"
                    " perceptual anomalies, grandiosity markers) to"
                    " systematically document intense behavioral and cognitive"
                    " presentations across textual accounts."
                ),
                "systemicLimitation": (
                    "Reduces profound religious, theological, and"
                    " socio-political prophecy into pathologized 'symptom"
                    " checklists,' ignoring the cultural and apocalyptic"
                    " framework of 1st-century Judea."
                ),
            },
            {
                "nodeId": 2,
                "nodeName": "Clinical Threshold",
                "caseMapping": (
                    "Evaluating whether the subject's radical departure from"
                    " societal norms and intense ideological convictions caused"
                    " clinical distress, functional impairment, or whether they"
                    " constituted adaptive charismatic leadership."
                ),
                "clinicalUtility": (
                    "Forces an evaluation of whether behavioral extremes"
                    " disrupt baseline functioning versus serving an"
                    " effective, goal-directed historical purpose."
                ),
                "systemicLimitation": (
                    "Diagnostic thresholds struggle heavily with historical or"
                    " religious figures, frequently misinterpreting high-conviction"
                    " spiritual leadership, self-sacrifice, or intense"
                    " asceticism as clinical impairment due to Western, secular"
                    " bias."
                ),
            },
            {
                "nodeId": 3,
                "nodeName": "Exclusionary Boundaries",
                "caseMapping": (
                    "Attempting to rule out medical, neurological, or"
                    " substance-induced causes based entirely on ancient,"
                    " secondary biographical accounts lacking clinical"
                    " interviews."
                ),
                "clinicalUtility": (
                    "Establishes a rigorous methodology that mandates ruling"
                    " out organic etiologies before assigning psychological"
                    " labels."
                ),
                "systemicLimitation": (
                    "Entirely inadequate for historical analysis; ancient texts"
                    " provide zero capacity for physical exams, neurological"
                    " screening, or toxicology, rendering differential"
                    " exclusion speculative at best."
                ),
            },
            {
                "nodeId": 4,
                "nodeName": "Temporal Progression",
                "caseMapping": (
                    "Tracing the evolution of the subject's public ministry,"
                    " intensification of apocalyptic rhetoric, and final"
                    " trajectory leading to execution over a compressed"
                    " historical window."
                ),
                "clinicalUtility": (
                    "Aids in mapping longitudinal development, chronicity, and"
                    " pattern acceleration over time."
                ),
                "systemicLimitation": (
                    "Relying on compressed, religiously motivated narrative"
                    " texts distorts real temporal progression, converting"
                    " theological staging into a clinical course of illness."
                ),
            },
            {
                "nodeId": 5,
                "nodeName": "Dimensional Modifiers",
                "caseMapping": (
                    "Attempting to quantify the 'severity' or specifiers of"
                    " anomalous psychological phenomena within the narrative"
                    " accounts."
                ),
                "clinicalUtility": (
                    "Allows clinicians to scale the intensity of specific"
                    " behavioral features rather than using rigid all-or-nothing"
                    " categories."
                ),
                "systemicLimitation": (
                    "Applying modern psychometric severity scales to ancient,"
                    " non-clinical texts is fundamentally anachronistic,"
                    " superimposing modern institutional metrics onto a"
                    " completely foreign historical paradigm."
                ),
            },
        ],
        "synthesis": (
            "Attempting to map a historical and religious figure like Jesus of"
            " Nazareth through modern diagnostic taxonomies exposes the"
            " profound limitations of algorithmic frameworks when applied"
            " outside contemporary clinical settings. It highlights how rigid"
            " checklists risk pathologizing culturally normative prophecy,"
            " high-conviction spirituality, and ancient socio-political"
            " resistance by stripping away vital historical and theological"
            " context."
        ),
    },
    "Vincent van Gogh (Creativity & Affective Instability)": {
        "subjectName": "Vincent van Gogh (Affective Instability Profile)",
        "nodes": [
            {
                "nodeId": 1,
                "nodeName": "Core Presentation",
                "caseMapping": (
                    "Profound mood lability, intense creative output surges,"
                    " impulsive self-harm episodes, and severe interpersonal"
                    " friction documented via extensive personal correspondence."
                ),
                "clinicalUtility": (
                    "Quickly categorizes observable markers of affective"
                    " dysregulation and episodic behavioral extremes."
                ),
                "systemicLimitation": (
                    "Conflates acute psychological distress and neuro-divergent"
                    " temperament with pathology, completely divorcing the"
                    " symptom profile from its artistic and communicative output."
                ),
            },
            {
                "nodeId": 2,
                "nodeName": "Clinical Threshold",
                "caseMapping": (
                    "Weighing debilitating depressive episodes and erratic"
                    " social functioning against hyper-productive, genius-level"
                    " artistic production periods."
                ),
                "clinicalUtility": (
                    "Identifies clear areas where social and occupational"
                    " functioning breaks down."
                ),
                "systemicLimitation": (
                    "Binary impairment metrics fail to capture how psychological"
                    " friction can fuel transcendent creative synthesis."
                ),
            },
            {
                "nodeId": 3,
                "nodeName": "Exclusionary Boundaries",
                "caseMapping": (
                    "Differential diagnosis must account for potential"
                    " contributors like absinthe toxicity, temporal lobe"
                    " epilepsy, or syphilis alongside primary mood disorders."
                ),
                "clinicalUtility": (
                    "Mandates comprehensive differential scanning to prevent"
                    " mislabeling organic or toxic conditions as purely"
                    " psychiatric."
                ),
                "systemicLimitation": (
                    "Retrospective medical guessing lacks definitive diagnostic"
                    " precision, resulting in overlapping, competing diagnostic"
                    " labels."
                ),
            },
            {
                "nodeId": 4,
                "nodeName": "Temporal Progression",
                "caseMapping": (
                    "Episodic pattern of profound winter depressions followed"
                    " by intense, sun-drenched painting frenzies in Arles and"
                    " Auvers."
                ),
                "clinicalUtility": (
                    "Captures cyclical recurrence and longitudinal shifts in"
                    " severity over time."
                ),
                "systemicLimitation": (
                    "Reduces a complex, seasonal, and environmentally"
                    " responsive life trajectory into a flat clinical course"
                    " graph."
                ),
            },
            {
                "nodeId": 5,
                "nodeName": "Dimensional Modifiers",
                "caseMapping": (
                    "Severe emotional dysregulation specifiers applied alongside"
                    " functional disability ratings during crisis intervals."
                ),
                "clinicalUtility": (
                    "Provides a mechanism to grade intensity rather than"
                    " treating illness as an absolute state."
                ),
                "systemicLimitation": (
                    "Fails to account for periods of profound lucidity, deep"
                    " philosophical introspection, and epistolary brilliance."
                ),
            },
        ],
        "synthesis": (
            "The taxonomy effectively organizes van Gogh's behavioral crises"
            " and functional breakdowns, but its rigid diagnostic framing"
            " struggles to honor the symbiotic relationship between intense"
            " affective states and revolutionary artistic creation."
        ),
    },
}

# ==========================================
# 3. Sidebar Selection
# ==========================================
with st.sidebar:
  st.header("Navigator Settings")
  selected_case_key = st.selectbox(
      "Select Preset Case Study", options=list(CASES.keys())
  )

  st.divider()
  st.markdown("### About This App")
  st.markdown(
      "This version runs entirely on pre-compiled analytical modules. No API"
      " keys, internet calls, or model versioning issues required."
  )

# ==========================================
# 4. Main Display Logic
# ==========================================
active_case = CASES[selected_case_key]

st.header(f"Subject: {active_case['subjectName']}")

for node in active_case["nodes"]:
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
st.write(active_case["synthesis"])
