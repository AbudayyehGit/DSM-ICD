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
           
