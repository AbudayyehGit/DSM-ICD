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
    " international diagnostic frameworks (DSM-5-TR & ICD-11) and holistic"
    " human experience.*"
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
    * **DSM-5-TR (Diagnostic and Statistical Manual of Mental Disorders):** Leveraged for its operationalized **symptom checklists**, structural thresholds, and North American clinical criteria.
    * **ICD-11 (International Classification of Diseases):** Leveraged for its narrative **clinical prototypes**, contextual guidelines, and global etiological perspective.

    ### The Unified 5-Step Architecture
    When you enter a name or profile below, the engine maps the subject across a 5-step framework that contrasts **Clinical Utility** (how well the checklist or prototype successfully standardizes the condition) against **Systemic Limitation** (where the taxonomy oversimplifies, pathologizes normal variation, or strips away vital historical context).
    """)

# ==========================================
# 3. Expanded Local Diagnostic Database
# ==========================================
DATABASE = {
    "vincent van gogh": {
        "subjectName": "Vincent van Gogh (Affective & Temporal Lobe Profile)",
        "nodes": [
            {
                "nodeId": 1,
                "nodeName": (
                    "Core Presentation (DSM Checklists & ICD Prototypes)"
                ),
                "caseMapping": (
                    "Episodic profound depressed mood, severe psychomotor"
                    " agitation, impulsive self-harm, perceptual disturbances,"
                    " and hyper-productive creative surges documented through"
                    " extensive epistolary records. Mapped to DSM-5-TR Unspecified"
                    " Bipolar and Related Disorder / Major Depressive Episode"
                    " criteria alongside ICD-11 affective episode prototypes."
                ),
                "clinicalUtility": (
                    "Provides explicit categories for tracking cyclical mood"
                    " lability, impulsivity, and perceptual anomalies."
                ),
                "systemicLimitation": (
                    "Conflates neurodivergent artistic temperament and acute"
                    " situational distress with pathology, stripping away the"
                    " communicative and cathartic function of his art."
                ),
            },
            {
                "nodeId": 2,
                "nodeName": (
                    "Clinical Threshold (Distress vs. Normative Experience)"
                ),
                "caseMapping": (
                    "Weighing debilitating social isolation, self-mutilation"
                    " crises, and hospitalization against transcendent creative"
                    " periods (e.g., the Arles and Auvers painting frenzies) that"
                    " yielded foundational post-impressionist masterworks."
                ),
                "clinicalUtility": (
                    "Identifies clear operational metrics where interpersonal"
                    " and occupational functioning breaks down completely."
                ),
                "systemicLimitation": (
                    "Binary clinical impairment models fail to capture how"
                    " psychological friction and affective intensity directly"
                    " fueled his unique visual synthesis."
                ),
            },
            {
                "nodeId": 3,
                "nodeName": (
                    "Exclusionary Boundaries (Differential & Medical Rules)"
                ),
                "caseMapping": (
                    "Differential evaluation must reconcile overlapping"
                    " hypotheses including acute intermittent porphyria,"
                    " digitalis/absinthe toxicity, temporal lobe epilepsy,"
                    " Meniere's disease, and primary mood disorder."
                ),
                "clinicalUtility": (
                    "Mandates rigorous differential ruling to prevent"
                    " misattributing organic or toxic insults entirely to"
                    " psychiatric illness."
                ),
                "systemicLimitation": (
                    "Retrospective medical analysis of 19th-century letters"
                    " lacks definitive biomarker verification, resulting in"
                    " competing, unprovable medical labels."
                ),
            },
            {
                "nodeId": 4,
                "nodeName": (
                    "Temporal Progression (Duration & Longitudinal Course)"
                ),
                "caseMapping": (
                    "Demonstrates a chronic, relapsing-remitting course"
                    " characterized by seasonal winter depressive crashes"
                    " followed by explosive spring/summer creative productivity."
                ),
                "clinicalUtility": (
                    "Aids in mapping longitudinal chronicity and cyclical"
                    " recurrence over a compressed lifespan timeline."
                ),
                "systemicLimitation": (
                    "Flattens a deeply volatile, environmentally responsive"
                    " life trajectory into a rigid clinical course graph."
                ),
            },
            {
                "nodeId": 5,
                "nodeName": (
                    "Dimensional Modifiers (Severity & Extension Codes)"
                ),
                "caseMapping": (
                    "Severe affective dysregulation specifiers with"
                    " psychological distress codes applied during"
                    " institutionalization intervals."
                ),
                "clinicalUtility": (
                    "Grades the intensity and functional impact of episodes"
                    " rather than viewing illness as an all-or-nothing state."
                ),
                "systemicLimitation": (
                    "Fails to account for periods of profound philosophical"
                    " lucidity and epistolary brilliance occurring simultaneously"
                    " with crisis."
                ),
            },
        ],
        "synthesis": (
            "The dual DSM/ICD framework effectively categorizes van Gogh's"
            " behavioral crises and functional breakdowns, but its rigid"
            " diagnostic mapping struggles to honor the symbiotic"
            " relationship between affective volatility and revolutionary"
            " artistic creation."
        ),
    },
    "abraham lincoln": {
        "subjectName": "Abraham Lincoln (Melancholia & Resilience Profile)",
        "nodes": [
            {
                "nodeId": 1,
                "nodeName": (
                    "Core Presentation (DSM Checklists & ICD Prototypes)"
                ),
                "caseMapping": (
                    "Profound, recurring depressive episodes ('melancholy'),"
                    " somatic vegetative symptoms, severe anhedonia, and"
                    " suicidal ideation documented during his Illinois"
                    " legislative and presidential years. Mapped to DSM-5-TR"
                    " Persistent Depressive Disorder / Major Depressive Episode"
                    " and ICD-11 Depressive Episode."
                ),
                "clinicalUtility": (
                    "Directly flags severe vegetative depression, vegetative"
                    " shifts, and psychological distress via standardized"
                    " symptom criteria."
                ),
                "systemicLimitation": (
                    "Risks pathologizing deep grief, political burden, and"
                    " existential dread as a chemical defect."
                ),
            },
            {
                "nodeId": 2,
                "nodeName": (
                    "Clinical Threshold (Distress vs. Normative Experience)"
                ),
                "caseMapping": (
                    "Evaluating severe internal suffering and acute functional"
                    " paralysis against an unprecedented capacity for"
                    " high-stakes executive leadership and historical statecraft"
                    " during the American Civil War."
                ),
                "clinicalUtility": (
                    "Assesses the threshold where internal emotional distress"
                    " threatens basic occupational and public duties."
                ),
                "systemicLimitation": (
                    "Struggles to capture 'depressive realism' or functional"
                    " compartmentalization—how severe internal suffering can"
                    " coexist with supreme political execution."
                ),
            },
            {
                "nodeId": 3,
                "nodeName": (
                    "Exclusionary Boundaries (Differential & Medical Rules)"
                ),
                "caseMapping": (
                    "Differentiating situational grief (loss of Ann Rutledge,"
                    " marital strain) and chronic adjustment distress from"
                    " primary endogenous affective disorders."
                ),
                "clinicalUtility": (
                    "Requires separating environmental and situational trauma"
                    " triggers from biologically driven mood pathology."
                ),
                "systemicLimitation": (
                    "19th-century medical records lack standardized"
                    " neuroendocrine or psychiatric evaluation protocols."
                ),
            },
            {
                "nodeId": 4,
                "nodeName": (
                    "Temporal Progression (Duration & Longitudinal Course)"
                ),
                "caseMapping": (
                    "A lifelong, episodic longitudinal course with acute"
                    " multi-week depressive collapses (notably in 1835 and 1841)"
                    " interspersed with long periods of high-functioning"
                    " compensation."
                ),
                "clinicalUtility": (
                    "Maps the chronic, recurrent nature of affective"
                    " disorders over decades."
                ),
                "systemicLimitation": (
                    "Fails to account for how the subject actively utilized"
                    " writing, humor, and purpose as adaptive mechanisms to"
                    " alter the longitudinal trajectory."
                ),
            },
            {
                "nodeId": 5,
                "nodeName": (
                    "Dimensional Modifiers (Severity & Extension Codes)"
                ),
                "caseMapping": (
                    "Moderate-to-severe depressive specifiers with prominent"
                    " cognitive rumination features."
                ),
                "clinicalUtility": (
                    "Quantifies symptom severity without requiring complete"
                    " continuous incapacitation."
                ),
                "systemicLimitation": (
                    "Overlooks post-traumatic growth and the adaptive utility"
                    " of emotional depth in political leadership."
                ),
            },
        ],
        "synthesis": (
            "Analyzing Lincoln through modern diagnostic taxonomies exposes"
            " the limitation of viewing severe melancholia purely as a"
            " pathology, missing how deep psychological endurance can be"
            " forged into political resilience."
        ),
    },
    "friedrich nietzsche": {
        "subjectName": "Friedrich Nietzsche (Philosophical/Affective Profile)",
        "nodes": [
            {
                "nodeId": 1,
                "nodeName": (
                    "Core Presentation (DSM Checklists & ICD Prototypes)"
                ),
                "caseMapping": (
                    "Profound intellectual intensity, grandiose philosophical"
                    " mission, progressive cognitive fragmentation, behavioral"
                    " disinhibition, and late-stage psychological collapse in"
                    " Turin. Mapped against ICD organic mental disorder"
                    " prototypes and DSM neurocognitive markers."
                ),
                "clinicalUtility": (
                    "Provides operational categories for tracking rapid"
                    " executive function decline and behavioral disinhibition."
                ),
                "systemicLimitation": (
                    "Conflates revolutionary philosophical critique and"
                    " high-intensity creative output with early-stage"
                    " psychiatric disturbance."
                ),
            },
            {
                "nodeId": 2,
                "nodeName": (
                    "Clinical Threshold (Distress vs. Normative Experience)"
                ),
                "caseMapping": (
                    "Distinguishing visionary philosophical disruption and"
                    " social isolation from complete reality-testing collapse"
                    " and subsequent institutionalization."
                ),
                "clinicalUtility": (
                    "Identifies the precise boundary where eccentric"
                    " intellectual output transitions into unmanageable"
                    " functional deterioration."
                ),
                "systemicLimitation": (
                    "Prone to retrospective pathography—labeling unconventional"
                    " philosophical concepts as symptoms of underlying mental"
                    " illness."
                ),
            },
            {
                "nodeId": 3,
                "nodeName": (
                    "Exclusionary Boundaries (Differential & Medical Rules)"
                ),
                "caseMapping": (
                    "Differential evaluation between tertiary neurosyphilis"
                    " (general paresis of the insane), slow-growing retrobulbar"
                    " meningioma, frontotemporal dementia, or atypical bipolar"
                    " affective psychosis."
                ),
                "clinicalUtility": (
                    "Enforces medical and neurological rule-outs before"
                    " accepting primary psychiatric labels."
                ),
                "systemicLimitation": (
                    "Historical medical notes and preserved letters do not"
                    " provide definitive differential confirmation."
                ),
            },
            {
                "nodeId": 4,
                "nodeName": (
                    "Temporal Progression (Duration & Longitudinal Course)"
                ),
                "caseMapping": (
                    "Decades of chronic migraine and visual impairment"
                    " followed by an abrupt, cataclysmic psychological collapse"
                    " in January 1889 leading to permanent unresponsiveness."
                ),
                "clinicalUtility": (
                    "Tracks chronic progressive decline versus acute"
                    " catastrophic encephalopathic onset."
                ),
                "systemicLimitation": (
                    "Reduces a rich, evolving intellectual life trajectory into"
                    " a terminal medical decline narrative."
                ),
            },
            {
                "nodeId": 5,
                "nodeName": (
                    "Dimensional Modifiers (Severity & Extension Codes)"
                ),
                "caseMapping": (
                    "Global cognitive impairment specifiers with profound"
                    " executive dysfunction coding."
                ),
                "clinicalUtility": "Scores end-stage functional loss objectively.",
                "systemicLimitation": (
                    "Completely misses the philosophical legacy and conceptual"
                    " framework generated prior to cognitive collapse."
                ),
            },
        ],
        "synthesis": (
            "The DSM and ICD frameworks capture late-stage organic cognitive"
            " decay effectively, but struggle to map the complex intersection"
            " between intense intellectual genius and biological"
            " vulnerability."
        ),
    },
    "captain ahab": {
        "subjectName": "Captain Ahab (Literary Monomaniacal Profile)",
        "nodes": [
            {
                "nodeId": 1,
                "nodeName": (
                    "Core Presentation (DSM Checklists & ICD Prototypes)"
                ),
                "caseMapping": (
                    "Fixed, unshakeable delusional belief system (monomania)"
                    " centered on a specific persecutory object (the white"
                    " whale), unyielding preoccupation, and intense behavioral"
                    " narrowing. Mapped to DSM-5-TR Delusional Disorder"
                    " (Persecutory/Grandiose subtype) and ICD-11 Delusional"
                    " Disorders."
                ),
                "clinicalUtility": (
                    "Provides immediate operational markers for fixed, non-bizarre"
                    " systems of belief and intense behavioral fixation."
                ),
                "systemicLimitation": (
                    "Reduces literary archetypes and allegorical explorations"
                    " of human vengeance into a rigid clinical symptom checklist."
                ),
            },
            {
                "nodeId": 2,
                "nodeName": (
                    "Clinical Threshold (Distress vs. Normative Experience)"
                ),
                "caseMapping": (
                    "Evaluating total occupational absorption and the complete"
                    " subordination of crew, ship, and personal survival to a"
                    " singular revenge objective against baseline maritime"
                    " leadership."
                ),
                "clinicalUtility": (
                    "Highlights severe impairment across social, occupational,"
                    " and survival domains."
                ),
                "systemicLimitation": (
                    "Fails to account for the symbolic, cultural, and mythic"
                    " dimensions of obsession within maritime whaling traditions."
                ),
            },
            {
                "nodeId": 3,
                "nodeName": (
                    "Exclusionary Boundaries (Differential & Medical Rules)"
                ),
                "caseMapping": (
                    "Differentiating primary psychotic disorders from"
                    " obsessive-compulsive extremes, traumatic brain injury"
                    " sequels (ivory leg / physical trauma), or cultural"
                    " vengeance norms."
                ),
                "clinicalUtility": (
                    "Mandates ruling out organic head injury and substance"
                    " factors before confirming delusional pathology."
                ),
                "systemicLimitation": (
                    "Fictional characters cannot undergo real neurological"
                    " screening, rendering differential diagnosis a speculative"
                    " exercise."
                ),
            },
            {
                "nodeId": 4,
                "nodeName": (
                    "Temporal Progression (Duration & Longitudinal Course)"
                ),
                "caseMapping": (
                    "Chronic, unyielding escalation of mono-ideational"
                    " obsession culminating in catastrophic terminal execution."
                ),
                "clinicalUtility": (
                    "Tracks the chronic, unremitting trajectory of unyielding"
                    " fixations."
                ),
                "systemicLimitation": (
                    "Treats narrative plot pacing as an organic medical disease"
                    " progression."
                ),
            },
            {
                "nodeId": 5,
                "nodeName": (
                    "Dimensional Modifiers (Severity & Extension Codes)"
                ),
                "caseMapping": (
                    "Severe functional impairment with total loss of reality"
                    " testing regarding risk."
                ),
                "clinicalUtility": (
                    "Quantifies extreme risk-taking and functional deficit."
                ),
                "systemicLimitation": (
                    "Ignores the rhetorical and narrative brilliance embedded"
                    " within the subject's monologues."
                ),
            },
        ],
        "synthesis": (
            "Combining DSM structural thresholds with ICD narrative prototypes"
            " effectively flags extreme behavioral fixation, but misses the"
            " symbolic, thematic, and literary dimensions of human drive."
        ),
    },
}


def generate_dynamic_profile(subject):
  subject_clean = subject.strip().title()
  subject_lower = subject.lower()

  for key, profile in DATABASE.items():
    if key in subject_lower or subject_lower in key:
      return profile

  return {
      "subjectName": f"{subject_clean} (Clinical & Behavioral Profile Analysis)",
      "nodes": [
          {
              "nodeId": 1,
              "nodeName": (
                  "Core Presentation (DSM Checklists & ICD Prototypes)"
              ),
              "caseMapping": (
                  f"Observable behavioral markers, cognitive patterns, and"
                  f" reported traits associated with {subject_clean}, mapped"
                  " through synthesized DSM-5-TR operational symptom"
                  " checklists and ICD-11 clinical narrative prototypes."
              ),
              "clinicalUtility": (
                  "Provides immediate operational categories to structure"
                  " observable features across standardized criteria."
              ),
              "systemicLimitation": (
                  "Reduces complex lived patterns into static symptom"
                  " summaries, ignoring unique environmental and cultural"
                  " drivers."
              ),
          },
          {
              "nodeId": 2,
              "nodeName": (
                  "Clinical Threshold (Distress vs. Normative Experience)"
              ),
              "caseMapping": (
                  "Evaluating whether the profile's traits cross the boundary"
                  " from eccentric adaptation, high-drive focus, or lifestyle"
                  " variation into clinically significant impairment or"
                  " distress."
              ),
              "clinicalUtility": (
                  "Establishes a dual-system baseline rule to separate typical"
                  " human variation from actual pathological impairment."
              ),
              "systemicLimitation": (
                  "Arbitrary cutoffs across both manuals often mislabel"
                  " unconventional lifestyles or stress adaptations as mental"
                  " illness."
              ),
          },
          {
              "nodeId": 3,
              "nodeName": (
                  "Exclusionary Boundaries (Differential & Medical Rules)"
              ),
              "caseMapping": (
                  "Mandatory differential review requiring the exclusion of"
                  " acute medical conditions, neurological insults, substance"
                  " effects, or external situational stressors."
              ),
              "clinicalUtility": (
                  "Ensures compliance with international medical standards by"
                  " preventing misdiagnosis of organic issues."
              ),
              "systemicLimitation": (
                  "Limited or retrospective profile data makes definitive"
                  " physiological and differential exclusion nearly impossible."
              ),
          },
          {
              "nodeId": 4,
              "nodeName": (
                  "Temporal Progression (Duration & Longitudinal Course)"
              ),
              "caseMapping": (
                  "Longitudinal mapping of trait stability, developmental"
                  " onset, and duration requirements across a standardized"
                  " lifespan timeline."
              ),
              "clinicalUtility": (
                  "Aids in mapping whether a condition or pattern is acute,"
                  " episodic, or chronic."
              ),
              "systemicLimitation": (
                  "Flattens rich life trajectories into linear clinical courses"
                  " that ignore environmental triggers."
              ),
          },
          {
              "nodeId": 5,
              "nodeName": (
                  "Dimensional Modifiers (Severity & Extension Codes)"
              ),
              "caseMapping": (
                  "Quantification of functional impact, severity specifiers,"
                  " and contextual disability coding drawing from both"
                  " standards."
              ),
              "clinicalUtility": (
                  "Utilizes dimensional grading to score severity rather than"
                  " treating diagnoses as rigid binaries."
              ),
              "systemicLimitation": (
                  "Standardized severity scales often fail to capture internal"
                  " resilience or qualitative nuances of human experience."
              ),
          },
      ],
      "synthesis": (
          f"Analyzing {subject_clean} through the dual DSM-5-TR and ICD-11"
          " framework highlights the persistent friction between standardizing"
          " human traits into rigid algorithmic categories and appreciating"
          " individual holistic context."
      ),
  }


# ==========================================
# 4. User Input Interface
# ==========================================
st.markdown("### Profile Input")
subject_input = st.text_input(
    "Type any name or historical profile (try 'Vincent van Gogh', 'Abraham"
    " Lincoln', 'Friedrich Nietzsche', or 'Captain Ahab'):",
    placeholder="e.g., Vincent van Gogh, Abraham Lincoln...",
)

if st.button("Run Diagnostic Analysis", type="primary"):
  if not subject_input.strip():
    st.warning("Please enter a name or profile to analyze.")
  else:
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
